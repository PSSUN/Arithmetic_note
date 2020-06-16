def permutation(x):
    if len(x) <= 1:
        return x
    result = []
    for i in range(len(x)):
        s = x[:i] + x[i + 1:]
        p = permutation(s)
        for j in p:
            result.append(x[i:i + 1] + list(j))
    return result


if __name__ == '__main__':
    case = permutation(['a', 'b', 'c'])
    print(case)
