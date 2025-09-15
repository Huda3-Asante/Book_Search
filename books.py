from db import books_collection

sample_books = [
{
  "title": "The Originals: Oliver Twist",
  "author":"Charles Dickens",
  "published_date": "July 5, 2018",
  "user_status": "reading"
},
{
  "title": "The Mountain Is You",
  "author":"Brianna Wiest",
  "published_date": "February 2024",
  "user_status": "Finished"
},
{
  "title": "Think and Grow Rich",
  "author":"Napoleon Hill",
  "published_date": "October 12, 2020",
  "user_status": "reading"
},
{
  "title": "Exactly What to Say",
  "author":"Phil M. Jones",
  "published_date": "July 26, 2017",
  "user_status": "reading"
},
{"title": "Words that Change Minds",
  "author":"Shelle Rose Charvet",
  "published_date": "1997",
  "user_status": "Finished"
},
{
  "title": "Win Your Inner Battles",
  "author":"Darius Foroux",
  "published_date": "December 19, 2016",
  "user_status": "reading"
}                         
]

if sample_books:  # prevents empty inserts
    books_collection.insert_many(sample_books)
    print("Sample books inserted successfully!")