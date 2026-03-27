import ee

ee.Authenticate()      # Run only once
ee.Initialize(project="lake-encroachment-analysis")

# ==================== LIST OF LAKES ====================
lakes = {
    "Bellandur":        [77.635, 12.915, 77.685, 12.950],   
    "Sambhar":          [74.95,  26.85,  75.30,  27.10],    
    "Pulicat":          [80.15,  13.40,  80.35,  13.70],    
    "Dal":              [74.80,  34.05,  74.90,  34.15],    
    "Chilika":          [85.00,  19.60,  85.40,  19.85],    
    "Vembanad":         [76.35,  9.40,   76.55,  9.70],     
    "Loktak":           [93.75,  24.40,  93.95,  24.60]   
}

years = [2018, 2024]

print("Starting export for multiple lakes...\n")

for lake_name, bbox in lakes.items():
    region = ee.Geometry.Rectangle(bbox)
    
    for year in years:
        collection = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED') \
            .filterBounds(region) \
            .filterDate(f'{year}-01-01', f'{year}-12-31') \
            .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 10)) \
            .select(['B8', 'B4', 'B3', 'B2'])

        image = collection.median()

        task = ee.batch.Export.image.toDrive(
            image=image,
            description=f'{lake_name.lower()}_lake_{year}',
            folder='multi_lake_data',
            scale=10,
            region=region,
            maxPixels=1e8
        )
        task.start()
        
        print(f"Exporting {lake_name} Lake - {year} ...")

print("\nAll tasks submitted successfully!")
print("Go to your Google Drive → 'multi_lake_data' folder and download the .tif files.")