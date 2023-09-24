import xml.etree.ElementTree as et


def get_optins(start_point: str = 'DXB', end_point: str = 'BKK'):
    pass


tree = et.parse('RS_Via-3.xml')
root = tree.getroot()
all_flights = root[1]
item = all_flights[0]
for c in item:
    print(c.tag, c.attrib)
print()
item_onwards_flights = item[0]
item_return_flights = item[1]

test = root.find('Source')
print(test.text)
for c in item_onwards_flights:
    for c1 in c:
        for c2 in c1:
            print(c2.tag, c2.text)
