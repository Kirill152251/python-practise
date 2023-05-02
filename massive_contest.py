def task1():
    a = list(map(int, input().split()))
    if a[0] <= a[2] and a[1] <= a[2]:
        print("YES")
    else:
        print("NO")


def task2():
    n = int(input())
    a = [0] * n
    max_count = 0
    count = 0

    for i in range(n):
        a[i] = int(input())

    for item in a:
        if item == 1:
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count

    print(max_count)


def task3():
    a = list()
    while True:
        input_char = input()
        if input_char != '#':
            a.append(input_char)
        else:
            break
    a = max(a)
    b = min(a)
    c = sum(a) / len(a)
    pass


def task4():
    string = input()
    a = int(input())
    if a > 0:
        print(string * a)
    else:
        number_of_parts = len(string) / -a
        if not number_of_parts.is_integer():
            print("NO SOLUTION")
        else:
            parts = []
            positive_a = -a
            for i in range(positive_a):
                cut = slice(i * positive_a, i * positive_a + positive_a)
                parts.append(string[cut])
            parts_set = set()
            for item in parts:
                parts_set.add(item)
            if len(parts_set) == 1:
                print(parts_set.pop())
            else:
                print("NO SOLUTION")


task4()
