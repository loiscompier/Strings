# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

## part 1 

# create variables; players who scored a goal 
player1 = "Ruud Gullit"
player2 = "Marco van Basten"

# create variables; for each minute a goal is made 
goal_0 = 32
goal_1 = 54

# create a string that reports on who scored when
scorers =player1+ " " +  str(goal_0) + ", "+ player2 + " " + str(goal_1)

print (scorers)

# create a single string with information about who scored when in a different format
report = f'{player1} scored in the {goal_0}nd minute {player2} scored in the {goal_1}th minute' 


print (report)

#str(goal_0) + ","+ player2 +  str(goal_1)b scorer_name> scored in the <when_they_scored>nd minute

#<scorer_name> scored in the <when_they_scored>th minute

## part 2 


# player that played in the soccer match
player = "Ronald_Koeman"

# use slicing and the find-method to isolate and store the player's first name.
first_name = player[0:6]

print(first_name)

# use find, slicing and len to isolate and store the length of their last name.

last_name = "Koeman"

last_name = player[7:]

last_name_len = len (last_name)

print(last_name_len)

# isolate and store the player's name in another format 
name_short = player[0:1] + ". " + player[7:13]
print(name_short)

# their first name plus an exclamation mark(!), x-times, where x is the number of characters in their first name
first_name_len = len (first_name)
chant= first_name_len *( first_name + "! ")

print (chant)

# Make super-sure the last character of chant is not a space by using the inequality operator (!=)
good_chant =  chant [-0]!= " "

print(good_chant)

# value is true = niet gelijk 
