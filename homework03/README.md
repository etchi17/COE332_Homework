# Analyzing Water: Calculating Tubridity and Time Needed to Reach Safe Threshold

In this project, were given a data set containing the qualities and properties of water samples. We then use those properties to calculate the average turbidity of the five most recent samples. Once acquired, we calculate how long it would take for that turbidity to reach a safe threshold. These types of calculations take the calibration constant and detector current of water into account during its turbidity calculations and the decay factor during its time to reach a safe threshold calculations. It uses known equations to calculate these values, providing relatively accurate approximations. This is important as having clean water is important for a variety of reasons, including analyzing samples and personal health. As such, being able to analyze the quality of water, seeing if it is clean enough, and calculating how long it would take to be clean enough is extremely useful for those reasons above. 

# Downloading Water Quality Data Set

The first step is to make sure the water quality data set, containing the turbidity data, is downloaded. To do so, simply use the wget command by entering:

    wget https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json

Alternatively, the data set can also be acquired by pasting the above link in a web browser and copying and pasting the contents into user created JSON file.

# analyze_water_turb.py

This is the first script that should be run after downloading the data set that takes the five most recent water samples, calculates the turbidity of the water, and calculates the time it takes for the water to reach a safe threshold. The script contains the function calc_turb which takes in a list of dictionaries(the water quality data set) and the two keys from that list of dictionaries(calibration_constant and detector_current). The function then creates a new list containing the five most recent dictionaries from the list of dictionaries inputted and calculates the average turbidity of those water samples. The script also contains the function calc_min_time which calculates how long it should take for an inputted turbidity to reach a safe turbidity in a specific decay factor. The script takes in a safe turbidity value, the current turbidity value, and decay factor and solves for the time. The overall script takes the water quality data set and calculates the average turbidity using calc_turb. Once acquired, it takes the average turbidity calculated and compared it to the safe turbidity threshold of 1 and outputs a log displaying either a warning or info if it's above or below the threshold, respectively. It then uses that turbidity and calculates how long it takes to reach a safe turbidity threshold of 1 at a decay factor of 0.02 using calc_min_time. It then outputs all of that data at once as so:

    Average turbidity based on most recent five measurements = 1.1497522 NTU
    WARNING:root:Turbidity is above threshold for safe use
    Minimum time required to return below a safe threshold = 6.907313891267473 hours

displaying the average turbidity calculated, the logging message, and time needed to reach the safe threshold.

# test_analyze_water_turb.py

This script contains the unit tests for the previous script and is used to test the functions for the script above. It tests to make sure the calc_turb and calc_min_time functions are arithmetically correct and output the correct values. It tests whether both functions output floats, and tests if they output errors when they are supposed to. When running the unit tests, all of them should pass.
