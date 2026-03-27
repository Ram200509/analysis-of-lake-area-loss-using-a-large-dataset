import rasterio
import matplotlib.pyplot as plt
import numpy as np

file_paths = [
    r"D:\\Lake encroachment\\tif_files\\2024\\bellandur_lake_2024.tif",
    r"D:\\Lake encroachment\\tif_files\\2024\\sambhar_lake_2024.tif",
    r"D:\\Lake encroachment\\tif_files\\2024\\pulicat_lake_2024.tif",
    r"D:\\Lake encroachment\\tif_files\\2024\\dal_lake_2024.tif",
    r"D:\\Lake encroachment\\tif_files\\2024\\chilika_lake_2024.tif",
    r"D:\\Lake encroachment\\tif_files\\2024\\vembanad_lake_2024.tif",
    r"D:\\Lake encroachment\\tif_files\\2024\\loktak_lake_2024.tif",
    r"D:\\Lake encroachment\\tif_files\\2024\\hussain_sagar_2024.tif"
]

# Create grid
rows = 3
cols = 3
fig, axes = plt.subplots(rows, cols, figsize=(15, 15))

axes = axes.flatten()  # Convert 2D array of axes to 1D for easy indexing

for i, file_path in enumerate(file_paths):
    
    with rasterio.open(file_path) as src:
        image_array = src.read([1, 2, 3])
        
        # Normalize Sentinel-2 values
        image_array = image_array / 10000.0
        image_array = np.clip(image_array, 0, 0.3) / 0.3
        
        # Rearrange from (bands, height, width) → (height, width, bands)
        image_array = np.transpose(image_array, (1, 2, 0))
        
        axes[i].imshow(image_array)
        
        lake_name = file_path.split("\\")[-1].split("_")[0]
        axes[i].set_title(f"{lake_name.capitalize()} - 2024")
        axes[i].axis("off")

# Hide unused subplots (since 9 spaces but 7 images)
for j in range(len(file_paths), rows * cols):
    axes[j].axis("off")

plt.tight_layout()
plt.show()