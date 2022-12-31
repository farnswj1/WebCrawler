FROM python:3.9-slim-bullseye

# set environment variables
ENV PYTHONUNBUFFERED 1

# expose port(s)
EXPOSE 6800

# set directory
WORKDIR /app

# add application and install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile
COPY . ./

# run the program
CMD ["supervisord", "-c", "supervisord.conf"]
