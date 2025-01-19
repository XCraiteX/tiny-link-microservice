import requests

links = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    "https://www.python.org",
    "https://www.djangoproject.com",
    "https://www.wikipedia.org",
    "https://www.reddit.com",
    "https://www.medium.com",
    "https://www.npmjs.com",
    "https://www.cloudflare.com",
    "https://www.nonexistentwebsite1.com",  # не существует
    "https://www.nonexistentwebsite2.com",  # не существует
    "https://www.nonexistentwebsite3.net",  # не существует
    "https://www.nonexistentwebsite4.org",  # не существует
    "https://www.nonexistentwebsite5.edu",  # не существует
    "https://www.nonexistentwebsite6.co",  # не существует
    "https://www.nonexistentwebsite7.biz",  # не существует
    "https://www.nonexistentwebsite8.store",  # не существует
    "https://www.nonexistentwebsite9.museum",  # не существует
    "https://www.nonexistentwebsite10.asia",  # не существует
    "https://www.spotify.com",
    "https://www.amazon.com",
    "https://www.netflix.com",
    "https://www.apple.com",
    "https://www.microsoft.com",
    "https://www.youtube.com",
    "https://www.twitch.tv",
    "https://www.facebook.com",
    "https://www.instagram.com",
    "https://www.twitter.com",
    "https://www.coursera.org",
    "https://www.udemy.com",
    "https://www.edx.org",
    "https://www.academia.edu",
    "https://www.linkedin.com",
    "https://www.pinterest.com",
    "https://www.quora.com",
    "https://www.github.io",
    "https://www.hackerrank.com",
    "https://www.kaggle.com",
    "https://www.nonexistentwebsite11.xyz",  # не существует
    "https://www.nonexistentwebsite12.tv",  # не существует
    "https://www.nonexistentwebsite13.cc",  # не существует
    "https://www.nonexistentwebsite14.pro",  # не существует
    "https://www.nonexistentwebsite15.tel",  # не существует
    "https://www.nonexistentwebsite16.mobi",  # не существует
    "https://www.nonexistentwebsite17.jobs",  # не существует
    "https://www.nonexistentwebsite18.coop",  # не существует
    "https://www.nonexistentwebsite19.name",  # не существует
    "https://www.nonexistentwebsite20.museum",  # не существует
    "https://www.disney.com",
    "https://www.bbc.com",
    "https://www.nytimes.com",
    "https://www.reuters.com",
    "https://www.washingtonpost.com",
    "https://www.theguardian.com",
    "https://www.bloomberg.com",
    "https://www.aljazeera.com",
    "https://www.cnn.com",
    "https://www.forbes.com"
]


def test_create_short(links):
    for link in links:
        try:
            values = {'link': link, 'limit': 5}
            response = requests.post(url='http://127.0.0.1:8000/lnk/api', json={'link': link})
            print(response.json())

        except Exception as e: print(e)

test_create_short(links)