from flask import Flask, render_template, request, url_for, Markup
import os
import pandas as pd
import numpy as np
from random import randrange
import nltk
nltk.download('vander_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
app = Flask(__name__)

#load quotes in memory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#declare global variable
quotes = None

@app.before_request
def getScore():
	global quotes

	#load the quote file
	quotes = pd.read_csv(ps.path.join(BASE_DIR, 'quotes.csv'))