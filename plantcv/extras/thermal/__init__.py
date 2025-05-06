from importlib.metadata import version

# Auto versioning
__version__ = version("plantcv")

from plantcv.extras.thermal.flir_rename import flir_rename
from plantcv.extras.thermal.flir_convert import flir_convert


__all__ = [
    "flir_rename",
    "flir_convert"
]
