ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]
       }
unique_ids = []

for k, v in ids.items():
    for val in v:
        unique_ids.append(val)
unique_ids = set(unique_ids)
print(unique_ids)

