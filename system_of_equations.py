def rearrange_system_of_equations(coefficient_matrix,
                                  unknown_vector,
                                  constant_vector):
    m = coefficient_matrix.shape[0]
    if m != coefficient_matrix.shape[1] or \
       m != unknown_vector.shape[0] or \
       m != constant_vector.shape[0]:
       raise ValueError("Dimensions do not match")

    A = np.zeros([m, m])
    b = np.zeros(m)
    i = 0
    j = 0
    for number in unknown_vector:
        if number == None:
            A[:, i] = coefficient_matrix[:, j]
            i += 1
        elif number != 0:
            b -= number * coefficient_matrix[:, j]
        j += 1
    j = 0
    for number in constant_vector:
        if number == None:
            temp = np.zeros(m)
            temp[j] = -1
            A[:, i] = temp
            i += 1
        elif number != 0:
            temp = np.zeros(m)
            temp[j] = number
            b += temp
        j += 1
    return A, b
