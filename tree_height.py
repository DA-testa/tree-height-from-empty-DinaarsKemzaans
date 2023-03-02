#Dinārs Kemzāns 221RDB321 17.grupa

import sys
import threading


def compute_height(n, parents):
    # Write this function
    resultats = [-1] * n

    def aprekins(node):
        if resultats[node] != -1:
            return resultats[node]
        if parents[node] == -1:
            resultats[node] = 1
        else:
            resultats[node] = aprekins(parents[node]) + 1
        return resultats[node]

    max_height = 0
    for x in range(n):
        max_height = max(max_height, aprekins(x))

    return max_height


def main():
    text = str(input())
    if "I" in text:
        skaits = int(input())
        dati = list(map(int, input().split()))
        print(compute_height(skaits, dati))

    if "F" in text:
        name = str(input())
        name = "test/" + str(name)
        with open(name, 'r') as file:
            skaits = int(file.readline())
            dati = list(map(int, file.readline().split()))
        print(compute_height(skaits, dati))



# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
