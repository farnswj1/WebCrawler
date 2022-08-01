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
go to http://localhost using your web browser. To schedule a task,
run ```curl http://localhost/schedule.json -d project=tutorial -d spider=quotes```
in the terminal.
