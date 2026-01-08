# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
n = 5
def hollow_square(n):
    result = ""

    # top line
    for i in range(1):
        result += "*" * n

    # middle lines
    for j in range(n - 2):
        result += "\n*"
        for k in range(n - 2):
            result += " "
        for l in range(n > 1):
            result += "*"

    # bottom line
    for j in range(n > 1):
        result += "\n" + "*" * n

    return result
print(hollow_square(5))

    

# 1
# 12
# 123
# 1234
n = 4
def number_pattern(n):
    result = ""

    for i in range (n):
        count = 1
        for k in range(i + 1):
            result += str(count)
            count += 1
        result += "\n"
        
    return result.strip()

print(number_pattern(4))

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
n = 5
def sum_of_natural_numbers(n):
    result = 0
    count = 1

    while count <= n:
        result += count
        count += 1

    return result

    

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""

    for i in range(n):
        spaces = n - i - 1
        stars = 2 * i + 1

        result += " " * spaces
        result += "*" * stars

        if i < n - 1:
            result += "\n"

    return result
