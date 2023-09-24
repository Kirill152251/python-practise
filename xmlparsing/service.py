import xml.etree.ElementTree as ET
from dataclasses import dataclass


@dataclass
class Flight:
    source: str
    destination: str
    carrier: str
    number_of_stops: str
    departure_time_stamp: str
    arrival_time_stamp: str
    flight_class: str
    ticket_type: str


tree = ET.parse(r'D:\python-practise\xmlparsing\RS_Via-3.xml')
root = tree.getroot()
flight_list: list[Flight] = []

for flight in root.iter('Flight'):
    flight_data = {
        'Source': None,
        'Destination': None,
        'Carrier': None,
        'NumberOfStops': None,
        'DepartureTimeStamp': None,
        'ArrivalTimeStamp': None,
        'Class': None,
        'TicketType': None
    }
    for attrib in flight:
        if attrib.tag in flight_data:
            flight_data[attrib.tag] = attrib.text
    flight_list.append(Flight(*flight_data.values()))
