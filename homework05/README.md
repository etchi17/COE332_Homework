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
