import yaml

with open('Base.yaml') as f :
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(type(data))
    for key, value in data.items():
        print(key)

"-----------------------------------------------------------------"
# import yaml
#
# with open('data.yaml') as f:
#     docs = yaml.load_all(f, Loader=yaml.FullLoader)
#
#     for doc in docs:
#
#         for k, v in doc.items():
#             print(k, "->", v)

'''---------------------------------------------------------------'''

# import yaml
#
# users = [{'name': 'John Doe', 'occupation': 'gardener'},
#          {'name': 'Lucy Black', 'occupation': 'teacher'}]
#
# print(yaml.dump(users))

'''---------------------------------------------------------------'''

# import yaml
#
# with open('Base.yaml') as f:
#     data = yaml.load(f, Loader=yaml.FullLoader)
#     print(data)
#
#     sorted = yaml.dump(data, sort_keys=True)
#     print(sorted)

'''---------------------------------------------------------------'''
'''We can work with a lower-level API when parsing YAML files.
 The scan method scans a YAML stream and produces scanning tokens.'''
# import yaml
#
# with open('Base.yaml') as f:
#     data = yaml.scan(f, Loader=yaml.FullLoader)
#
#     for token in data:
#         print(token)