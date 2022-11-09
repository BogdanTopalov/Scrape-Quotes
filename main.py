import json
from urllib.request import urlopen

from bs4 import BeautifulSoup


QUOTES_URL = 'https://quotes.toscrape.com/'

all_quotes = []

for page_number in range(1, 11):
    page_url = QUOTES_URL + f'page/{page_number}/'

    page = urlopen(page_url)

    soup = BeautifulSoup(page, 'html.parser')

    page_quotes = soup.find_all('div', 'quote')

    for quote in page_quotes:
        quote_text = quote.find('span', 'text').text

        # Remove quotation marks.
        quote_text = quote_text.strip('“”')

        quote_author = quote.find('small', 'author').text

        tags = [
            q.text
            for q in quote.find_all('a', 'tag')
        ]

        # Convert the tags list to string.
        quote_tags = ';'.join(tags)

        quote_info = {
            'text': quote_text,
            'author': quote_author,
            'tags': quote_tags,
            'url': page_url
        }

        all_quotes.append(quote_info)


# Create JSON file with the quotes' data.
with open('quotes.json', 'w') as output:
    json.dump(all_quotes, output, indent=2)

print('JSON file created successfully.')
