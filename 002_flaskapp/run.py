from flask import Flask, jsonify, request, render_template, redirect, url_for, session
import json
import pandas as pd
import numpy as np
import pickle
from Transformer import Transformer
from gensim import corpora, models


dictionary = corpora.Dictionary.load('../001_model/job_description_text.dict')
lda_model = models.LdaModel.load('../001_model/LDA.model')

with open("../001_model/final_model_salary_lower.pkl","rb") as f:
    model_lower = pickle.load(f)
    
with open("../001_model/final_model_salary_upper.pkl","rb") as f:
    model_upper = pickle.load(f)

app = Flask(__name__)
app.secret_key = 'Lauren66'

@app.route('/',methods=["GET","POST"])
def index():
    pred = ""
    form_data = {}
    if request.method == "POST":
        # raw data

        form_data = request.form
        data = dict(form_data)
        tf = Transformer(data = data, lda_model = lda_model, dictionary = dictionary)
        
        process_data = tf.data_process()

        df = pd.DataFrame({0:process_data}).T

        salary_lower = model_lower.predict(df)[0]
        salary_upper = model_upper.predict(df)[0]
        
        # Store the results in the session
        session['pred'] = f"The estimated annual salary range for this position is from ${salary_lower:,.0f} to ${salary_upper:,.0f}."
        return redirect(url_for('results'))

    return render_template("index.html")

@app.route('/results')
def results():
    # Retrieve the results from the session
    pred = session.get('pred', '')

    # The results page
    return render_template("results.html", pred=pred)




if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port=8050)