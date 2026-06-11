# AutoJudge – Programming Problem Difficulty Predictor

## Author Details
- Name : Ved Parikh
- Enrollment No : 24112080
- Demo Link : https://youtu.be/Z7UbZ2m8rxo
- Project Report : [AutoJudge Project Report.pdf](https://github.com/user-attachments/files/24451371/AutoJudge.Project.Report.pdf)


## Project Overview
AutoJudge is a machine learning–based system that predicts the difficulty of programming problems (primarily DSA / Competitive Programming problems) using their textual descriptions. The system classifies problems into three categories — Easy, Medium, and Hard — and also predicts a numeric difficulty score on a scale of 1 to 10.

The project implements a complete end-to-end pipeline, including data preprocessing, feature extraction, supervised learning for classification and regression, and deployment through a web interface using Flask.

---

## Dataset Used
- Source: Provided dataset  
- Original format: `.jsonl`  
- Converted format: `.csv`  
- Total samples: 4112 programming problems  

### Dataset Fields
- Title  
- Description  
- input_description  
- output_description  
- sample_io  
- problem_class (Easy / Medium / Hard)  
- problem_score (numeric difficulty)  
- url  

---

## Approach and Models Used

### Text Preprocessing
- Combined the first five textual fields (title, description, input description, output description, sample I/O) into a single text field  
- Handled missing values by replacing them with empty strings  

---

### Feature Extraction
- Calculated the frequency of commonly used algorithmic keywords such as `dp`, `greedy`, `dfs`, `bfs`, `graph`, etc.  
- Converted textual data into numerical features using **TF-IDF vectorization**  
- Added text length as an additional numeric feature  

---

### Classification Models
The dataset was split into training and testing sets using an 80–20 split.

- **Logistic Regression**  
  - Accuracy: 48.60%  
  - Confusion Matrix:
    ```
            easy  hard  medium
    easy      91    26      36
    hard      66   200     123
    medium    71   101     109
    ```

- **Random Forest Classifier**  
  - Accuracy: 54.19%  
  - Confusion Matrix:
    ```
            easy  hard  medium
    easy      55    77      21
    hard       8   363      18
    medium    23   225      33
    ```

- **Support Vector Machine (SVM)**  
  - Accuracy: 47.39%  
  - Confusion Matrix:
    ```
            easy  hard  medium
    easy       1   152       0
    hard       0   389       0
    medium     0   281       0
    ```

#### Observations
- Logistic Regression predicts all classes but is mainly confused between Easy–Medium and Medium–Hard.  
- Random Forest achieved the best classification accuracy among all tested models, though it tends to classify a large number of problems as Hard.  
- SVM collapsed to predicting a single class (Hard), indicating poor generalization on this dataset.  

---

### Regression Models
The same 80–20 train–test split was used for regression.

- **Linear Regression**  
  - RMSE: 2.87  

- **Random Forest Regressor**  
  - RMSE: 2.05  

- **Gradient Boosting Regressor**  
  - RMSE: 2.07  

#### Observations
- The relatively high RMSE of Linear Regression indicates a non-linear relationship between textual features and numeric difficulty scores.  
- Random Forest significantly improved performance by modeling non-linear relationships.  
- Gradient Boosting produced similar results, but Random Forest performed slightly better overall.  

---

## Final Models Used
Based on evaluation results:
- **Random Forest Classifier** was used for difficulty classification  
- **Random Forest Regressor** was used for numeric difficulty prediction  

---

## Evaluation Metrics
- **Classification:** Accuracy, Confusion Matrix  
- **Regression:** Root Mean Squared Error (RMSE)  

Best results achieved:
- Classification Accuracy: ~54.19%  
- Regression RMSE: ~2.05  

---

## Web Interface Explanation

### Frontend
- Built using **HTML and CSS** for the user interface  
- **JavaScript** is used to send requests and dynamically update prediction results  
- Users can input:
  - Problem description
  - Input format
  - Output format  

---

### Backend
- Implemented using **Flask**  
- Loads trained machine learning models  
- Processes user input and performs inference  
- Returns predictions in JSON format  

### Backend Technologies
- Flask (Python web framework)  
- scikit-learn (machine learning models)  
- joblib (model loading)  
- NumPy and SciPy (feature handling)  

---

## Steps to Run the Project Locally

### 1. Clone the repository
```bash
git clone https://github.com/VEDxyz7/AutoJudge.git
cd AutoJudge
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the web application
```bash
cd app
python app.py
```

### 5. Open the application
```
http://127.0.0.1:5000
```
