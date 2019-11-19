def fact(number):
    res = 1
    for i in range(number + 1):
        res = i * res
    return res

# def sin1(x, e):
#     sin_x = ((-1)** n) * (x**((2*n+1)/(2*n+1)))

def main():
    print(fact(5))


if __name__ == "__main__":
    main()