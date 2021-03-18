#!/usr/bin/env python3

import numpy
import cv2

def get_image(image):

    img = numpy.array(image, dtype = numpy.uint32)

    return img.tolist()