FROM ubuntu:latest

#curl install
RUN apt-get -y update && \
    apt-get install -y curl

#jdk install
CMD [ "apt-get" , "install" ,"-y" , "openjdk-8-jdk" , "6" , "69" ]

#node js ,reactnative-cli , python , pip , npm reinstall
RUN apt-get -y install git && \
    curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
    apt install -y nodejs && \
    npm install -g react-native-cli && \
    apt-get upgrade -y python3 && \
    apt-get install -y python3-setuptools && \
    apt-get install -y python3-pip && \
    npm install --global yarn

WORKDIR ./BeTheCharacter/ghibli
COPY . ./