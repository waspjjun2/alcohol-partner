import os


PACKAGE_DIR = os.path.abspath(os.path.dirname(__file__))
RESOURCES_DIR = os.path.join(PACKAGE_DIR, 'resources')


def path_for(image):
    return os.path.join(RESOURCES_DIR, image)
