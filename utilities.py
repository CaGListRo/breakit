import pygame as pg
import os

BASE_PATH = 'images/'

def load_image(path: str, img_name: str) -> pg.Surface:
    """
    Load image from file and return it as a pygame Surface object.
    Args:
    path (str): Path to the image file. BASE_PATH = 'images/'
    img_name (str): Name of the image file.
    Returns:
    pg.Surface: Loaded image as a pygame Surface object.
    """
    image: pg.Surface = pg.image.load(BASE_PATH + path + '/' + img_name).convert_alpha()
    return image

def load_images(path: str) -> list[pg.Surface]:
    """
    Load all images from a directory and return them as a list of pygame Surface objects.
    Args:
    path (str): Path to the directory containing the image files. BASE_PATH = 'images/
    Returns:
    list[pg.Surface]: List of loaded images as pygame Surface objects.
    """
    images: list[pg.Surface] = []
    for img_name in sorted(os.listdir(BASE_PATH + path)):
        images.append(load_image(path, img_name))
    return images