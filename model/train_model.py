import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

# load dataset
data = pd.read_csv("../data/spam.csv", encoding="latin-1")[["v1","v2"]]
data.columns = ["label","message"]

# convert labels
data["label"] = data["label"].map({"ham":0,"spam":1})

# split data
X_train, X_test, y_train, y_test = train_test_split(
    data["message"], data["label"], test_size=0.2
)

# text vectorization
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

# train model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# save model
joblib.dump(model,"spam_model.pkl")
joblib.dump(vectorizer,"vectorizer.pkl")

print("Model trained successfully")