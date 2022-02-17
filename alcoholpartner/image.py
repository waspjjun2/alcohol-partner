import os


PACKAGE_DIR = os.path.abspath(os.path.dirname(__file__))
IMAGES_DIR = os.path.join(PACKAGE_DIR, 'images')


def path_for(image):
    return os.path.join(IMAGES_DIR, image)
