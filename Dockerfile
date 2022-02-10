FROM python:3.7-slim
COPY api_yamdb/requirements.txt ./
RUN pip3 install -r requirements.txt --no-cache-dir
COPY ./ ./
CMD python api_yamdb/manage.py runserver 0:8000
