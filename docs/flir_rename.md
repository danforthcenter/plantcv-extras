## Change Filenames of Thermal images 

This function changes the filenames of thermal images to include date and timestamp from metadata.

**plantcv.extras.thermal.flir_rename**(*filename, sep='_', new_dir*)


- **Parameters:**
    - filename - Path to an image or directory.
    - sep - Character that separates metadata terms of the filename. Needs to be set to '\_' or '-' (default = '_'). 
    - new_dir - Path to a new directory. Images in input directory stay unchanged while renamed images are copied to the new directory. Note: New directory needs to exist.
- **Context:**
    - Used to rename filenames of thermal images to include date and time data.
    - Note: If you plan on running the renamed images in parallel later on, it is important to have the same number of metadata components in the filenames (see [Parallelization documentation](https://plantcv.readthedocs.io/en/stable/pipeline_parallel/)). FLIR image names start with FLIR but switch to IR_ once 10000 images are reached. If your dataset contains a combination of both "FLIR_##" and "IR_##" then you need to use '-' as a separator otherwise images will have different numbers of metadata terms in the filename when running in parallel.


```python

from plantcv.extras import thermal as th

# change filename of a single image or a directory
th.flir_rename(filename="home/user/images/raw/FLIR1234.jpg", sep='_', new_dir="home/user/images/renamed/")

```

**Source Code:** [Here](https://github.com/danforthcenter/plantcv-extras/blob/main/plantcv/extras/thermal/flir_rename.py)
