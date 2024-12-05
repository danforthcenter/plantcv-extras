
# thermal functions for reading metadata and renaming files

# Importing Functions
import subprocess
import os
from plantcv.plantcv import fatal_error


def flir_rename(filename, sep='_', test=True, new_dir=None):
    """
    Function that renames rgb and thermal images to include create date and time metadata

    INPUTS:
    1) filename: path to a single image or a directory
    2) sep: character that is used for separating filename, date, and time (default='_')
    3) test: wether or not to test file renaming, dry run (default=True)
    4) new_dir: path to new directory to copy renamed images to; default will rename files in input directory (default=None)

    OUTPUTS:
    Changes FLIR image names (eg. FLIR5003.jpg > FLIR5003_2024-6-12T10-35.jpg)

    :param filename: str
    :param sep: str
    :param test: bool
    :param new_dir: str
    """
    if os.path.exists(filename) is False:
        fatal_error(filename + "could not be found")

    if sep not in ("_", "-"):
        fatal_error("Must specify either '_' or '-' for sep")       # separator characters are limited to these two options

    date_format = "%Y-%m-%dT%H-%M"      # sets date_format if sep is set to default
    testname1 = "-testname<%"
    testname2 = "f_$datetimeoriginal.%e"
    args = ["-d"]       # if no new directory is specified, args is set to "-d"

    if sep == "-":
        date_format = "%Y_%m_%dT%H_%M"      # sets date_format if sep is set to "-"
        testname2 = "f-$datetimeoriginal.%e"

    if test is False:
        testname1 = "-filename<%"

    if new_dir is not None:
        # check if given directory exists and if not
        args = ["-r", "-o", new_dir, "-d"]

    testname = testname1+testname2

    subprocess.run(['exiftool', *args, date_format, testname, filename], check=True)
