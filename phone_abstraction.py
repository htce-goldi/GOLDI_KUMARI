from abc import ABC, abstractmethod

class phone(ABC):
    @abstractmethod
    def call(self):
        pass

class redminote6pro(phone):
    def call(self):
        print("redmi note 6 pro")
    def my_phone(self):
        print("this is my phone")    

    def chargingtype(self):
        print("this phone uses usb-c charging")

    def internetaccess(self):
        print("accessing internet from redmi note 6 pro")

    def cameradetails(self):
        print("redmi note 6 pro has a 12mp + 5mp dual rear camera")

phone = redminote6pro()
phone.my_phone()
phone.call()
phone.chargingtype()
phone.internetaccess()
phone.cameradetails()
