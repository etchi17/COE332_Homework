# Introduction to Kubernetes

In this project, we build upon our previous project, which involved loading and retrieving meteorite landing site data from a Redis database server with a Flask application, by deploying the Flask app and Redis server in Kubernetes. For this project, we do so in a test environment within the TACC COE332 Kubernetes system under ISP02.

## Files
- `Dockerfile`: Same as previous project, used for building and pushing flask app.
- `requirements.txt`: Same as previous project, used in Dockerfile to install Flask and Redis.
- `app.py`: Same as previous project, contains all of the data reading and retrieving routes but host IP address was changed to match that of the redis deployment. Further information regarding this will be discussed in a later section.
- `deployment-python-debug.yml`: deployment used to debug and run Flask app in Kubernetes.
- `ehc586-test-flask-deployment.yml`: deployment for Flask app.
- `ehc586-test-flask-service.yml`: service for Flask app, provides IP address used for curling.
- `ehc586-test-redis-deployment.yml`: deployment for Redis server.
- `ehc586-test-redis-pvc.yml`: creates persistent volume used in Redis deployment.
- `ehc586-test-redis-service.yml`: service for Redis server, provides IP address used in the Python redis client object for `app.py`.

## Downloading Data Set

To start, we need to first make sure to download the meteorite landing site data that was provided for the previous project to use and store in our Redis database server deployment. In order to do that, simply run the following command in your command line terminal:
```
wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
```

## Description of Data

The data that we will be working with again is the meteorite landing site data. The following is an entry contained within the sample data:
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

## Deployment in Kubernetes

To start our deployment in Kubernetes, we first need to log in to a Kubernetes cluster running at TACC through ISP02. To do so simply ssh into ISP02 and then ssh into `coe332-k8s.tacc.cloud` as shown:
```
[laptop~] $ ssh <tacc_username>@isp02.tacc.utexas.edu
[isp02~] $ ssh <tacc_username>@coe332-k8s.tacc.cloud
```

Now, clone this repository and `cd` into this folder using the following commands:
```
git clone <the cloning url for this repository>
cd COE332_homework/homework06/
```

With the files now in the Kubernetes cluster, we can start to deploy all of the yaml files. To do so simply run the following command on all 6 yaml files:
```
kubectl apply -f <yaml-file>
```
In our case, we would perform this 6 times, replacing <yaml-file> with `deployment-python-debug.yml`, `ehc586-test-flask-deployment.yml`, `ehc586-test-flask-service.yml`, `ehc586-test-redis-deployment.yml`, `ehc586-test-redis-pvc.yml`, and `ehc586-test-redis-service.yml`.
  
With all of our yaml files deployed, we can check if everything is up and running by using these commands:
```
kubectl get pods
kubectl get deployments
kubectl get services
```
When used, we should get outputs similar to these:
- pods/deployments
  ```
  NAME                                            READY   STATUS    RESTARTS      AGE
  ehc586-test-flask-deployment-648ff46b44-h9nwd   1/1     Running   0             41m
  ehc586-test-redis-deployment-6947dbd669-jkzhf   1/1     Running   0             72m
  py-debug-deployment-5dfcf7bdd9-kxccr            1/1     Running   0             4h52m
  ```
- services
  ```
  NAME                        TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
  ehc586-test-flask-service   ClusterIP   10.97.122.105   <none>        5000/TCP   65m
  ehc586-test-redis-service   ClusterIP   10.97.154.87    <none>        6379/TCP   54m
  ```
  
If the `STATUS` is shown as `Running` and there are IP addresses under `CLUSTER-IP`, we are good to go. 
NOTE: The IP address displayed here after `ehc586-test-redis-service` should be the one used in the Python redis client object for `app.py`, replacing the IP address previously there. The IP address displayed after `ehc586-test-flask-service` will be the one used for curling; we will go over this in a later section.
  
## Using POST and GET methods in Kubernetes

In order to use the routes in our Flask app, we first need to enter the debug deployment using the following command:
```
kubectl exec -it deployment-python-debug.yml -- /bin/bash
```

Once in the debugger, we can now curl and use our Flask app as follows:
  
As the Flask application only contains one route, `/data`, with two methods, `POST` and `GET`.

### POST
The `POST` method of this route serves to load and store the data into the Redis database server. As such, it should be the first request made, which we can do by executing the command:
```
curl <flask-service-IP>:5000/data -X POST
```
Once requested, the data from ML_Data_Sample.json should be stored in the Redis database and the following string should output, confirming the successful completion of the process:
```
Data has been loaded to Redis database instance
```

### GET
The `GET` method of this route serves to retrieve the data from the Redis database and output it. The command to execute this is shown below:
```
curl <flask-service-IP>:5000/data
```
Simply executing this command retrieves and outputs all of the data stored in the Redis database. For this particular set of data, it will output 300 meteor landing sight data sets in the form of a list of 300 dictionaries. If the user wants to set a start query parameter for the data that outputs all the data starting at the parameter until the end, the following command should be run instead:
```
curl <flask-service-IP>:5000/data?start=<start-parameter>
```
NOTE: Be sure to replace `<start-parameter>` with the value of your choice

The expected output format for the GET method for running the command are as follows:
```  
curl <flask-service-IP>:5000/data?start=10300
  
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

Keep in mind that for this specific set of data, only numeric start parameters between 10001 and 10300 are accepted. Any other input will cause the route to return a string detailing the acceptable start parameters as shown below:
```
Invalid start value; start must be numeric (between 10001 and 10300, inclusive).
```

