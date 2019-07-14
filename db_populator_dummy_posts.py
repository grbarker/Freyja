from app import create_app
app = create_app()
app.app_context().push()

from app import db
from app.models import *
import random

users = User.query.all()
dummy_posts = [
    'hello', 'hi there', 'yarp', 'how are you', "what's up people!",
    'what a test', 'haha', 'yes', 'no', 'I want some beer', 'Hello everyone!',
    'How is everyone doing today?', "I'm doing good", "I have a question",
    "Man do I love this website!", "I love makeup!", "I love beauty products",
    "Can anyone recommend an eye liner?", "Good morning",
    "Found some foundation that works well with my skin tone",
    "Artus makes the best lip gloss", "one", "two", "three", "fouir", "five",
    "six", "seven", "eight", "nine", "ten", "Party like it's 1999!", "Why?",
    "How?", "I can't wait for the next sale.", "thanks", "Thanks"
    ]

for user in users:
    posts =[]
    while len(posts) < 7:
        random_post = random.choice(dummy_posts)
        if random_post not in posts:
            posts.append(random_post)
            post = Post(body = random_post, author=user)
            db.session.add(post)
db.session.commit()

print('!!!!!!!!!!___DUMMY_____POSTS_____SUCCESSFULLY_____ADDED___!!!!!!!!!!')

