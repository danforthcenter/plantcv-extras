import os
import pytest
from plantcv.extras.thermal import flir_rename


# tests fatal error if file doesn't exist or cannot be found
def test_flir_rename_fatal_filename(test_data):
    """Test for PlantCV.Extras"""
    with pytest.raises(RuntimeError):
        flir_rename(filename="test.jpg", sep='_', test=True, new_dir=None)


# tests fatal error if separator is not dash or underscore
def test_flir_rename_fatal_sep(test_data):
    """Test for PlantCV.Extras"""
    # Read in a test pseudo colored thermal image
    with pytest.raises(RuntimeError):
        flir_rename(test_data.datadir, sep='T', test=True, new_dir=None)


# tests dash as separator and copies the renamed image into a temp directory
def test_flir_rename_newdir(test_data, tmpdir):
    """Test for PlantCV.Extras"""
    cache_dir = tmpdir.mkdir("cache")
    # Read in a test pseudo colored thermal image
    flir_rename(test_data.datadir, sep='-', test=False, new_dir=cache_dir)
    newname = os.listdir(cache_dir)[0]
    assert newname == "FLIR5612-2024_05_16T15_47.jpg"
