import ee

ee.Authenticate()
ee.Initialize(project="lake-encroachment-analysis")

# Bellandur Lake bounding box [Min Longitude, Min Latitude, Max Longitude, Max Latitude]
region = ee.Geometry.Rectangle([77.635, 12.915, 77.685, 12.950])

# ==========================================
# 2018 IMAGE (Older Baseline)
# ==========================================
collection_old = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED') \
    .filterBounds(region) \
    .filterDate('2018-01-01', '2018-12-31') \
    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 10)) \
    .select(['B8', 'B4', 'B3', 'B2']) # <-- Notice B8 (Near-Infrared) is now included

image_old = collection_old.median()

task_old = ee.batch.Export.image.toDrive(
    image=image_old,
    description='bellandur_lake_2018',
    folder='bellandur_data',
    scale=10,
    region=region,
    maxPixels=1e8
)
task_old.start()
print("Exporting 2018 Bellandur image...")

# ==========================================
# 2024 IMAGE (Recent Baseline)
# ==========================================
collection_new = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED') \
    .filterBounds(region) \
    .filterDate('2024-01-01', '2024-12-31') \
    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 10)) \
    .select(['B8', 'B4', 'B3', 'B2']) # <-- B8 included here too

image_new = collection_new.median()

task_new = ee.batch.Export.image.toDrive(
    image=image_new,
    description='bellandur_lake_2024',
    folder='bellandur_data',
    scale=10,
    region=region,
    maxPixels=1e8
)
task_new.start()
print("Exporting 2024 Bellandur image...")

print("Tasks submitted! Check your Google Drive 'bellandur_data' folder in a few minutes.")