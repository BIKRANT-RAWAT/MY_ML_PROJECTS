<!DOCTYPE html>
<html lang="en">
<body style="font-family: 'Arial', 'Helvetica', sans-serif; line-height:1.6; background-color:#f8f9fa; color:#2c3e50; padding:40px; max-width:900px; margin:auto;">

  <!-- Title -->
  <h1 style="text-align:center; font-size:3em; color:#2a3d66; background:#dbe9ff; padding:20px; border-radius:12px;">
    👶 Birth Weight Prediction
  </h1>
  <p style="text-align:center; font-size:1.1em; color:#555;">
    Part of the <strong>MY_ML_PROJECTS</strong> collection by BIKRANT-RAWAT — Predicting newborn birth weight based on maternal factors, health & habits.
  </p>

  <hr style="border:1px solid #ccc; margin:25px 0;">

  <!-- Project Overview -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>📖 Project Overview</h2>
    <p>
      The aim of this project is to build a model to predict the birth weight of newborns, given features such as maternal gestation period, smoking habit, mothers weight ,mothers height, etc.
      This helps in early risk assessment and medical planning.
    </p>
  </div>

   <!-- Project looks -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>💡 Project looks</h2>
    <ul>
      <h3>🔥 Index page </h3>
<img src="https://github.com/BIKRANT-RAWAT/MY_ML_PROJECTS/blob/master/birth_weight_prediction/images/predictpage.jpg" alt="Index page" width="500">
      <h3>🔥 Predict page</h3>
<img src="https://github.com/BIKRANT-RAWAT/MY_ML_PROJECTS/blob/master/birth_weight_prediction/images/prediction.jpg" alt="prediction" width="500">
      
   
  </div>


  <!-- Importance -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>💡 Why Birth Weight Prediction Matters</h2>
    <ul>
      <li>👩‍⚕️ Early detection of low birth weight helps in ensuring better neonatal care.</li>
      <li>📈 Understanding contributing factors can guide public health interventions.</li>
      <li>🤖 Demonstrates application of machine learning in healthcare and prediction problems.</li>
    </ul>
  </div>

  <!-- Data & Features -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>🔍 Data & Features</h2>
    <ul>
      <li>Input features include: mother's age, height, weight, smoking condition, gestation period etc.</li>
      <li>Target variable: Birth weight (continuous).</li>
      <li>Data cleaning: handling missing values, outliers, feature scaling.</li>
    </ul>
  </div>

  <!-- Model & Approach -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>🛠️ Model & Approach</h2>
    <ul>
      <li>Exploratory Data Analysis (EDA) to understand distributions, correlations, feature importance.</li>
      <li>Feature engineering: deriving new features, handling categorical data, normalization.</li>
      <li>Modeling: Linear Regression, Lasso , Ridge.</li>
      <li>Evaluation: metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), R² score.</li>
      <li>Cross-validation to ensure model generalizability.</li>
    </ul>
  </div>

  <!-- Project Structure -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>📂 Project Structure</h2>
    <pre style="background:#2c2f33; color:#f8f8f2; padding:15px; border-radius:8px; overflow:auto;">
birth_weight_prediction/
│
├── templates/             # flask file
├── images/                # contains images
├── model.ipynb            # Main EDA and Model training
├── model.pkl              # pickle file 
├── README.md              # This project readme
└── requirements.txt       # Dependencies listing
    </pre>
  </div>

  <!-- Technologies Used -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>🧰 Technologies Used</h2>
    <ul>
      <li>Python — primary language</li>
      <li>Pandas, NumPy — data manipulation & handling missing data</li>
      <li>Matplotlib, Seaborn — data visualization</li>
      <li>Scikit-Learn — machine learning models</li>
      <li>MSE, MAE,R2score</li>
      <li>Jupyter Notebook for experimentation</li>
    </ul>
  </div>

  <!-- How to Run / Usage -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>⚙️ How to Run</h2>
    <ol>
      <li>Clone the repo:<br>
        <pre style="background:#2c2f33; color:#f8f8f2; padding:10px; border-radius:6px; overflow:auto;">git clone https://github.com/BIKRANT-RAWAT/MY_ML_PROJECTS.git</pre>
      </li>
      <li>Navigate to the project directory:<br>
        <code>cd MY_ML_PROJECTS/birth_weight_prediction</code>
      </li>
      <li>Install dependencies:<br>
        <pre style="background:#2c2f33; color:#f8f8f2; padding:10px; border-radius:6px; overflow:auto;">pip install -r requirements.txt</pre>
      </li>
       <li>Run :
         <pre style="background:#272822; color:#f8f8f2; padding:10px; border-radius:6px; overflow:auto;">python app.py</pre>
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
  <img src="https://github.com/BIKRANT-RAWAT/MY_ML_PROJECTS/blob/master/birth_weight_prediction/images/birthweight%20mothersweight.png" alt="bw weight" width="350">
  <img src="https://github.com/BIKRANT-RAWAT/MY_ML_PROJECTS/blob/master/birth_weight_prediction/images/birthweight%20gestation.png" alt="bg weight" width="350">
  <li> Mothers weight ranging 100 to 160 pound gives birth to babies ranging 100 to 140 ounces. </li>
  <li>Mothers gestation period ranging in 280 to 300 days mostly produce healthy babies.</li>
</p>

  </div>


  <!-- Acknowledgement -->
  <div style="background:#ffffff; padding:20px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:25px;">
    <h2>🙏 Acknowledgement</h2>
    <p>
      I am grateful for the guidance and teaching by mentor Noorain sir and all learning resources I referenced.  
      Thanks to dataset sources, documentation, tutorials, and open-source tools that made this project possible.
    </p>
  </div>

  <footer style="text-align:center; margin-top:30px; font-size:0.9em; color:#555;">
    &copy; 2025 BIKRANT-RAWAT — Birth Weight Prediction Project under MY_ML_PROJECTS.
  </footer>

</body>
</html>
