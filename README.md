# MKAD-distance-flask

Flask app in Docker that calculates distance between Moscow Ring Road(MKAD) and input address.

## Build APP
Build the Docker image by cloning repo.

`$ git clone https://github.com/remzizorpuzan/MKAD-distance-flask.git`

`$ docker build -t ring-road-distance .`

## Run container

` docker run -p 5000:5000 ring-road-distance `

### Go to http://localhost:5000   (set port is 5000 from docker)

## Without container usage

After include necessary packages (geopy,flask,requests..)

### Open a terminal and from project directory `[your path]\Scripts\activate.bat`

after inside virtual environment run the app.
