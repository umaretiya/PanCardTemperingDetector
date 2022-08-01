#Create a ubuntu base image with python 3 installed.
FROM python:3.10

#Set the working directory
WORKDIR /

#copy all the files
COPY . .

#Install the dependencies
RUN apt-get -y update
RUN apt-get update && apt-get install -y python3 python3-pip
# installing a cv2 module
RUN pip install opencv-python
RUN apt-get install ffmpeg libsm6 libxext6  -y 
RUN apt-get update && apt-get install libgl1
RUN apt-get update && apt-get install -y python3-opencv

RUN pip3 install -r requirements.txt

#Expose the required port
EXPOSE 5000

#Run the command
CMD gunicorn app:app