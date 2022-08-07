# How to run the streamlit app


1. Update the procfile (this is starting point of the program)
2. update the setup.sh file
3. Make suere you create a file called .env in 
the root folder of this project and add your Twitter keys in it
4. Dump all this files directly in Github Repository.(Not inside folder)

## Docker Instructions:
====================

docker ps -a
docker rm <ID>
docker rmi <image ID>

docker build -t rbyakod/twitter-sentiment .
docker run -p 9000:9000 -d rbyakod/twitter-sentiment

docker login -u  rbyakod
docker push rbyakod/twitter-sentiment:latest


## AWS commands:
=============
LOGIN to your AWC instance:
ssh -i "twitter-sentiment.pem" ec2-user@ec2-18-237-125-37.us-west-2.compute.amazonaws.com

port forwarding on your localhost:
ssh -i "./twitter-sentiment.pem" ec2-user@ec2-18-237-125-37.us-west-2.compute.amazonaws.com -L 2081:localhost:2041 -L 4888:localhost:4888 -L 2080:localhost:2080 -L 27017:localhost:27017 -L 28017:localhost:28017  -L 8050:localhost:8050 -L 4141:localhost:4141 -L 3880:localhost:3880 -L 9001:localhost:9001

copying files to AWS :
scp -r -i "./twitter-sentiment.pem" "Codes/DockerCompose/" ec2-user@ec2-18-237-125-37.us-west-2.compute.amazonaws.com:/home/ec2-user/docker_compose

run docker:

you can pull as well:
docker pull rbyakod/twitter-sentiment:latest

or run directly:
docker run -p 9001:9001 -d rbyakod/twitter-sentiment

LOGs:
docker logs <container ID> -f

access by using last host port combo:
http://18.237.125.37:9001
