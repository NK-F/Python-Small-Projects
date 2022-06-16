# Importing random module
import random

# Storing random data into lists to create story.
when = ['A long time ago', 'Yesterday', 'Before you were born', 'In the future', 'Before Thanos arrived', 'In another universe']
who = ['Black Panther', 'Storm', 'Green Lantern', 'Iron Man', 'Batman', 'Superman', 'Captain America', 'Wonder Woman']
went = ['Arkham Asylum', 'Gotham City', 'Metropolis', 'Stark Tower', 'Bat Cave', 'Avengers HQ']
what = ['to eat a lot of cakes', 'to fight for justice', 'to steal ice cream', 'to dance', 'to play video games']

# Using string concatenition & randome.choice() to print a random element from all the lists 
print(random.choice(when) + ', ' + random.choice(who) + ' went to ' + random.choice(went) + ' ' + random.choice(what) + '.')