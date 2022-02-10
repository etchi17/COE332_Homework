import json
import random

composition = ['stony', 'iron', 'stony-iron']
landing_sites = {}
landing_sites['sites'] = []

for i in range(5):
    site_dict = {}
    site_dict['site_id'] = i+1
    site_dict['latitude'] = random.uniform(16.0, 18.0)
    site_dict['longitude'] = random.uniform(82.0, 84.0)
    site_dict['composition'] = composition[random.randint(0, 2)]
    landing_sites['sites'].append(site_dict)

with open('Meteorite_Landings.json', 'w') as out:
    json.dump(landing_sites, out, indent=2)
