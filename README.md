# Inalab Simple Flask App Project

Application is containerized using docker compose with nginx reverse proxy listening on port 80 and flask app listening on port 5000. 
Cloudformation template in folder cloudformation. Need to replace ami to be used.

## Docker Compose

Run Application with docker-compose up
This will start the 2 containers 1 for nginx 1 for flask app
To Change Hello, World! edit the .env file and change the variable CONTENT

## Scripting

To run data verifcation script use command python3 ./test-data.py
This script parses json data and creates files in files directory under name [id].txt and sum's the files contents using SHA256 and compares to file names

## Reverse proxy using Cloudformation

This creates the following resources in 2 Availabiltiy Zones for redundancy

*VPC using subnet 192.168.0.0/22 
*Public Subnet1: 192.1658.0.0/24
*Public Subnet2: 192.1658.1.0/24
*Private Subnet1: 192.1658.2.0/24
*Private Subnet2: 192.1658.3.0/24
*2 NAT Gateways
*1 Internet Gateway
*2 EC2 Intances Running NGINX
*2 Load Balancers

And corresponding security groups, route tables, Elastic IPS, and Network ACL's

EC2 Instances are in the private subnets only being accessible from the private subnet
Load Balancers are on the public subnet to route traffic to the EC2 Instances

Need to setup route 53 to point to 2 load balancrs

EC2 Instances install docker & docker compose, will clone this repository and run docker-compose up at startup

