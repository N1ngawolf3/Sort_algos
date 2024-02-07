from random import randint


def bubble_sort(data):
    for i in range(len(data)-1):
        for j in range(len(data) - i - 1):
            color = ['red' if x == j or x == j+1 else 'blue' for x in range(len(data))]
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                yield data, color
    color = ['blue' for _ in range(len(data))]
    yield data, color

def selection_sort(data):
    for i in range(len(data) - 1):
        smallest = i
        for j in range(i + 1, len(data)):
            if data[j] < data[smallest]:
                smallest = j
            color = ['red' if x == i or x == smallest else 'blue' for x in range(len(data))]
        data[i], data[smallest] = data[smallest], data[i]
        yield data, color
    color = ["blue" for _ in range(len(data))]
    yield data, color


def insertion_sort(data):
    for i in range(1, len(data)):
        j = i
        while data[j-1] > data[j] and j > 0:
            color = ['red' if x == j or x == j-1 else 'blue' for x in range(len(data))]
            data[j], data[j-1] = data[j-1], data[j]
            j -= 1
            yield data, color
    color = ['blue' for _ in range(len(data))]
    yield data, color


def merge_sort(data): 
    if len(data) > 1: 
        mid = len(data)//2
        left = data[:mid] 
        right = data[mid:]
        merge_sort(left) 
        merge_sort(right) 

        i = j = k = 0

        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                data[k] = left[i] 
                i += 1
            else: 
                data[k] = right[j] 
                j += 1
            k += 1

        while i < len(left): 
            data[k] = left[i] 
            i += 1
            k += 1

        while j < len(right): 
            data[k] = right[j] 
            j += 1
            k += 1
    

if __name__ == '__main__':
    data = [randint(-10, 10) for _ in range(7)]
    # ins = insertion_sort(data)
    # while True:
    #     new = input('new: ')
    #     if new == 'n':
    #         print(next(ins))
    #     else:
    #         break

