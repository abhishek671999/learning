# Start by basing on another image
FROM node:18-alpine3.18

# set environment variables
ENV abhishek=1

# Run any linux command
 # inside the container
RUN mkdir -p /home/app

# COPY is run between host and contianer
COPY . /home/app 

# Entry point command to the container (just one)
CMD ["node", "server.js"]