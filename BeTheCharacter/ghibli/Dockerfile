FROM ubuntu:latest

RUN apt-get -y update && \
    apt-get install -y curl

CMD [ "apt-get" , "install" ,"-y" , "openjdk-8-jdk" , "6" , "69" ]

RUN apt-get -y install git && \
    curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
    apt install -y nodejs && \
    npx start && \
    npm install -g react-native-cli && \
    apt-get upgrade -y python3 && \
    apt-get install -y python3-setuptools && \
    apt-get install -y python3-pip && \
    npm cache clean --force && \
    rm -rf node_modules package-lock.json && \
    npm install

COPY ./ ./