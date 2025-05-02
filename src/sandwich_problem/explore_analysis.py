import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# The input and output variables
file_path = 'datasets/sandwich.csv'
group_stats_path = 'results/group_stats.csv'

# The plotting attributes
bread_type_plot_info = {
    'plot_info': {'x': 'bread', 'y': 'antCount', 'palette': 'viridis'},
    'axis_info': {'title': 'Average Ant Count by Bread Type', 'xlabel': 'Bread Type', 'ylabel': 'Average Ant Count'}
}

topping_plot_info = {
    'plot_info': {'x': 'topping', 'y': 'antCount', 'palette': 'magma'},
    'axis_info': {'title': 'Average Ant Count by Topping', 'xlabel': 'Topping', 'ylabel': 'Average Ant Count'}
}

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


# Generate Bar Plots for Average Ant Counts
def generate_bar_plot(df: pd.DataFrame):
    # Set the visual theme for the plots (optional, for aesthetics)
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(14, 7))  # Create a figure to hold the subplots (adjusted size for better label spacing)

    # Plot 1: Average ant count by Bread Type
    plt.subplot(1, 2, 1)
    generate_average_ant_count_plot(df, bread_type_plot_info['plot_info'], bread_type_plot_info['axis_info'])

    # Plot 2: Average ant count by Topping
    plt.subplot(1, 2, 2)  # Select the second plot area
    generate_average_ant_count_plot(df, topping_plot_info['plot_info'], topping_plot_info['axis_info'])

    plt.tight_layout()  # Adjust spacing between plots to prevent labels overlapping
    print("Displaying bar plots for average ant counts...")
    plt.show()  # Render and display the plots
    print("-" * 30)


def generate_average_ant_count_plot(df: pd.DataFrame, plot_info: dict, axis_label: dict):
    ax = sns.barplot(x=plot_info['x'], y=plot_info['y'], data=df, palette=plot_info['palette'], hue=plot_info['x'], legend=False)
    ax.set_title(axis_label['title'])
    ax.set_xlabel(axis_label['xlabel'])
    ax.set_ylabel(axis_label['ylabel'])
    plt.xticks(rotation=45, ha='right')


def generate_statical_table(df: pd.DataFrame) -> dict:
    grouped_stats = df.groupby(['bread', 'topping', 'butter'])['antCount'].agg(['mean', 'std'])

    # Rename the aggregated columns for clarity
    grouped_stats = grouped_stats.rename(columns={
        'mean': 'Mean Ant Count',
        'std': 'Std Dev Ant Count'
    })

    # Round the results to 2 decimal places for cleaner presentation (optional)
    grouped_stats = grouped_stats.round(2)

    # Fill potential NaN values in standard deviation (which occur for groups with only one member) with 0
    grouped_stats['Std Dev Ant Count'] = grouped_stats['Std Dev Ant Count'].fillna(0)
    return grouped_stats

def write_statical_results(grouped_stats: dict, file_path: str) -> None:
    try:
        grouped_stats.to_csv(file_path, index=True,
                             encoding='utf-8-sig')  # Use utf-8-sig for better Excel compatibility
        print(f"Statistical table successfully saved to: '{file_path}'")
    except Exception as e:
        print(f"Error saving the statistical table to CSV: {e}")

    print("-" * 30)

# --- 1. Load Data ---
df = read_csv_file(file_path)

# --- 2. Data Structure Summary ---
print("Data Structure Summary:")
df.info() # Provides column names, non-null counts, and data types

print("\nFirst 5 rows of the datasets:")
print(df.head()) # Display the first few rows to see the data

print("\nUnique values for categorical variables:")
# Explicitly list the unique values found in the specified columns
print(f"Bread Types: {df['bread'].unique().tolist()}")
print(f"Toppings: {df['topping'].unique().tolist()}")
print(f"Butter Options: {df['butter'].unique().tolist()}")

print("\nDescriptive statistics for 'antCount':")
print(df['antCount'].describe()) # Show count, mean, std, min, max, quartiles for the numeric column
print("-" * 30)

# --- 3. Bar Plots for Average Ant Counts ---
generate_bar_plot(df)

# --- 4. Statistical Table (Mean and Standard Deviation) ---
print("Statistical Table: Mean and Standard Deviation of Ant Counts for Each Combination:")
grouped_stats = generate_statical_table(df)

# Store the grouped_stats in group_stats.csv file
write_statical_results(grouped_stats, group_stats_path)

print("Analysis complete.")