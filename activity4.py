# store points from the various teams; I used houses from my school
dayton_team = 182
blackhawk_team = 120
eastman_team = 110
halsted_team = 4

# make up a cumulative number for last weeks stars
last_week_total = 400

# now let's assume that we get one reward star per 12 points; 5 stars go in one box
points_per_star = 12
stars_per_box = 5

# calculating total and average points
total = dayton_team + blackhawk_team + eastman_team + halsted_team
average = total / 4

print("the total points are    :", total)
print("the average points are  :", average)

#pack stars into boxes
stars = total // points_per_star
boxes = stars // stars_per_box
leftover_points = total % points_per_star
leftover_stars = stars % stars_per_box

print("The prelim amount of stars generated is   :", stars)
print("The prelim amount of boxes needed to pack the stars is :", boxes)
print("There are ", leftover_points," leftover points.")
print("There are ", leftover_stars,"leftover stars that were not put into boxes.")

# compare to last week's output
beat_last_week = total > last_week_total
print("Did we beat last week?", beat_last_week)
print("Did we tie last week?", total == last_week_total)
print("Did we at least match last week?", total >= last_week_total)


# Assignment operators like += and -=
# bonus points awarded for being exceptionally handsome
total += 100

# subtracted points for fistfighting
total -= 110

# final star count
stars = total // points_per_star
boxes = stars // stars_per_box

# final boxes packed
print("The final amount of stars generated is   :", stars)
print("The final amount of boxes needed to pack the stars is :", boxes)