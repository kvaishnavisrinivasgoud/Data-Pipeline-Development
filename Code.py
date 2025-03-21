# Import necessary libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# Step 1: Extract - Load the dataset
def extract_data(file_path):
    """
    Load data from a CSV file.
    """
    df = pd.read_csv(file_path)
    print("Data extracted successfully.")
    return df

# Step 2: Transform - Preprocess and transform the data
def transform_data(df):
    """
    Preprocess and transform the data.
    """
    # Define numerical and categorical columns
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns

    # Preprocessing for numerical data
    numerical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),  # Fill missing values with mean
        ('scaler', StandardScaler())  # Standardize numerical data
    ])

    # Preprocessing for categorical data
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),  # Fill missing values with most frequent value
        ('onehot', OneHotEncoder(handle_unknown='ignore'))  # One-hot encode categorical data
    ])

    # Combine preprocessing steps
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_cols),
            ('cat', categorical_transformer, categorical_cols)
        ])

    # Apply preprocessing
    transformed_data = preprocessor.fit_transform(df)
    print("Data transformation completed.")
    return transformed_data, preprocessor

# Step 3: Load - Save the transformed data
def load_data(transformed_data, output_file_path):
    """
    Save the transformed data to a CSV file.
    """
    transformed_df = pd.DataFrame(transformed_data)
    transformed_df.to_csv(output_file_path, index=False)
    print(f"Transformed data saved to {output_file_path}.")

# Main ETL Pipeline
def etl_pipeline(input_file_path, output_file_path):
    """
    Run the ETL pipeline: Extract, Transform, Load.
    """
    # Step 1: Extract
    df = extract_data(input_file_path)

    # Step 2: Transform
    transformed_data, preprocessor = transform_data(df)

    # Step 3: Load
    load_data(transformed_data, output_file_path)

# Run the ETL pipeline
if __name__ == "__main__":
    input_file_path = "input_data.csv"  # Replace with your input file path
    output_file_path = "transformed_data.csv"  # Replace with your desired output file path
    etl_pipeline(input_file_path, output_file_path)
