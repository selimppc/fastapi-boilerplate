# MongoDB with FastAPI

```bash

# Install the requirements:
pip install -r requirements.txt

# Configure the location of your MongoDB database:
MONGODB_URL="mongodb+srv://reza:reza123@127.0.0.1/fastapi?retryWrites=true&w=majority"

# Start the service:
uvicorn main:app --reload --port=8080


```

## API Endpoints

```bash

1. Base API: 

#base URL
http://127.0.0.1:8080

2. Hello World API/V1: 

# hello world
http://127.0.0.1:8080/api/v1/hello

```