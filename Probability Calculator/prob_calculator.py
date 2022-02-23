import copy
import random
# Consider using the modules imported above.

class Hat:

  random.seed()
  def __init__(self, **kwargs):
    self.contents= []
    for key,value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self,number):
    removed=[]
    if number> len(self.contents):
      return self.contents
    for i in range(number):
      ball=self.contents.pop(int(random.random()* len(self.contents)))
      removed.append(ball)
    return removed
    


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count=0

  for i in range(num_experiments):
    expected=copy.deepcopy(expected_balls)
    hat_copy=copy.deepcopy(hat)
    colors=hat_copy.draw(num_balls_drawn)

    for balls in colors:
      if (balls in expected):
        expected[balls]-=1

    if (all(x<=0 for x in expected.values())):
      count+=1
      
  return count/num_experiments
  
