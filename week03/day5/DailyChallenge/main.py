from requests import get, exceptions
from datetime import datetime
from re import match


def stopwatch_decorator(func):
    def wrapper(*args):
        start = datetime.now()
        func(*args)
        end = datetime.now()
        return (end - start).total_seconds()

    return wrapper


@stopwatch_decorator
def request_a_page(page_url):
    try:
        get(page_url)
    except exceptions.RequestException as e:
        raise e


while True:
    site_url = input("Enter a website URL: ")
    if match(r'^((http|https)://)', site_url):
        break
    else:
        print("Enter a valid URL!")

print(f"To reach {site_url} we need {request_a_page(site_url)}s")
