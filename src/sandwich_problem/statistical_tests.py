import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns
import os

# The input and output variables
file_path = 'datasets/sandwich.csv'

# The plotting attributes
bread_butter_interaction_plot_info = {
    'plot_info': {'x': 'bread', 'y': 'antCount', 'palette': 'magma', 'hue': 'butter'},
    'axis_info': {'title': 'Interaction between Bread and Butter', 'xlabel': 'Bread Type', 'ylabel': 'Average Ant Count'}
}

# Interaction plot between bread and butter
def generate_bar_plot(df: pd.DataFrame, plot_info: dict, axis_label: dict):
    plt.figure(figsize=(8, 6))
    sns.pointplot(data=df, x=plot_info['x'], y=plot_info['y'], hue=plot_info['hue'], dodge=True, capsize=0.1, palette=plot_info['palette'])
    plt.title(axis_label['title'])
    plt.ylabel(axis_label['xlabel'])
    plt.xlabel(axis_label['ylabel'])
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Read the data from the CSV file
def read_csv_file(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found. Please ensure the file is in the correct directory.")
        exit()  # Exit the script if the file is missing
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded data from '{file_path}'.")
        print("-" * 30)
        return df
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        exit()  # Exit if there's an error during file reading

# --- 1. Load Data ---
df = read_csv_file(file_path)

# convert to category
df['bread'] = df['bread'].astype('category')
df['topping'] = df['topping'].astype('category')
df['butter'] = df['butter'].astype('category')

# Use the Three-Way ANOVA Model
model = ols('antCount ~ C(bread) + C(topping) + C(butter) + \
             C(bread):C(topping) + C(bread):C(butter) + C(topping):C(butter)', data=df).fit()

# Table (Type II ANOVA) number 2
anova_table = sm.stats.anova_lm(model, typ=2)
print("Three-Way ANOVA Table:")
print(anova_table)

# --- 2. Bar Plots for Average Ant Counts ---
generate_bar_plot(df, bread_butter_interaction_plot_info['plot_info'], bread_butter_interaction_plot_info['axis_info'])

print("Analysis complete.")
