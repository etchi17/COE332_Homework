from flask import Flask, request
import redis
import json

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def load_data() -> str:
    with open('ML_Data_Sample.json', 'r') as f:
        ml_data = json.load(f)

    rd = redis.Redis(host='172.17.0.15', port=6379)
    for n in ml_data['meteorite_landings']:
        rd.set(n['id'], json.dumps(n))

    return f'Data has been loaded to Redis database instance\n'

@app.route('/data', methods=['GET'])
def get_data() -> str:
    rd = redis.Redis(host='172.17.0.15', port=6379)
    start = request.args.get('start',10001)
    
    keys_list = []
    for key in rd.keys():
        keys_list.append(json.loads(key))

    minID = min(keys_list)
    maxID = max(keys_list)
        
    if start:
        try:
            start = int(start)
            if start < minID or start > maxID:
                raise TypeError('oofers bro')
                return f'Invalid start value(skipped the oofer); start must be numeric (between {minID} and {maxID}, inclusive).\n'
            data_list = []
            while start <= 10000 + len(rd.keys()):
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
