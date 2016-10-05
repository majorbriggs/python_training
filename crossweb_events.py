from collections import namedtuple
from google_calendar_api.api_utils import get_calendar_service, get_upcoming_events
import re
import datetime
from bs4 import BeautifulSoup
from bs4 import NavigableString
import requests
import logging
import logconf

LOGGER = logging.getLogger(__name__)

Event = namedtuple("Event", ['title', 'date', 'topic', 'type', 'paid'])
url = "http://crossweb.pl/wydarzenia/?miasto=trojmiasto"

def add_event(event):
    service = get_calendar_service()
    startdate = event.date.strftime("%Y-%m-%d")
    enddate = event.date.strftime("%Y-%m-%d")
    paid = event.paid
    event = {
            "summary": event.title,
            "description": "@Topic: {topic}\n@Event Type: {type}\n@Paid: {paid}".format(topic=event.topic, type=event.type, paid=paid),
            "start": {"date": startdate},
            "end": {"date": enddate}
            }

    service.events().insert(calendarId='primary', body=event).execute()

def get_existing_events():
    description_regex = re.compile('@Topic: (.*)\n@Event Type: (.*)\n@Paid: (.*)')
    event_tuples = []
    events = get_upcoming_events()
    for event in events:
        date_str = event['start'].get('dateTime', event['start'].get('date'))
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        title = event['summary']
        topic, type, paid = description_regex.search(event['description']).groups()
        e = Event(title=title, date=date, topic=topic, type=type, paid=paid)
        event_tuples.append(e)
    return event_tuples

def get_events_elements():
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "html.parser")
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

def get_list_of_events():
    events = []
    for e in get_events_elements():
        day, month = map(int, e.find('span', class_='colDataDay').text.split('.'))
        event_year = datetime.date.today().year if month >= datetime.date.today().month else datetime.date.today().year+1
        date = datetime.datetime(year=event_year, month=month, day=day)
        title = e.find('div', class_='title').text.strip()
        topic = e.find('div', class_='topic').text
        type = e.find('div',  class_='type').text
        paid = 'No' if e.find('div',  class_='cost').text == 'Bezpłatny' else 'Yes'
        events.append(Event(title=title, date=date, topic=topic, type=type, paid=paid))
    return events


def synchronize_calendar():
    existing_events = get_existing_events()
    LOGGER.info('{} items found on crossweb'.format(len(existing_events)))
    for e in get_list_of_events():
        if e not in existing_events:
            LOGGER.info('Adding new event {}'.format(e.title.encode("utf-8")))
            add_event(e)

if __name__ == "__main__":
    synchronize_calendar()


