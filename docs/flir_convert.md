## Convert thermal images to .csv 

This function converts thermal .jpg into .csv.

**plantcv.extras.thermal.flir_convert**(*pseudo_dir, csv_dir, thermal_index=None, contains_str=None*)


- **Parameters:**
    - pseudo_img - Path to a directory.
    - csv_dir - Path to a directory where csv output files are saved. Note: New directory needs to exist.
    - thermal_index - Filter (optional) that selects thermal images to convert based on if the first number in the filename is 'even' or 'odd'. Example: FLIR1234_11-03-2001.jpg > even.
    - contains_str = Filter (optional) that selects thermal images to convert based on a containing substring.
- **Context:**
    - Used to convert thermal images from .jpg to .csv.


```python

from plantcv.extras import thermal as th

# 
th.flir_convert(pseudo_dir="home/user/images/thermal/pseudo", csv_dir="./thermal_csv", thermal_index='even')

```

**Source Code:** [Here](https://github.com/danforthcenter/plantcv-extras/blob/main/plantcv/extras/thermal/flir_convert.py)
