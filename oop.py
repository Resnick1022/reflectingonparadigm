class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  def repair(self):
    self.condition = "repaired"


class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price)
  
  def boost(self):
    self.max_speed *= 2

class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price)
  
  def flame_jet(self,other):
    other.condition = "trashed"

anakins_pod = AnakinsPod(max_speed=500, condition="repaired", price=1000)

print(anakins_pod.max_speed) 
print(anakins_pod.condition)  
print(anakins_pod.price) 


#How does this solution demonstrate the four pillars of OOP?
  #it inherits it from the original class
#Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
  #I am not sure, honestly
#How in particular did Object Oriented Programming assist in the solving of this problem?
  #oop helps us program by re using code without having to repeat the code multiple times