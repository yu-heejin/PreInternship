FROM python:3.10.2

RUN pip install Django==4.0.2

WORKDIR ./django

EXPOSE 8000

COPY ./ ./

CMD ["python" ,"manage.py" , "migrate"]