

def bubble_sort(data):
    for i in range(len(data)-1):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                yield data

def selection_sort(data):
    pass

if __name__ == '__main__':
    bubble_sort()