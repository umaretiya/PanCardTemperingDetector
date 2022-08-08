# PanCardTemperingDetector
Pancard image tampering detector project, It can be apply on similar way on Adhaar card, Driving Licence etc.

Run: Just upload image and check its tampered or not ,
if accuracy is higher means image is less tampered and vice versa
### Build docker image 

docker build -t pan_card:latest .
pan_card to pan-card Docker images
docker images 

docker run -p 5000:5000 -e PORT=5000 <image id>

docker ps 
image name = pan_card
docker stop <container_id> 

docker tag flask_docker <your-docker-hub-username>/<flask-docker>
docker tag flask_docker <your-docker-hub-username>/<flask-docker>


docker push <your-docker-hub-username>/<flask-docker>
docker images
heroku login
docker login --username=<your-username> --password=<your-password>
heroku create <app-name>
heroku container:push web --app <app-name>
heroku container:release web --app <app-name>
> Note: imagename fro docker must be lowercase

app name:: pan-card-tempered

heroku container:push web -a <name heroku app>
heroku container:release web -a <name heroku app>
heroku open -a <name heroku app>
heroku logs --tail -a <name heroku app>