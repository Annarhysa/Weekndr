from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the data from a CSV file
data = pd.read_csv('data/weekend_plans.csv')


# Endpoint to suggest weekend plans
@app.route('/suggest-plans', methods=['GET'])
def suggest_plans():
    location = request.args.get('location', '')
    
    # Check if location is provided
    if not location:
        return jsonify({'error': 'Location is required!'}), 400

    # Filter the data based on the provided location
    filtered_data = data[data['city'] == location]

    #extracting the plan for the specific city and the descripton of the plan
    filtered_data_columns = filtered_data[['plan', 'description', 'reference']]
    filtered_data_list = filtered_data_columns.apply(lambda x: x.unique().tolist()).tolist()

    return jsonify({'suggested_plans': filtered_data_list[0]},
                    {'Description': filtered_data_list[1]},
                    {'Link': filtered_data_list[2]})

if __name__ == '__main__':
    app.run(debug=True)
