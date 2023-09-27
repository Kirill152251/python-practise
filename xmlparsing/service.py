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
    warning_text: str
    price_value: float
    currency: str


tree = ET.parse(r'/home/kirill/pythonProject/xmlparsing/RS_Via-3.xml')
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
        'WarningText': '',
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

for i in range(6):
    print(parsed_flights[i])
