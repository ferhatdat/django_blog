from faker import Faker
from .models import Category, Post

def run():
    fake = Faker(["tr-TR"])
    categories = ("Life", "Science", "Politics", "Sports")

    for category in categories:
        new_category = Category.objects.create(name=category)
        for i in range(10):
            Post.objects.create(category = new_category, title = fake.name(), content=fake.text())
    print("Finished")