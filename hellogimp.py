#!/usr/bin/python
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# 

from gimpfu import *
import math

def plugin_main(timg, tdrawable, x=36, b=TRUE):
    print 'Hello world: %x, %r' % (x, b)

register(
        "python_fu_helloworld",
        "blurb: Here is the first text",
        "help: Here is the help text",
        "author: My name",
        "copyright: My company",
        "date: 2020",
        "<Image>/Filters/Hello GIMP!",
        "RGB*, GRAY*",
        [
            (PF_INT, "x", "An integer value:", "36"),
            (PF_BOOL, "b", "Is the weather nice?", TRUE),
        ],
        [],
        plugin_main)

main()
