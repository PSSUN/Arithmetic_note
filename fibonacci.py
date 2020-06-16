def f(n):
    assert n >= 0, "n>0"
    if n <= 1:
        return n
    return f(n-1) + f(n-2)


if __name__ == '__main__':
    print(f(3))
    
    
