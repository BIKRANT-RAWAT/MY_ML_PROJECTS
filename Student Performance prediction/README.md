<!DOCTYPE html>
<html lang="en">
<body style="font-family: 'Arial', 'Helvetica', sans-serif; line-height:1.6; background-color:#f8f9fa; color:#2c3e50; padding:40px; max-width:900px; margin:auto;">

  <!-- Title -->
  <h1 style="text-align:center; font-size:3em; color:#273746; background:#d6eaf8; padding:20px; border-radius:12px;">
    🎓 Student Performance Prediction
  </h1>
  <p style="text-align:center; font-size:1.1em; color:#555;">
    Part of <strong>MY_ML_PROJECTS</strong> by BIKRANT-RAWAT — Predicting students’ academic performance based on demographic, social, and educational features.
  </p>

  <hr style="border:1px solid #ccc; margin:25px 0;">

  <!-- Project Overview -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>📖 Project Overview</h2>
    <p>
      This project aims to build a predictive model to estimate student Mathematics performance using features such as demographics, parental background, test prep, and other academic record (e.g. Reading and Writing score). The goal is to identify which students may need additional support, and understand which factors most influence student outcomes.
    </p>
  </div>

<!-- Importance -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>💡Project Looks</h2>
    <ul>
      <h3>🔥 Index page </h3>
<img src="https://github.com/BIKRANT-RAWAT/MY_ML_PROJECTS/blob/master/Student%20Performance%20prediction/images/indexpage.jpg" alt="Index page" width="500">
      <h3>🔥 Predict page</h3>
<img src="https://github.com/BIKRANT-RAWAT/MY_ML_PROJECTS/blob/master/Student%20Performance%20prediction/images/prediction%20page.jpg" alt="prediction page" width="500">
<h3>🔥 Prediction</h3>
<img src="https://github.com/BIKRANT-RAWAT/MY_ML_PROJECTS/blob/master/Student%20Performance%20prediction/images/prediction.jpg" alt="prediction" width="500">
      
  </div>

  <!-- Importance -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>💡 Objectives </h2>
    <ul>
      <li>📊 Educational planning & policy: identifying at-risk students early helps in targeted interventions.</li>
      <li>🏫 Supporting teachers & institutions to understand key factors affecting student success (e.g., parental support, study habits, test preparation).</li>
      <li>📈 Demonstrates how ML can help in predictive analytics in education and social science contexts.</li>
    </ul>
  </div>

  <!-- Data & Features -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>🔍 Data & Features</h2>
    <ul>
      <li>Data includes gender, ethnicity, socio-economic info, other subject performance, test preparation status, etc.</li>
      <li>Features also include parental education level, lunch type, etc.</li>
      <li>Target variable: Final grade / aggregated score or classification of Maths subject.</li>
      <li>Preprocessing steps: handling missing values, encoding categorical variables, scaling numerical features.</li>
    </ul>
  </div>

  <!-- Model & Approach -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>🛠️ Model & Approach</h2>
    <ul>
      <li>Exploratory Data Analysis (EDA): distributions, correlation heatmap, examining feature relationships etc.</li>
      <li>Feature engineering: create new features, encode categorical data, combine features, etc.</li>
      <li>Model types tried: Linear Regression, Decision Tree / Random Forest, Boosting (XGBoost,CatBoost,AdaBoost, etc.), SVM, etc.</li>
      <li>Evaluation metrics: MAE, MSE, R² (for regression) , Accuracy, Precision, Recall, etc.</li>
      <li>Cross-validation and train/test splitting to ensure model generalization.</li>
    </ul>
  </div>

  <!-- Project Structure -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>📂 Project Structure</h2>
    <pre style="background:#2c2f33; color:#f8f8f2; padding:15px; border-radius:8px; overflow:auto;">
Student Performance Prediction/
│
├── artifacts/             # Raw & cleaned datasets and pickle file
├── notebooks/             # Jupyter notebooks for exploration & prototyping
├── images/                # Saved images 
├── templates/             # flask file
├── src/                   # Core scripts (preprocessing, training, inference)
├── README.md              # This file
└── requirements.txt       # Python dependencies
    </pre>
  </div>

  <!-- Technologies Used -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>🧰 Technologies Used</h2>
    <ul>
      <li>Python — primary language</li>
      <li>Pandas, NumPy — data handling and cleaning</li>
      <li>Matplotlib, Seaborn, Plotly — data visualization</li>
      <li>Scikit-Learn — model building and evaluation</li>
      <li>XGBoost, AdaBoost, CatBoost  — for boosting models </li>
      <li>K-Neighbour , DecisionTree, etc. </li>
      <li>Jupyter Notebooks / IDE for prototyping</li>
    </ul>
  </div>

  <!-- How to Run / Usage -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>⚙️ How to Run</h2>
    <ol>
      <li>Clone repository:<br>
        <pre style="background:#2c2f33; color:#f8f8f2; padding:10px; border-radius:6px; overflow:auto;">git clone https://github.com/BIKRANT-RAWAT/MY_ML_PROJECTS.git</pre>
      </li>
      <li>Change directory:<br>
        <code>cd MY_ML_PROJECTS/Student Performance Prediction</code>
      </li>
      <li>Install dependencies:<br>
        <pre style="background:#2c2f33; color:#f8f8f2; padding:10px; border-radius:6px; overflow:auto;">pip install -r requirements.txt</pre>
      </li>
      <li>Run :
         <pre style="background:#272822; color:#f8f8f2; padding:10px; border-radius:6px; overflow:auto;">python application.py</pre>
      </li>
      <li>click on ctrl + local host link to predict on local host.</li>
      <li>Deployment can be done as require.</li>
    </ol>
  </div>


 <!-- Results & Insights -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>📊 Results & Insights</h2>
    <h3>📊 EDA Plots</h3>
<p align="center">
  <img src="https://github.com/BIKRANT-RAWAT/MY_ML_PROJECTS/blob/master/Student%20Performance%20prediction/images/piechart.png" alt="Piechart" width="350">
  <li>- Number of Male and Female students is almost equal, Number students are greatest in Group C, Number of students who have standard lunch are greater, Number of students who have not enrolled in any test preparation course is greater, Number of students whose parental education is "Some College" is greater followed closely by "Associate's Degree"</li>
  <img src="https://github.com/BIKRANT-RAWAT/MY_ML_PROJECTS/blob/master/Student%20Performance%20prediction/images/totalmarks%20hist.png" alt="total marks" width="350">
  <li>Female students tend to perform well then male students.</li>
   <img src="https://github.com/BIKRANT-RAWAT/MY_ML_PROJECTS/blob/master/Student%20Performance%20prediction/images/pairplot.png" alt="Pair Plot" width="350">
   
<li>From the above plot it is clear that all the scores increase linearly with each other.</li>
  <!-- Acknowledgement -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>🙏 Acknowledgement</h2>
    <p>
      I thank the data sources, educational research, and open dataset communities for making this project possible.  
      Also grateful to mentor Krish Naik sir and online resources guiding through ML, data preprocessing, and performance improvement.
    </p>
  </div>

  <footer style="text-align:center; margin-top:30px; font-size:0.9em; color:#555;">
    &copy; 2025 BIKRANT-RAWAT — Student Performance Prediction under MY_ML_PROJECTS.
  </footer>

</body>
</html>
