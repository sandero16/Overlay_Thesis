import SimpleITK as sitk
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image

#Important part for overlay!!!
def overlay(fixedImageString, movingImageString, resultImageString):
    os.system('magick composite -blend 30 ' + fixedImageString + ' ' +movingImageString + ' ' +'merged_original'+movingImageString)


fixedImageString = "town3.jpeg"
movingImageString = "town3.bmp"
resultImageString = "result.png"
overlay(fixedImageString, movingImageString, resultImageString)



