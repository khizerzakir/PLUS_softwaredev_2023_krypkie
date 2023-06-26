# A4: modules, functions and imports¶
This notebook will provide explanation of the module's functions, their purpose, and dependencies. It also includes an example usage section to demonstrate how to use the functions in practice.
It tries to use relevant but simple geofunctions to perform basic analysis on raster data. However the primary objective of this exercise is to understand the packaging of functions as separate libraries and the utilization of docstrings in the documentation process.
This module provides functions for reading, analyzing, and visualizing raster data. It leverages various Python libraries, including xarray, rasterio, pandas, and numpy, to perform different operations on raster datasets.

This module provides functions for reading, analyzing, and visualizing raster data. It leverages various Python libraries, including xarray, rasterio, pandas, and numpy, to perform different operations on raster datasets.

## Function Overview

- `read_and_plot_tiff(file_path)`: This function searches for a TIFF file in the specified directory, reads it using rasterio and xarray, plots each band individually, plots the combined bands, and displays the raster cell values.

- `plot_raster_with_coordinates(path_tiff)`: This function opens a TIFF file using rasterio, reads the raster data, and plots the raster image with the original coordinate system.

- `calculate_ndvi(path_tiff)`: This function calculates the NDVI (Normalized Difference Vegetation Index) for a raster file using rasterio and numpy. It returns the normalized NDVI values as a numpy array.

- `plot_ndvi(ndvi)`: This function plots the NDVI image using matplotlib, visualizing the vegetation index.

- `print_ndvi_stats(ndvi)`: This function calculates and prints statistics for the NDVI values, including the minimum, maximum, mean, median, and standard deviation.

- `get_top_ndvi_values(ndvi, num_values=10)`: This function retrieves the top N NDVI values and their corresponding indices, creating a pandas DataFrame to store the results.

- `draw_square_on_raster(path_tiff)`: This function opens a raster image using rasterio, reads the raster data, and allows the user to input coordinates to draw a square on the image using matplotlib.

## Dependencies

This module depends on the following Python libraries:
- [xarray](https://xarray.pydata.org/)
- [rasterio](https://rasterio.readthedocs.io/)
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)

Make sure to install these libraries before using the functions in this module.

## Example Usage (Provided in the start of each section)
