import pandas as pd

# Data from your results
data = {
    'Lake Name': [
        'Bellandur', 'Sambhar', 'Pulicat', 'Dal', 'Chilika',
        'Vembanad', 'Loktak', 'Hussain Sagar'
    ],
    '2018 Water Area (sq m)': [
        1345900, 4462800, 510760900, 20306400, 437542900,
        119887300, 83702400, 1549600
    ],
    '2024 Water Area (sq m)': [
        753600, 28924900, 509153800, 13887700, 411424800,
        106871400, 63123300, 4513800
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate difference
df['Change (sq m)'] = df['2024 Water Area (sq m)'] - df['2018 Water Area (sq m)']

# Add status and color coding for display
df['Status'] = df['Change (sq m)'].apply(lambda x: 'Lost' if x < 0 else 'Gained')
df['Change (hectares)'] = (df['Change (sq m)'] / 10000).round(2)
df['Change (sq km)'] = (df['Change (sq m)'] / 1000000).round(4)

# Reorder columns to match your screenshot
df = df[['Lake Name', '2018 Water Area (sq m)', '2024 Water Area (sq m)', 
         'Change (sq m)', 'Status', 'Change (hectares)', 'Change (sq km)']]

# Print nicely formatted table
print("\n" + "="*80)
print("          LAKE WATER AREA CHANGE ANALYSIS (2018 vs 2024)")
print("="*80)
print(df.to_string(index=False))
print("="*80)

# Save to CSV (optional, for report)
df.to_csv('results/lake_area_summary_table.csv', index=False)
print("\nTable saved as 'results/lake_area_summary_table.csv'")