FROM ubuntu:18.04

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y python python-pip

#pre-requests for textract which is used to read pdf 
RUN apt-get install -y python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr \
flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig zlib1g-dev libpulse-dev

RUN pip install ganga PyPDF2 textract

COPY . .

CMD sh ./start.sh
