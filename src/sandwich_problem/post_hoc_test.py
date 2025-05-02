from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# The input and output variables
file_path = 'datasets/sandwich.csv'

# Read the data from the CSV file
def read_csv_file(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found. Please ensure the file is in the correct directory.")
        exit()  # Exit the script if the file is missing
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded data from '{file_path}'.")
        print("-" * 69)
        return df
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        exit()  # Exit if there's an error during file reading

# --- 1. Load Data ---
df = read_csv_file(file_path)

# convert to category
df['topping'] = df['topping'].astype('category')

# Post-hoc Test for topping
tukey = pairwise_tukeyhsd(endog=df['antCount'],
                          groups=df['topping'],
                          alpha=0.05)

print(tukey)
tukey.plot_simultaneous()
plt.title("Tukey HSD for Topping")
plt.show()
