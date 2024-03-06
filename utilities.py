import pygame as pg
import os

PATH = 'images/'

def load_image(path, img_name):
    image = pg.image.load(PATH + path + '/' + img_name).convert_alpha()
    return image

def load_images(path):
    images = []
    for img_name in sorted(os.listdir(PATH + path)):
        images.append(load_image(path, img_name))
    return images