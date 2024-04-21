# DSalary Predictor

## Description
This project is designed to predict salaries for data science roles, utilizing Linkedin job postings as a primary data source. It enables users to obtain personalized salary estimates by entering specific details such as their skills, work experience, geographical location, company size, and other relevant information.

## Prerequisites
- **Python 3**
- **Jupyter Notebook**

### Required Libraries
- **Data Handling and Analysis:** `pandas`, `numpy`
- **Data Visualization:** `matplotlib`, `seaborn`
- **Data Serialization:** `pickle`, `json`
- **Natural Language Processing:** `nltk`, `gensim`
- **Machine Learning:** `sklearn`, `xgboost`, `catboost`

## Project Structure
- `DSalary_Predictor.ipynb`: Main project notebook containing all code.
- `job_post_data.csv`: Cleaned structural data for analysis and model training.

## Execution of the Project
1. Start Jupyter Notebook.
2. Import necessary packages and comment out any lines required solely for the Data Collection section.
3. Skip the Data Collection section (cells 2 - 17), as it involves complex automation operations that may not be compatible with all operating systems, such MacOS and Linux.
4. Execute the Data Processing section (cells 18 - 22) to prepare categorical, numerical, and textual features.
5. Execute the EDA section (cells 23 - 40) to analyze feature patterns and their relationships with the target variable.
6. Execute the Latent Dirichlet Allocation section (cells 41 - 51) to classify job description texts into three main topics.
7. Execute the Data Modeling section (cells 52 - 68) to develop, evaluate, and save the final models.

## Reproducing Results
1. Follow the execution instructions sequentially as outlined in this README to ensure accurate reproduction of results.
2. Ensure the `job_post_data.csv` file is in the same directory as the Jupyter notebook.

## Support
For any issues or inquiries, please contact the developer at [xig423@lehigh.edu](mailto:xig423@lehigh.edu).

## Application
[DSalary Predictor](http://ec2-18-188-191-239.us-east-2.compute.amazonaws.com:8050/).

