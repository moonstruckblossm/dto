#author: <author here>
# date: <date here>

# --------------- Section 3 --------------- #
#  String Duplication / Pattern Recognition #

# you may choose to use any symbol, it does not have to be the dollar sign

# create the following pattern using string duplication and print statments:
#
# $
# $$
# $$$
# $$$$
# $$$$$
print("$")
print("$"*2)
print("$"*3)
print("$"*4)
print("$"*5)
print()

# create the following pattern using string duplication and print statments:
#
# $$$$$
# $$$$
# $$$
# $$
# $
print("$"*5)
print("$"*4)
print("$"*3)
print("$"*2)
print("$")

print()

# create the following pattern using string duplication and print statments:
#
#     $
#    $$
#   $$$
#  $$$$
# $$$$$

#though they are not visible, the spaces before each dollar sign are characters
#for each line you print, there is a certain number of spaces and a certain number of dollar signs
#either way, you'll want to have FIVE characters on each line that you print, so how can we approach this?

#think about how many dollar signs are on each line. if you need five characters on each line, but there's less than five
#dollar signs on a line, what will you do?

#remember that both spaces (" ") and dollar signs ($) are characters!

#FIVE characters in total - the number of dollar signs you want = the amount of spaces to put before the dollar signs!

#for example, if you want THREE dollar signs, you'll want to put TWO spaces before them, since three plus two is five.
#your total number of characters five.


print((" "*4)+"$"*1)
print((" "*3)+"$"*2)
print((" "*2)+"$"*3)
print((" "*1)+"$"*4)
print((" "*0)+"$"*5)
print()
# create the following pattern using string duplication and print statments:
#
# $$$$$
#  $$$$
#   $$$
#    $$
#     $

#this is very similar to the previous problem! you'll just want to do the same thing in the opposite order to get a
#right-oriented upside down right triangle!

print((" "*0)+"$"*5)
print((" "*1)+"$"*4)
print((" "*2)+"$"*3)
print((" "*3)+"$"*2)
print((" "*4)+"$"*1)