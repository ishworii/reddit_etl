<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reddit Post Downloader and Sentiment Analysis</title>
</head>
<body>
    <h1>Reddit Post Downloader and Sentiment Analysis</h1>
    <p>
        This project downloads the top posts from a specified subreddit and stores text posts in a PostgreSQL database. It also performs sentiment analysis on the post text using the NLTK library.
    </p>

    <h2>Requirements</h2>
    <p>
        Before running the scripts, install the required Python libraries using pip:
    </p>
    <pre><code>pip install praw python-dotenv psycopg2-binary sqlalchemy nltk</code></pre>

    <h2>Configuration</h2>
    <p>
        Create a <code>.env</code> file in the project root directory with the following content:
    </p>
    <pre><code>REDDIT_CLIENT_ID=your_client_id

REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=your_user_agent
DATABASE_URL=postgresql://username:password@localhost/dbname
</code></pre>
<p>Replace <code>your_client_id</code>, <code>your_client_secret</code>, <code>your_user_agent</code>, <code>
username</code>, <code>password</code>, and <code>dbname</code> with your actual Reddit API and PostgreSQL
credentials.</p>

    <h2>Usage</h2>
    <p>
        Run the <code>reddit_post_downloader.py</code> script to download the top posts from a subreddit and store them in the PostgreSQL database:
    </p>
    <pre><code>python reddit_post_downloader.py</code></pre>
    <p>
        Run the <code>sentiment_analysis.py</code> script to perform sentiment analysis on the post text and display the results:
    </p>
    <pre><code>python sentiment_analysis.py</code></pre>

</body>
</html>
