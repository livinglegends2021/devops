FROM python 
COPY . /app
WORKDIR /app 
RUN pip install -r requirements.txt 

EXPOSE 5000
CMD ["python","app.py"]

# docker run --rm -p 80:5000 livinglegends/devopswithpython:latest