📊 Financial Analysis & Investment System
An AI-powered web application that serves as a Personal Financial Advisor. This project uses Machine Learning (Linear Regression) to predict expenses and provides tailored investment recommendations based on risk profiling.

🛠️ Tech Stack
Backend: Python, Flask
Machine Learning: Scikit-Learn (Linear Regression, KNN), NumPy
Frontend: HTML5, CSS3, JavaScript
Data Visualization: Chart.js

🧠 Core Features
Expense Prediction: Uses LinearRegression to forecast spending based on income trends.
Risk Assessment: Calculates risk appetite (High to Low) based on the user's age.
Investment Strategy: Suggests Equity/Debt split and Emergency Fund requirements.
Health Metrics: Generates a Financial Health Score and Savings Rate percentage.
Interactive Charts: Dynamic Scatter and Line plots to visualize financial data.

📂 Project Structure
project_folder/
│
├── app.py              # Flask Backend, ML Model & Financial Logic
├── static/
│   └── style.css       # UI Styling & Responsive Design
├── templates/
│   ├── index.html      # User Input Form / Analysis Report & Chart.js Dashboards
└── README.md           # Project Documentation

🚀 Installation & Setup
1. Clone the project
2. Install dependencies:
   pip install flask numpy scikit-learn matplotlib
3. Run the application:
   python app.py
4.View in browser: " http://127.0.0.1:5000 "

