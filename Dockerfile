FROM  jjanzic/docker-python3-opencv
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip uninstall opencv-contrib-python
RUN pip uninstall opencv-python
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install --upgrade opencv-contrib-python
COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
