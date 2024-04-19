# DSalary-Predictor

## Description:
This project is designed to predict salaries for data science roles, utilizing Linkedin job postings as a primary data source. It enables users to obtain personalized salary estimates by entering specific details such as their skills, work experience, geographical location, company size, and other relevant information.

## Prerequisites:
### Python 3

### Required libraries: 
#### 1. Data Handling and Analysis
pandas, numpy
#### 2. Data Visualization
matplotlib, seaborn
#### 3. Data Serialization
pickle, json
#### 4. Natural Language Processing
nltk, gensim
#### 5. Machine Learning
sklearn, xgboost, catboost

### Jupyter Notebook

## Project Structure:
•	DSalary_Predictor.ipynb: Project notebook containing all codes.
•	job_post_data.csv: structural data after cleaning for analysis and model training

##  Execution of the Project
1. Start Jupyter Notebook
2. Import necessary packages and comment out any lines required solely for the Data Collection section.
3. Skip the Data Collection section (cells 2 - 17), as it involves complex automation operations that may not be compatible with all operating systems, including MacOS and Linux.
4. Run the Data Processing section (cells 18 - 22) in sequence to convert categorical, numerical, and textual features.
5. Run the EDA section (cells 23 - 40) in sequence to discover feature patterns and their correlations with the target variable.
6. Run the Latent Dirichlet Allocation section (cells 41 - 51) in sequence to classify job description text to three main topics.
7. Run the Data Modeling section (cells 52 - 68) in sequence to develop, evaluate, and save the final models.

##  Reproducing Results
1. Ensure sequential execution by carefully following the instructions for each step of processing, analysis, and modeling outlined in this Readme file.
2. Verify that the csv file referenced in the instruction is located in the same directory as the Jupyter notebook file

## Support
If you encounter any issues, please contact the developer at xig423@lehigh.edu.

