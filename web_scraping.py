from bs4 import BeautifulSoup
from bs4 import NavigableString
import requests
from collections import namedtuple
import datetime

url = "http://crossweb.pl/wydarzenia/?miasto=trojmiasto"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")
event = namedtuple("Event", ['title', 'date', 'topic', 'type', 'paid'])


def get_list_of_events():
    future_events = []
    event_list = bs.find('div', attrs={'id': 'eventList'})
    for child in event_list.children:
        if isinstance(child, NavigableString):
            continue
        if child.get('class') == ['brow']:
            future_events.append(child)
            continue
        if child.name == 'h2':
            return future_events


def parse_events(event_elements):
    events = []
    for e in get_list_of_events():
        day, month = e.find('span', class_='colDataDay').text.split('.')
        date = datetime.datetime(year=datetime.date.today().year, month=int(month), day=int(day))
        title = e.find('div', class_='title').text.strip()
        topic = e.find('div', class_='topic').text
        type = e.find('div',  class_='type').text
        paid = e.find('div',  class_='cost').text != 'Bezpłatny'
        events.append(event(title=title, date=date, topic=topic, type=type, paid=paid))
    return events


for e in parse_events(get_list_of_events()):
    print(e)
