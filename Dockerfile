FROM python:3.7-alpine
WORKDIR /usr/src/backend
RUN pip install pipenv
COPY Pipfile* ./
RUN pipenv install
COPY . .
EXPOSE 5000
CMD pipenv run flask run