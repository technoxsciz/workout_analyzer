import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# Connect to Postgres
engine = create_engine("postgresql://postgres:192315@localhost:5432/workout_analyzer")

# Pull entire dataset into a DataFrame
df = pd.read_sql("SELECT * FROM exercises", engine)

# Quick overview
print(df.shape)
print(df.head())
print(df.dtypes)

# Clean equipment column - strip whitespace and invisible characters
df['equipment'] = df['equipment'].str.strip()

# Check how many unique equipment types we have now
print(df['equipment'].nunique())
print(df['equipment'].unique())

# Remove invisible zero-width space characters
df['equipment'] = df['equipment'].str.replace('\u200b', '', regex=False)

# Also clean up the messy names like "Assisted  Chest Dip  "
df['equipment'] = df['equipment'].str.replace(r'\s+', ' ', regex=True).str.strip()

# Check unique count now
print(df['equipment'].nunique())
print(df['equipment'].unique())

# --- CHART 1: Exercise count per muscle group ---
muscle_counts = df['main_muscle'].value_counts()

plt.figure(figsize=(10, 6))
plt.bar(muscle_counts.index, muscle_counts.values, color='violet')
plt.title('Number of Exercises per Muscle Group')
plt.xlabel('Muscle Group')
plt.ylabel('Number of Exercises')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('chart1_muscle_counts.png')
plt.show()
print("✅ Chart 1 saved!")

# --- CHART 2: Average difficulty per muscle group ---
avg_difficulty = df.groupby('main_muscle')['difficulty_1-5'].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(avg_difficulty.index, avg_difficulty.values, color='cyan')
plt.title('Average Difficulty per Muscle Group')
plt.xlabel('Muscle Group')
plt.ylabel('Average Difficulty (1-5)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('chart2_avg_difficulty.png')
plt.show()
print("✅ Chart 2 saved!")

# --- CHART 3: Equipment breakdown ---
equipment_counts = df['equipment'].value_counts().head(10)  # Top 10 only

plt.figure(figsize=(10, 6))
plt.bar(equipment_counts.index, equipment_counts.values, color='olive')
plt.title('Top 10 Equipment Types by Exercise Count')
plt.xlabel('Equipment')
plt.ylabel('Number of Exercises')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('chart3_equipment.png')
plt.show()
print("✅ Chart 3 saved!")

# --- CHART 4: Heatmap - Compound vs Isolated per muscle group ---
heatmap_data = df.groupby(['main_muscle', 'mechanics']).size().unstack(fill_value=0)

plt.figure(figsize=(10, 6))
plt.imshow(heatmap_data.values, cmap='YlOrRd', aspect='auto')
plt.colorbar(label='Number of Exercises')
plt.title('Compound vs Isolated Exercises per Muscle Group')
plt.xlabel('Mechanics')
plt.ylabel('Muscle Group')
plt.xticks(range(len(heatmap_data.columns)), heatmap_data.columns)
plt.yticks(range(len(heatmap_data.index)), heatmap_data.index)
plt.tight_layout()
plt.savefig('chart4_heatmap.png')
plt.show()
print("✅ Chart 4 saved!")