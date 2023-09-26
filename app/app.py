from flask import Flask, render_template, request, jsonify
import boto3
import uuid
from flask_cors import CORS
import requests
import sys
from datetime import datetime
from datetime import datetime

sys.path.append('/home/ubuntu/effyaiweb/app')

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
        return {"error":"input error"}
    
    try:
        currentAge = int(input.get("currentAge"))
        retirementAge = int(input.get("retirementAge"))
        corpusGoal = float(input.get("corpusGoal"))
        interestRate = float(input.get("interestRate"))
        s3_url_final = str(input.get("s3_image_path"))
    except Exception as e:
        print("Value type error: ",e) 
        return {"error":"value error"}

    data = {
        "current_age": currentAge,
        "retirement_age": retirementAge,
        "s3_image_path": s3_url_final
    }
    print(data)

    try:
        json_response = requests.post("http://18.234.117.148/get_aging_video", json=data)
        response = json_response.json()
        print(response)
        video_path = response.get("video_output")
        # print(video_path)
        
    except Exception as e:
            print("video link api issue: ",e)
            return {"error": "server error"}
        
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
    #print(response_data)
    try:
        return response_data
    except Exception as e:
        print("Not able to send json data: ",e)
        return {"error":"server error"}

if __name__ == "__main__":
    app.run()














# @app.route('/calculate_sip', methods=['POST'])
# def calculate_sip():
#     currentAge = int(request.form['CurrentAge'])
#     retirementAge = int(request.form['RetirementAge'])
#     corpusGoal = float(request.form['CorpusGoal'])
#     interestRate = float(request.form['InterestRate']) / 100
#     # Local file path to the image you want to upload
#     local_image_path = '/temp/image.jpg'
#     # S3 bucket and object details
#     bucket_name = 'effy-bandhan'
    
#     try:
#         # Check if the request contains a file with the key 'image'
#         if 'uploadedImage' not in request.files:
#             print('No file part')
#         # Get the file from the request
#         file = request.files['uploadedImage']
#         # Check if the file is empty
#         if file.filename == '':
#             return 'No selected file'
#         # Generate a unique object key for S3 (you may modify this)
#         object_key = f'images/{file.filename}'
#         # Initialize the S3 client
#         s3 = boto3.client('s3', aws_access_key_id="AKIAVZBVXJWJLAWNRCWZ",
#                           aws_secret_access_key="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",
#                           region_name="us-east-1")
#         # Upload the file to S3
#         s3.upload_fileobj(file, bucket_name, object_key)
#         # Return the S3 URL of the uploaded file
#         s3_url = f'https://{bucket_name}.s3.amazonaws.com/{object_key}'
#         print(s3_url)
#         send_data = {
#             "s3_image_path":s3_url,
#             "current_age": currentAge,
#             "retirement_age":retirementAge
#         }
#         post_request = requests.post("http://18.234.117.148/get_aging_video", send_data)
#         post_request.headers['Content-Type'] = 'application/json'

#         video_url = post_request.json()
#         print(video_url)

#     except Exception as e:
#         return f'Error: {e}'
#     monthlyinterestRate = interestRate / 12
#     numberofMonths = (retirementAge - currentAge) * 12
#     MonthlySIP = (corpusGoal * monthlyinterestRate) / ((1 + monthlyinterestRate) ** numberofMonths - 1)
#     roundMonthlySIP = round(MonthlySIP)
#     # MonthlySIP = (corpusGoal * monthlyinterestRate) / (math.pow(1 + monthlyinterestRate, numberofMonths) - 1)
#     # Initialize a list to store closing balances for each year
#     closingBalances = []
#     openingBalance = 0
#     for year in range(currentAge, retirementAge + 1):
#         # Calculate the annual contribution (12 times the monthly SIP)
#         annualContribution = MonthlySIP * 12
#         # Calculate the interest earned for the year
#         interestEarned = (openingBalance + annualContribution) * interestRate
#         # Calculate the closing balance for the year
#         closingBalance = openingBalance + annualContribution + interestEarned
#         # Append the closing balance to the list
#         closingBalances.append({
#             "Age": year,
#             "ClosingBalance": round(closingBalance)
#         })
#         # Update the opening balance for the next year
#         openingBalance = closingBalance
    
#     # for item in closingBalances:
#     #     print(f"Age: {item['Age']}, Closing Balance: {item['ClosingBalance']:.2f}")
#     # Include the id in the JSON response
#     response_data = {
#         "Monthly SIP":roundMonthlySIP,
#         "closing balances":closingBalances,
#         "video_output":video_url
#     }
#     return jsonify(response_data)


# # 





# Local file path to the image you want to upload
    # local_image_path = '/temp/image.jpg'
    # S3 bucket and object details
    # bucket_name = 'effy-bandhan'

    # try:
    #     # Check if the request contains a file with the key 'image'
    #     if 'uploadedImage' not in request.files:
    #         return 'No file part'

    #     # Get the file from the request
    #     file = request.files['uploadedImage']

    #     # Check if the file is empty
    #     if file.filename == '':
    #         return 'No selected file'

    #     # Generate a unique object key for S3 (you may modify this)
    #     object_key = f'images/{file.filename}'

    #     # Initialize the S3 client
    #     s3 = boto3.client('s3', aws_access_key_id="AKIAVZBVXJWJLAWNRCWZ",
    #                       aws_secret_access_key="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",
    #                       region_name="us-east-1")

    #     # Upload the file to S3
    #     s3.upload_fileobj(file, bucket_name, object_key)

    #     # Return the S3 URL of the uploaded file
    #     s3_url = f'https://{bucket_name}.s3.amazonaws.com/{object_key}'
    #     print(f"Input url :{s3_url}")
        #http://18.234.117.148/get_aging_video
