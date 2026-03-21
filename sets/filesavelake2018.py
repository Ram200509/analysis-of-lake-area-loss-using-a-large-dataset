import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt
import numpy as np

# Path to your downloaded TIF file
file_path = "D:\\Lake encroachment\\bellandur_lake_2018.tif"
with rasterio.open(file_path) as src:
    # Read and normalize the data
    image_array = src.read([1, 2, 3])
    image_array = image_array / 10000.0
    image_array = np.clip(image_array, 0, 0.3) / 0.3 

    # Plot the image
    fig, ax = plt.subplots(figsize=(10, 10))
    show(image_array, transform=src.transform, ax=ax)
    
    plt.title('Bellandur Lake - 2018')
    plt.axis('off') 

    # --- NEW CODE: Save the plot as a JPG ---
    # dpi=300 ensures it is saved in high resolution
    # bbox_inches='tight' removes unnecessary white space around the borders
    plt.savefig('bellandur_lake_2018_render.jpg', format='jpg', dpi=300, bbox_inches='tight')
    print("Saved 'bellandur_lake_2018_render.jpg' to your current folder!")

    # Display the image window (Must come AFTER savefig)
    plt.show()