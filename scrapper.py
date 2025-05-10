import requests
from bs4 import BeautifulSoup
import json
import csv
import sqlite3

URL = "https://quotes.toscrape.com/"

def create_table():
    con = sqlite3.connect("quotes.sqlite3")
    cursor = con.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS quotes(
            id INTEGER primary key autoincrement,
            text TEXT,
            author TEXT,
            tags TEXT
        );
        '''
    )
    con.close()
    print("Database and table created successfully.")

def insert_quote(text, author, tags):
    con = sqlite3.connect("quotes.sqlite3")
    cursor = con.cursor()
    # Only join if tags is a list
    if isinstance(tags, list):
        tags_str = ', '.join(tags)
    else:
        tags_str = tags
    cursor.execute(
        "INSERT INTO quotes (text, author, tags) VALUES (?, ?, ?)", (text, author, tags_str)
    )
    con.commit()
    con.close()

def scrape_site(url):
    response = requests.get(url)
    if response.status_code != 200:
        return []
    
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, "html.parser")
    quote_elements = soup.find_all("div", class_="quote")

    quotes = []
    for quote in quote_elements:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        tags = [tag.text for tag in quote.find_all("a", class_="tag")]
        quotes.append({
            'text': text,
            'author': author,
            'tags': tags
        })

    print("All data Scrapped.")
    return quotes

def save_to_json(quotes):
    with open('quotes.json', 'w', encoding="utf-8") as f:
        json.dump(quotes, f, indent=4, ensure_ascii=False)

def save_to_csv(quotes):
    with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["text", "author", "tags"])
        writer.writeheader()
        for quote in quotes:
            # Make a copy to avoid modifying the original list
            quote_copy = quote.copy()
            # Convert list of tags to a comma-separated string
            if isinstance(quote_copy['tags'], list):
                quote_copy['tags'] = ', '.join(quote_copy['tags'])
            writer.writerow(quote_copy)

quotes = scrape_site(URL)
save_to_json(quotes)
save_to_csv(quotes)

# Database functionality
create_table()
for quote in quotes:
    insert_quote(quote['text'], quote['author'], quote['tags'])

