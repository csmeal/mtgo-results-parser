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


def get_all_for_date(year, month, day):
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