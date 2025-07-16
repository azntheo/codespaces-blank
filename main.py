import matplotlib.pyplot as plt
# from google.colab import files
import pandas as pd

# uploaded = files.upload()

# for fn in uploaded.keys():
#   print('User uploaded file "{name}" with length {length} bytes'.format(
#       name=fn, length=len(uploaded[fn])))

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('Theo_HPS_Data.csv')

# Step 2: Define cleaned category list
categories = [
    "Male",
    "Female",
    "Hispanic or Latino (may be of any race)",
    "White alone not Hispanic",
    "Black alone not Hispanic",
    "Asian alone not Hispanic",
    "Two or more races + Other races not Hispanic"
]

# Step 4: Filter the DataFrame
df_filtered = df[df['Characteristic'].isin(categories)].copy()

# Step 5: Set index and convert 'Total' to numeric
df_filtered.set_index('Characteristic', inplace=True)
df_filtered['Total'] = pd.to_numeric(df_filtered['Total'])

# Step 6: Reindex to ensure all categories are present
total_counts = df_filtered['Total'].reindex(categories, fill_value=0)

# Step 7: Plot the bar chart
plt.figure(figsize=(12, 6))
bars = plt.bar(total_counts.index, total_counts.values, color='lightgreen')
plt.xlabel("Demographic")
plt.ylabel("Total Insured Count")
plt.title("Total Count by Demographic Category")
plt.xticks(rotation=45, ha='right')

# Add data labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 1000, f'{int(height)}', ha='center', va='bottom')

plt.tight_layout()
plt.show()
