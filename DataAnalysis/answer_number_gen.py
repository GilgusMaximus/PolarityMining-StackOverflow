from random import randint
from random import seed
from datetime import datetime

seed(datetime.now())
posts = []
for i in range(0, 20):
    posts.append(randint(1, 648789))

print(posts)