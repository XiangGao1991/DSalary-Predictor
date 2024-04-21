#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import pandas as pd
import nltk
from nltk.corpus import words
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

nltk.data.path.append("../001_model/nltk_data/")


class Transformer:
    def __init__(self, data, lda_model, dictionary):
        self.data = data
        self.job_level_dict = {'Intern': 2, 'entry': 3, 'Entry': 3, 'Junior': 4, 'junior': 4, 'Jr': 4, 'Assistant': 5, 'Associate': 6, 'I': 7, 'Intermediate': 8, 'Mid': 9, 'II': 10, 'Advanced': 11, 'III': 12, 'Senior': 13, 'Sr': 13, 'Staff': 14, 'Lead': 15, 'Leading': 15, 'IV': 16, 'Direct': 17, 'Director': 17, 'Dir': 17, 'VP': 18}
        self.security_level_set = {'Security', 'Clearance','Safety'}
        self.key_state = {'AK','AL','AZ','CA','CO','CT','DC','DE','FL','GA','IA','ID','IL','IN','KY','MA','MD','ME','MN','MO','NC','NJ','NV','NY','OH','OR','PA','RI','SC','TN','TX','UT','VA','WA','WI','WV'}
        self.skillset = {'AI','Cloud Computing','Communication','Computer Science','Critical Thinking','Data Analytics','Data Collection','Data Engineering','Data Modeling','Data Visualization','Database','Deep Learning','Distributed Computing','Experimental Design','HTML','Kaggle','LLM','Machine Learning','Mathematics','Metric Development','NLP','Other Programming Language','PIV','Pattern Recognition','Problem Solving','Python','R','SEO','Scala','Search Techniques','Statistics'}
        self.lda_model = lda_model
        self.dictionary = dictionary

    def data_process(self):

        process_data = {}
        # process job title
        JobTitle = self.data["JobTitle"]
        process_data['Job_Level'] = max([value for key,value in self.job_level_dict.items() if key in JobTitle])
        process_data['Security_level'] = int(len([keyword for keyword in self.security_level_set if keyword in JobTitle])>0)

        # process Job_Type
        process_data['Job_Type_Contract'] = 0
        process_data['Job_Type_Full-time'] = 0
        process_data['Job_Type_Internship'] = 0
        process_data['Job_Type_Part-time'] = 0
        process_data['Job_Type_Temporary'] = 0
        process_data['Job_Type_Unknown'] = 0

        Assign_Job_Type = 'Job_Type_' + self.data["Job_Type"]
        process_data[Assign_Job_Type] = 1

        # process Remote
        process_data['Remote_Hybrid'] = 0
        process_data['Remote_On-site'] = 0
        process_data['Remote_Remote'] = 0
        process_data['Remote_Unknown'] = 0

        Assign_Remote = 'Remote_' + self.data["Remote"]
        process_data[Assign_Remote] = 1

        # process Experience_Level
        process_data['Experience_Level_Associate'] = 0
        process_data['Experience_Level_Director'] = 0
        process_data['Experience_Level_Entry level'] = 0
        process_data['Experience_Level_Internship'] = 0
        process_data['Experience_Level_Mid-Senior level'] = 0
        process_data['Experience_Level_Unknown'] = 0

        Assign_Experience_Level = 'Experience_Level_' + self.data["Experience_Level"]
        process_data[Assign_Experience_Level] = 1

        # process Company_Size
        process_data['Company_Size_5'] = 0
        process_data['Company_Size_30'] = 0
        process_data['Company_Size_125'] = 0
        process_data['Company_Size_350'] = 0
        process_data['Company_Size_750'] = 0
        process_data['Company_Size_3000'] = 0
        process_data['Company_Size_7500'] = 0
        process_data['Company_Size_20000'] = 0

        Assign_Company_Size = 'Company_Size_' + self.data["Company_Size"]
        process_data[Assign_Company_Size] = 1

        # process State
        process_data['State_AK'] = 0
        process_data['State_AL'] = 0
        process_data['State_AZ'] = 0
        process_data['State_CA'] = 0
        process_data['State_CO'] = 0
        process_data['State_CT'] = 0
        process_data['State_DC'] = 0
        process_data['State_DE'] = 0
        process_data['State_FL'] = 0
        process_data['State_GA'] = 0
        process_data['State_IA'] = 0
        process_data['State_ID'] = 0
        process_data['State_IL'] = 0
        process_data['State_IN'] = 0
        process_data['State_KY'] = 0
        process_data['State_MA'] = 0
        process_data['State_MD'] = 0
        process_data['State_ME'] = 0
        process_data['State_MN'] = 0
        process_data['State_MO'] = 0
        process_data['State_NC'] = 0
        process_data['State_NJ'] = 0
        process_data['State_NV'] = 0
        process_data['State_NY'] = 0
        process_data['State_OH'] = 0
        process_data['State_OR'] = 0
        process_data['State_PA'] = 0
        process_data['State_RI'] = 0
        process_data['State_SC'] = 0
        process_data['State_TN'] = 0
        process_data['State_TX'] = 0
        process_data['State_UT'] = 0
        process_data['State_VA'] = 0
        process_data['State_WA'] = 0
        process_data['State_WI'] = 0
        process_data['State_WV'] = 0
        process_data['State_Unknown'] = 0

        if self.data["State"] in self.key_state:
            Assign_State = 'State_' + self.data["State"]
            process_data[Assign_State] = 1
        else:
            process_data['State_Unknown'] = 1

        # process Field
        process_data['Field_Consumer Services & Retail'] = 0
        process_data['Field_Energy & Utilities'] = 0
        process_data['Field_Financial & Business Services'] = 0
        process_data['Field_Healthcare & Biotech'] = 0
        process_data['Field_Manufacturing & Industrial'] = 0
        process_data['Field_Media, Entertainment & Education'] = 0
        process_data['Field_Others'] = 0
        process_data['Field_Technology & IT'] = 0

        Assign_Field = 'Field_' + self.data["Field"]
        process_data[Assign_Field] = 1

        # process skills
        skill_num = 0
        for skill in self.skillset:
            Assign_Skill = 'Skill_' + skill
            process_data[Assign_Skill] = self.data.get(skill,0)
            skill_num += int(self.data.get(skill,0))
        

        if skill_num == 0:
            process_data['Skill_None'] = 1
        else:
            process_data['Skill_None'] = 0

        # process job description
        text = self.data['JobDescription']
        token = self.ldf_data_preprocess(text)
        tokens = self.dictionary.doc2bow(token)
        topic_distribution = self.lda_model.get_document_topics(tokens)
        topic = str(max(topic_distribution, key=lambda x: x[1])[0])
        process_data['Job_Description_Topic_0'] = 0
        process_data['Job_Description_Topic_1'] = 0
        process_data['Job_Description_Topic_2'] = 0

        Assign_Job_Description_Topic = 'Job_Description_Topic_' + topic
        process_data[Assign_Job_Description_Topic] = 1

        return process_data

    
    def ldf_data_preprocess(self,text):
        # lowercase the text to ensure uniformity
        lowercased_text = text.lower()

        # split the text into individual words or tokens.
        tokens = word_tokenize(lowercased_text)

        # remove the stop words to focus on more significant words
        stop_words = set(stopwords.words('english'))
        tokens_filtered = [word for word in tokens if word not in stop_words]
        
        # remove the words that have less or equal to 3 letters
        stop_words = set(stopwords.words('english'))
        tokens_filtered = [word for word in tokens if len(word)>3]

        # removing punctuation and special characters
        tokens_filtered = [word for word in tokens_filtered if word.isalpha()]

        # reduce words to their root form
        lemmatizer = WordNetLemmatizer()
        tokens_lemmatized = [lemmatizer.lemmatize(word) for word in tokens_filtered]
        
        # remove some words that are not important(based on human experience and understanding)
        tokens = [word for word in tokens_filtered if word not in ('your','allen','booz','tiktok','meta','candidates')]
        return tokens