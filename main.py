from fastapi import FastAPI, HTTPException, status
import os, requests  
from pymongo import MongoClient
from pydantic import BaseModel
from dotenv import load_dotenv 


load_dotenv()
tags_metadata=[
    {"name":"HomePage"},
    {"name":"Manage Books"},
]

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

db = client ["book_search_db"]
reading_list_collection = db["reading_list"]

app =FastAPI(title ="📖Book Search API", description="Welcome to Huda's Library! Explore🚀, Find🔍, Read📖 and Manage Books and get recommendations of Books from the Best Authors around the world.", version="1.0")
class NewBook(BaseModel):
   title: str
   author: list [str]
   published_date: str
   user_status: str

@app.get("/Home", tags=["HomePage"])
def Welcome():
    return{"message": "📚Welcome to Huda's Book Search API! Explore, Find, Read and Manage your Favourite Books with ease⭐"}

@app.get("/books_title/{title}", tags=["Manage Books"])
def get_book(title: str):
    url = f"https://www.googleapis.com/books/v1/volumes?q=intitle:{title}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error fetching data from Google Books API")
    data = response.json()
    if "items" not in data:
        raise HTTPException(status_code=404, detail="No books found")

    books = []
    for item in data["items"]:
        volume = item.get("volumeInfo", {})
        books.append({
            "title": volume.get("title"),
            "authors": volume.get("authors", []),
            "published_date": volume.get("publishedDate", "N/A")
        })
    return{"Search results":books}

@app.post("/reading_list", tags=["Manage Books"])
def save_book(book: NewBook):
    reading_list_collection.insert_one(book.model_dump())
    return{"Status":"Book Saved✅"}

@app.get("/reading_books", tags=["Manage Books"])
def reading_books():
    books = list(reading_list_collection.find({"user_status":"reading"}, {"_id": 0}))
    return {"reading": books}

@app.get("/finished_books", tags=["Manage Books"])
def finished_books():
    books = list(reading_list_collection.find({"user_status":"Finished"}, {"_id": 0}))
    return {"Finished": books}

@app.get("/Recommendations/{author}", tags=["Based on your search"])
def get_book(author: str):
    url = f"https://www.googleapis.com/books/v1/volumes?q=inauthor:{author}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error fetching data from Google Books API")
    data = response.json()
    if "items" not in data:
        raise HTTPException(status_code=404, detail="No authors found")

    books = []
    for item in data["items"]:
        volume = item.get("volumeInfo", {})
        books.append({
            "title": volume.get("title"),
            "authors": volume.get("authors", []),
            "published_date": volume.get("publishedDate", "N/A")
        })
    return{"Search results":books}