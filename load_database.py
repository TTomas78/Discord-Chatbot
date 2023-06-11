from services.PineconeService import PineconeService
from dotenv import load_dotenv
import os

load_dotenv()
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_ENV = os.getenv('PINECONE_ENV')

pinecone_service = PineconeService(PINECONE_API_KEY, PINECONE_ENV)
pinecone_service.create_database('data.csv')