"""
Project Settings file
"""
import os
from starlette.datastructures import CommaSeparatedStrings, Secret

default_route_str = "/api"

ALLOWED_HOSTS = CommaSeparatedStrings(os.getenv("ALLOWED_HOSTS", "*"))

SECRET_KEY = Secret(os.getenv(
    "SECRET_KEY",
    "4bf4f696a653b292bc674daacd25195b93fce08a8dac7373b36c38f63cd442938b12ef911bd5d7d0")
)
ALGORITHM = str(os.getenv("ALGORITHM", "HS256"))

# Mongo configuration
MONGO_MAX_CONNECTIONS = int(os.getenv("MAX_CONNECTIONS_COUNT", 10))
MONGO_MIN_CONNECTIONS = int(os.getenv("MIN_CONNECTIONS_COUNT", 10))

# MONGO DATABASE
MONGO_HOST = str(os.getenv("MONGO_HOST", "127.0.0.1"))
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_DATABASE = str(os.getenv("MONGO_DB", "fastapi"))
MONGO_USERNAME = str(os.getenv("MONGO_USERNAME", "fastapi"))
MONGO_PASSWORD = str(os.getenv("MONGO_PASSWORD", "reza1234"))
# MONGO_URL = f"mongodb://localhost:27017/{MONGO_DATABASE}"
MONGO_URL = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DATABASE}"
# MONGO_URL = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DATABASE}" \
#             f"?retryWrites=true&w=majority "

# Sendgrid configuration
SG_API = os.getenv("SENDGRID_API", "")
FROM_EMAIL = "noreply@email.com"
