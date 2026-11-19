"""
Unit Tests for Ephemerides Downloader
Moonwalker Project - Lunar Landing Site Analysis Swarm

Sources:
    - Skyfield Documentation: https://rhodesmill.org/skyfield/
    - Python unittest documentation: https://docs.python.org/3/library/unittest.html
"""

import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

# Ensure src is discoverable in PYTHONPATH
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.ephemerides import download_ephemerides


class TestDownloadEphemerides(unittest.TestCase):
    """
    Test suite for download_ephemerides function verifying loader invocation,
    directory handling, and parameter passing.
    """

    @patch("src.ephemerides.Loader")
    def test_default_parameters(self, mock_loader_cls):
        """
        Tests download_ephemerides with default settings:
        kernel 'de421.bsp', cache directory 'data/ephemerides', reload=False.
        """
        # Configure mock loader instance and return value
        mock_loader_instance = MagicMock()
        mock_kernel = MagicMock()
        mock_loader_instance.return_value = mock_kernel
        mock_loader_cls.return_value = mock_loader_instance

        # Call function with defaults
        result = download_ephemerides()

        # Assert Loader was instantiated with default path 'data/ephemerides'
        mock_loader_cls.assert_called_once_with("data/ephemerides", verbose=False)
        # Assert kernel call was executed with de421.bsp and reload=False
        mock_loader_instance.assert_called_once_with("de421.bsp", reload=False)
        self.assertEqual(result, mock_kernel)

    @patch("src.ephemerides.Loader")
    def test_custom_parameters_and_dir_creation(self, mock_loader_cls, tmp_path=None):
        """
        Tests download_ephemerides with custom kernel name, cache dir,
        reload=True, and verbose=True.
        """
        mock_loader_instance = MagicMock()
        mock_kernel = MagicMock()
        mock_loader_instance.return_value = mock_kernel
        mock_loader_cls.return_value = mock_loader_instance

        custom_dir = Path("tests/scratch_cache_test")
        try:
            result = download_ephemerides(
                kernel_name="de440s.bsp",
                cache_dir=custom_dir,
                reload=True,
                verbose=True,
            )

            # Check that directory was created
            self.assertTrue(custom_dir.exists())
            mock_loader_cls.assert_called_once_with(str(custom_dir), verbose=True)
            mock_loader_instance.assert_called_once_with("de440s.bsp", reload=True)
            self.assertEqual(result, mock_kernel)
        finally:
            if custom_dir.exists():
                custom_dir.rmdir()


if __name__ == "__main__":
    unittest.main()
