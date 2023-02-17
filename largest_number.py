def largest_number(some_digit):
    return 10 ** some_digit - 1

some_digit = 2
#some_digit = 6 => 999999
#some_digit = 2 => 99
#some_digit = 4 => 9999
print(largest_number(some_digit))