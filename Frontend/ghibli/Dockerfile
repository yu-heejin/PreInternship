FROM node:16.13.2

#curl , python , pip install
RUN apt-get -y update && \
    apt-get upgrade -y python3 && \
    apt-get install -y python3-setuptools && \
    apt-get install -y python3-pip

#jdk install
CMD [ "apt-get" , "install" ,"-y" , "openjdk-8-jdk" , "6" , "69" ]

# reactnative-cli , react-native-camera install
RUN npm install -g react-native-cli
RUN yarn add react-native-camera@git+https://git@github.com/react-native-community/react-native-camera.git

# @react-navigation/native , @react-navigation/stack , react-native-gesture-handler , react-native-safe-area-context , react-native-screens , styled-components , install
CMD ["npm" , "install" , "@react-navigation/native" , "npm" , "install" , "@react-navigation/stack" , "npm" , "i" , "react-native-gesture-handler" , "npm" , "i" , "react-native-safe-area-context" , "npm" , "i" , "react-native-screens" , "npm" , "i" , "styled-components" ]

WORKDIR ./BeTheCharacter/ghibli
COPY . ./