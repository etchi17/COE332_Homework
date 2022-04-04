# Accessing Meteorite Landing Data with Redis and Flask

In this project, we are given one data set containing a multitude of meteorite landing site data to work with. Our goal is to containerize and launch a Redis database server that we can both load data to and retrieve data from using a Flask application that we will containerize using a Dockerfile. With the prevalence of large sets of data in our modern age, having a reliable method to store all of that data is important. Equivallently, having a method that updates, loads, and retrieves that data when necessary is just as important. As such, this project aims to solve these core issues using a Redis database and Flask application to facilitate the storage and retrieval of data from large data sets like these.

## Downloading Data Set

Before we can start utilizing these methods, we need to first download the meteorite landing site data that we're going to be working with. In order to do that, simply run the following command in your command line terminal:
```
wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
```
