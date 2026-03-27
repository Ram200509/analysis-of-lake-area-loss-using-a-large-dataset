import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt
import numpy as np
import os

# Add all your TIF file paths here
file_paths = [
    r"D:\\Lake encroachment\\tif_files\\2018\\bellandur_lake_2018.tif",
    r"D:\\Lake encroachment\\tif_files\\2018\\sambhar_lake_2018.tif",
    r"D:\\Lake encroachment\\tif_files\\2018\\pulicat_lake_2018.tif",
    r"D:\\Lake encroachment\\tif_files\\2018\\dal_lake_2018.tif",
    r"D:\\Lake encroachment\\tif_files\\2018\\chilika_lake_2018.tif",
    r"D:\\Lake encroachment\\tif_files\\2018\\vembanad_lake_2018.tif",
    r"D:\\Lake encroachment\\tif_files\\2018\\loktak_lake_2018.tif",
    r"D:\\Lake encroachment\\tif_files\\2018\\hussain_sagar_2018.tif"
]

for file_path in file_paths:

    with rasterio.open(file_path) as src:
        
        # Read and normalize
        image_array = src.read([1, 2, 3])
        image_array = image_array / 10000.0
        image_array = np.clip(image_array, 0, 0.3) / 0.3

        # Create figure
        fig, ax = plt.subplots(figsize=(10, 10))
        show(image_array, transform=src.transform, ax=ax)

        # Extract lake name automatically
        file_name = os.path.basename(file_path)   # bellandur_lake_2018.tif
        lake_name = file_name.replace(".tif", "") # bellandur_lake_2018

        plt.title(f"{lake_name.replace('_', ' ').title()}")
        plt.axis('off')

        # Save JPG
        output_name = f"{lake_name}_render.jpg"
        plt.savefig(output_name, format='jpg', dpi=300, bbox_inches='tight')
        
        print(f"Saved '{output_name}' successfully!")

        plt.close(fig)  # Important: prevents memory overload