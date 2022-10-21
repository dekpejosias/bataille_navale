import numpy as np
import unittest
class Weapons:
    def __init__(self,munition: int ,range :int):
        #assert munition>=0 and munition<=10, "les munitions doivent etre des entiers"
        #assert range>0
        self._munition=munition
        self._range=range

    def fire_at(self,x,y,z):
        if _munition==0:
            print("NoAmunitionError")
        else:
             _munition=_munition-1

#implementation des armes:
Lance_missiles_antisurface=Weapons(40,30)


class LMantisurface(Weapons):
    def __init__(self,munition: int,range: float):
        super().__init__(self,munition,range)

    def fire_at(self,x,y,z):
        assert self.z==0 and np.sprt(self.x**2+self.y**2+self.z**2)<30,"OutOfRangeError"
        if self.z==0 or np.sprt(x**2+y**2+z**2)>30:
            print("OutOfRangeError")
            self._munition -=1
        else :
            self._munition -=1
class Lancetorpilles(Weapons):
    def __init__(self,munition,range):
        super().__init__(self,munition,range)

    def fire_at(self,x,y,z):
        assert self.z <= 0 and self.x ** 2 + self.y ** 2 + self.z ** 2 < 400, "OutOfRangeError"
        if self.z>0 or self.x**2+self.y**2+self.z**2 > 400:
            print("OutOfRangeError")
            self._munition -=1
        else:
            self._munition -=1
class LMantiair(Weapons):
    def __init__(self,munition,range):
        super().__init__(self,munition,range)

    def fire_at(self,x,y,z):
        assert self.z > 0 and self.x ** 2 + self.y ** 2 + self.z ** 2 < 1600, "OutOfRangeError"
        if self.z<=0 or self.x**2+self.y**2+self.z**2 > 1600:
            print("OutOfRangeError")
            self._munition -=1
        else:
            self._munition -=1

if __name__=='__main__':
    unittest.main()
