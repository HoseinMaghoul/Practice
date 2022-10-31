
def main():
    number = number_()
    x, y = find_numbers(number)
    print(x, y)
    s_t = find_satars(number)
    draw(number, s_t)


def draw(number, s_t):

    mat = pixels(number)
    starts(mat, number, s_t)
    for row in mat:
        print("".join(row))


def starts(mat, number, s_t):
    for x, y in s_t:
        if number % 4 == 0 or number % 4 == 1:
            mat[number // 2 - 2 * y][number // 2 + 2 * x] = "* "
        if number % 4 == 2:
            mat[number // 2 - 1 - 2 * y][number // 2 - 1 + 2 * x] = "* "
        if number % 4 == 3:
            mat[number // 2 + 1 - 2 * y][number // 2 - 1 + 2 * x] = "* "



def pixels(number):
    if number % 2 == 0:
        mat = [[" " for _ in range(number + 1)] for _ in range(number + 1)]
    else:
        mat = [[" " for _ in range(number)] for _ in range(number)]
    return  mat


def find_satars(number):
    c = []
    for i in range(1, number +1):
        x, y = find_numbers(i)
        c.append((x, y))
    return c





def find_numbers(number):
    x, y = 0, 0
    if number % 4 == 0:
        x, y = - number // 4, number // 4
    if number % 4 == 1:
        x, y = -(number -1) // 4, -(number -1) // 4
    if number % 4 == 2:
        x, y = (number + 2) // 4, -(number -2) // 4
    if number % 4 == 3:
        x, y = (number +1) // 4, (number + 1) //4
    return x, y





def number_():
    number = input()
    number = int(number)
    return  number




if __name__ == "__main__":
    print(main())