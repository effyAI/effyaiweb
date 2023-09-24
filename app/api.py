import math
from decimal import Decimal

from flask import Flask, render_template, request, jsonify
from flask_restful import Api
# import sys
# sys.path.append('/home/ubuntu/effyaiweb/src')
from src.get_aging_video import age_input

app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return {"response": "Hello"}


@app.route('/calculate_sip', methods=['POST'])
def calculate_sip():
    data = request.get_json()

    currentAge = data['CurrentAge']
    retirementAge = data['RetirementAge']
    corpusGoal = data['CorpusGoal']
    interestRate = data['InterestRate']/100

    monthlyinterestRate = interestRate / 12
    numberofMonths = (retirementAge - currentAge) * 12
    MonthlySIP = (corpusGoal * monthlyinterestRate) / ((1 + monthlyinterestRate) ** numberofMonths - 1)
    # MonthlySIP = (corpusGoal * monthlyinterestRate) / (math.pow(1 + monthlyinterestRate, numberofMonths) - 1)

    # Initialize a list to store closing balances for each year
    closingBalances = []
    openingBalance = 0

    for year in range(currentAge, retirementAge + 1):
        # Calculate the annual contribution (12 times the monthly SIP)
        annualContribution = MonthlySIP * 12

        # Calculate the interest earned for the year
        interestEarned = (openingBalance + annualContribution) * interestRate

        # Calculate the closing balance for the year
        closingBalance = openingBalance + annualContribution + interestEarned

        # Append the closing balance to the list
        closingBalances.append({
            "Age": year,
            "ClosingBalance": "{:.2f}".format(closingBalance)
        })

        # Update the opening balance for the next year
        openingBalance = closingBalance

    # for item in closingBalances:
    #     print(f"Age: {item['Age']}, Closing Balance: {item['ClosingBalance']:.2f}")

    # Sending the response in decimal places
    return jsonify({'MonthlySIP': Decimal(MonthlySIP), 'ClosingBalance': closingBalances})

@app.route('/get_aging_video', methods=['GET'])
def get_aging_video():
    # data = request.get_json()
    input_img = 'https://i.pinimg.com/736x/ad/b4/60/adb4602cbd454354e71b5f214fb4e0ec.jpg'
    currentAge = 25
    retirementAge = 80
    res = age_input(input_img, currentAge, retirementAge)
    return res

if __name__ == "__main__":
    app.run(debug=True)
