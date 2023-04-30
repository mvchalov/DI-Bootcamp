from faker import Faker
from rent.models import Customer
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


def run():
    fake = Faker()
    for i in range(100):
        name = fake.name().split()
        customer = Customer(
            first_name=name[0],
            last_name=name[1],
            email=fake.email(),
            phone_number=fake.phone_number(),
            city=fake.city(),
            country=fake.country()
        )
        customer.save()