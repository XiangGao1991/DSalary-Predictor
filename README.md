# DSalary-Predictor
A project designed to predict salaries for data science roles, utilizing Linkedin job postings as a primary data source. 

When I applied to this master's program, I was encouraged by one statement - the U.S. Bureau of Labor Statistics projects jobs in the (data) field to grow more than 30 percent between 2020 and 2030. With graduation on the horizon, my focus has naturally evolved towards understanding the potential earnings within this burgeoning field. To address this, I will embark on a project designed to predict salaries for data science roles, utilizing Glassdoor job postings as a primary data source. This tool enables users to obtain personalized salary estimates by entering specific details such as their skills, work experience, geographical location, company size, and other relevant information.

Introduction:<br>
•	Problem: Graduates are uncertain about the salary levels they can achieve in data science positions.<br>
•	Dataset: Data science job listings scraped from the LinkedIn website.<br>
•	Goals: Providing graduates with realistic salary expectations tailored to their skills, experience, and the status of the company.<br>
•	Methods: Applying Random Forest, XGBoost, Latent Dirichlet Allocation, etc.<br>

Data Collection:<br>
•	Sources: data science job listings from LinkedIn website.<br>
•	Techniques: web scraping tools (pyautogui, selenium.webdriver, BeautifulSoup).<br>

Data Processing:<br>
•	Cleaning: Regularized location information, standardized salary units, and removed unnecessary information.<br>
•	Feature Engineering: Created and refined of features, including the extraction of keywords from job titles using nltk.<br>

Exploratory Data Analysis:<br>
•	Distribution Analysis: Analyze job distribution by state, job type, remote availability, experience level, company size, and field.<br>
•	Salary Level Analysis: Examine how salaries vary across different categories such as state, job type, and experience level.<br>
•	Keyword Analysis: Investigate common keywords in job titles and skills, drawing insights on the demand for specific roles and skills.<br>

Latent Dirichlet Allocation:<br>
•	Preprocess the text data in the job descriptions.<br>
•	Create a Bag of Words containing the number of times a word appears in the training set.<br>
•	Develop the LDA Model.<br>
•	View the model performance and latent topics.<br>
•	Fine-tune the model to find the best descriptive topics.<br>
•	Assign the topic to job description.<br>

Data Modeling:<br>
•	Build a Transformer to process data<br>
•	Create training and testing sets.<br>
•	Model Training and Fine-tuning for Salary Lower Bound & Upper Bound<br>
•	Select the final model based on performance on salary lower and upper bound.<br>

Application Deployment:<br>
•	TBD<br>
