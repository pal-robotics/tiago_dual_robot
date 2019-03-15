#!/usr/bin/env

import os
import sys

print(sys.argv)
for i in range(1, len(sys.argv)):
    filename = sys.argv[i]
    with open(filename, "r") as f:
        contents = f.read()


    for side in ["left", "right"]:
        new_name = filename.replace("arm_", "arm_" + side + "_")
        new_contents = contents.replace("arm_", "arm_" + side + "_")

        with open(new_name, "w") as f:
            f.write(new_contents)







