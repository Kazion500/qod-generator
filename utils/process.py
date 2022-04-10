from bs4 import BeautifulSoup
from requests import request
from .send_email import send_email


def get_document(url):
    response = request('GET', url)
    return response.text


def process_document():
    try:
        soup = BeautifulSoup(get_document(
            'https://www.brainyquote.com/quote_of_the_day'), 'html.parser')
        link = soup.find('a', {'class': 'oncl_q'})
        quote = link.contents[1]['alt']
        send_email(quote)
        return quote
    except Exception as e:
        print(e)
        print('Error: Could not get quote of the day')
        send_email('Sorry We failed to get the quote of the day 🥹')
        return None
