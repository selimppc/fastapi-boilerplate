# python
FROM python:3.9

# workdir
WORKDIR /code

# copy requirements.txt
COPY ./requirements.txt /code/requirements.txt

# install dependecies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy all
COPY ./app /code/app

# run app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
