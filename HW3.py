def inner_q1(num, old_num, sum):
    if old_num == 1:
        return 1
    if num == 0:
        return sum
    if old_num % num == 0:
        sum += num
    return inner_q1(num - 1, old_num, sum)


def inner_q2(lst, x, lst_len, m, count_x):
    if m == lst_len:
        if x == 0:
            count_x += 1
        return count_x
    count_x = inner_q2(lst, x - lst[m], lst_len, m + 1, count_x)
    count_x = inner_q2(lst, x, lst_len, m + 1, count_x)
    return count_x


def inner_q3_a(mat, indices, epidemic, count):
    n = indices[0]
    m = indices[1]
    if count == 0:
        if mat[n][m] != 0:
            mat[n][m] = epidemic
            return None
    if n >= 0 | n <= len(mat) | m >= 0 | m <= len(mat[0]):
        if mat[n][m] == 0:
            mat[n][m] = epidemic
    else:
        return None
    count += 1
    if n + 1 < len(mat):
        if mat[n + 1][m] == 0:
            inner_q3_a(mat, (n + 1, m), epidemic, count)
    if n - 1 >= 0:
        if mat[n - 1][m] == 0:
            inner_q3_a(mat, (n - 1, m), epidemic, count)
    if m + 1 < len(mat[0]):
        if mat[n][m + 1] == 0:
            inner_q3_a(mat, (n, m + 1), epidemic, count)
    if m - 1 >= -1:
        if mat[n][m - 1] == 0:
            inner_q3_a(mat, (n, m - 1), epidemic, count)


def inner_q3b_1(mat, indices, sum):
    sum.append(0)
    n = indices[0]
    m = indices[1]
    if n < 0 | n > len(mat) | m < 0 | m > len(mat[0]):
        return sum
    if n + 1 < len(mat):
        sum = inner_q3b_2(mat, indices, 0, len(sum) - 1, sum)
        sum = inner_q3b_1(mat, (n + 1, m), sum)
    if m + 1 < len(mat[0]):
        sum = inner_q3b_2(mat, indices, 0, len(sum) - 1, sum)
        sum = inner_q3b_1(mat, (n, m + 1), sum)
    return sum


def inner_q3b_2(mat, indices, count, place, sum):
    n = indices[0]
    m = indices[1]
    if count == 0:
        if mat[n][m] != 0:
            mat[n][m] = 4
            sum[place] = 0
    if n >= 0 | n <= len(mat) | m >= 0 | m <= len(mat[0]):
        if mat[n][m] == 0:
            mat[n][m] = 4
            sum[place] += 1
    else:
        sum.append(0)
        return sum
    count += 1
    if n + 1 < len(mat):
        if mat[n + 1][m] == 0:
            sum = inner_q3b_2(mat, (n + 1, m), count, place, sum)
    if n - 1 >= 0:
        if mat[n - 1][m] == 0:
            sum = inner_q3b_2(mat, (n - 1, m), count, place, sum)
    if m + 1 < len(mat[0]):
        if mat[n][m + 1] == 0:
            sum = inner_q3b_2(mat, (n, m + 1), count, place, sum)
    if m - 1 >= -1:
        if mat[n][m - 1] == 0:
            sum = inner_q3b_2(mat, (n, m - 1), count, place, sum)
    return sum


def question1(num):
    # Qs1
    sum_of_divisors = inner_q1(num - 1, num, 0)
    return num == sum_of_divisors


def question2(lst, x):
    """
    Qs2
    """
    return inner_q2(lst, x, len(lst), 0, 0)


def question3_a(mat, indices, epidemic):
    """
    Qs3a
    """
    inner_q3_a(mat, indices, epidemic, 0)
    print(mat)


def question3_b(mat):
    """
    Qs3b
    """
    # WRITE YOUR CODE HERE!
    if len(mat) == 1:
        if len(mat[0]) == 1:
            if mat[0][0] == 0:
                return 1
    sum = []
    sum = inner_q3b_1(mat, (0, 0), sum)
    return max(sum)