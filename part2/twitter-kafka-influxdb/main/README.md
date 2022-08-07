

![Architecture diagram](docs/twitter-sentiment-analysis-diagram.png)

## Deployment

Local deployment is done through this [docker-compose.yaml](docker-compose.yaml) file.

To handle this, design your application to attempt to re-establish a connection to the database after a failure. If the application retries the connection, it can eventually connect to the database.

### Requirements

- After obtaining your set of Twitter API key and secret, you have to set those in the [secret.ini](./produce-tweets/secret.ini) file.


## CONFIGURATION:

Please remove or comment out the cluster ID row in ./persistance/kafka/meta.properties 
before starting kafka command everytime.

1 - please remove or comment out the cluster ID row in ./persistance/kafka/meta.properties 
before starting next command everytime

2 - add your twitter credentials to the secre.ini file

3 - docker exec -it <influxdb container id> bash
- infkux
- create database sentiments
- create database languages
- quit
- exit

3 - open grafana by going to http://localhost:3000

    1 - sign in and provide/create root user and password 

    2 - choose Datasources menu and create 2 influxdb datasources

    3 - create an influxdb datasource names Influxdb-tweets, databse as languages, 
host as http://<influxDB container NAME>:8086/

    4 - create an influxdb datasource names Influxdb-sentiments, databse as sentiment, host as http://<influxDB container NAME>:8086/

4 - Create a docker network by the name "twittersentimentanalysis_network" using
command docker network create <network name>

**<VERY IMPORTANT to test the datasources -- make sure you provide rhe influxdb CONTANIER NAME>
**

# Building docker files

cd to consume-tweets
make sure all requirements are met
docker build -t rbyakod/tweet-consumer .


cd to produce-tweets
docker build -t rbyakod/tweet-producer .

if you wish to push the images to docker hub then follow these steps below:
docker login -u <your username>
docker push <image id>

go back to main directory


### Starting the Services

Services need to be started in a specific order with the following commands:
```
please remove or comment out the cluster ID row in ./persistance/kafka/meta.properties 
before starting next command everytime

# Start Kafka and InfluxDB
docker-compose up -d kafka influxdb

# Start Grafana
docker-compose up -d grafana

# Start the producer and the consumer
docker-compose up -d producer consumer

you can check that the producer/consumer are working by chekcing their logs
docker logs -f <docker container id>

### Useful Links
- [Twitter Developers portal](https://developer.twitter.com/en/docs)
- [Sentiment Analysis - Great article](https://monkeylearn.com/sentiment-analysis/)
- [Sentiment Analysis](https://medium.com/analytics-vidhya/twitter-sentiment-analysis-b9a12dbb2043)
- [Top 5 sentiment analysis projects](https://medium.com/analytics-vidhya/top-5-unknown-sentiment-analysis-projects-on-github-to-help-you-through-your-nlp-projects-8d8f195e80fc)
- [Sentiment Analysis with Python NLTK](https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk)
- [Kafka Quickstart](https://kafka.apache.org/quickstart)
- [A Practical Introduction to Kafka Storage Internals](https://medium.com/@durgaswaroop/a-practical-introduction-to-kafka-storage-internals-d5b544f6925f)
- [Deploy a Kafka broker in a Docker container](https://www.kaaproject.org/kafka-docker)
