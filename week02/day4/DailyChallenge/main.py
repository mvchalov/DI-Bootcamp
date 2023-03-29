# Daily Challenge: Solve The Matrix
input_data = [
    "7i3",
    "Tsi",
    "h%x",
    "i #",
    "sM ",
    "$a ",
    "#t%",
    "^r!"
]


def transposer(matrix):
    transposed_matrix = []
    for i in range(len(matrix[0])):
        transposed_matrix.append([])
        for j in range(len(matrix)):
            transposed_matrix[i].append(matrix[j][i])
    return transposed_matrix


def replacer(items):
    updated_list = []
    for item in enumerate(items):
        index, value = item
        if index > 0:
            if value != " " and not value.isalpha() and updated_list[-1] != " " and not updated_list[-1].isalpha():
                updated_list.append(" ")
            else:
                updated_list.append(value)
        else:
            updated_list.append(value)
    return updated_list


flattened_list = [item for sublist in transposer(list(map(lambda e: [*e], input_data))) for item in sublist]
print("".join(list(filter(lambda e: e.isalpha() or e == " ", replacer(flattened_list)))))
