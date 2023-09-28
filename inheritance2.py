class Car:
    def __init__(self,wheels=4):
        self.wheels=wheels

class Gas(Car):
    def __init__(self,engine='Gas',tank_cap=20):
        Car.__init__(self)
        self.engine=engine
        self.tank_cap=tank_cap
        self.tank=0

    def refuel(self):
        self.tank=self.tank_cap

class Electric(Car):
    def __init__(self,engine='Electric',kWh_cap=60):
        Car.__init__(self)
        self.engine=engine
        self.kWh_cap=kWh_cap
        self.kWh=0

    def recharge(self):
        self.kWh=self.kWh_cap


class Hybrid(Gas, Electric):
    def __init__(self,engine='Hybrid', tank_cap=11,kWh_cap=5):
        Gas.__init__(self,engine,tank_cap)
        Electric.__init__(self,engine,kWh_cap)


prius = Hybrid()
print(prius.engine)
print(prius.tank_cap)
print(prius.tank)
print(prius.kWh_cap)
print(prius.kWh)
prius.recharge()
prius.refuel()
print(prius.tank)
print(prius.kWh)





