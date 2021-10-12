import xml.etree.ElementTree as et

min_word_len = 6

parser = et.XMLParser(encoding='utf-8')
tree = et.parse('files/newsafr.xml', parser)
root = tree.getroot()

xml_descriptions = root.findall('channel/item/description')

words = []
for news in xml_descriptions:
    for word in news.text.split(' '):
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

