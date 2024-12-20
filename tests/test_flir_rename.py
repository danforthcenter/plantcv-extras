import os
import pytest
from plantcv.extras.thermal import flir_rename
import subprocess

# tests fatal error if file doesn't exist or cannot be found
def test_flir_rename_fatal_filename(test_data, tmpdir):
    """Test for PlantCV.Extras"""
    cache_dir = tmpdir.mkdir("cache")
    with pytest.raises(RuntimeError):
        flir_rename(filename="test.jpg", new_dir=cache_dir, sep='_')


# tests fatal error if separator is not dash or underscore
def test_flir_rename_fatal_sep(test_data, tmpdir):
    """Test for PlantCV.Extras"""
    cache_dir = tmpdir.mkdir("cache")
    with pytest.raises(RuntimeError):
        flir_rename(test_data.datadir, new_dir=cache_dir, sep='T')


# tests dash as separator and copies the renamed image into a temp directory
def test_flir_rename_newdir(test_data, tmpdir):
    """Test for PlantCV.Extras"""
    #subprocess.run(["which", "exiftool"])
    cache_dir = tmpdir.mkdir("cache")
    flir_rename(test_data.thermal_img, new_dir=cache_dir, sep='-')
    newname = os.listdir(cache_dir)[0]
    assert newname == "FLIR5612-2024_05_16T15_47.jpg"
