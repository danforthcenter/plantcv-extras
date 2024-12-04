import pytest
import os
import matplotlib

# Disable plotting
matplotlib.use("Template")


class TestData:
    def __init__(self):
        """Initialize simple variables."""
        # Test data directory
        self.datadir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testdata")
        # thermal image
        self.thermal_img = os.path.join(self.datadir, "FLIR5612.jpg")


@pytest.fixture(scope="session")
def test_data():
    """Test data object for the PlantCV-extras package."""
    return TestData()
