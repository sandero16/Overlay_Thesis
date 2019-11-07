import SimpleITK as sitk
import matplotlib.pyplot as plt
import numpy as np
import os
import argparse
from PIL import Image

PARAM_TAG = "--"
PARAM_UNDER = "underlay"
PARAM_OVER = "over"
PARAM_RESULT = "result"

#Important part for overlay!!!
def overlay(fixedImageString, movingImageString, resultImageString):
    os.system('magick composite -blend 30 ' + fixedImageString + ' ' +movingImageString + ' ' +'merged_original'+movingImageString)

def make_transparent(name, color):
    img = Image.open(name)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((0, 0, 0, 0))
        else:
            if(color == "new"):
                newData.append((34,255,0,1000))
            else:
                newData.append((255,0,0,1000))
    img.putdata(newData)
    newName = name.replace(".bmp",".png")
    img.save(newName, "PNG")
    return newName

def make_gif(original, result):
    outputname = result.replace(".png","_bspline")

    original = original.replace("/", "\\")
    result = result.replace("/", "\\")
    outputname = outputname.replace("/", "\\")

    os.system("gif_making "+original + " " + result + " " + outputname)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(PARAM_TAG + PARAM_UNDER, type=str, help="path to underlaying.", required=True)
    parser.add_argument(PARAM_TAG + PARAM_OVER, type=str, help="path to overlaying.", required=True)
    parser.add_argument(PARAM_TAG + PARAM_RESULT, type=str, help="path to result.", required=True)


    flags, _unparsed = parser.parse_known_args()
    param_dict = yaml.load(open(flags.parameter_file))
    fixedImageString = "town3.jpeg"
    movingImageString = "town3.bmp"
    resultImageString = "result.png"
    overlay(fixedImageString, movingImageString, resultImageString)

if __name__ == "__main__":
    main()

