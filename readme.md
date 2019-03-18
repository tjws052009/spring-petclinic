# Spring PetClinic Application with the Elastic Stack

A docker compose allows the user to run the application, backed with Mysql as the data layer, with Elastic APM and Beat instrumentation enabled. The following services are deployed:

- Pet Clinic via embedded Tomcat with REST API. Instrument with Elastic Java Agent.
- React UI for Pet Clinic using above. Instrument with Elastic RUM Agent.
- Elasticsearch
- Kibana
- MySQL
- Packetbeat - **PENDING**
- Metricbeat - **PENDING**
- Filebeat - **PENDING**
- Nginx - **PENDING**

This allows collection of the following metrics:

- Java APM data as available from the Java Agent i.e. transactions, spans and errors
- MYSQL, HTTP traffic via Packetbeat **PENDING**
- Application Logs + NGINX Logs via Filebeat **PENDING**
- JMX, Docker, Mysql, Nginx metrics via Metricbeat  **PENDING**

## Running Petclinic with the Elastic Stack

`ES_VERSION=6.4.2 docker-compose -f docker-compose.yml up`

Other versions of the Elasticstack may work. Currently, only version 6.4.2 has been tested.

## Running petclinic locally for development

See instructions for each of the components of the application.


## Understanding the Spring Petclinic application with a few diagrams
<a href="https://speakerdeck.com/michaelisvy/spring-petclinic-sample-application">See the presentation here</a>

