from abc import ABCMeta, abstractmethod, ABC

class UnmannedVehicle():

    def __init__(self, name=None):
      if name:
        self.name = name

    def __del__(self):
      print("%s Auto destruction NOW"%(self.name))

    def name(self):
      return self.__name

    def do_something_interesting(self):
        print("%s do smtg interesting"%(self.name))

class AerialVehicle(ABC):
    """ A vehicle made for ground fields."""

    @abstractmethod
    def decolage(self):
        pass

class GroundVehicle(ABC):
    """ A vehicle made for ground fields."""

    @abstractmethod
    def roule(self):
        pass

class AerialAndGroundVehicle(AerialVehicle, GroundVehicle):
    print("Aerial and ground vehicle")
    
    

class UnderseaVehicle(ABC):
    """ A vehicle made for ground fields."""
    @abstractmethod
    def mise_a_l_eau(self):
        pass

class UAV(AerialVehicle):
    """Unmanned Aerial Vehicle"""
    def decolage(self):
        print("DECOLAGE")

class UUV(UnderseaVehicle):
    """Unmanned Undersea Vehicle"""
    def mise_a_l_eau(self):
        print("MISE A L'EAU")
    
    def do_something_interesting(self):
        print("UUV do smtg interesting")

class UGV(GroundVehicle):
    """Unmanned Ground Vehicle"""
    def roule(self):
        print("ROULE")


# uav = UAV()
# uav.do_something_interesting()
# uav.do_something_aerial_specific()

# ugv = UGV()
# ugv.do_something_interesting()
# ugv.do_something_ground_specific()

uuv = UUV()
uuv.mise_a_l_eau()
# uuv.do_something_interesting()
# uuv.do_something_undersea_specific()

