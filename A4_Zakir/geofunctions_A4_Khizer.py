"""
This module provides functions for working with raster data in TIFF format, including reading, plotting, and analyzing
raster images. It utilizes the rasterio, xarray, matplotlib, numpy, and pandas libraries for various operations.

Functions:
- read_and_plot_tiff(file_path): Searches for a TIFF file in the given file path, reads it using rasterio and xarray,
    plots all the bands individually and the combined bands, and displays the raster cell values. Returns the raster dataset.
- plot_raster_with_coordinates(path_tiff): Opens a TIFF file using rasterio, reads the raster data, and plots the raster
    image with the original coordinate system. Returns the coordinate system name.
- calculate_ndvi(path_tiff): Calculates the NDVI (Normalized Difference Vegetation Index) for a raster file. Returns
    the normalized NDVI values.
- plot_ndvi(ndvi): Plots the NDVI image.
- print_ndvi_stats(ndvi): Prints the statistics for the NDVI.
- get_top_ndvi_values(ndvi, num_values=10): Retrieves the top N NDVI values and their corresponding indices. Returns
    a pandas DataFrame containing the top NDVI values and indices.
- draw_square_on_raster(path_tiff): Draws a small square on a raster image.

Dependencies:
- os, glob: For file path handling and searching.
- matplotlib.pyplot: For plotting raster images.
- xarray: For handling raster datasets.
- rasterio, rasterio.plot: For reading and visualizing raster data.
- numpy: For numerical operations on raster data.
- pandas: For creating vector tables and statistics calculations.

Note: These functions assume the input raster files are in TIFF format and follow specific band order conventions.

Please make sure to have the necessary dependencies installed before using these functions.
"""

import os
import glob
import matplotlib.pyplot as plt
import xarray as xr
import rasterio
from rasterio.plot import show
import numpy as np
import pandas as pd


def read_and_plot_tiff(file_path):
    """
    Searches for a TIFF file in the given file path, reads it using rasterio and xarray,
    plots all the bands individually and the combined bands, and displays the raster cell values.

    Args:
        file_path (str): The path to the directory containing the TIFF file.

    Returns:
        xarray.Dataset: The raster dataset.
    """
    tiff_files = glob.glob(os.path.join(file_path, "*.tif"))
    if not tiff_files:
        raise ValueError("No TIFF files found in the specified path.")

    with rasterio.open(tiff_files[0]) as src:
        raster_data = src.read()

    raster_dataset = xr.DataArray(raster_data, dims=('band', 'y', 'x'), name='raster')

    # Plot individual bands
    num_bands = raster_dataset.shape[0]
    num_rows = (num_bands + 1) // 2  # Calculate the number of rows needed

    fig, axes = plt.subplots(nrows=num_rows, ncols=2, figsize=(12, 4*num_rows))

    for band, ax in zip(range(num_bands), axes.flatten()):
        ax.imshow(raster_dataset[band], cmap='viridis')
        ax.set_title(f'Band {band+1}')
        ax.axis('on')

    plt.tight_layout()
    plt.show()

    # Plot combined bands
    combined_image = raster_dataset.mean(dim='band')
    plt.imshow(combined_image, cmap='viridis')
    plt.title('Combined Bands')
    plt.colorbar(label='Pixel Value')
    plt.axis('on')
    plt.show()

    # Display raster cell values
    print("Raster Cell Values:")
    print(raster_dataset)

    return raster_dataset


def plot_raster_with_coordinates(path_tiff):
    """
    Opens a TIFF file using rasterio, reads the raster data, and plots the raster image
    with the original coordinate system.

    Args:
        path_tiff (str): The path to the TIFF file.

    Returns:
        str: The coordinate system name.
    """
    with rasterio.open(path_tiff) as src:
        # Read the raster data
        raster_data = src.read()

        # Get the coordinate system name
        crs_name = src.crs.to_string()

        # Get the raster coordinates for each corner of the image
        xmin, ymin = src.bounds.left, src.bounds.bottom
        xmax, ymax = src.bounds.right, src.bounds.top

        # Plot the raster image
        plt.imshow(raster_data.transpose(1, 2, 0), extent=[xmin, xmax, ymin, ymax])
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        plt.title('Raster Image - Coordinate System: {}'.format(crs_name))
        plt.colorbar(label='Pixel Value')
        plt.show()

        # Return the coordinate system name
        return crs_name


def calculate_ndvi(path_tiff):
    """
    Calculates the NDVI (Normalized Difference Vegetation Index) for a raster file.

    Args:
        path_tiff (str): The path to the TIFF file.

    Returns:
        numpy.ndarray: The normalized NDVI values.
    """
    with rasterio.open(path_tiff) as src:
        # Read the raster bands
        bands = src.read()

        # Identify the red and near-infrared bands
        red_band = bands[2]  # Band 3
        nir_band = bands[3]  # Band 4

        # Calculate the NDVI
        denominator = nir_band + red_band
        ndvi = np.where(denominator != 0, (nir_band - red_band) / denominator, 0)

        # Normalize the NDVI values to the range -1 to +1
        ndvi = np.clip(ndvi, -1, 1)

    return ndvi

def plot_ndvi(ndvi):
    """
    Plots the NDVI image.

    Args:
        ndvi (numpy.ndarray): The NDVI values.
    """
    plt.imshow(ndvi, cmap='RdYlGn', vmin=-1, vmax=1)
    plt.title('Normalized Difference Vegetation Index (NDVI)')
    plt.colorbar(label='NDVI')
    plt.show()

def print_ndvi_stats(ndvi):
    """
    Prints the statistics for the NDVI.

    Args:
        ndvi (numpy.ndarray): The NDVI values.
    """
    print("NDVI Statistics:")
    print("Minimum:", np.nanmin(ndvi))
    print("Maximum:", np.nanmax(ndvi))
    print("Mean:", np.nanmean(ndvi))
    print("Median:", np.nanmedian(ndvi))
    print("Standard Deviation:", np.nanstd(ndvi))
    

def get_top_ndvi_values(ndvi, num_values=10):
    """
    Retrieves the top N NDVI values and their corresponding indices.

    Args:
        ndvi (numpy.ndarray): The NDVI values.
        num_values (int): The number of top values to retrieve. Default is 10.

    Returns:
        pandas.DataFrame: The vector table containing the top NDVI values and indices.
    """
    # Flatten the NDVI array and retrieve the top N values and indices
    flat_ndvi = ndvi.flatten()
    top_indices = flat_ndvi.argsort()[-num_values:][::-1]
    top_values = flat_ndvi[top_indices]

    # Create a pandas DataFrame for the vector table
    df = pd.DataFrame({'NDVI': top_values, 'Index': top_indices})

    return df



def draw_square_on_raster(path_tiff):
    """
    Draws a small square on a raster image.

    Args:
        path_tiff (str): The path to the raster file.

    Returns:
        None
    """
    # Open the raster image
    with rasterio.open(path_tiff) as src:
        # Read the raster data
        raster_data = src.read()

    # Plot the raster image
    plt.imshow(raster_data.transpose(1, 2, 0))

    # Prompt the user to input square coordinates
    print("Enter the coordinates for the square:")
    xmin = int(input("xmin (x > 200): "))
    ymin = int(input("ymin (y > 200): "))
    xmax = int(input("xmax (x < 400): "))
    ymax = int(input("ymax (y < 400): "))

    # Draw the square on the image
    plt.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], color='red')

    # Display the plot
    plt.show()






