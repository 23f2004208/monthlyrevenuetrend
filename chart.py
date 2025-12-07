import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic monthly revenue data for different customer segments
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_numbers = list(range(1, 13))

# Create realistic revenue data for three customer segments
# Premium segment: Higher baseline, steady growth
premium_revenue = [85000 + i * 3500 + np.random.normal(0, 4000) for i in range(12)]

# Standard segment: Mid-range baseline, moderate growth with seasonal spike
standard_revenue = [52000 + i * 2000 + np.random.normal(0, 3000) + 
                   (8000 if i in [10, 11] else 0) for i in range(12)]

# Basic segment: Lower baseline, modest growth
basic_revenue = [28000 + i * 1200 + np.random.normal(0, 2000) for i in range(12)]

# Create DataFrame in long format for Seaborn
data = []
for i, month in enumerate(months):
    data.append({'Month': month, 'Month_Num': month_numbers[i], 
                 'Revenue': premium_revenue[i], 'Segment': 'Premium'})
    data.append({'Month': month, 'Month_Num': month_numbers[i], 
                 'Revenue': standard_revenue[i], 'Segment': 'Standard'})
    data.append({'Month': month, 'Month_Num': month_numbers[i], 
                 'Revenue': basic_revenue[i], 'Segment': 'Basic'})

df = pd.DataFrame(data)

# Set Seaborn style and context for professional appearance
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=0.9)

# Create figure with specified size for 512x512 output
plt.figure(figsize=(8, 8))

# Create lineplot with professional styling
sns.lineplot(data=df, x='Month_Num', y='Revenue', hue='Segment', 
             marker='o', linewidth=2.5, markersize=8,
             palette=['#2E86AB', '#A23B72', '#F18F01'])

# Customize the plot
plt.title('Monthly Revenue Trend Analysis by Customer Segment', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Month', fontsize=13, fontweight='semibold')
plt.ylabel('Revenue ($)', fontsize=13, fontweight='semibold')

# Set x-axis ticks to show month names
plt.xticks(month_numbers, months, rotation=45, ha='right')

# Format y-axis to show currency
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))

# Customize legend
plt.legend(title='Customer Segment', title_fontsize=11, fontsize=10, 
           loc='upper left', frameon=True, shadow=True)

# Add grid for better readability
plt.grid(True, alpha=0.3, linestyle='--', linewidth=0.7)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the figure as PNG with exactly 512x512 pixels
plt.savefig('chart.png', dpi=64, bbox_inches='tight')

print("Chart successfully generated and saved as 'chart.png'")
print(f"Image dimensions: 512x512 pixels")
