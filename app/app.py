from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
cors = CORS(app)

c_age  = 0
r_age = 0

info = {}

app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def home():
    return render_template('index.html')
@app.route('/hello')
def hello():
    return {"response": "Hello"}

@app.route('/calculate_it', methods=['POST'])
def calculate_it():
    print("API called.")
    try:
        input = request.get_json()
        print(input)
    except Exception as e:
        print("Post data reading error:",e) # Send error to server
        return {"error":403}
    
    try:
        currentAge = int(input.get("currentAge"))
        retirementAge = int(input.get("retirementAge"))
        corpusGoal = float(input.get("corpusGoal"))
        interestRate = float(input.get("interestRate"))
        s3_url_final = str(input.get("s3_image_path"))
    except Exception as e:
        print("Value type error: ",e) 
        return {"error":403}

    data = {
        "current_age": currentAge,
        "retirement_age": retirementAge,
        "s3_image_path": s3_url_final
    }
    print(data)

    
    json_response = requests.post("http://18.234.117.148/get_aging_video", json=data)
    response = json_response.json()
    print(response)
    if response == {"error":405}:
        return {"error":405}    
    else:
        video_path = response.get("video_output")
        print(video_path)
    
        if video_path != None:        
            interestRate = interestRate/100
            monthlyinterestRate = interestRate / 12
            numberofMonths = (retirementAge - currentAge) * 12
            MonthlySIP = (corpusGoal * monthlyinterestRate) / ((1 + monthlyinterestRate) ** numberofMonths - 1)
                # Initialize a list to store closing balances for each year
            RoundMonthlySIP = round(MonthlySIP/1000) *1000
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
                        "ClosingBalance": round(closingBalance)
                    })
                        # Update the opening balance for the next year
                openingBalance = closingBalance
                    
            response_data={
                    "monthly sip": RoundMonthlySIP,
                    "closing balance": closingBalances,
                    "s3_output": video_path
            }
            print(response_data)
            try:
                return response_data
            except Exception as e:
                print("Not able to send json data: ",e)
                return {"error":500}
        else:
            return {"error":500}
        
if __name__ == "__main__":
    app.run()