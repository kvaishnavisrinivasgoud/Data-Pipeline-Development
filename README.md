# Data-Pipeline-Development

*COMPANY* : CODETECH IT SOLUTIONS

*NAME* : KANDLAPALLY VAISHNAVI

*INTERN ID* : CT08VYQ

*DOMAIN* : DATA SCIENCE

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANOTOSH


## Explanation of the Script:                                                                                                                                                                                         
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

## How to Use:

1.Replace input_data.csv with the path to your input dataset.                                                                                                                                                    
2.Replace transformed_data.csv with the desired output file path.                                                                                                                                                
3.Run the script to perform the ETL process.                                                                                                                                                                     


## Dependencies:                                                                                                                                                                                                      
Make sure you have the required libraries installed:     

                                      pip install pandas scikit-learn

This script can be extended or modified based on specific requirements, such as handling different data formats, adding more transformation steps, or integrating with databases.


## Expected Output:                                                                                                                                                                                                 

1.Extract:                                                                                                                                                                                                       
-The script will load the dataset from the specified input_file_path (e.g., input_data.csv).                                                                                                                     
-Output in the console:

                                Data extracted successfully.
                                
2.Transform:                                                                                                                                                                                                     
-The script will preprocess and transform the data:                                                                                                                                                              
   -Numerical columns will be imputed (missing values filled with the mean) and scaled.                                                                                                                          
   -Categorical columns will be imputed (missing values filled with the most frequent value) and one-hot encoded.                                                                                                
   -Output in the console:      
   
                                Data transformation completed.
                                
3.Load:
-The transformed data will be saved to the specified output_file_path (e.g., transformed_data.csv).
-Output in the console:

                                Transformed data saved to transformed_data.csv                                                                                                                                  
                                

## Explanation of the Output:

1.Numerical Columns:

-Age and Salary are scaled using StandardScaler, so their values are now centered around 0 with a standard deviation of 1.

-Missing values are imputed with the mean of the respective column.

2.Categorical Columns:

-Gender and Country are one-hot encoded. 

 For example:
--Gender becomes Gender_Female and Gender_Male.
        
--Country becomes Country_India, Country_UK, and Country_USA.
        
-Missing values are imputed with the most frequent value.

3.Output File:

-The transformed data is saved as a CSV file (transformed_data.csv).


Notes:

-If your dataset has different columns or data types, you may need to adjust the script accordingly.

-The output file (transformed_data.csv) will not have column names by default because scikit-learn's ColumnTransformer outputs a NumPy array. You can add column names manually if needed.
For example:

                             transformed_df = pd.DataFrame(transformed_data, columns=column_names)
where column_names is a list of the transformed column names.




                                                                                                                                        
