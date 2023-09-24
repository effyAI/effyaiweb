import math
from decimal import Decimal

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
# import sys
# sys.path.append('/home/ubuntu/effyaiweb/src')
from src.get_aging_video import age_input
import boto3
from app.database import db
from app.models import CorpusData

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///corpus_data.db'
db.init_app(app)

# Create the tables (run only once when the app starts)
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return {"response": "Hello"}


@app.route('/calculate_sip', methods=['POST'])
def calculate_sip():
    currentAge = int(request.form['CurrentAge'])
    retirementAge = int(request.form['RetirementAge'])
    corpusGoal = float(request.form['CorpusGoal'])
    interestRate = float(request.form['InterestRate']) / 100

    # Local file path to the image you want to upload
    local_image_path = '/temp/image.jpg'
    # S3 bucket and object details
    bucket_name = 'effy-bandhan'

    try:
        # Check if the request contains a file with the key 'image'
        if 'uploadedImage' not in request.files:
            return 'No file part'

        # Get the file from the request
        file = request.files['uploadedImage']

        # Check if the file is empty
        if file.filename == '':
            return 'No selected file'

        # Generate a unique object key for S3 (you may modify this)
        object_key = f'images/{file.filename}'

        # Initialize the S3 client
        s3 = boto3.client('s3', aws_access_key_id="AKIAVZBVXJWJLAWNRCWZ",
                          aws_secret_access_key="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",
                          region_name="us-east-1")

        # Upload the file to S3
        s3.upload_fileobj(file, bucket_name, object_key)

        # Return the S3 URL of the uploaded file
        s3_url = f'https://{bucket_name}.s3.amazonaws.com/{object_key}'
    except Exception as e:
        return f'Error: {e}'


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
    # Store the calculated data in the database
    corpus_data = CorpusData(
        current_age=currentAge,
        retirement_age=retirementAge,
        corpus_goal=corpusGoal,
        interest_rate=interestRate,
        monthly_sip=MonthlySIP,
        closing_balance=closingBalances,
        image_url=s3_url
    )
    db.session.add(corpus_data)
    db.session.commit()
    # for item in closingBalances:
    #     print(f"Age: {item['Age']}, Closing Balance: {item['ClosingBalance']:.2f}")

    # Include the id in the JSON response
    response_data = {
        'id': corpus_data.id
    }

    return jsonify(response_data)


@app.route('/fetch_corpus_data/<int:id>', methods=['GET'])
def fetch_corpus_data_by_id(id):
    corpus_data = CorpusData.query.get(id)

    if corpus_data is None:
        return jsonify({'error': 'Record not found'}), 404

    data = {
        'id': corpus_data.id,
        'CurrentAge': corpus_data.current_age,
        'RetirementAge': corpus_data.retirement_age,
        'CorpusGoal': corpus_data.corpus_goal,
        'InterestRate': corpus_data.interest_rate,
        'MonthlySIP': corpus_data.monthly_sip,
        'ClosingBalance': corpus_data.closing_balance,
        's3_url': corpus_data.image_url
    }
    return jsonify(data)

@app.route('/get_aging_video', methods=['GET'])
def get_aging_video():
    # data = request.get_json()
    input_img = 'https://i.pinimg.com/736x/ad/b4/60/adb4602cbd454354e71b5f214fb4e0ec.jpg'
    currentAge = 25
    retirementAge = 80
    res = age_input(input_img, currentAge, retirementAge)
    return res

if __name__ == "__main__":
    app.run(debug = True, port=5000)
