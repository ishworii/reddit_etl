import os
from datetime import datetime

import praw
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

load_dotenv()

# Set up Reddit API
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)


# Set up SQLAlchemy ORM
class Base(DeclarativeBase):
    pass


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    post_id = Column(String(255), unique=True)
    title = Column(Text)
    text = Column(Text)
    author = Column(String(255))
    created_utc = Column(DateTime)
    score = Column(Integer)
    num_comments = Column(Integer)
    permalink = Column(Text)
    url = Column(Text)


def download_top_posts(subreddit_name, num_posts=100, Session=None):
    subreddit = reddit.subreddit(subreddit_name)
    top_posts = subreddit.top(limit=num_posts)

    with Session() as session:
        for post in top_posts:
            if not post.is_self:
                continue  # Skip posts without text

            post_entry = Post(
                post_id=post.id,
                title=post.title,
                text=post.selftext,
                author=str(post.author),
                created_utc=datetime.utcfromtimestamp(post.created_utc),
                score=post.score,
                num_comments=post.num_comments,
                permalink=post.permalink,
                url=post.url

            )

            session.add(post_entry)

        session.commit()
        session.close()


def main():
    engine = create_engine(os.getenv("DATABASE_URL"))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    subreddit_name = "Upwork"
    download_top_posts(subreddit_name, num_posts=500, Session=Session)


if __name__ == "__main__":
    main()
