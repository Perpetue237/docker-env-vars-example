FROM python:3.10-slim

#Get Variables from build context

ARG MY_BUILD_ARG
ARG MY_BUILD_ARG_FROM_DC
ENV MY_VARIABLE=$MY_BUILD_ARG
ENV MY_BUILD_ARG_FROM_DC=$MY_BUILD_ARG_FROM_DC

#Set a variable in this dockerfile

ENV MY_VARIABLE_FROM_DOCKERFILE="Hello from Dockerfile!"

COPY app/ /app
WORKDIR /app

CMD ["python", "app.py"]