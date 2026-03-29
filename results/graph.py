import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# ==================== DATA ====================
lakes = ['Bellandur', 'Sambhar', 'Pulicat', 'Dal', 'Chilika', 
         'Vembanad', 'Loktak', 'Hussain Sagar']

area_2018 = [1345900, 4462800, 510760900, 20306400, 437542900, 
             119887300, 83702400, 1549600]

area_2024 = [753600, 28924900, 509153800, 13887700, 411424800, 
             106871400, 63123300, 4513800]

x = np.arange(len(lakes))
width = 0.35

fig, ax = plt.subplots(figsize=(18, 11))

bars1 = ax.bar(x - width/2, area_2018, width, label='2018', color='#1f77b4')
bars2 = ax.bar(x + width/2, area_2024, width, label='2024', color='#ff7f0e')

# Y-axis increased to 700 million as requested
ax.set_ylim(0, 700_000_000)

def full_number(x, pos):
    return f'{int(x):,}'

ax.yaxis.set_major_formatter(FuncFormatter(full_number))
ax.set_ylabel('Water Area (Square Meters)', fontsize=14, fontweight='bold')
ax.set_title('Lake Water Area Comparison: 2018 vs 2024', fontsize=16, fontweight='bold', pad=30)

ax.set_xticks(x)
ax.set_xticklabels(lakes, fontsize=12, rotation=0, ha='center')

ax.legend(fontsize=12, loc='upper right')

# Diagonal labels above bars
def autolabel(bars):
    for bar in bars:
        height = bar.get_height()
        if height == 0:
            continue
        ax.annotate(f'{height:,.0f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 18),
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=10, fontweight='bold',
                    rotation=45)

autolabel(bars1)
autolabel(bars2)

# Scale note at top-right
ax.text(0.98, 0.92, "Y-axis\n1 unit = 100,000,000 sqm", 
        transform=ax.transAxes, fontsize=10, 
        verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.savefig('results/lake_area_comparison_graph_final.png', dpi=300, bbox_inches='tight')
plt.show()

print("Final graph saved successfully!")