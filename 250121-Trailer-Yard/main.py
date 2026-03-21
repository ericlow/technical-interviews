import json

def process_events(events):
    pass


def process_event_data():
    with open('data.json', 'r') as file:
        events = json.load(file)

    process_events(events)


if __name__ == '__main__':
    process_event_data()