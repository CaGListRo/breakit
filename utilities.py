import pygame as pg
import os

PATH = 'images/'

def load_image(path, img_name, width):
    image = pg.image.load(PATH + path + '/' + img_name).convert_alpha()
    old_width = image.get_width()
    old_height = image.get_height()
    factor = width * 100 // old_width
    new_height = old_height *  factor // 100
    image = pg.transform.scale(image, (width, new_height))
    return image

def load_images(path, width):
    images = []
    for img_name in sorted(os.listdir(PATH + path)):
        images.append(load_image(path, img_name, width))
    return images