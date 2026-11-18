"""
Ephemerides Downloader Module
Moonwalker Project - Lunar Landing Site Analysis Swarm

Sources:
    - Skyfield Documentation: https://rhodesmill.org/skyfield/planets.html
    - Rhodes, B., Skyfield: High precision astronomy for Python,
      Astrophysics Source Code Library, ascl:1907.024, 2019.
    - NASA JPL Solar System Dynamics (SSD) Ephemerides:
      https://ssd.jpl.nasa.gov/planets/eph_export.html
"""

from pathlib import Path
from typing import Union
from skyfield.api import Loader
from skyfield.jpllib import SpiceKernel


def download_ephemerides(
    kernel_name: str = "de421.bsp",
    cache_dir: Union[str, Path, None] = None,
    reload: bool = False,
    verbose: bool = False,
) -> SpiceKernel:
    """
    Downloads and loads JPL ephemerides of celestial bodies using Skyfield.

    This function fetches a NASA JPL SPICE kernel (.bsp file) if not already
    cached locally, and loads it into a Skyfield SpiceKernel object. The kernel
    provides high-precision positions and velocities for celestial bodies
    (e.g., Earth, Moon, Sun, planetary barycenters).

    Physical Quantities & Units:
        - Position coordinates: Distance in kilometers [km] or Astronomical Units [au]
        - Velocity vectors: Speed in kilometers per second [km/s] or [au/day]
        - Epoch / Time: Barycentric Dynamical Time (TDB) [s] / Julian Date [day]

    Sources:
        - Rhodes, B. (2019). Skyfield: Elegant Astronomy for Python.
          URL: https://rhodesmill.org/skyfield/
        - Folkner, W. M., et al. (2014). The Planetary and Lunar Ephemeris
          DE430 and DE431. IPN Progress Report 42-196, JPL/NASA.
          URL: https://ssd.jpl.nasa.gov/planets/eph_export.html

    Parameters:
        kernel_name (str): Filename or URL of the SPICE kernel to download.
            Defaults to 'de421.bsp' (covers 1900-2050, ~17 MB).
        cache_dir (str | Path | None): Directory path to cache downloaded files.
            Defaults to 'data/ephemerides' relative to current working directory.
        reload (bool): If True, forces redownload even if file is cached locally.
        verbose (bool): If True, displays download progress bar to standard output.

    Returns:
        SpiceKernel: Skyfield SPICE kernel object containing celestial body data.
    """
    # Resolve target cache directory and ensure it exists
    target_dir = Path(cache_dir) if cache_dir is not None else Path("data/ephemerides")
    target_dir.mkdir(parents=True, exist_ok=True)

    # Initialize Skyfield loader with designated cache directory
    loader = Loader(str(target_dir), verbose=verbose)

    # Fetch (if not already cached) and load the SPICE kernel
    ephemeris_kernel: SpiceKernel = loader(kernel_name, reload=reload)

    return ephemeris_kernel
