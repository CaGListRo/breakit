import pygame as pg
import os

PATH = 'images/'

def load_image(path, img_name, width, height=None):
    image = pg.image.load(PATH + path + '/' + img_name).convert_alpha()
    if height == None:
        old_width = image.get_width()
        old_height = image.get_height()
        factor = width * 100 // old_width
        height = old_height *  factor // 100
    image = pg.transform.scale(image, (width, height))
    return image

def load_images(path, width, height=None):
    images = []
    for img_name in sorted(os.listdir(PATH + path)):
        images.append(load_image(path, img_name, width, height))
    return images