### Calculate Time Required to Investigate Five Meteorite Landing Sites On Mars

In this project, we randomly generate five meteorite landing sites on the North Eastern Hemisphere(Syrtis Major) 
of Mars. We then calculate the amount of time it would take a robotic vehicle to visit and sample every single
meteorite. This kind of simulation serves to provide estimations on the total amount of time (in hours) required to 
travel to and analyze such meteorites in this specific section of Mars while considering the speed of the robot as 
well as the spherical shape of the planet. This is important as it gives researchers studying samples on other
planets an idea of how long it should take for their data to be fully accumulated. It also provides a method that can
be used to approximate the time to receive data for other types of samples on other planets as well.

#### Script 1: meteorite_landings.py

This python script should be the first one run and is what generates the five meteorite landing sites on the 
Syrtis Major in Mars. This script creates a dictionary containing a list of five dictionaries, one for each
landing site. Each landing site has a randomly generated latitude(16-18 degrees North), 
longitude(82-84 degrees East), and composition(stony, iron, stony-iron). Running the script should create a 
json file titled "Meteorite_Landings.json," containing the previously described dectionary, in the same directory
that it was run.

#### Script 2: calc_time.py

Once the "Meteorite_Landings.json" json file has been obtained, this script should be run. This script contains
the function calc_gcd which takes the latitude and longitude of 2 points and calculates the distance between the
two on a spherical object. When run, the script calculates the time needed to get from the starting position
(16, 82) to the first landing site by using the calc_gcd function and speed of the robot, adds the sample time 
based on the composition of the meteorite, and prints out that information for each leg of the trip. Once this
has been done for every leg, it prints out a summary containing the total amount of time needed to get through 
the entirety of the trip, from the starting position to analyzing the last landing site sample.
