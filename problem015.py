# Starting in the top left corner of a 2x2 grid, and only being able to
# move to the right and down, there are exactly 6 routes to the bottom
# right corner:
#
# right right down down
# right down right down
# right down down right
# down right right down
# down right down right
# down down right right
#
# How many such routes are there through a 20×20 grid?

# step numbers in grid is always length + width
# always 20 right steps and 20 down steps = 40 steps total
# just need to calculate number of possible hat draws from hat with 20 "right" and 20 "down"

# answer is 40! / (20!*20!) = 137846528820
# see http://www.regentsprep.org/regents/math/algebra/apr2/LpermRep.htm