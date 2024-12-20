
# thermal functions for reading metadata and renaming files

# Importing Functions
import subprocess
import os
from plantcv.plantcv import fatal_error


def flir_rename(filename, new_dir, sep='_'):
    """
    Function that renames rgb and thermal images to include create date and time metadata

    INPUTS:
    1) filename: path to a single image or a directory
    2) sep: character that is used for separating filename, date, and time (default='_')
    4) new_dir: path to new directory to copy renamed images to

    OUTPUTS:
    Changes FLIR image names (eg. FLIR5003.jpg > FLIR5003_2024-6-12T10-35.jpg)

    :param filename: str
    :param sep: str
    :param new_dir: str
    """
    # finds path to exiftool
    exiftool_path = str(os.environ.get('exiftoolpath'))

    if os.path.exists(filename) is False:
        fatal_error(filename + "could not be found")

    # separator characters are limited to these two options
    if sep not in ("_", "-"):
        fatal_error("Must specify either '_' or '-' for sep")

    # sets date_format if sep is set to default
    date_format = "%Y-%m-%dT%H-%M"
    changename = "-filename<%f_$datetimeoriginal.%e"
    args = ["-r", "-o", new_dir, "-d"]

    # sets date_format if sep is set to "-"
    if sep == "-":
        date_format = "%Y_%m_%dT%H_%M"
        changename = "-filename<%f-$datetimeoriginal.%e"
        
    result = subprocess.run(['which', 'exiftool'], capture_output=True, text=True, check=True)
    exiftool_path = str(result.stdout[:-1])
    
    subprocess.run([exiftool_path, *args, date_format, changename, filename], check=True)
