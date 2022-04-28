# Software Diagram for Querying Data on ISS

In this project, we were tasked with creating a software diagram for one of our previous projects: [ISS-Sighting-Location](https://github.com/etchi17/ISS-Sighting-Location). Our goal is to show off an interesting aspect of this project and explain it through simple text and an easily understandable visual. With the evergrowing complexity of certain processes, products, and applications used in our modern world, having a visual to aid in our understanding of it helps immensely. It can help clear potential misunderstandings and help guide newcomers through the basics of it in an organized fashion. As such, this project aims to do just that, albeit in a much simpler scale.

## Software Diagram Description

Shown below is a software diagram depicting all the routes and returned outputs present in the [ISS-Sighting-Location](https://github.com/etchi17/ISS-Sighting-Location) project. It demonstrates the actions, commands, and path a user would have to take in order to receive a specifc output, detailing everything a user would need to know in order to fully use the Flask API once set up. 

![](https://github.com/etchi17/COE332_homework/blob/e9f1118521f8e774290277ea630fb73499b61b3a/homework07/Software_Diagram.png)

To start, the software diagram shows two routes that a user can take. NOTE: All routes shown are donw following `curl localhost:5007`, ex: `curl localhost:5007/` for the first route.

1. The first route is the help route, which can be executed using: `/`. This returns a string containing all routes in the Flask application, how to use them, and their expected outputs:
	```
	### ISS Sighting Location ###

	Informational and Management Routes:

	/                                                      (GET) print this information
	/read_data                                             (POST) resets data, reads and loads all data from files

	Routes for Querying Positional and Velocity Data:

	/epochs                                                (GET) lists all epochs in positional and velocity data
	/epochs/<epoch>                                        (GET) lists all data associated with a specific <epoch> in positional and velocity data

	Routes for Querying Sighting Data

	/countries                                             (GET) lists all countries in sighting data
	/countries/<country>                                   (GET) lists all data associated with a specific <country> in sighting data
	/countries/<country>/regions                           (GET) lists all regions in a specific <country> in sighting data
	/countries/<country>/regions/<region>                  (GET) lists all data associated with a specific <region> in a specific <country> in sighting data
	/countries/<country>/regions/<region>/cities           (GET) lists all cities in a specific <region> in a specific <country> in sighting data
	/countries/<country>/regions/<region>/cities/<city>    (GET) lists all data associated with a specific <city> in a specific <region> in a specific <country> in sighting data
	```

2. The second route is the data reading and storing route, which can be done with: `/read_data -X POST`. Taking this route allows the user to successfully use the other data querying routes in the application as it reads and stores all of the positional, velocity, and sighting data that the data querying routes use. Following this route are the two data sets that get read and stored:
    1. The `ISS Positional and Velocity Data` set
        1. The first data querying route that uses this data set is: `/epochs`. This route returns a large string listing all epochs in the positional and velocity data. The outputted data should look look like this:

            ```
            ...
            2022-057T11:12:56.869Z
            2022-057T11:16:56.869Z
            2022-057T11:20:56.869Z
            2022-057T11:24:56.869Z
            2022-057T11:28:56.869Z
            2022-057T11:32:56.869Z
            2022-057T11:36:56.869Z
            2022-057T11:40:56.869Z
            2022-057T11:44:56.869Z
            2022-057T11:48:56.869Z
            2022-057T11:52:56.869Z
            2022-057T11:56:56.869Z
            2022-057T12:00:00.000Z
            ```
        2. The second route in this data set is: `/epochs/<epoch>`. This returns a dictionary listing all positional (X, Y, Z) and velocity (X_DOT, Y_DOT, Z_DOT) data for a specific epoch. For example, the output for `/epochs/2022-057T12:00:00.000Z` is: 
            ```
            {
              "X": {
                "#text": "6626.5027288478996",
                "@units": "km"
              },
              "X_DOT": {
                "#text": "-0.48760287876274999",
                "@units": "km/s"
              },
              "Y": {
                "#text": "-824.23928357807699",
                "@units": "km"
              },
              "Y_DOT": {
                "#text": "4.9312583060242199",
                "@units": "km/s"
              },
              "Z": {
                "#text": "-1255.3633426653601",
                "@units": "km"
              },
              "Z_DOT": {
                "#text": "-5.8454326130222896",
                "@units": "km/s"
              }
            }
            ```
    2. The `ISS Sighting Data` set
        1. The first data querying route for this set is: `/countries`. This returns a dictionary listing all countries in the sighting data as the key with the number of sightings in that country as the value. The output for this route should look like: 
            ```
            {
              "United_States": 5476
            }
            ```
         2. The second route that uses this data set is: `/countries/<country>`. This returns a large string listing all the data associated with a specific country in the sighting data. The output for `/countries/United_States` is:
            ```
            ...
            New_Port_Richey, Florida: ISS was spotted on Sat Feb 19/05:39 AM for 3 minutes at a max elevation of 67, entering 67 above N, exiting 10 above NE, with utc offset: -5.0, utc time: 10:39, and utc date: Feb 19, 2022
            New_Port_Richey, Florida: ISS was spotted on Sun Feb 20/04:54 AM for < 1 minutes at a max elevation of 12, entering 12 above NE, exiting 10 above NE, with utc offset: -5.0, utc time: 09:54, and utc date: Feb 20, 2022
            New_Port_Richey, Florida: ISS was spotted on Sun Feb 20/06:27 AM for 2 minutes at a max elevation of 12, entering 11 above WNW, exiting 10 above NNW, with utc offset: -5.0, utc time: 11:27, and utc date: Feb 20, 2022
            New_Port_Richey, Florida: ISS was spotted on Mon Feb 21/05:41 AM for 1 minutes at a max elevation of 15, entering 15 above N, exiting 10 above N, with utc offset: -5.0, utc time: 10:41, and utc date: Feb 21, 2022
            New_Smyrna_Beach, Florida: ISS was spotted on Mon Feb 14/06:25 AM for 4 minutes at a max elevation of 16, entering 10 above SSE, exiting 10 above E, with utc offset: -5.0, utc time: 11:25, and utc date: Feb 14, 2022
            New_Smyrna_Beach, Florida: ISS was spotted on Wed Feb 16/06:24 AM for 7 minutes at a max elevation of 64, entering 10 above SSW, exiting 10 above NE, with utc offset: -5.0, utc time: 11:24, and utc date: Feb 16, 2022
            New_Smyrna_Beach, Florida: ISS was spotted on Thu Feb 17/05:37 AM for 6 minutes at a max elevation of 29, entering 11 above S, exiting 10 above ENE, with utc offset: -5.0, utc time: 10:37, and utc date: Feb 17, 2022
            New_Smyrna_Beach, Florida: ISS was spotted on Fri Feb 18/04:52 AM for 2 minutes at a max elevation of 15, entering 15 above ESE, exiting 10 above E, with utc offset: -5.0, utc time: 09:52, and utc date: Feb 18, 2022
            New_Smyrna_Beach, Florida: ISS was spotted on Fri Feb 18/06:25 AM for 6 minutes at a max elevation of 31, entering 10 above WSW, exiting 10 above NNE, with utc offset: -5.0, utc time: 11:25, and utc date: Feb 18, 2022
            New_Smyrna_Beach, Florida: ISS was spotted on Sat Feb 19/05:40 AM for 3 minutes at a max elevation of 63, entering 63 above NW, exiting 10 above NE, with utc offset: -5.0, utc time: 10:40, and utc date: Feb 19, 2022
            New_Smyrna_Beach, Florida: ISS was spotted on Sun Feb 20/04:54 AM for 1 minutes at a max elevation of 16, entering 16 above NE, exiting 10 above NE, with utc offset: -5.0, utc time: 09:54, and utc date: Feb 20, 2022
            New_Smyrna_Beach, Florida: ISS was spotted on Sun Feb 20/06:27 AM for 2 minutes at a max elevation of 11, entering 10 above NW, exiting 10 above NNW, with utc offset: -5.0, utc time: 11:27, and utc date: Feb 20, 2022
            New_Smyrna_Beach, Florida: ISS was spotted on Mon Feb 21/05:41 AM for 1 minutes at a max elevation of 17, entering 17 above NNW, exiting 10 above N, with utc offset: -5.0, utc time: 10:41, and utc date: Feb 21, 2022
            ```
        3. The third route following this is: `/countries/<country>/regions`. This returns a dictionary listing all regions in the sighting data for a specified country as the key with the number of sightings in that region as the value. The output for `/countries/United_States/regions` is:
            ```
            {
              "California": 1702,
              "Colorado": 1173,
              "Connecticut": 657,
              "DC": 1060,
              "Delaware": 100,
              "Florida": 784
            }
            ```
        4. The fourth route after that is: `/countries/<country>/regions/<region>`. This returns a large string listing all the data associated with a specific region in a specific country in the sighting data. The output for `/countries/United_States/regions/California` is:
            ```
            ...
            Yuba_City: ISS was spotted on Wed Feb 23/05:48 AM for 4 minutes at a max elevation of 21, entering 18 above NW, exiting 10 above NNE, with utc offset: -8.0, utc time: 13:48, and utc date: Feb 23, 2022
            Yuba_City: ISS was spotted on Thu Feb 24/05:01 AM for 2 minutes at a max elevation of 25, entering 25 above N, exiting 10 above NE, with utc offset: -8.0, utc time: 13:01, and utc date: Feb 24, 2022
            Yuba_City: ISS was spotted on Fri Feb 25/04:15 AM for < 1 minutes at a max elevation of 10, entering 10 above NE, exiting 10 above NE, with utc offset: -8.0, utc time: 12:15, and utc date: Feb 25, 2022
            Yuba_City: ISS was spotted on Fri Feb 25/05:48 AM for 3 minutes at a max elevation of 13, entering 11 above NW, exiting 10 above NNE, with utc offset: -8.0, utc time: 13:48, and utc date: Feb 25, 2022
            Yucca_Valley: ISS was spotted on Tue Feb 15/05:45 AM for 5 minutes at a max elevation of 18, entering 10 above S, exiting 10 above E, with utc offset: -8.0, utc time: 13:45, and utc date: Feb 15, 2022
            Yucca_Valley: ISS was spotted on Thu Feb 17/05:45 AM for 7 minutes at a max elevation of 64, entering 10 above SW, exiting 10 above NE, with utc offset: -8.0, utc time: 13:45, and utc date: Feb 17, 2022
            Yucca_Valley: ISS was spotted on Fri Feb 18/04:58 AM for 5 minutes at a max elevation of 31, entering 17 above S, exiting 10 above ENE, with utc offset: -8.0, utc time: 12:58, and utc date: Feb 18, 2022
            Yucca_Valley: ISS was spotted on Sat Feb 19/04:12 AM for 1 minutes at a max elevation of 16, entering 16 above ESE, exiting 10 above E, with utc offset: -8.0, utc time: 12:12, and utc date: Feb 19, 2022
            Yucca_Valley: ISS was spotted on Sat Feb 19/05:45 AM for 6 minutes at a max elevation of 36, entering 12 above WSW, exiting 10 above NNE, with utc offset: -8.0, utc time: 13:45, and utc date: Feb 19, 2022
            Yucca_Valley: ISS was spotted on Sun Feb 20/05:00 AM for 3 minutes at a max elevation of 69, entering 68 above NW, exiting 10 above NE, with utc offset: -8.0, utc time: 13:00, and utc date: Feb 20, 2022
            Yucca_Valley: ISS was spotted on Mon Feb 21/04:14 AM for 1 minutes at a max elevation of 19, entering 19 above ENE, exiting 10 above NE, with utc offset: -8.0, utc time: 12:14, and utc date: Feb 21, 2022
            Yucca_Valley: ISS was spotted on Mon Feb 21/05:47 AM for 4 minutes at a max elevation of 15, entering 11 above WNW, exiting 10 above N, with utc offset: -8.0, utc time: 13:47, and utc date: Feb 21, 2022
            Yucca_Valley: ISS was spotted on Tue Feb 22/05:01 AM for 2 minutes at a max elevation of 21, entering 21 above NNW, exiting 10 above NNE, with utc offset: -8.0, utc time: 13:01, and utc date: Feb 22, 2022
            Yucca_Valley: ISS was spotted on Wed Feb 23/04:15 AM for < 1 minutes at a max elevation of 11, entering 11 above NNE, exiting 10 above NNE, with utc offset: -8.0, utc time: 12:15, and utc date: Feb 23, 2022
            Yucca_Valley: ISS was spotted on Thu Feb 24/05:01 AM for < 1 minutes at a max elevation of 10, entering 10 above NNW, exiting 10 above N, with utc offset: -8.0, utc time: 13:01, and utc date: Feb 24, 2022
            ```
        5. The fifth route in the data set is: `/countries/<country>/regions/<region>/cities`. This returns a dictionary listing all cities in the sighting data for a specified region in a specified country as the key with the number of sightings in that city as the value. The output for `/countries/United_States/regions/California/cities` is:
            ```
            {
              "Lemoore": 11,
              "Livermore": 11,
              "Lompoc": 10,
              "Long_Beach": 11,
              "Los_Altos": 11,
              "Los_Angeles": 11,
              "Los_Gatos": 10,
              "Madera": 10,
              "Magalia": 12,
              "Manteca": 12,
              "Manzanar_National_Historic_Site": 13,
              "Marina": 10,
              ...
            }
	          ```
        6. Finally, the last route in the data set following these routes is: `/countries/<country>/regions/<region>/cities/<city>`. This returns a large string listing all the data associated with a specific city in a specific region of a specific country in the sighting data. The output for `/countries/United_States/regions/California/cities/Los_Angeles` is:
            ```
            Los_Angeles, California, United_States
            ISS was spotted on Tue Feb 15/05:45 AM for 4 minutes at a max elevation of 15, entering 10 above SSE, exiting 10 above E, with utc offset: -8.0, utc time: 13:45, and utc date: Feb 15, 2022
            ISS was spotted on Thu Feb 17/05:44 AM for 7 minutes at a max elevation of 52, entering 10 above SSW, exiting 10 above ENE, with utc offset: -8.0, utc time: 13:44, and utc date: Feb 17, 2022
            ISS was spotted on Fri Feb 18/04:58 AM for 5 minutes at a max elevation of 26, entering 16 above S, exiting 10 above ENE, with utc offset: -8.0, utc time: 12:58, and utc date: Feb 18, 2022
            ISS was spotted on Sat Feb 19/04:12 AM for 1 minutes at a max elevation of 13, entering 13 above ESE, exiting 10 above E, with utc offset: -8.0, utc time: 12:12, and utc date: Feb 19, 2022
            ISS was spotted on Sat Feb 19/05:45 AM for 6 minutes at a max elevation of 42, entering 15 above WSW, exiting 10 above NNE, with utc offset: -8.0, utc time: 13:45, and utc date: Feb 19, 2022
            ISS was spotted on Sun Feb 20/05:00 AM for 3 minutes at a max elevation of 74, entering 74 above NNE, exiting 10 above NE, with utc offset: -8.0, utc time: 13:00, and utc date: Feb 20, 2022
            ISS was spotted on Mon Feb 21/04:14 AM for 1 minutes at a max elevation of 15, entering 15 above ENE, exiting 10 above ENE, with utc offset: -8.0, utc time: 12:14, and utc date: Feb 21, 2022
            ISS was spotted on Mon Feb 21/05:47 AM for 4 minutes at a max elevation of 17, entering 13 above WNW, exiting 10 above NNE, with utc offset: -8.0, utc time: 13:47, and utc date: Feb 21, 2022
            ISS was spotted on Tue Feb 22/05:01 AM for 2 minutes at a max elevation of 22, entering 22 above N, exiting 10 above NNE, with utc offset: -8.0, utc time: 13:01, and utc date: Feb 22, 2022
            ISS was spotted on Wed Feb 23/04:15 AM for < 1 minutes at a max elevation of 10, entering 10 above NE, exiting 10 above NE, with utc offset: -8.0, utc time: 12:15, and utc date: Feb 23, 2022
            ISS was spotted on Thu Feb 24/05:01 AM for < 1 minutes at a max elevation of 11, entering 11 above N, exiting 10 above N, with utc offset: -8.0, utc time: 13:01, and utc date: Feb 24, 2022
            ```
            
All of these routes ultimately come together at a connection point towards the end, where the user has already gotten their desired output and would have to go back to the start if they desire a different one.
