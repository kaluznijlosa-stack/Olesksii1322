import requests

for page in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    books_text = requests.get(url).text

    books = books_text.split('<h3>')

    for book in books:
        if 'title="' in book:
            name = book.split('title="')[1].split('"')[0]
            print(name)
