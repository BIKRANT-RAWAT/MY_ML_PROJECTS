<!DOCTYPE html>
<html lang="en">
<body style="font-family: 'Segoe UI', Tahoma, Verdana, sans-serif; line-height:1.6; background-color:#f7f9fc; color:#2c3e50; padding:40px; max-width:900px; margin:auto;">

  <!-- Main Title -->
  <h1 style="text-align:center; font-size:3em; color:#1f3b73; background:#e0efff; padding:20px; border-radius:12px;">
    🌲 Algerian Forest Fire Prediction
  </h1>
  <p style="text-align:center; font-size:1.1em; color:#555;">
    A Machine Learning project to predict forest fires in Algeria, from the <strong>MY_ML_PROJECTS</strong> collection by BIKRANT-RAWAT.
  </p>

  <hr style="border:1px solid #ccc; margin:25px 0;">

  <!-- Project Overview -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>📖 Project Overview</h2>
    <p>
      The goal of this project is to build a predictive model that estimates the likelihood or extent of forest fires in Algeria based on environmental and meteorological data.
      It involves steps such as data exploration, feature engineering, model training and evaluation.
    </p>
  </div>

   <!-- Project looks -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>💡 Project looks</h2>
    <ul>
      <h3>🔥 Index page </h3>
<img src="https://github.com/BIKRANT-RAWAT/MY_ML_PROJECTS/blob/master/Algerian_forest_fire_prediction/images/index_img.jpg" alt="Index page" width="500">
      <h3>🔥 Predict_datapoint page</h3>
<img src="https://github.com/BIKRANT-RAWAT/MY_ML_PROJECTS/blob/master/Algerian_forest_fire_prediction/images/predic_page.jpg" alt="prediction page" width="500">
      
   
  </div>

  <!-- Why This Project Matters -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>💡 Why It Matters</h2>
    <ul>
      <li>🌍 Forest fires cause serious ecological damage and economic loss; prediction helps prevention and resource allocation.</li>
      <li>📊 Understanding environmental patterns (temperature, humidity, wind, etc.) is essential for actionable insights.</li>
      <li>🤖 Demonstrates machine learning applied to real-world, high-impact problems.</li>
    </ul>
  </div>

  <!-- Data & Features -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>🔍 Data & Features</h2>
    <ul>
      <li>Data sources include meteorological and environmental variables from Algerian weather stations.</li>
      <li>Features such as temperature, relative humidity, wind speed, rain, seasonal indicators, etc.</li>
      <li>Data cleaning to handle missing values and correct anomalies.</li>
    </ul>
  </div>

  <!-- Model & Approach -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>🛠️ Model & Approach</h2>
    <ul>
      <li>Exploratory Data Analysis to understand distributions, correlations and outliers.</li>
      <li>Feature engineering (e.g. seasonal encoding, categorical features, scaling).</li>
      <li>Try multiple models — e.g., Rigde,Lasso etc.</li>
      <li>Model evaluation using metrics like RMSE, MAE, or classification metrics if framed as classification problem.</li>
      <li>Cross-validation to ensure generalization.</li>
    </ul>
  </div>

  <!-- Project Structure -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>📂 Project Structure</h2>
    <pre style="background:#272822; color:#f8f8f2; padding:15px; border-radius:8px; overflow:auto;">
Algerian_forest_fire_prediction/
│
├── data/                  # Raw & processed datasets
├── notebooks/             # Notebooks for exploration & prototyping
├── models/                # Saved model artifacts
├── src/                   # Core scripts (preprocessing, training, evaluation)
├── README.md              # This project readme
└── requirements.txt       # Dependencies
    </pre>
  </div>

  <!-- Technologies Used -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>🧰 Technologies Used</h2>
    <ul>
      <li>Python – main programming language</li>
      <li>Pandas, NumPy – data manipulation</li>
      <li>Matplotlib, Seaborn – visualization</li>
      <li>Scikit-Learn – machine learning models</li>
      <li>flask for web framework</li>
      <li>Jupyter Notebook for prototyping</li>
    </ul>
  </div>

  <!-- How to Run / Usage -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>⚙️ How to Run</h2>
    <ol>
      <li>Clone this project:  
        <pre style="background:#272822; color:#f8f8f2; padding:10px; border-radius:6px; overflow:auto;">git clone https://github.com/BIKRANT-RAWAT/MY_ML_PROJECTS.git</pre>
      </li>
      <li>Navigate to the project folder:  
        <code>cd MY_ML_PROJECTS/Algerian_forest_fire_prediction</code>
      </li>
      <li>Install dependencies:  
        <pre style="background:#272822; color:#f8f8f2; padding:10px; border-radius:6px; overflow:auto;">pip install -r requirements.txt</pre>
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
  <img src="https://github.com/BIKRANT-RAWAT/MY_ML_PROJECTS/blob/master/Algerian_forest_fire_prediction/images/Histplot.png" alt="Histogram" width="350">
  <img src="https://github.com/BIKRANT-RAWAT/MY_ML_PROJECTS/blob/master/Algerian_forest_fire_prediction/images/fire%20or%20not%20fire.png" alt="fire or not fire" width="350">
   <img src="https://github.com/BIKRANT-RAWAT/MY_ML_PROJECTS/blob/master/Algerian_forest_fire_prediction/images/sidi%20bel%20region.png" alt="Sidi bel region" width="350">
   <img src="https://github.com/BIKRANT-RAWAT/MY_ML_PROJECTS/blob/master/Algerian_forest_fire_prediction/images/Bejaia%20region.png" alt="Bejaia region" width="350">
<li>Its observed that August and September had the most number of forest fires for both regions. And from the above plot of months, we can understand few things

Most of the fires happened in August and very high Fires happened in only 3 months - June, July and August.

Less Fires was on September</li>
</p>

  </div>

  <!-- Acknowledgement -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>🙏 Acknowledgement</h2>
    <p>
      Special thanks to the mentor Krish Naik sir and data science community for inspiring resources and mentorship.  
      Thanks to the open datasets and documentation that made this project possible.
    </p>
  </div>

  <footer style="text-align:center; margin-top:30px; font-size:0.9em; color:#555;">
    &copy; 2025 BIKRANT-RAWAT — Algerian Forest Fire Prediction project under MY_ML_PROJECTS.
  </footer>

</body>
</html>
