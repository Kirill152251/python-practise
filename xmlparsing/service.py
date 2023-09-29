import xml.etree.ElementTree as ET
from dataclasses import dataclass
import json


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
    warning_text: str
    price_value: float
    currency: str


def parce_flights_xml(path: str) -> list[Flight]:
    tree = ET.parse(path)
    root = tree.getroot()
    priced_itineraries = root.find('PricedItineraries')
    parsed_flights: list[Flight] = []

    for flights_attr in priced_itineraries.findall('Flights'):
        flight_data = {
            'Source': None,
            'Destination': None,
            'Carrier': None,
            'NumberOfStops': None,
            'DepartureTimeStamp': None,
            'ArrivalTimeStamp': None,
            'Class': None,
            'TicketType': None,
            'WarningText': None,
            'price': None,
            'currency': None
        }
        price_data_block = flights_attr.find('Pricing')
        flight_data['currency'] = price_data_block.get('currency')
        for item in price_data_block.findall('ServiceCharges'):
            if item.get('ChargeType') == 'TotalAmount':
                flight_data['price'] = float(item.text)

        for flight in flights_attr.iter('Flight'):
            for attr in flight:
                if attr.tag in flight_data:
                    flight_data[attr.tag] = attr.text
            parsed_flights.append(Flight(*flight_data.values()))
    return parsed_flights


data = parce_flights_xml("xmlparsing/RS_Via-3.xml")
procced_data = [flight for flight in data
                if flight.destination == 'BKK' and flight.source == 'DXB']
serializable_data = [x.__dict__ for x in procced_data]
with open('data_json.json', 'w') as file:
    json.dump(serializable_data, file, indent=4)
lowest_price = sorted(procced_data, key=lambda flight: flight.price_value)[0]
highest_price = sorted(procced_data, key=lambda flight: flight.price_value)[-1]
print(highest_price)
print(lowest_price)
