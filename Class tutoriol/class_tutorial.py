class Robot:
# 一个类变量，用来计数机器人的数量
    population = 0
    __newPro='1stPro'

    def __init__(self, name):
        self.name = name
        print("(Initializing {0})".format(self.name))
        self.population+=1
        Robot.population += 1

    def die(self):
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))


    def say_hi(self):
        print("Greetings, my masters call me {}.".format(self.name))


    @classmethod
    def how_many(cls):
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
print(dir(droid1))
#droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
print(droid2.population)
#droid2.say_hi()
Robot.how_many()
#Robot.say_hi('Ray')
#print("\nRobots can do some work here.\n")
#print("Robots have finished their work. So let's destroy them.")

droid1.die()
droid2.die()
print(droid2.how_many())
print(Robot.how_many())
print(droid2.population)
