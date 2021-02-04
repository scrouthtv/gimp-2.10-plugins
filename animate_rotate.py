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

def plugin_main(timg, tdrawable, steps=36, autocenter=TRUE, rotorlayer=None, backdroplayer=None, cx=0, cy=0):

    print "Hello world"
    angle = 2 * math.pi / steps

    #rotorlayer = pdb.gimp_image_get_layer_by_name(timg, "rotor")
    #backdroplayer = pdb.gimp_image_get_layer_by_name(timg, "backdrop")

    for x in range(steps-1):
        mybackdrop = pdb.gimp_layer_copy(backdroplayer, FALSE)
        pdb.gimp_image_insert_layer(timg, mybackdrop, None, 0)

        myrotor = pdb.gimp_layer_copy(rotorlayer, FALSE)
        pdb.gimp_image_insert_layer(timg, myrotor, None, 0)
        pdb.gimp_item_transform_rotate(myrotor, (x + 1) * angle, autocenter, cx, cy)

        pdb.gimp_image_merge_down(timg, myrotor, 1)

    pdb.gimp_image_merge_down(timg, rotorlayer, 1)

register(
        "python_fu_animate_rotate",
        "Plugin that animates an image by rotating it",
        "The plugin rotates a layer called rotor steps times around either its center or a specified point and merges each layer with a layer called backdrop",
        "Lenni vH",
        "Lenni vH",
        "2020",
        "<Image>/Filters/Animation/Rotate...",
        "RGB*, GRAY*",
        [
            (PF_INT, "steps", "Animation Steps", "36"),
            (PF_BOOL, "autocenter", "Rotate around the center of the rotor", TRUE),
            (PF_LAYER, "rotorlayer", "Which layer should be rotated", None),
            (PF_LAYER, "backdroplayer", "Which layer should be static", None),
            (PF_INT, "cx", "X Center of rotation", "0"),
            (PF_INT, "cy", "Y Center of rotation", "0"),
        ],
        [],
        plugin_main)

main()
