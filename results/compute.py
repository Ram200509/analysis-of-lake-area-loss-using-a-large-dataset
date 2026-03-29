import rasterio
import numpy as np
import matplotlib.pyplot as plt

def calculate_water_area(tif_path):
    with rasterio.open(tif_path) as src:
        nir = src.read(1).astype(np.float64)     # NIR
        green = src.read(3).astype(np.float64)   # Green
        
        denominator = green + nir
        denominator[denominator == 0] = np.nan
        
        ndwi = (green - nir) / denominator
        
        water_mask = ndwi > 0
        
        water_pixels = np.sum(water_mask)
        area_sqm = water_pixels * 100
        
        return water_mask, area_sqm

# ============================================================
# DATASET CONFIGURATION
# ============================================================
lakes = [
    ("Bellandur", r"D:\\Lake encroachment\\tif_files\\2018\\bellandur_lake_2018.tif", r"D:\\Lake encroachment\\tif_files\\2024\\bellandur_lake_2024.tif"),
    ("Sambhar", r"D:\\Lake encroachment\\tif_files\\2018\\sambhar_lake_2018.tif", r"D:\\Lake encroachment\\tif_files\\2024\\sambhar_lake_2024.tif"),
    ("Pulicat", r"D:\\Lake encroachment\\tif_files\\2018\\pulicat_lake_2018.tif", r"D:\\Lake encroachment\\tif_files\\2024\\pulicat_lake_2024.tif"),
    ("Dal", r"D:\\Lake encroachment\\tif_files\\2018\\dal_lake_2018.tif", r"D:\\Lake encroachment\\tif_files\\2024\\dal_lake_2024.tif"),
    ("Chilika", r"D:\\Lake encroachment\\tif_files\\2018\\chilika_lake_2018.tif", r"D:\\Lake encroachment\\tif_files\\2024\\chilika_lake_2024.tif"),
    ("Vembanad", r"D:\\Lake encroachment\\tif_files\\2018\\vembanad_lake_2018.tif", r"D:\\Lake encroachment\\tif_files\\2024\\vembanad_lake_2024.tif"),
    ("Loktak", r"D:\\Lake encroachment\\tif_files\\2018\\loktak_lake_2018.tif", r"D:\\Lake encroachment\\tif_files\\2024\\loktak_lake_2024.tif"),
    ("Hussain Sagar", r"D:\\Lake encroachment\\tif_files\\2018\\hussain_sagar_2018.tif", r"D:\\Lake encroachment\\tif_files\\2024\\hussain_sagar_2024.tif")
]

print("\nProcessing images and generating visualization...\n")

# ============================================================
# PLOTTING LOGIC
# ============================================================
rows = len(lakes)
fig, axes = plt.subplots(rows, 2, figsize=(12, 5 * rows), constrained_layout=True)
fig.patch.set_facecolor('#f0f0f0') 

for i, (lake_name, file_2018, file_2024) in enumerate(lakes):
    
    mask_2018, area_2018 = calculate_water_area(file_2018)
    mask_2024, area_2024 = calculate_water_area(file_2024)
    
    area_difference = area_2024 - area_2018
    change_status = "Gained" if area_difference > 0 else "Lost"
    text_color = 'green' if area_difference > 0 else 'red'

    title_2018 = f"{lake_name} (2018)\n{area_2018:,.0f} sqm"
    axes[i, 0].imshow(mask_2018, cmap='Blues_r')
    axes[i, 0].set_title(title_2018, fontsize=12, fontweight='bold', pad=10)
    axes[i, 0].axis("off")
    
    title_2024 = (f"{lake_name} (2024)\n"
                  f"{area_2024:,.0f} sqm\n"
                  f"{change_status}: {abs(area_difference):,.0f} m²")
    
    axes[i, 1].imshow(mask_2024, cmap='Blues_r')
    axes[i, 1].set_title(title_2024, fontsize=12, fontweight='bold', color=text_color, pad=10)
    axes[i, 1].axis("off")

plt.suptitle("Lake Water Area Change Analysis (2018 vs 2024)", fontsize=18, fontweight='bold', y=1.02)

# ==================== SAVE AS JPG ====================
plt.savefig('lake_water_masks_comparison.jpg', format='jpg', dpi=300, bbox_inches='tight')
print("Graph saved successfully as 'lake_water_masks_comparison.jpg'")

plt.show()