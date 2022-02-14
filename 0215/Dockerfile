FROM python:3.10.2

RUN python3 -m pip install --upgrade pip

RUN pip install Django==4.0.2 && \
    pip install Djongo==1.3.6 && \
    pip install pymongo==3.12.1 && \
    pip install djangorestframework==3.13.1  && \
    pip install pymongo==3.12.1 && \
    pip install pytz==2021.3 && \
    pip install dnspython==2.2.0

WORKDIR ./django

EXPOSE 8000

COPY ./Ghibli ./