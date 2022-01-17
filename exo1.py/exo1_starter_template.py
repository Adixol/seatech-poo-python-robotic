ROBOT_COUNT = 0

class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutown', 'running']
    
    def __init__(self, name=None):
      if name:
        self.name = name
      global ROBOT_COUNT
      ROBOT_COUNT += 1

    def __del__(self):
      print("%s Auto destruction NOW"%(self.name))
      global ROBOT_COUNT
      ROBOT_COUNT -= 1

    def name(self):
      return self.__name

    def run(self):
      self.power = True

    def stop(self):
      self.power = False

    def charge(self, __battery_level=0):
      for i in range(100):
        print(__battery_level)
        __battery_level =+ 1
      print("Robot chargé")
       

r = Robot()
r.name = "bob"
print(r.name)
r.charge
