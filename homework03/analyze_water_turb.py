import json
import math
import logging
from typing import List

logging.basicConfig(level = logging.INFO)

def calc_turb(turb_data_list_dict: List[dict], calibration_const_key: str, detect_current_key: str) -> float:
    """
    Iterates through the last 5 dictionaries in a list of dictionaries, pulling out values associated with 2 given keys, the calibration constant and detector current. Returns the average of the product of those 2 values.

    Args:
        turb_data_list_dict (list): A list of dictionaries with the same set of keys.
        calibration_const_key (string): A key that appears in each dictionary containing a float item, the calibration constant.
        detect_current_key (string): A key that appears in each dictionary containing a float item, the detector current.

    Returns:
        result (float): The average of the product of the 2 float arguments from each dictionary. The sum of all calculated turbidities divided by number of dictionaries iterated over.
    """
    N = 5
    recent_dicts_data = turb_data_list_dict[-N:]

    turbs = []
    for item in recent_dicts_data:
        a0 = item[calibration_const_key]
        I90 = item[detect_current_key]
        turbs.append(a0*I90)

    turb_sum = 0
    for turb in turbs:
        turb_sum = turb_sum + turb

    return(turb_sum/N)

def calc_min_time(turb_thresh: float, current_turb: float, decay_factor: float) -> float:
    """
    Calculates the time it takes for an inputted float value, the current turbidity, to decay and reach another inputted float value, the turbidity threshold, using a decay function

    Args:
        turb_thresh (float): the turbidity threshold for safe water and end value that the current turbidity is being dacayed towards in NTU
        current_turb (float): the current turbidity of the water in NTU
        decay_factor (float): the decay factor per hour that determines the rate that the current turbidity decays, expressed as a decimal

    Returns:
        time (float): the time it takes, in hours, for the current turbidity to reach the turbidity threshold for safe water.
    """
    time = (math.log(turb_thresh/current_turb)) / (math.log(1 - decay_factor))
    if time < 0:
        time = 0

    return(time)


def main():
    DECAY_FACTOR = 0.02
    TURB_THRESH = 1

    with open('turbidity_data.json', 'r') as f:
        turb_data = json.load(f)

    avg_turb = calc_turb(turb_data['turbidity_data'], 'calibration_constant', 'detector_current')
    print("Average turbidity based on most recent five measurements = " + str(avg_turb) + " NTU")

    if avg_turb > TURB_THRESH:
        logging.warning("Turbidity is above threshold for safe use")
    else:
        logging.info("Turbidity is below threshold for safe use")

    min_time = calc_min_time(TURB_THRESH, avg_turb, DECAY_FACTOR)
    print("Minimum time required to return below a safe threshold = " + str(min_time) + " hours")

if __name__ == '__main__':
    main()
