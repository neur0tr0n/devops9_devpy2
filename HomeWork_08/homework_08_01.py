import json

min_word_len = 6

with open('files/newsafr.json', 'r') as f:
    data = json.load(f)

news_list = data['rss']['channel']['items']
words = []
for news in news_list:
    for word in news['description'].split(' '):
        words.append(word)

words_dict = {}

for word in words:
    if len(word) >= min_word_len:
        if word.lower() in words_dict.keys():
            words_dict[word.lower()] += 1
        else:
            words_dict[word.lower()] = 1

counts = words_dict.values()
sorted_counts = sorted(counts, reverse=True)
for i in range(0, 10):
    for word, count in words_dict.items():
        if count == sorted_counts[i]:
            print(f'Слово "{word}" встречается {count} раз.')

