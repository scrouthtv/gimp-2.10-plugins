# Writing python plugins for GIMP v2.10

In early 2021, I was bored and decided to animate this profile picture that I've been using for some time now:
![Minimalistic windmill](./templ.jpeg)

I wanted the rotors to spin in an animated gif and decided to use GIMP for this task (later someone told me, that something like AE would be more suited).
My idea was to separate the picture into two layers: the backdrop and the rotor. Then I simply needed to clone the rotor layer 360 times and rotate each layer by 1 degree. 
Afterwards, I'd also clone the backdrop 360 times and merge it with each rotated rotor image.

Here is an example with 12 frames made by hand:
![Simple animation](./anim1.gif)
And this little ugly thing took me already half an hour.

As there is a lot of work to do, I wanted a script / plugin to do it for me. In my opinion, the beauty of GIMP is that it's so easily extensible and comes with a fair amount of good plugins installed.

## Tutorials on the internet

Now here the trouble starts. I could only find three (good) references on writing GIMP plugins:
 - [Nathan Good: Use Python to write plug-ins for GIMP](https://ibm.com/developerworks/opensource/library/os-autogimp/index.html#resources)
 - [Calinou: InsaneBump GIMP plugin](https://gist.github.com/Calinou/5b9bd428079959558ba8)
 - [An Example Plugin in the GIMP reference](https://gimp.org/docs/python/index.html#STRUCTURE-OF-PLUGIN)
Keep in mind that the third link is for GIMP v1 (which is, funny enough, still from the last millenium).
Also there's [How to write a GIMP plug-in](https://developer.gimp.org/writing-a-plug-in/1/index.html), but this is mostly technical stuff spread over three parts - and it is also for GIMP v1.
