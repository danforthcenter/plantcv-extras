## Change Filenames of Thermal images 

This function changes the filenames of thermal images to include date and timestamp from metadata.

**plantcv.extras.thermal.flir_rename**(*filename, sep='_', test=True, new_dir=None*)


- **Parameters:**
    - filename - String of a path to an image or directory.
    - sep - Character that separates metadata terms of the filename. Needs to be set to '_' or '-'. If FLIR images start with FLIR and IR_ then you need to set sep to '-' otherwise there will be a different amount of metadata terms when running in parallel later on (default = '_'). 
    - test - (default = True).
    - new_dir - String of path to a new directory. Images in input directory stay unchanged while renamed images are copied to the new directory. New directory needs to exist (default = None).
- **Context:**
    - Used to rename filenames of thermal images to include date and time data. 


```python

from plantcv.extras import thermal as th

# change filename of a single image or a directory
th.flir_rename(filename=filename, sep='_')

```

**Source Code:** [Here](add link here)
