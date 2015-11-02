__author__ = 'petert'
# One possible solution would be to change the tab width, but the first column already has more space than it needs.
# The best solution would be to set the width of each column independently. As you may have guessed by now, string
# formatting provides a much nicer solution. We can also right-justify each field:

layout = "{0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>24}"

print(layout.format("i", "i**2", "i**3", "i**5", "i**10", "i**20"))
for i in range(1, 11):
    print(layout.format(i, i**2, i**3, i**5, i**10, i**20))