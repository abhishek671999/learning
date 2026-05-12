FROM ubuntu:latest

RUN apt-get update && apt-get install -y curl
RUN apt-get install zstd
RUN apt-get update && apt-get install -y pciutils lshw && rm -rf /var/lib/apt/lists/*
