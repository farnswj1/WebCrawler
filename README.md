# Web Crawler
This is a containerized web crawler.

## Setup
The project uses the following:
- Python 3.9
- Scrapy
- Nginx 1.21
- Docker
- Docker Compose

For additional information on project specifications, see ```web_crawler/Pipfile```.

## Building
The project uses Docker. Ensure Docker and Docker Compose are installed before continuing.

To build, run ```docker-compose build```

## Running
To run the web app, run ```docker-compose up -d```, then 
go to http://localhost using your web browser.

## Deploying A Project To Scrapy
Initially, the server will not have the project in the app registered for use.
To fix this, run ```docker exec -it web_crawler scrapyd-deploy default```.
