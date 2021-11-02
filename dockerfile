FROM python 
COPY . /app
WORKDIR /app 
RUN pip install -r req.txt 
CMD ["python","app.py"]