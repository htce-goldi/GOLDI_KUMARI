from abc import ABC, abstractmethod

class phone(ABC):
    @abstractmethod
    def call(self):
        pass

    def chargingtype(self):
        print("his phone uses USB-C charging")

class smartphone(phone):
    def call(self):
        print("this is a smartphone")

    def internetaccess(self):
        print("accessing internet from smartphone")

device = smartphone()
device.call()
device.internetaccess()
device.chargingtype()
