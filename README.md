# Multi-Temporal Analysis of Indian Lakes Using Sentinel-2 Imagery and NDWI (2018–2024)

**Author:** Pranav Prayaga  
**Internship:** IDEAS @ Indian Statistical Institute, Kolkata (Spring 2026)  
**Branch:** `lake_area_variation_analysis` (Individual Contribution)  
**Project Type:** Standalone Chapter for Group Repository

---

## Project Overview

This project performs satellite-based analysis and quantification of **lake water area changes** across 8 major Indian lakes between 2018 and 2024.

Using **Google Earth Engine**, **Sentinel-2 imagery**, and the **Normalized Difference Water Index (NDWI)**, the workflow:

- Extracts multi-temporal satellite data
- Computes water masks using NDWI
- Quantifies water area (sq.m, hectares, sq.km)
- Detects water gain/loss due to encroachment and drying
- Generates visual comparisons, bar graphs, and summary tables

**Bellandur Lake** was used as the primary proof-of-concept. The same pipeline was applied to 7 other critically affected lakes.

---

## Lakes Analyzed
- Bellandur Lake (Bengaluru)
- Sambhar Lake (Rajasthan)
- Pulicat Lake (Tamil Nadu)
- Dal Lake (Jammu & Kashmir)
- Chilika Lake (Odisha)
- Vembanad Lake (Kerala)
- Loktak Lake (Manipur)
- Hussain Sagar Lake (Hyderabad)

---

## Technologies Used
- Python 3.x
- Google Earth Engine (Python API)
- Sentinel-2 Surface Reflectance (COPERNICUS/S2_SR_HARMONIZED)
- Rasterio, NumPy, Matplotlib, Pandas

---

## Project Structure

```bash
lake_area_variation_analysis/
├── data/
│   ├── 2018_renders/
│   │   ├── bellandur_lake_2018_render.jpg
│   │   ├── sambhar_lake_2018_render.jpg
│   │   ├── pulicat_lake_2018_render.jpg
│   │   ├── dal_lake_2018_render.jpg
│   │   ├── chilika_lake_2018_render.jpg
│   │   ├── vembanad_lake_2018_render.jpg
│   │   ├── loktak_lake_2018_render.jpg
│   │   └── hussain_sagar_lake_2018_render.jpg
│   ├── 2024_renders/
│   │   ├── bellandur_lake_2024_render.jpg
│   │   ├── sambhar_lake_2024_render.jpg
│   │   ├── pulicat_lake_2024_render.jpg
│   │   ├── dal_lake_2024_render.jpg
│   │   ├── chilika_lake_2024_render.jpg
│   │   ├── vembanad_lake_2024_render.jpg
│   │   ├── loktak_lake_2024_render.jpg
│   │   └── hussain_sagar_lake_2024_render.jpg
│   ├── Lakes_2018_renders.png
│   └── Lakes_2024_renders.png
├── results/
|   ├──compute.py
|   ├── graph.py
|   ├──tablevalues.py
│   ├── lake_area_comparison_graph_final.png
│   ├── lake_water_masks_comparison.jpg
│   ├── Result_data2.png
│   ├── summarytable.png
│   └── lake_area_summary_table.csv
├── scripts/
│   └── data_collection.py
├── sets/
│   ├── 2018lake.py
│   ├── 2024lake.py
│   ├── filesavelake2018.py
│   └── filesavelake2024.py
├── equation.png
├── requirements.txt
├── README.md
└── .gitignore
```
---

## NDWI Calculation

NDWI = (Green - NIR) / (Green + NIR)

- **Green** = Band 3  
- **NIR** = Band 8  

Water pixels are identified where **NDWI > 0**.

**Water Area Calculation**  
Each pixel = 10 m × 10 m → **100 sq.m**  
Water Area = (Number of water pixels × 100)

**Change Detection**  
Change = Area₂₀₂₄ − Area₂₀₁₈  
(Positive = Gained | Negative = Lost)

---

## Key Results

**6 out of 8 lakes showed net water loss.**

**Example Summary Table** (saved as `results/lake_area_summary_table.csv`):

| Lake Name     | 2018 Area (sq m) | 2024 Area (sq m) | Change (sq m)   | Status   |
|---------------|------------------|------------------|-----------------|----------|
| Bellandur     | 1,345,900        | 753,600          | -592,300        | Lost     |
| Sambhar       | 4,462,800        | 28,924,900       | +24,462,100     | Gained   |
| Chilika       | 437,542,900      | 411,424,800      | -26,118,100     | Lost     |
| Loktak        | 83,702,400       | 63,123,300       | -20,579,100     | Lost     |

(Full table available in `results/` folder)

---

## Visual Outputs

**1. Water Mask Comparison (2018 vs 2024)**  
![Water Mask Comparison](results/lake_water_masks_comparison.jpg)

**2. Lake Water Area Comparison Graph (2018 vs 2024)**  
![Area Comparison Graph](results/lake_area_comparison_graph_final.png)

**3. Satellite Image Renders**  
- 2018 Renders  `data/Lakes_2018_renders.png`  
- 2024 Renders  `data/Lakes_2024_renders.png`

---

## How to Run the Project

1. Clone this branch:
   git clone -b lake-area-change-analysis https://github.com/sm7313617-create/Overhead-Satellite-Drone-Image-Analysis.git
   cd Overhead-Satellite-Drone-Image-Analysis

2. Set up virtual environment
  python -m venv venv
  For Windows - 'venv/scripts/activate.bash

3. Install dependencies: 
   pip install -r requirements.txt

4. Run scripts in order:
   python scripts/data_collection.py     # (only if you need fresh TIFs)
   python compute.py
   python graph.py
   python tablevalues.py
All outputs will be saved in the results/ folder.

## Applications
1. Lake encroachment monitoring
2. Urban expansion impact assessment
3. Hydrological change detection
4. Environmental policy planning

# Author
Pranav Prayaga
Computer Science Student | Remote Sensing & Environmental Data Analysis Enthusiast
