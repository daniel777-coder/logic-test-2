import json


def format_data():
    with open('source_file_2.json') as json_file:
        data = json.load(json_file)

    data.sort(key=lambda x: x['priority'])

    watchers = {}
    managers = {}
    for item in data:
        for watcher in item['watchers']:
            watchers.setdefault(watcher, []).append(item['name'])
        for manager in item['managers']:
            managers.setdefault(manager, []).append(item['name'])

    with open('watchers.json', 'w') as watchers_file:
        json.dump(watchers, watchers_file, indent=4)

    with open('managers.json', 'w') as managers_file:
        json.dump(managers, managers_file, indent=4)


if __name__ == '__main__':
    format_data()
