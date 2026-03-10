from fastapi import FastAPI
import joblib
import time

app = FastAPI()

# load model
model = joblib.load("model/spam_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

@app.get("/")
def home():
    return {"message": "AI Model Monitoring API Running"}

@app.post("/predict")
def predict(text: str):

    start = time.time()

    # convert text
    text_vec = vectorizer.transform([text])

    # prediction
    prediction = model.predict(text_vec)[0]
    confidence = model.predict_proba(text_vec).max()

    latency = time.time() - start

    return {
        "prediction": "spam" if prediction == 1 else "ham",
        "confidence": float(confidence),
        "latency": latency
    }