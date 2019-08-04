import requests
from mtgoResults import get_all_urls_for_date, get_card_count_from_url

def main():
    urls = get_all_urls_for_date(2019, 7, 22)
    for url in urls:
        print(url)
    results = []
    print(get_card_count_from_url(urls[0]['url']))
    


if __name__ == "__main__":
    main()