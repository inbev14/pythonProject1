def sort_grades(data: list):
    for _ in data:
        letter = data.pop(0)
        data.append(letter.upper())
    data.sort(reverse=True)
    return data


print(sort_grades(['A', 'B', 'C', 'C', 'F', 'A']))
print(['F', 'C', 'C', 'B', 'A', 'A'])
print(sort_grades(['b', 'c', 'c', 'f', 'a', 'd']))
print(['F', 'C', 'C', 'B', 'A'])
print(sort_grades([]))
print([])
