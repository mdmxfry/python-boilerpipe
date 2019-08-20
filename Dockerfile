# Set the base image to Ubuntu
FROM ubuntu

# Update the sources list
RUN apt-get update
RUN apt-get install -y python3 python3-dev python-distribute python3-pip
RUN apt-get install -y git-core

RUN apt-get install -y default-jre
RUN apt-get install -y default-jdk

# Python 2.7 will retire officially soon. That is why decision to use sorpaas fork for Python 3 was made
# https://www.python.org/dev/peps/pep-0373/
RUN git clone https://github.com/sorpaas/python-boilerpipe.git
RUN cd python-boilerpipe && python3 setup.py install

# Copy the application folder inside the container
ADD ./boilerpipe-api.py /boilerpipe-api.py
ADD ./requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt
EXPOSE 8080

CMD ["python3", "boilerpipe-api.py"]
