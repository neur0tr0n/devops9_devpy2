list_ = ['2018-01-01', 'yandex', 'cpc', 100]

dict_ = {}
val = None
for i in reversed(list_):
    if val is None:
        val = i
    else:
        key = i
        if len(dict_) == 0:
            val = i
        else:
            val = dict(dict_)
            dict_.clear()
        dict_[key] = val
print(dict_)
