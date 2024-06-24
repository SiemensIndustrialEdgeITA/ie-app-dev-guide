from dataclasses import dataclass
from datetime import datetime
from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
from sql_manager import SqlClient, SqlConfig
from typing import Union
import json
import os


# SQL client
sql_client: Union[SqlClient, None] = None

# Setup Flask
app = Flask(__name__)
CORS(app) # Enable CORS for all routes

@app.route('/api/get-last-data', methods=['GET'])
def get_last_data():
    """Send last inserted data from DB to Front-end
    """
    query = f'SELECT * FROM words ORDER BY datetimecolumn DESC LIMIT 1'
    rows = sql_client.select_data(query)
    return jsonify({'res': rows}), 200

@app.route('/api/post-data', methods=['POST'])
def post_data():
    """Save data received from Front-end to DB
    """
    if request.method == 'POST':
        # Access the incoming JSON data
        data = request.json
        
        # Reverse data {"text": "..."}
        reversed_data = data['text'][::-1]

        query = f"INSERT INTO words (datetimecolumn, word, reverseword) \
                VALUES('{datetime.now().isoformat()}', '{data['text']}', '{reversed_data}');"
        print(query)
        sql_client.insert_data(query)
        
        # Return a JSON response
        return jsonify({'text': reversed_data}), 200

if __name__ == "__main__":    
    # Load configuration from config folder
    jsonData = None
    with open('/cfg-data/rest_config.json') as file:
        jsonData = json.load(file)

    if jsonData == None:
        # Pass configuration to sql_client and start connection
        sql_config = SqlConfig(
            host=os.getenv('POSTGRES_HOST'),
            port=5432,
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD'),
            db='mydb',
        )
    else:
        sql_config = SqlConfig(
            host=jsonData['postgresHost'],
            port=5432,
            user=jsonData['postgresUser'],
            password=jsonData['postgresPassword'],
            db='mydb',
        )

    sql_client = SqlClient(sql_config=sql_config)
    app.run(host='0.0.0.0', debug=True, port=5000, threaded=True)