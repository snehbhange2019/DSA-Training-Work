def add(*args):
    total = 0

    for i in args:
        total += i

    print("Sum =", total)


# Different cases
add(10)
add(10, 20)
add(11, 22, 33)

