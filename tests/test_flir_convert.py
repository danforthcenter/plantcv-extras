import os
import pytest
from plantcv.extras.thermal import flir_convert


# tests fatal error if directory doesn't exist or cannot be found
def test_flir_convert_fatal_filename(test_data, tmpdir):
    """Test for PlantCV.Extras"""
    cache_dir = tmpdir.mkdir("cache")
    with pytest.raises(RuntimeError):
        flir_convert(pseudo_dir="test.jpg", csv_dir=cache_dir)


# tests the filtering by 'even' or a containing string and if the file already exists
def test_flir_convert_even(test_data, tmpdir):
    """Test for PlantCV.Extras"""
    cache_dir = tmpdir.mkdir("cache")
    # Define the path for the temporary file within that directory
    temp_file = cache_dir.join("FLIR5612.csv")
    # Create the file and write
    temp_file.write("test")
    flir_convert(test_data.datadir, csv_dir=cache_dir, thermal_index='even',
                 contains_str='FLIR')
    newname = os.listdir(cache_dir)[1]
    assert newname == "FLIR5612_new.csv"


# tests the filtering by 'odd' which should return nothing
def test_flir_convert_odd(test_data, tmpdir):
    """Test for PlantCV.Extras"""
    cache_dir = tmpdir.mkdir("cache")
    flir_convert(test_data.datadir, csv_dir=cache_dir, thermal_index='odd')
    assert len(os.listdir(cache_dir)) == 0
