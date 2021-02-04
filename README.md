# Writing python plugins for GIMP v2.10

In early 2021, I was bored and decided to animate this profile picture that I've been using for some time now:
<img alt="Minimalistic windmill" src="./templ.jpeg" height="480" />

I wanted the rotors to spin in an animated gif and decided to use GIMP for this task (later someone told me, that something like AE would be more suited).
My idea was to separate the picture into two layers: the backdrop and the rotor. Then I simply needed to clone the rotor layer 360 times and rotate each layer by 1 degree. 
Afterwards, I'd also clone the backdrop 360 times and merge it with each rotated rotor image.

Here is an example with 12 frames made by hand:

<img alt="Simple animation" src="./anim1.gif" height="480" />

And this little ugly thing took me already half an hour.

As there is a lot of work to do, I wanted a script / plugin to do it for me. In my opinion, the beauty of GIMP is that it's so easily extensible and comes with a fair amount of good plugins installed.

## Tutorials on the internet

Now here the trouble starts. I could only find three (good) references on writing GIMP plugins:
 - [Nathan Good: Use Python to write plug-ins for GIMP](https://ibm.com/developerworks/opensource/library/os-autogimp/index.html#resources)
 - [Calinou: InsaneBump GIMP plugin](https://gist.github.com/Calinou/5b9bd428079959558ba8)
 - [An Example Plugin in the GIMP reference](https://gimp.org/docs/python/index.html#STRUCTURE-OF-PLUGIN)

Keep in mind that the third link is for GIMP v1 (which is, funny enough, still from the last millenium).
Also there's [How to write a GIMP plug-in](https://developer.gimp.org/writing-a-plug-in/1/index.html), but this is mostly technical stuff spread over three parts - and it is also for GIMP v1.

GIMP has plug-ins and scripts (the two have separate folders in the configuration). I couldn't find any information on the internet on the difference of these two.
I'll just call them plug-ins from now on. [There are multiple ways to write write plug-ins in GIMP](https://wiki.gimp.org/wiki/Hacking:Plugins#Choosing_a_Language_for_a_GIMP_Plug-in):
 - A Script-Fu script (a Lua-type language)
 - A Python script (using `import gimpfu`)
 - A C library that is compiled using gimptool (using `#include <libgimp/gimp.h>`)

For the sake of simplicity, I chose to use python.

On Windows, the default GIMP installation comes with its own python version. Look in `Program Files\GIMP 2\bin\python.exe`.
From what I can tell, this is just a plain python version (v2.7.18 comes with GIMP 2.10.20) compiled for Windows, that includes the gimpfu libary.
On Linux, the shared Python installation is used. I don't know if there is compatibility for Python 3, as [Python plugin support is completely disabled in Arch Linux](https://git.archlinux.org/svntogit/packages.git/tree/trunk/PKGBUILD?h=packages/gimp#n49).

I just learned about most of the things I'm writing here. The information is *not* double-checked or written in any official Reference or Help. Also keep in mind, that by no means I know much about Python. My examples may contain code that can be considered "bad", I'm just doing this for demonstration purposes.

## Python Plugin: The Basics
A Python *plugin* consists of a single python file that is executable and has `#!/usr/bin/python` in the first line. It must be placed in any of the directories mentioned in GIMP via `Edit > Preferences > Folders > Plug-ins`. It is also possible to add directories using the `+` button in the top left.

The plugin must call the gimpfu.register() function. Help for every provided function can be viewed via the built-in Python Console (`Filters > Python-Fu > Console`) by `import gimpfu` and `help(gimpfu.<function>)`:
```
>>> import gimpfu
>>> help(gimpfu.register)
Help on function register in module gimpfu:

register(proc_name, blurb, help, author, copyright, date, label, imagetypes, params, results, function, menu=None, domain=None, on_query=None, on_run=None)
    This is called to register a new plug-in.
```

This is somewhat helpful. But what is a `blurb`? How should the `params` be specified? What `imagetypes` are there? Etc. etc.

According to [the GIMP reference](https://developer.gimp.org/writing-a-plug-in/1/index.html) (scroll down to "The query() function"), "gimp_install_procedure [which is the C aequivalent to python-fu's register] declares the procedure name, some description and help strings [...]". A paragraph down, there is a list of image types (which might very well be outdated as the article is from 2003).

However, [Natahn Good's article](https://ibm.com/developerworks/opensource/library/os-autogimp/index.html#resources) has a table with all parameters.


