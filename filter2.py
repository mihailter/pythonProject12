#Из случайного списка Найти все отрицательные числа кратные 3
def check(num):
    return num < 0 and num % 3 == 0
import random

if __name__ == '__main__':
    n = 100
    random_list = [random.randint(-100, 100) for _ in range(n)]

    print(list(filter(check, random_list)))

    for value in filter(check, random_list):
        print(value)
        

