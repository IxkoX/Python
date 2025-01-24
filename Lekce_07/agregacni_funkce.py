def get_min(data):
    min_value = data[0]

    for value in data:
        if value < min_value:
            min_value = value
    
    return min_value


def get_max(data):
    max_value = data[0]

    for value in data:
        if value > max_value:
            max_value = value
    
    return max_value

def get_sum(data):
    celkem = 0

    for value in data:
        celkem += value

    return value

def get_avg(data):
    # avg = average = průměr
    return get_sum(data) / len(data)


print(get_min([1, 2, 7238]))
print(get_min([238, 82, 29]))

