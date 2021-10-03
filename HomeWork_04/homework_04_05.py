list_ = ['2018-01-01', 'yandex', 'cpc', 100]

dict_ = {}
val = ''
for i in reversed(list_):
    if val == '':
        val = i
    else:
        if len(dict_) != 0:
            val = dict(dict_)
            dict_.clear()
        dict_[i] = val
print(dict_)
