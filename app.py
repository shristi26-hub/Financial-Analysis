from flask import Flask, render_template, request
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# =========================
# Train Model Once
# =========================
data = np.array([
  [5000, 4400],
[7000, 6100],
[9000, 7500],
[11000, 8800],
[13000, 10100],
[15000, 11700],
[18000, 13900],
[21000, 15900],
[24000, 17800],
[27000, 19600],

[30000, 21000],
[33000, 22400],
[36000, 24400],
[40000, 26800],
[45000, 29700],
[50000, 33000],
[60000, 38400],
[70000, 43400],
[80000, 48000],
[90000, 52200],

[100000, 56000],
[120000, 64800],
[140000, 74200],
[160000, 83200],
[180000, 91800],
[200000, 100000],
[230000, 113000],
[260000, 127000],
[300000, 144000],
[340000, 160000],

[380000, 176000],
[420000, 193000],
[460000, 211000],
[500000, 225000],
[550000, 247500],
[600000, 270000],
[650000, 292500],
[700000, 315000],
[750000, 337500],
[800000, 360000],

[830000, 373500],
[860000, 387000],
[890000, 400500],
[920000, 414000],
[950000, 427500],
[970000, 436500],
[980000, 441000],
[990000, 445500],
[995000, 448000],
[1000000, 450000]
])

income = data[:, 0].reshape(-1, 1)
expenses = data[:, 1]

reg_model = LinearRegression()
reg_model.fit(income, expenses)


# =========================
# Single Page Route
# =========================
@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        # =========================
        # Collect Form Data
        # =========================
        user_income = float(request.form["income"])
        user_age = int(request.form["age"])
        occupation = request.form["occupation"]
        family_size = int(request.form["family_size"])
        city_type = request.form["city_type"]
        savings_goal = float(request.form["goal"])

        # =========================
        # Predict Expense
        # =========================
        new_income = np.array([[user_income]])
        predicted_expense = reg_model.predict(new_income)[0]

        # Prevent negative values
        predicted_expense = max(0, predicted_expense)

        # Prevent expense exceeding income
        predicted_expense = min(predicted_expense, user_income * 0.95)

        # Optional: round it nicely
        predicted_expense = round(predicted_expense, 2)

        # =========================
        # Savings Calculations
        # =========================
        actual_savings = max(0, user_income - predicted_expense)
        annual_savings = actual_savings * 12

        # =========================
        # Goal Achievement
        # =========================
        if savings_goal > 0:
            goal_percentage = min((actual_savings / savings_goal) * 100, 100)
        else:
            goal_percentage = 0

        if actual_savings >= savings_goal:
            status = "Goal Achieved"
        else:
            status = "Goal Not Achieved"

        # =========================
        # Financial Metrics
        # =========================
        if user_income > 0:
            savings_rate = actual_savings / user_income
            expense_ratio = predicted_expense / user_income
        else:
            savings_rate = 0
            expense_ratio = 0

        financial_health_score = int(savings_rate * 100)

        # Spending Type
        if expense_ratio < 0.5:
            spending_type = "Saver"
        elif expense_ratio < 0.75:
            spending_type = "Balanced"
        else:
            spending_type = "Spender"

        # =========================
        # Investment Recommendation
        # =========================

        # Risk Profile
        if user_age <= 30:
            risk_level = "High"
            equity_percent = 70
        elif user_age <= 45:
            risk_level = "Moderate"
            equity_percent = 50
        elif user_age <= 60:
            risk_level = "Low-Moderate"
            equity_percent = 35
        else:
            risk_level = "Low"
            equity_percent = 20

        debt_percent = 100 - equity_percent

        # Expense Assessment
        if expense_ratio > 0.8:
            expense_message = "Your expense ratio is high. Expense optimization is recommended before aggressive investing."
        elif expense_ratio > 0.7:
            expense_message = "Your expenses are moderately high. Maintain financial discipline."
        else:
            expense_message = "Your expense level is healthy."

        # Emergency Fund
        if occupation.lower() == "business":
            emergency_months = 9
        elif occupation.lower() == "job":
            emergency_months = 6
        else:
            emergency_months = 3

        emergency_fund = int(predicted_expense * emergency_months)

        # Investment Instruments
        if risk_level == "High":
            instruments = [
                "Index Funds",
                "Large & Mid Cap Mutual Funds",
                "Selective Equity Stocks"
            ]
        elif risk_level == "Moderate":
            instruments = [
                "Large Cap Mutual Funds",
                "Hybrid Funds",
                "Debt Funds"
            ]
        elif risk_level == "Low-Moderate":
            instruments = [
                "Balanced Advantage Funds",
                "Debt Mutual Funds",
                "Public Provident Fund"
            ]
        else:
            instruments = [
                "Fixed Deposits",
                "Public Provident Fund",
                "Government Bonds"
            ]

        # SIP Suggestion
        if savings_rate < 0.15:
            invest_percent = 0.5
        elif savings_rate < 0.25:
            invest_percent = 0.7
        else:
            invest_percent = 0.85

        recommended_sip = int(actual_savings * invest_percent)

        # =========================
        # Graph Data (Only 2 Graphs)
        # =========================

        income_list = income.flatten().tolist()
        expense_list = expenses.tolist()

        predicted_line = reg_model.predict(income).flatten().tolist()

        # =========================
        # Final Result Object
        # =========================
        result = {
            "income": int(user_income),
            "expense": int(predicted_expense),
            "savings": int(actual_savings),
            "annual_savings": int(annual_savings),
            "savings_goal": int(savings_goal),
            "goal_percentage": round(goal_percentage, 2),
            "status": status,
            "spending_type": spending_type,
            "savings_rate": round(savings_rate * 100, 2),
            "expense_ratio": round(expense_ratio * 100, 2),
            "health_score": financial_health_score,
            "age": user_age,
            "occupation": occupation.capitalize(),
            "family_size": family_size,
            "city_type": city_type.capitalize(),
            "risk_level": risk_level,
            "equity_percent": equity_percent,
            "debt_percent": debt_percent,
            "expense_message": expense_message,
            "emergency_fund": emergency_fund,
            "recommended_sip": recommended_sip,
            "instruments": instruments,
            "income_list": income_list,
            "expense_list": expense_list,
            "predicted_line": predicted_line,
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)