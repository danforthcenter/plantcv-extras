# function for converting .jpg to .csv image files from FLIR thermal camera

# Importing Functions
from plantcv.plantcv import fatal_error
import numpy as np
import os
import re
from flirextractor import FlirExtractor


def flir_convert(pseudo_dir, csv_dir, thermal_index=None, contains_str=None):
    """ Function that converts pseudo colored thermal images into csv files
    INPUTS:
    1) pseudo_dir: path to a directory with thermal/pseudo colored (and rgb) images
    2) csv_dir: output directory where csv files are saved
    3) thermal_index: (optional) "odd" or "even" (default=None)
                        - selects thermal images based on first integer in the filename
                        - eg. FLIR1024_11-3-23_9-45.jpg -> "even"
                        - helpful if thermal and rgb images are in the same folder
    4) contains_str: (optional) specify a substring in the name to run over a subset of images only

    OUTPUTS:
    Converts thermal images from .jpg to .csv files

    :param pseudo_dir: str
    :param csv_dir: str
    :param thermal_index: str
    :param contains_str: str
    """

    if not os.path.exists(pseudo_dir):
        fatal_error(pseudo_dir + " could not be found")

    # filter images based on extension and optional criteria
    thermal_list = _filter_images(pseudo_dir, thermal_index, contains_str)
    failed_files = []
    # loops through all images in thermal_list and converts them to .csv files,
    # saves outputs in csv_dir
    # recommended to use 'with:' context manager
    with FlirExtractor() as extractor:
        for image in thermal_list:
            try:
                _convert_image(image, pseudo_dir, csv_dir, extractor)
            except Exception as e:
                failed_files.append(f"{os.path.join(pseudo_dir, image)}: {e}")
    # prints filenames and error messages of files that failed to process
    if failed_files:
        print("\n some files failed to process:")
        print("\n".join(failed_files))
    return failed_files


def _filter_images(pseudo_dir, thermal_index, contains_str):
    """helper function that filters images in a directory based on index and substring"""
    # creates a list of all thermal images in img_dir
    thermal_list = [f for f in os.listdir(pseudo_dir) if f.endswith('.jpg')]

    if thermal_index in ('even', 'odd'):  # this only checks the first integer
        # selects all images that end with an even number
        thermal_list = [f for f in thermal_list if int(re.findall(r'\d+', f)[0]) % 2 == 0]
        # selects all images that end with an odd number
        if thermal_index == 'odd':
            thermal_list = [f for f in thermal_list if int(re.findall(r'\d+', f)[0]) % 2 != 0]

    # filter list by contain_str
    if contains_str:
        thermal_list = [f for f in thermal_list if contains_str in f]

    return thermal_list


def _convert_image(image, pseudo_dir, csv_dir, extractor):
    """helper function to extract thermal data and save into csv"""
    new_name = image[:-4]      # removes extension .jpg
    old_path = os.path.join(pseudo_dir, image)      # combines path to directory with filename
    thermal_data = extractor.get_thermal(old_path)      # extracts the temperature data from the .jpg
    new_path = os.path.join(csv_dir, new_name) + ".csv"     # combines new directory, new name and new extension
    # combines new directory, new name and new extension if filename already exists and adds "_new" to name
    if os.path.exists(new_path):
        new_path = os.path.join(csv_dir, new_name) + "_new" + ".csv"
    np.savetxt(new_path, thermal_data, delimiter=",")       # saves temperature data in a csv file
