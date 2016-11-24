print "Time to format some strings!"

name   = "Landon Manning"
age    = 28
height = 178
weight = 100
eyes   = "Green"
hair   = "Brown"

print "So this %s guy, right? only %d years old!" % (name, age)
print "He's a tall dude, 'bout %dcm." % height
print "Bit on the heavy side though, %dkg." % weight
print "But at least he has luxurious %s eyes, and wonderful %s hair!" % (
	eyes, hair
)
