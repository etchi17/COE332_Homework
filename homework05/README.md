# Accessing Meteorite Landing Data with Redis and Flask

In this project, we are given one data set containing a multitude of meteorite landing site data to work with. Our goal is to containerize and launch a Redis database server that we can both load data to and retrieve data from using a Flask application that we will containerize using a Dockerfile. With the prevalence of large sets of data in our modern age, having a reliable method to store all of that data is important. Equivallently, having a method that updates, loads, and retrieves that data when necessary is just as important. As such, this project aims to solve these core issues using a Redis database and Flask application to facilitate the storage and retrieval of data from large data sets like these.

## Downloading Data Set

Before we can start utilizing these methods, we need to first download the meteorite landing site data that we're going to be working with in a desired directory. In order to do that, simply run the following command in your command line terminal within your desired directory:
```
wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
```

## Launch Redis Database

In order to containerize and launch your Redis database, we need to first make sure we have redis installed. To do so, execute the command shown below:
```
pip3 install --user redis
```
As we seek to launch our containerized instance using the stock redis:6 image, we also need to make sure we execute the following command to pull that image:
```
docker pull redis:6
```
Once that is done, we can finally launch our containerized Redis database server. We want to connect our assigned Redis port to the default Redis port and have it save 1 backup file every second to a /data folder. We can do all of that by executing this command:
```
docker run -d -p <redis-port#>:6379 -v $(pwd)/data:/data:rw --name=<your-name>-redis redis:6 --save 1 1
```
NOTE: Be sure to replace `<redis-port#>` with your own/assigned redis port and `<your-name>` with your name.

You can check if it is up and running with `docker ps -a`, which should output a table of the format displayed below.
```
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS             PORTS                                                         NAMES
(Container ID) redis:6    "docker-entrypoint.s…"   (time created)  Up (time created)  0.0.0.0:<redis-port#>->6379/tcp, :::<redis-port#>->6379/tcp   "container-name"
```
You should see your container with the name you gave it on the table generated with the STATUS as Up and the port you assigned it.

If any of the above is not found, you can try to debug it using: 
```
docker logs "container-name"
```

If you decide to use your own redis-port, be sure to follow the following instructions to connect your Redis database server to your Flask application:
- Run `docker inspect <container ID> | grep IPAddress` to find the IP (e.g. 172.xx.x.x)
- Replace the redis client in the Flask app as: `redis.Redis(host='172.xx.x.x', port=6379)`
- Replace `172.xx.x.x` with the actual IP you find in the first part

## Pull/Build/Launch Flask Application

1. In order to use the Flask application, we first start off by pulling it from Dockerhub using the following command:
  ```
  docker pull <username>/<code>:<version>
  ```
  - To specifically pull mine, replace `<username>/<code>:<version>` with `etchi17/flask-ml-data-sample:hw5`

2. Before we can build or launch the Flask application, we're going to need to add 2 new files to our directory:

	### Dockerfile:
	- This file is already included in the repository, but if you would like to create your own...
	- Touch a file named "Dockerfile" into your directory by executing `touch Dockerfile`
	- Go in and edit the newly created file with a text editor of your choice (vim was used as the text editor of choice) by executing `vim Dockerfile`
	- Once inside enter the following lines of code to complete building the Dockerfile:
	```
	FROM python:3.9

	RUN mkdir /app
	WORKDIR /app
	COPY requirements.txt /app/requirements.txt
	RUN pip install -r /app/requirements.txt
	COPY . /app

	ENTRYPOINT ["python"]
	CMD ["app.py"]
	```

	### requirements.txt:
	- Touch a file named "requirements.txt" into your directory by inputting `touch requirements.txt`
	- Open the newly created file with a text editor with `vim requirements.txt`
	- Add the following lines of code and exit out of the file:
    ```
    Flask==2.0.3
    redis==4.2.1
    ```
  
3. Once those files have been added to your directory, you can build the container by running the following command:
	```
	docker build -t <username>/<code>:<version> .
	```
	NOTE: Be sure to replace `<username>` with your Docker Hub username, `<code>` with the name of your code, and `<version>` with the name of your version of choice.

4. Once built, you can then run and launch the docker container by executing the command:
	```
	docker run --name "container-name" -d -p <port#>:5000 <username>/<code>:<version>
	```
	NOTE: Be sure to replace `<port#>` with your own Flask port number and `"container-name"` with a name of your choice
  
You can check if it is up and running with `docker ps -a`, which should output a table of the format displayed below.
```
CONTAINER ID   IMAGE                         COMMAND           CREATED         STATUS             PORTS                                             NAMES
(Container ID) <username>/<code>:<version>   "python app.py"   (time created)  Up (time created)  0.0.0.0:<port#>->5000/tcp, :::<port#>->5000/tcp   "container-name"
```
You should see your container with the name you gave it on the table generated with the STATUS as Up and the port you assigned it.

If any of the above is not found, you can try to debug it using: 
```
docker logs "container-name"
```

## Using POST and GET methods in the Flask Application

This Flask application only contains one route, `/data`, with two methods, `POST` and `GET`.

### POST
The `POST` method of this route serves to load and store the data into the Redis database server. As such, it should be the first request made, which we can do by executing the command:
```
curl localhost:<port#>/data -X POST
```
Once requested, the data from ML_Data_Sample.json should be stored in the Redis database and the following string should output, confirming the successful completion of the process:
```
Data has been loaded to Redis database instance
```

### GET
The `GET` method of this route serves to retrieve the data from the Redis database and output it. The command to execute this is shown below:
```
curl localhost:<post#>/data
```
Simply executing this command retrieves and outputs all of the data stored in the Redis database. For this particular set of data, it will output 300 meteor landing sight data sets in the form of a list of 300 dictionaries. If the user wants to set a start query parameter for the data that outputs all the data starting at the parameter until the end, the following command should be run instead:
```
curl localhost:<post#>/data?start=<start-parameter>
```
NOTE: Be sure to replace `<start-parameter>` with the value of your choice

Keep in mind that for this specific set of data, only numeric start parameters between 10001 and 10300 are accepted. Any other input will cause the route to return a string detailing the acceptable start parameters as shown below:
```
Invalid start value; start must be numeric (between 10001 and 10300, inclusive).
```

## Description of Data

The data that we have been working with all this time is meteorite landing site data. The following is an entry contained within the sample data:
  ```
  ...
    {
    "name": "Jennifer",
    "id": "10299",
    "recclass": "L5",
    "mass (g)": "539",
    "reclat": "-84.0579",
    "reclong": "69.9994",
    "GeoLocation": "(-84.0579, 69.9994)"
  },
  {
    "name": "Christina",
    "id": "10300",
    "recclass": "H5",
    "mass (g)": "4291",
    "reclat": "-38.1533",
    "reclong": "-46.7127",
    "GeoLocation": "(-38.1533, -46.7127)"
  }
  ```
  
As shown here, each entry (one for each id and meteorite) in the dataset contains the name of the person that discovered and analyzed the meteorite, the id number of the meteorite site, the classification of the meteorite, the mass of the meteorite, the latitudinal and longitudinal location of the meteorite, and the geolocation of the meteorite. All of this data is contained in one dictionary. The dataset we're working with includes 300 of these entries all within a list. That list is a value in the singular key:value pair in the dictionary that is this data set.
