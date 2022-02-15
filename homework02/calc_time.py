import json
import math

mars_radius = 3389.5 
robot_start = {}
robot_start['latitude'] = 16.0
robot_start['longitude'] = 82.0
robot_speed = 10

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )

def main():
    with open('Meteorite_Landings.json', 'r') as f:
        ml_data = json.load(f)

    lat1 = robot_start['latitude']
    lon1 = robot_start['longitude']
    total_time = 0

    for row in ml_data['sites']:
        leg = row['site_id']
        lat2 = row['latitude']
        lon2 = row['longitude']
        distance = calc_gcd(lat1, lon1, lat2, lon2)
        travel_time = distance/robot_speed

        if row['composition'] == 'stony':
            sample_time = 1
        elif row['composition'] == 'iron':
            sample_time = 2
        else:
            sample_time = 3

        total_time = total_time + travel_time + sample_time
        print('leg = '+ str(leg) + ', time to travel = '+ str(travel_time) + ' hr, time to sample = ' + str(sample_time) +' hr')
	
        lat1 = lat2
        lon1 = lon2

    print('summary: number of legs = '+ str(leg) + ', total time elapsed = '+ str(total_time) +' hr')

if __name__ == '__main__':
    main()	    
