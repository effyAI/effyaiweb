from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from src.get_aging_video import age_input
from src.models.psp import pSp
import os
import pprint
import torch
from argparse import Namespace
import uuid

# Model Loading
model_path = "/home/ubuntu/development/effyaiweb/app/src/pretrained_models/sam_ffhq_aging.pt"
if not os.path.exists(model_path):
    print('Download pretained model and save it in "app/src/pretained_models" dir or if already downloaded then save the model path correctly')
ckpt = torch.load(model_path, map_location='cpu')
opts = ckpt['opts']
# pprint.pprint(opts)
opts['checkpoint_path'] = model_path
opts = Namespace(**opts)
net = pSp(opts)
print('Model is loaded...')


app = Flask(__name__)
cors = CORS(app)
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

    app.logger.info('This is an access log message.')

    print("Starting Calculate_it...")
    try:
        input = request.get_json()
        print(input)
    except Exception as e:
        #print("Post data reading error:",e) # Send error to server
        return {"error":403}
    
    currentAge = int(input.get("currentAge"))
    retirementAge = int(input.get("retirementAge"))
    corpusGoal = float(input.get("corpusGoal"))
    interestRate = float(input.get("interestRate"))

    RoundMonthlySIP , closingBalances = calculation(currentAge,retirementAge, corpusGoal,interestRate)
    
    response_data={
        "monthly sip": RoundMonthlySIP,
        "closing balances": closingBalances
    }
    #print(response_data)
    return response_data
           

@app.route('/get_video', methods=['POST'])
def get_video():
    print("Starting the face aging...")
    try:
        input = request.get_json()
        # print(input)
    except Exception as e:
        print("Post data reading error:",e) # Send error to server
        return {"error":403}
    
    
    current_age = int(input.get("currentAge"))
    retirement_age = int(input.get("retirementAge"))
    # corpusGoal = float(input.get("corpusGoal"))
    # interestRate = float(input.get("interestRate"))
    s3_image_path = str(input.get("s3_image_path")) 

    print(s3_image_path)

    # UUID generation
    uuid1 = uuid.uuid1()

    # res = age_input(s3_image_path, net, current_age, retirement_age, uuid1)
    # print(res)
    # torch.cuda.empty_cache() 

    try:
        res = age_input(s3_image_path, net, current_age, retirement_age, uuid1)
        print(res)
        # torch.cuda.empty_cache() 
    except Exception as e:
        print('exceptional error...', e)
        return {'error': 404}
    return res




# Calculation function
def calculation(currentAge,retirementAge,corpusGoal,interestRate):
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

    return RoundMonthlySIP, closingBalances
        
        
if __name__ == "__main__":
    app.run(debug=True)
