import re

def hex_numbers(string):
    words = string.split(" ")
    ret = []
    for word in words:
        if re.match("0x[A-F0-9]+$", word):
            ret.append(word)
        elif re.match("[A-F0-9]+$", word):
            ret.append("0x"+word)
    return " ".join(ret)

input_str = input()
print(hex_numbers(input_str))

from typing import List, Tuple

def knapsack(val: int, items: List[Tuple[int, int, str]]) -> List[str]:
    n = len(items)
    max_days, max_val = 16 * 2, val // 50
    dp = [[0 for _ in range(max_val + 1)] for _ in range(max_days + 1)]
    path = [[[] for _ in range(max_val + 1)] for _ in range(max_days + 1)]
    for i in range(1, n + 1):
        for j in range(1, max_days + 1):
            for k in range(max_val, items[i - 1][1] - 1, -1):
                if dp[j - 1][k - items[i - 1][1]] + items[i - 1][0] > dp[j][k]:
                    dp[j][k] = dp[j - 1][k - items[i - 1][1]] + items[i - 1][0]
                    path[j][k] = path[j - 1][k - items[i - 1][1]] + [items[i - 1][2]]
                elif dp[j - 1][k - items[i - 1][1]] + items[i - 1][0] == dp[j][k] and path[j][k] > path[j - 1][k - items[i - 1][1]] + [items[i - 1][2]]:
                    path[j][k] = path[j - 1][k - items[i - 1][1]] + [items[i - 1][2]]
            for k in range(items[i - 1][1] - 1, -1, -1):
                if dp[j][k] < dp[j -1][k]:
                    dp[j][k] = dp[j - 1][k]
                    path[j][k] = path[j - 1][k]

    return path[max_days][max_val]


def solve_problem():
    total_money = int(input())
    total_places = int(input())
    places: List[Tuple[int, int, str]] = []
    for _ in range(total_places):
        interest, cost, name = input().split(';')
        places.append((int(interest), int(cost) // 50, name))

    results = knapsack(total_money, places)
    print(';'.join(results))


solve_problem()


solve_problem()




