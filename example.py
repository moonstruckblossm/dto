# arithmetic operators - integers and floats
#   +  | addition
#   -  | subtraction
#   *  | multiplication
#   /  | true division
#   // | floor division
#   ** | exponentiation
#   %  | modulus

# addition
print('the sum of 5 + 7 =', 5 + 7)
print('the sum of 5 + 2 + -4 + 11 =', 5 + 2 + -4 + 11)

# subtraction
print('the difference of 11 - 2 =', 11 - 2)
print('the difference of 12 - -15 =', 12 - -15)

# multiplication

# true division
print('the dividend of 11 / 12 =', 11 / 12)
print('the dividend of 40 / -2 / 3 =', 40 / -2 / 3)

# floor division
print('the integer dividend of 44 / 3 =', 44 // 3)
print('the integer dividend of -234 / 15 =', -234 // 15)

# exponentiation
print('the power of 3 ^ 4 =', 3 ** 4)
print('the power of 21 ^ -2', 21 ** -2)

# modulus
print('the remainder of 15 / 8 =', 15 % 8)
print('the remainder of -14 / 5 =', -14 % 5)

# using mulitple operations in a single print statement
# grouping using ()
print('(4 - 2) ** 5 / 2 - (13 ** (4 - 2)) =', (4 - 2) ** 5 / 2 - (13 ** (4 - 2)))
print('(21 * 3 - 4) / (3 ** 2 + (1 - 2)) =', (21 * 3 - 4) / (3 ** 2 + (1 - 2)))

# --------------- string concatenation and duplication --------------- #

# string concatenation is the combination of strings via the addition operator
print('this is an example of concatenation of two sentences.' + ' as you can see it combines them together!')
print('when concatenating strings, it doesn\'t ' + 'a space between the sentences, so you\'ll have to do it yourself')

print('one ' + 'two ' + 'three ' + 'four ' + 'five')

# string duplication is the duplication of strings using multiplication
print('la' * 8)
print('cat' * 10)

print('$' * 1)
print('$' * 2)
print('$' * 3)
print('$' * 4)
print('$' * 5)
