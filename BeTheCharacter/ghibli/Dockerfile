FROM ubuntu:latest

RUN apt-get -y update && \
    apt-get install -y curl

CMD [ "apt-get" , "install" ,"-y" , "openjdk-8-jdk" , "6" , "69" ]

RUN apt-get -y install git && \
    curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
    apt install -y nodejs && \
    npm install -y -g expo-cli