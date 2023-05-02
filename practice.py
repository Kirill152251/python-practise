import random


def task1():
    number = input()
    answer = 0
    for digit in number:
        answer += int(digit)
    print(answer)


def task2():
    first_point = [int(input()), int(input())]
    second_point = [int(input()), int(input())]
    if first_point[0] == second_point[0]:
        print("YES")
    elif first_point[1] == second_point[1]:
        print("YES")
    elif sum(first_point) == sum(second_point):
        print("YES")
    elif first_point[0] - first_point[1] == second_point[0] - second_point[1]:
        print("YES")
    else:
        print("NO")


def task3():
    year = int(input())
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print('YES')
    else:
        print('NO')


def task4():
    number = int(input())
    square = 0
    for i in range(1, number ** 2):
        square = i ** 2
        if square > number:
            break
        else:
            print(square)


def task5():
    number = int(input())
    k = 1
    p = 0
    answer = 0
    while p < number:
        p = 2 * k
        k = k * 2
        answer += 1
    print(answer)


def task6():
    count = 0
    while True:
        if int(input()) != 0:
            count += 1
        else:
            break
    print(count)


a = [9]*10
print(a)
