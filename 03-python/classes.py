class Point():
  def __init__(self,input1,input2):
      self.x = input1
      self.y = input2


p = Point(2,8)

print(p)
print(p.x)
print(p.y)


class Flight():
   def __init__(self,capacity):
      self.capacity = capacity
      self.passagers = []

   def add_passagers(self,name):
      if not self.open_seats():
        return False
      self.passagers.append(name)
      return True 
   def open_seats(self):
      return self.capacity - len(self.passagers)
   
flight = Flight(3)

print(f"openseats is {flight.open_seats()}")


names = ["harry","Ron","heri","Ginny"]

for person in names:
   success = flight.add_passagers(person)
   if success:
      print(f"successful add {person} in flight")
else:
      print(f"{person} is not add in flight")
      
      
      
# 如何理解面向对象？





# 扩展：
