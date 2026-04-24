## Create mongo network
docker network create mongo-network

## Create mongo container
docker run -d --network mongo-network \                                     
-p 27017:27017 \
-e MONGO_INITDB_ROOT_USERNAME=admin \
-e MONGO_INITDB_ROOT_PASSWORD=password \
--name mongodb \
mongo

## Create mongo-express container
docker run -d \                                                             
-p 8081:8081 \
-e ME_CONFIG_MONGODB_SERVER=mongodb \
-e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
-e ME_CONFIG_MONGODB_ADMINPASSWORD=password \
--name mongodb-express \
--network mongo-network \
mongo-express

Docker commonds needs to be run in command line which can be pita if to be run multiple times. Hence docker-compse. 
Docker compose file can be found in here

Docker file is blueprint to create docker image


docker rm <docker-container-id> -> To delete container 
docker rmi <docker-image-id> -> To delete docker image
