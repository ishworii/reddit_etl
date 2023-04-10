# Reddit Post Downloader and Sentiment Analysis

This project downloads the top posts from a specified subreddit and stores text posts in a PostgreSQL database. It also
performs sentiment analysis on the post text using the NLTK library.

## Requirements

Before running the scripts, install the required Python libraries using pip:

`pip install praw python-dotenv psycopg2-binary sqlalchemy nltk`

## Configuration

Create a `.env` file in the project root directory with the following content:

`REDDIT_CLIENT_ID=your_client_id`

`REDDIT_CLIENT_SECRET=your_client_secret`

`REDDIT_USER_AGENT=your_user_agent`

`DATABASE_URL=postgresql://username:password@localhost/dbname`

Replace `your_client_id`, `your_client_secret`, `your_user_agent`, `username`, `password`, and `dbname` with your actual
Reddit API and PostgreSQL credentials.

## Usage

Run the `post_downloader.py` script to download the top posts from a subreddit and store them in the PostgreSQL
database:

Run the `main.py` script to perform sentiment analysis on the post text and display the results:

## TODO

- Update `main.py` to fetch post data from the PostgreSQL database instead of directly from the Reddit API. This will
  allow for better management and caching of the downloaded data.
- Implement comprehensive sentiment analysis by taking into account additional factors like context, sarcasm, and
  multi-sentence sentiment.
- Add keyword extraction functionality to identify and extract the most relevant keywords and topics from the post text.
- Develop visualization tools to display sentiment analysis and keyword extraction results, making it easier to
  understand trends and patterns in the data.
- Add table Author to store the author details