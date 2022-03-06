FROM python:3
COPY requirements.txt /requirements.txt
RUN pip install pip -U
RUN pip install -r /requirements.txt
COPY script.py /script.py
CMD ["python", "/script.py"]
