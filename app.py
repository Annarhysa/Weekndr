from flask import Flask, render_template, jsonify, redirect, url_for, request
from flask_cors import CORS
import json
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the data from a CSV file
data = pd.read_csv('data/weekend_plans.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest_plans', methods=['POST'])
def suggest_plans():
    location = request.json

    # Filter the data based on the provided location
    filtered_data = data[data['city'] == location["name"]]

    # Extracting the plan for the specific city and the description of the plan
    filtered_data_columns = filtered_data[['plan', 'description', 'reference']]
    filtered_data_list = filtered_data_columns.apply(lambda x: x.unique().tolist()).tolist()

    # Extract plans, descriptions, and links for the specific city
    plans = list(zip(filtered_data_list[0], filtered_data_list[1], filtered_data_list[2]))

    # Render the output on an HTML page
    return jsonify({'plans' : plans})

@app.route('/plans')
def plans():
    plans_data = request.args.get('plans', '[]')  # Retrieving plans data from query parameter
    plans = json.loads(plans_data)  # Parsing the plans data from JSON string to Python list
    return render_template('plans.html', plans=plans)

if __name__ == '__main__':
    app.run(debug=True)
