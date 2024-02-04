

def bubble_sort(data):
    for i in range(len(data)-1):
        for j in range(len(data) - i - 1):
            color = ['red' if x == j or x == j+1 else 'blue' for x in range(len(data))]
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
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


if __name__ == '__main__':
    pass
