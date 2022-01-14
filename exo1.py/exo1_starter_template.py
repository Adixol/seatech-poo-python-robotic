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

  def run(self):
    self.power = True

  def stop(self):
    self.power = False

  def charge(self):
    self.current_speed = 

        
    """
      Give your best code here ( •̀ ω •́ )✧
    """