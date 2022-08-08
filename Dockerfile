FROM python:3.7.13-slim

LABEL version="v0.1-dev1"
LABEL maintainer="Simeon Thomas"
LABEL maintaineremail="thomasolaoluwa@gmail.com"
LABEL org.opencontainers.image.source https://github.com/olaoluthomas/prop_predictor

# to show print statements and logs to display in Knative logs
ENV PYTHONUNBUFFERED True

# for test in local environment declare port #
ENV PORT 8080
EXPOSE $PORT

# copy installer and bash script
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY ./src/dist/prop_predict-0.1.dev1-py3-none-any.whl ./
COPY ./main.py ./__init__.py ./

# make RUN commands use `bash --login`
SHELL ["/bin/bash", "--login", "-c"]

# install prop-trainer
# RUN pip install --upgrade pip
RUN pip install ./prop_predict-0.1.dev1-py3-none-any.whl

# Run the web service on container startup. 
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow service
# to handle instance scaling.
# CMD exec gunicorn --bind :$PORT --workers 1 --threads 4 --timeout 0 main:app
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]