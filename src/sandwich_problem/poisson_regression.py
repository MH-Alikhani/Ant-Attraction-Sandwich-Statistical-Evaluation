import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
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
        print("-" * 30)
        return df
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        exit()  # Exit if there's an error during file reading

# --- 1. Load Data ---
df = read_csv_file(file_path)

# Convert to category
df['bread'] = df['bread'].astype('category')
df['topping'] = df['topping'].astype('category')
df['butter'] = df['butter'].astype('category')

# Poisson Regression Model
poisson_model = smf.glm(
    formula='antCount ~ bread + topping + butter',
    data=df,
    family=sm.families.Poisson()
).fit()

# Display the model
print(poisson_model.summary())

# Poisson Regression (likes ANOVA)
poisson_interaction_model = smf.glm(
    formula='antCount ~ bread + topping + butter + bread:topping + bread:butter + topping:butter',
    data=df,
    family=sm.families.Poisson()
).fit()

print(poisson_interaction_model.summary())
