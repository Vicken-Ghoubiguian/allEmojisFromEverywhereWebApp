#Put the python image as image's base
FROM python:latest

#
LABEL maintainer="ericghoubiguian@live.fr"

#Copy all the files and directories in the newly created directory allEmojisFromEverywhereWebApp
COPY . /allEmojisFromEverywhereWebApp

#Change work directory for the allEmojisFromEverywhereWebApp project one
WORKDIR /allEmojisFromEverywhereWebApp

#Install all of the pypi requirements to run the allEmojisFromEverywhereWebApp web app
RUN pip install -r requirements.txt

#Expose the docker container listening port
EXPOSE 80

#Container instruction as entrypoint: 'python allEmojisFromEverywhereWebApp.py'
ENTRYPOINT ["python", "allEmojisFromEverywhereWebApp.py"]