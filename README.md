# 📊 AI-Driven Financial Advisor & Investment System

A sophisticated web-based financial analysis tool that uses **Supervised Machine Learning** to predict user expenses and provide personalized investment roadmaps.

---

## 🚀 Overview
This system acts as a mini-financial consultant. By analyzing your income and personal profile, it provides:
* **Predictive Spending:** ML-based expense forecasting.
* **Risk Analysis:** Age-based risk tolerance profiling.
* **Asset Allocation:** Tailored Equity vs. Debt recommendations.
* **Emergency Planning:** Occupation-specific emergency fund targets.



---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.12 |
| **Backend** | Flask (Python Framework) |
| **Machine Learning** | Scikit-Learn (Linear Regression, KNN), NumPy |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Visualization** | Chart.js, Matplotlib |

---

## 🧠 Machine Learning & Logic

### 📈 Expense Prediction
The system utilizes a **Linear Regression** model to identify the correlation between income and expenses.
> **Formula:** $Expense = \beta_0 + \beta_1(Income)$

### 🛡️ Investment Strategy
The system implements a tiered risk logic:
* **High Risk (Age ≤ 30):** High Equity / Low Debt.
* **Moderate Risk (Age 31-45):** Balanced Portfolio.
* **Low Risk (Age > 60):** Principal Protection / High Debt.



---

## 📂 Project Structure

```text
📁 project_folder
├── 📄 app.py              # Main Flask app & ML Model logic
├── 📁 static
│   └── 📄 style.css       # UI Styling & Layout
├── 📁 templates
│   ├── 📄 index.html      # User Input Form and Analysis Dashboard & Interactive Charts
└── 📄 README.md           # Project Documentation
```
## ⚙️ Installation & Setup

To get this project running on your local machine, follow these steps:

### 1. Prerequisites
Ensure you have **Python 3.8+** installed. You can check by running:
```bash
python --version
```
### 2. Clone the Repository
Download the project files to your computer:
```
git clone [https://github.com/your-username/financial-analysis-system.git](https://github.com/your-username/financial-analysis-system.git)
cd financial-analysis-system
```
### 3. Install Dependencies
Install the required Python libraries using pip. These are necessary for the Machine Learning models and the Web Interface:
```
pip install flask numpy scikit-learn matplotlib
```
### 4. Run the Application
Start the Flask development server:
```
python app.py
```
### 5. Access the Dashboard
Once the terminal shows the server is active, open your browser and navigate to:
URL: http://127.0.0.1:5000

