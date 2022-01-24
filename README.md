# MongoDB with FastAPI

```bash

# Install the requirements:
pip install -r requirements.txt

# Configure the location of your MongoDB database:
MONGODB_URL="mongodb+srv://reza:reza123@127.0.0.1/fastapi?retryWrites=true&w=majority"

# Start the service:
uvicorn main:app --reload --port=8080


```