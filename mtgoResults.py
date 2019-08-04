import requests

FORMAT_TYPES = ['pauper', 'modern', 'legacy', 'vintage', 'standard']
LEAGUE_TYPES = ['mcq', 'mocs', 'league', 'challenge']
STARTING_URL = 'https://magic.wizards.com/en/articles/archive/mtgo-standings/'


def get_all(start_year, start_month, start_day, end_year, end_month, end_day):
    res = []
    for year in range(start_year, end_year):
        for month in range(start_month, end_month):
            for day in range(start_day, end_day):
                res.append(year, month, day)


def get_all_urls_for_date(year: int, month: int, day: int)->list:
    result = []
    year = year if len(str(year)) == 4 else '20' + str(year)
    month = month if len(str(month)) == 2 else '0' + str(month)
    day = day if len(str(day)) == 2 else '0' + str(day)
    date = f'{str(year)}-{str(month)}-{str(day)}'

    for f in FORMAT_TYPES:
        for t in LEAGUE_TYPES:
            url = f'{STARTING_URL}{f}-{t}-{date}'
            r = requests.get(url)
            if r.status_code == 200 and len(r.text) > 90000:
                result.append({
                    'date': date,
                    'url': url,
                    'format_type': f
                })

    return result

def get_card_count_from_url(url):
    results = []
    count_string = '<span class="card-count">'
    card_string = 'class="deck-list-link">'

    card_dictionary = {}
    req = requests.get(url)
    start = req.text.find(count_string)

    while start > 0:
        card_count = req.text[start +
                            len(count_string):start + len(count_string) + 1]
        start = req.text.find(card_string, start)
        end = req.text.find('<', start)
        card_name = req.text[start + len(card_string):end]
        if card_name not in card_dictionary:
            card_dictionary[card_name] = int(card_count)
        else:
            card_dictionary[card_name] += int(card_count)
        start = req.text.find(count_string, start + 1)

    # for result in card_dictionary.keys():
    #     print(result + ':' + str(card_dictionary[result]))
    return card_dictionary