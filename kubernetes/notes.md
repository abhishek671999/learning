# Kubernetes
- Smallest unit of K8
- Pod is abstraction of container
- Usually 1 container is run in 1 pod but helper containers can also be clubbed
- Each pod gets it's own IP address

## Service
- Permanent IP address
- Could be internal service and external service
- Lifecycle is independent of PODs
- Service is common across Nodes
- Also acts as load balancer to redirect requests to free nodes

## Ingres
- Sort of external services which takes in the request from external applications
- Ingress servie would also be running on their own POD in each node

## ConfigMap (helps to avoid rebuiding when something like db service has changed)
- External configuration of application like DB_URL=mongo-db-service

## Secret
- Just like configMap for username and password

## Volues
- For data persistant
- External storage outside container/POD
- It could be storage of local or remote storage

## Deployments
- Blueprint for PODs

## statefulset
- Database can't be replicated because DBs have state to maintain  
which should be resolved using another service called statefulset
- Sync is bit tricky

## PS
- Usually stateless applications are hosted in K8 cluster and other stateful applications are hosted outside K8 cluster

