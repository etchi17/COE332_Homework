from flask import Flask, request
import redis
import json

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def load_data() -> str:
    """
    Reads in a JSON data file (ML_Data_Sample.json) and stores it as a dictionary. Creates Python Redis client object and creates a new entry in the database for each id#:dictionary_of_data pair. Returns string confirming completion of process.

    Returns:
        output (string): Short string confirming all the data has been loaded to the Redis database instance.
    """
    with open('ML_Data_Sample.json', 'r') as f:
        ml_data = json.load(f)

    rd = redis.Redis(host='10.97.154.87', port=6379)
    for n in ml_data['meteorite_landings']:
        rd.set(n['id'], json.dumps(n))       
    keystest = len(rd.keys())
    return f'ETH {keystest} Data has been loaded to Redis database instance\n'

@app.route('/data', methods=['GET'])
def get_data() -> str:
    """
    Creates Python Redis client object and creates a list containing all keys in the database, identfying the keys(id#) with the highest(maxID) and lowest(minID) values. Searches for start query parameter(int) to store as start; if not found defaults to start = minID. Uses a try-except statement that converts the start parameter to an int, checks that the start parameter is within the range minID to maxID, appends all decoded data from start parameter key to the last key in the database(maxID) to a list, checks if there are items in the list, and returns the list as a string. During the process, if any errors occur or criterias fail, it returns a string indicating that the start value is invalid. If for some reason the entire try-except statement is skipped, it also returns a string indicating that the start value is invalid.
    
    Returns:
        data_list (string): List of dictionaries containing each entry in the database from the start parameter id to the highest id value as an individual dictionary item.
        output (string): Short string indicating that start parameter is invalid as it fails at least one of the tests and should be re-entered as a numeric integer within the specified range.
    """
    rd = redis.Redis(host='10.97.154.87', port=6379)
    keys_list = []     
    for key in rd.keys():
        keys_list.append(json.loads(key))

    minID = min(keys_list) 
    maxID = max(keys_list)

    start = request.args.get('start',minID)        
    if start:
        try:
            start = int(start) 
            if start < minID or start > maxID:
                return f'Invalid start value; start must be numeric (between {minID} and {maxID}, inclusive).\n'
            data_list = []
            while start <= maxID:
                data_list.append(json.loads(rd.get(start)))
                start += 1
 
            if len(data_list) == 0:
                return f'Invalid start value; start must be numeric (between {minID} and {maxID}, inclusive).\n'
       
            return json.dumps(data_list, indent=2)+'\n'
        except:
            return f'Invalid start value; start must be numeric (between {minID} and {maxID}, inclusive).\n'
   
    return f'Invalid start value; start must be numeric (between {minID} and {maxID}, inclusive).\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
