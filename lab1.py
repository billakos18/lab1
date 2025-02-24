import requests  # εισαγωγή της βιβλιοθήκης
import datetime


def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

# url = 'http://python.org/'  # προσδιορισμός του url

# with requests.get(url) as response:  # το αντικείμενο response
#     html = response.text
#     more(html)
url  = input("give url:\t")


if not url.startswith('https://'):
    url = 'https://' + url

print(url)

with requests.get(url) as response:  # το αντικείμενο response
    # for key in response.headers:
    #     print(f"Name: {key}, Value: {response.headers[key]}")

    print(f"Server: {response.headers.get('Server')}")

    print(f"Has cookies: {'Set-Cookie' in response.headers}")

    for cookie in response.cookies:
        print(f"Cookie name: {cookie.name}\tExpiration date: {datetime.datetime.fromtimestamp(cookie.expires)}")

