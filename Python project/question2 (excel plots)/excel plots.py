import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

try:
    current_dir = Path(__file__).parent
except NameError:
    current_dir = Path.cwd()

file_path = current_dir / 'data.xlsx'

df = pd.read_excel(file_path)

df.columns = df.columns.str.strip()

first_col = df.columns[0]

df[first_col] = df[first_col].astype(str).str.replace('KB', '', regex=False).str.strip()
df[first_col] = pd.to_numeric(df[first_col])

df.set_index(first_col, inplace=True)


#-------Plotting and saving as PDF-------

# --- Line Chart ---
ax1 = df.plot(kind='line', marker='o', figsize=(8, 5))
ax1.set_title('Algorithm Run Times')
ax1.set_ylabel('Run Time')
ax1.grid(True)
plt.tight_layout()
plt.savefig(current_dir / 'line_chart.pdf')

# --- Bar Chart ---
ax2 = df.plot(kind='bar', figsize=(8, 5))
ax2.set_title('Algorithm Run Times (Bar Chart)')
ax2.set_ylabel('Run Time')
ax2.grid(axis='y')
plt.tight_layout()
plt.savefig(current_dir / 'bar_chart.pdf')

# --- Box Plot ---
ax3 = df.plot(kind='box', figsize=(8, 5))
ax3.set_title('Run Time Distribution by Algorithm')
ax3.set_ylabel('Run Time')
ax3.grid(axis='y')
plt.tight_layout()
plt.savefig(current_dir / 'box_plot.pdf')

print("All charts have been successfully saved as PDF files.")

plt.show()


# ------- Calculate Average for Alg.2 (100 to 600 KB) -------
if 'Alg.2' in df.columns:
    filtered_df = df.loc[(df.index >= 100) & (df.index <= 600)]
    avg_alg2 = filtered_df['Alg.2'].mean()
    print(f"Average run time for Alg.2 (100KB - 600KB): {avg_alg2:.2f}")
else:
    print("Column 'Alg.2' not found in the dataset.")
print("-" * 40)
