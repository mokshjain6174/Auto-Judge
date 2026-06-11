from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
from scipy.sparse import hstack

app = Flask(__name__)

tfidf = joblib.load("../models/tfidf_vectorizer.pkl")
classifier = joblib.load("../models/classifier.pkl")
regressor = joblib.load("../models/regressor.pkl")  

keywords = ["dp", "graph", "tree", "recursion", "greedy", "binary", "dfs", "bfs"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    text = (
        data["description"] + " " +
        data["input_description"] + " " +
        data["output_description"]
    )

    # TF-IDF
    X_text = tfidf.transform([text])

    # Numeric features
    text_length = len(text)
    keyword_counts = [text.lower().count(k) for k in keywords]
    numeric_features = np.array([[text_length] + keyword_counts])

    X = hstack([X_text, numeric_features])

    # Predictions
    pred_class = classifier.predict(X)[0]
    pred_score = regressor.predict(X)[0]

    if pred_class == "easy":
        pred_score = 0.7 * pred_score + 1.5
    elif pred_class == "medium":
        pred_score = 0.7 * pred_score + 3.5
    else:
        pred_score = 0.7 * pred_score + 6.5

    return jsonify({
        "class": pred_class,
        "score": round(float(pred_score), 2)
    })

if __name__ == "__main__":
    app.run(debug=True)
