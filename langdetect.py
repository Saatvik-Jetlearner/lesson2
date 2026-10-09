import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data_lang = pd.read_csv("Language Detection.csv", delimiter=';', names=['Text', 'Language'])

print(data_lang.head())

print(data_lang["Label"].value_counts())

def custom_encoder(data):
    data.replace(to_replace='surprise', value=1, inplace=True)
    data.replace(to_replace='love', value=1, inplace=True)
    data.replace(to_replace='joy', value=1, inplace=True)
    data.replace(to_replace="fear", value=0, inplace=True)
    data.replace(to_replace="anger", value=0, inplace=True)
    data.replace(to_replace="sadness", value=0, inplace=True)

custom_encoder(data_lang["Language"])

nltk.download('stopwords')
nltk.download('wordnet')
lm = WordNetLemmatizer()

def text_transformation(data):
    corpus = []
    for sentence in data:
        new_item = re.sub('[^a-zA-Z]', ' ', str(sentence))
        new_item = new_item.lower()
        new_item = new_item.split()
        new_item = [lm.lemmatize(word) for word in new_item if word not in
                    set(stopwords.words('english'))]
        corpus.append(' '.join(str(x) for x in new_item))
    return corpus

corpus = text_transformation(data_lang["Text"])
print(corpus[1])


cv = CountVectorizer(ngram_range = (1,2))
X = cv.fit_transform(corpus)
Y = data_lang.language

parameters = {
    "max_features": ('auto', 'sqrt'),
    "n_estimators": [500, 1000, 1500],
    "max_depth": [5, 10, None],
    "min_samples_leaf": [1,2,5,10],
    "bootstrap": [True, False]
}



# finding the best parameters for the specified algorithm to get the best result
grid_search = GridSearchCV(
    RandomForestClassifier(),
    parameters,
    cv = 5,
    return_lang_score = True,
    n_jobs = -1
)
grid_search.fit(X, Y)
print(grid_search.best_params_)

rfc = RandomForestClassifier(
    max_features=grid_search.best_params_['max_features'],
    max_depth=grid_search.best_params_['max_depth'],
    n_estimators=grid_search.best_params_['n_estimators'],
    min_samples_split=grid_search.best_params_['min_samples_split'],
    min_samples_leaf=grid_search.best_params_['min_samples_leaf'],
    bootstrap=grid_search.best_params_['bootstrap']
)
rfc.fit(X, Y)
test_data = pd.read_csv('test.txt', delimiter=',', names=["Text", "Language"])
X_test, Y_test = test_data.text, test_data.label
Y_test = custom_encoder(Y_test)
X_test = text_transformation(X_test)
X_test = cv.transform(X_test)
y_pred = rfc.predict(X_test)


acc_score = accuracy_score(Y_test, y_pred)
print("Accuracy Score - ", acc_score)
report = classification_report(Y_test, y_pred)

def expression_check(inputStr):
    if inputStr == 1:
        print("Input Statement has positive sentiment.")
    elif inputStr == 0:
        print("Input Statement has negative sentiment.")
    else:
        print("No detectable sentiment.")

def sentiment_predictor(input):
    inputStr = text_transformation(inputStr)
    transformed_text = cv.transform(inputStr)
    prediction = rfc.predict(transformed_text)
    expression_check(prediction)


input1 = ["Sometimes I want to punch someone in the face."]
input2 = ["I traveled to Switzerland and The place is beautiful."]


sentiment_predictor(input1)
sentiment_predictor(input2)
