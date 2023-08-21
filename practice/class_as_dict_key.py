class MyThing:
    def __init__(self, name, some_list, count):
        self.name = name
        self.count = count
        self.some_list = some_list

    def __eq__(self, other):
        return (self.name, self.count, self.some_list) == (other.name, other.count, other.some_list)

    def __hash__(self):
        return hash((self.name, self.count))


first = MyThing('kk', [4], 0)
second = MyThing('kk', [4], 0)

test = {first: 'value1', second: 'value2'}
print(test)
