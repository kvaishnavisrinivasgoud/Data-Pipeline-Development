# Data-Pipeline-Development
Explanation of the Script:                                                                                                                                                                                         
1.Extract:

The extract_data function reads the dataset from a CSV file using pandas.      

2.Transform:

The transform_data function preprocesses the data:                                                                                                                                                                 
-Numerical columns are imputed (missing values filled with the mean) and scaled using StandardScaler.                                                                                                              
-Categorical columns are imputed (missing values filled with the most frequent value) and one-hot encoded using OneHotEncoder.                                                                                     
-The ColumnTransformer is used to apply different preprocessing steps to numerical and categorical columns.                                                                                                        
3.Load:                                                                                                                                                                                                            
The load_data function saves the transformed data to a new CSV file.                                                                                                                                               
4.ETL Pipeline:                                                                                                                                                                                                    
The etl_pipeline function combines all the steps into a single pipeline.                                                                                                                                           


How to Use:

1.Replace input_data.csv with the path to your input dataset.

2.Replace transformed_data.csv with the desired output file path.

3.Run the script to perform the ETL process.

Dependencies:                                                                                                                                                                                                      
Make sure you have the required libraries installed:                                                                                                                                                              

bash
pip install pandas scikit-learn                                                                                                                                                                                    
This script can be extended or modified based on specific requirements, such as handling different data formats, adding more transformation steps, or integrating with databases.

