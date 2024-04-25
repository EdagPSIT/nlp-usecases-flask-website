import paralleldots
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

api_key = os.environ.get("PARALLELDOTS_API_KEY")

# Setting your API key
paralleldots.set_api_key(api_key)


def sentiment_analysis(text):
    response = paralleldots.sentiment(text)
    return response