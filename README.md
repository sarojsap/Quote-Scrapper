# 📝 Quote Scraper

A Python-based web scraper that extracts inspirational quotes from [Quotes to Scrape](https://quotes.toscrape.com/) and stores them in multiple formats including **JSON**, **CSV**, and an **SQLite database**.

## 🚀 Features

- Scrapes quote text, author, and tags from each page
- Saves the scraped data to:
  - `quotes.json`
  - `quotes.csv`
  - `quotes.sqlite3` (SQLite database)
- Cleans and formats tag lists appropriately
- Includes structured database creation and insertion logic

## 🧰 Technologies Used

- `requests` – for fetching web pages  
- `BeautifulSoup` – for parsing HTML  
- `json` & `csv` – for data export  
- `sqlite3` – for storing quotes locally

## 📦 How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/sarojsap/Quote-Scrapper
   
