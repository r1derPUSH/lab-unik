def robot_route(matrix):
    if not matrix or not matrix[0]:
        return []

    result = []

    for i in range(len(matrix)):
        if i % 2 == 0:
            result.extend(matrix[i])
        else:
            result.extend(matrix[i][::-1])

    return result