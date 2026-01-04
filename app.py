from flask import Flask,request,jsonify,render_template
import pickle
import os
import re


app=Flask(__name__)

BASE_PATH=r"D:\machine learning\IMDB sentiment analysis"
model_path=os.path.join(BASE_PATH,"model","logistic_regression_model.pkl")
vectorizer_path = os.path.join(BASE_PATH, "model", "tfidf_vectorizer.pkl")

with open(model_path,"rb") as f:
    model=pickle.load(f)
    
with open(vectorizer_path,"rb") as f:
    vectorizer=pickle.load(f)
    
    
def clean_text(text):
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    text = text.lower()
    text = re.sub(r"\s+", " ", text).strip()
    return text

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    data=request.get_json()
    
    if not data or "text" not in data:
        return jsonify({"Error":"No text Provided"}),400
    text=data['text']
    clean=clean_text(text)
    vector=vectorizer.transform([clean])
    prediction=model.predict(vector)[0]
    probability = model.predict_proba(vector)[0].max()
    
    result = "Positive" if prediction == 1 else "Negative"

    return jsonify({
        "sentiment": result,
        "confidence": round(float(probability), 3)
    })
    
if __name__ == "__main__":
    app.run(debug=True)