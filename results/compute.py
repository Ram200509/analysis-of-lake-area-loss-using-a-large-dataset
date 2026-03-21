import rasterio
import numpy as np
import matplotlib.pyplot as plt

def calculate_water_area(tif_path):
    try:
        with rasterio.open(tif_path) as src:
            # In your Earth Engine script, you exported: ['B8', 'B4', 'B3', 'B2']
            # rasterio uses 1-based indexing, so:
            # Band 1 = B8 (Near-Infrared)
            # Band 2 = B4 (Red)
            # Band 3 = B3 (Green)
            # Band 4 = B2 (Blue)
            
            nir = src.read(1).astype(float)
            green = src.read(3).astype(float)
            
            # Suppress divide-by-zero warnings for blank pixels at the edges
            np.seterr(divide='ignore', invalid='ignore')
            
            # Calculate NDWI: (Green - NIR) / (Green + NIR)
            ndwi = (green - nir) / (green + nir)
            
            # Create a pure binary water mask. 
            # If NDWI > 0, it is strictly water.
            water_mask = ndwi > 0
            
            # Count the true water pixels
            water_pixels = np.sum(water_mask)
            
            # 1 pixel = 10m x 10m = 100 sq meters
            area_sqm = water_pixels * 100 
            
            return water_mask, water_pixels, area_sqm
            
    except FileNotFoundError:
        print(f"ERROR: Could not find {tif_path}. Make sure the TIF files have finished downloading from Google Drive!")
        exit()

# File paths to your downloaded TIFs
file_2018 = "D:\\Lake encroachment\\bellandur_lake_2018_render.jpg"
file_2024 = "D:\\Lake encroachment\\bellandur_lake_2024_render.jpg"

print("Analyzing raw satellite data using NDWI...")

# Process both years
mask_2018, pixels_2018, area_2018 = calculate_water_area(file_2018)
mask_2024, pixels_2024, area_2024 = calculate_water_area(file_2024)

# Calculate the difference
encroached_pixels = pixels_2018 - pixels_2024
encroached_sqm = encroached_pixels * 100

print("\n========================================")
print("       SCIENTIFIC AREA CALCULATIONS       ")
print("========================================")
print(f"2018 Water Area:  {area_2018:,.2f} sq meters")
print(f"2024 Water Area:  {area_2024:,.2f} sq meters")
print("----------------------------------------")

if encroached_pixels > 0:
    print(f"LOST WATER AREA (Encroachment/Drying):")
    print(f" -> {encroached_sqm:,.2f} sq meters")
    print(f" -> {encroached_sqm / 10000:,.2f} hectares")
    print(f" -> {encroached_sqm / 1000000:,.4f} sq kilometers")
elif encroached_pixels < 0:
    print(f"WATER AREA INCREASED BY:")
    print(f" -> {abs(encroached_sqm):,.2f} sq meters")
else:
    print("No change in water area detected.")
print("========================================\n")

# Visually prove the results by plotting the true mathematical masks
print("Opening visualization window...")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Display 2018 Mask
ax1.imshow(mask_2018, cmap='Blues')
ax1.set_title('2018 True Water Mask (NDWI > 0)')
ax1.axis('off')

# Display 2024 Mask
ax2.imshow(mask_2024, cmap='Blues')
ax2.set_title('2024 True Water Mask (NDWI > 0)')
ax2.axis('off')

plt.tight_layout()
plt.show()