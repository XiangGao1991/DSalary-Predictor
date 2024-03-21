# DSalary-Predictor
A project designed to predict salaries for data science roles, utilizing Linkedin job postings as a primary data source. 

When I applied to this master's program, I was encouraged by one statement - the U.S. Bureau of Labor Statistics projects jobs in the (data) field to grow more than 30 percent between 2020 and 2030. With graduation on the horizon, my focus has naturally evolved towards understanding the potential earnings within this burgeoning field. To address this, I will embark on a project designed to predict salaries for data science roles, utilizing Glassdoor job postings as a primary data source. This tool enables users to obtain personalized salary estimates by entering specific details such as their skills, work experience, geographical location, company size, and other relevant information.

Introduction:
•	Problem: Graduates are uncertain about the salary levels they can achieve in data science positions.
•	Dataset: Data science job listings scraped from the LinkedIn website.
•	Goals: Providing graduates with realistic salary expectations tailored to their skills, experience, and the status of the company.
•	Methods: Applying Random Forest, XGBoost, Latent Dirichlet Allocation, etc.

Data Collection:
•	Sources: data science job listings from LinkedIn website.
•	Techniques: web scraping tools (pyautogui, selenium.webdriver, BeautifulSoup).

Data Processing:
•	Cleaning: Regularized location information, standardized salary units, and removed unnecessary information.
•	Feature Engineering: Created and refined of features, including the extraction of keywords from job titles using nltk.

Exploratory Data Analysis:
•	Distribution Analysis: Analyze job distribution by state, job type, remote availability, experience level, company size, and field.
•	Salary Level Analysis: Examine how salaries vary across different categories such as state, job type, and experience level.
•	Keyword Analysis: Investigate common keywords in job titles and skills, drawing insights on the demand for specific roles and skills.

Data Modeling:
•	TBD

Application Deployment:
•	TBD
