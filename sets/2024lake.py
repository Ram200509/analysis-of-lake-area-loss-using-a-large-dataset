import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt
import numpy as np

# Path to your downloaded TIF file
file_path = "D:\\Lake encroachment\\bellandur_lake_2024.tif"

with rasterio.open(file_path) as src:
    # Read the data (Bands 1, 2, and 3 which correspond to Red, Green, Blue)
    # The data comes in as a NumPy array
    image_array = src.read([1, 2, 3])
    
    # Sentinel-2 data is often stored as raw integers (0-10000)
    # We normalize it to a 0-1 range for matplotlib to display it beautifully
    image_array = image_array / 10000.0
    
    # Clip any bright outliers to keep the image from looking washed out
    image_array = np.clip(image_array, 0, 0.3) / 0.3 

    # Plot the image
    fig, ax = plt.subplots(figsize=(10, 10))
    # rasterio's show() handles the coordinate mapping
    show(image_array, transform=src.transform, ax=ax)
    
    plt.title('Hussain Sagar Lake - 2024')
    plt.axis('off') # Hides the coordinate axes for a cleaner look
    plt.show()