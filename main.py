import requests
from thing import get_all_for_date


urls = get_all_for_date(2019, 7, 22)
for url in urls:
    print(url)
results = []
count_string = '<span class="card-count">'
card_string = 'class="deck-list-link">'

card_dictionary = {}
for url in urls:
    req = requests.get(url['url'])
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

    for result in card_dictionary.keys():
        print(result + ':' + str(card_dictionary[result]))
