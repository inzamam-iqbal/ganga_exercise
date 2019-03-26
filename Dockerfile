#this image is build based on the oficial ubuntu image
FROM ubuntu:18.04

# set the working directory in docker container
WORKDIR /usr/src/app

#install python, pip and git
RUN apt-get update && apt-get install -y python python-pip git

#pre-requests for textract which is used to read pdf 
RUN apt-get install -y python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr \
flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig zlib1g-dev libpulse-dev

#install PyPDF2 and textract for splitting the pdf and reading pdf
RUN pip install ganga PyPDF2 textract

# copy the current local directory to WORKDIR in docker container
RUN git clone https://github.com/inzamam-iqbal/ganga_exercise.git

#run start.sh file on start of the container
CMD cd ganga_exercise/ && bash ./start.sh
