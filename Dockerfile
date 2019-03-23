FROM ubuntu:18.04

#set the working directory
WORKDIR /usr/src/app

#install python and pip
RUN apt-get update && apt-get install -y python python-pip

#pre-requests for textract which is used to read pdf 
RUN apt-get install -y python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr \
flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig zlib1g-dev libpulse-dev

#install ganga and other dependancies which are needed for pdf splitting and reading
RUN pip install ganga PyPDF2 textract

#copy the current directory in the local system to WORKDIR of docker image
COPY . .

#run ganga job
CMD sh ./start.sh
