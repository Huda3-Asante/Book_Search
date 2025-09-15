import os, requests
from pymongo import MongoClient


MONGO_URL = MONGO_URI="mongodb+srv://book_search_api:booksearch333@grow-cohort6.vplsjeb.mongodb.net/book_search_db?retryWrites=true&w=majority&appName=Grow-Cohort6"

client = MongoClient(MONGO_URL)

# Connect to your new database
db = client["book_search_db"]

# Create collection
books_collection = db["reading_list"]
