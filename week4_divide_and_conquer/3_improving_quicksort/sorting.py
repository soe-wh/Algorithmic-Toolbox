# Uses python3
import sys
import random


def partition3(a, l, r):
    # write your code here
    pivot = a[l]
    j, k, m = l, 1, 0
    for i in range(l + 1, r + 1):
        if a[i] < pivot:
            j += 1
            a[i], a[j] = a[j], a[i]
        elif a[i] == pivot:
            j += 1
            a[i], a[j] = a[j], a[i]
            a[j], a[l + k] = a[l + k], a[j]
            k += 1
    while m < k:
        a[l + m], a[j - m] = a[j - m], a[l + m]
        m += 1
    return j, m


def partition2(a, l, r):
    pivot = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] < pivot:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m, n = partition3(a, l, r)
    randomized_quick_sort(a, l, m - n)
    randomized_quick_sort(a, m + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for pivot in a:
        print(pivot, end=' ')
