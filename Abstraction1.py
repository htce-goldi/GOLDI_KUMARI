from abc import ABC, abstractmethod

class phone(ABC):
    @abstractmethod
    def call(self):
        pass
    def chargingtype(self):
        print("this phone uses usb-c charging")
class redminote6pro(phone):
    def call(self):
        print("calling from redmi note 6 pro...")
    def chargingtype(self):
        print("this phone uses usb-c charging")
    def internetaccess(self):
        print("accessing internet on redmi note 6 pro")
    def cameradetails(self):
        print("redmi note 6 pro has a 12mp + 5mp dual rear camera")
class iphone13pro(phone):
    def call(self):
        print("calling from iphone 13 pro...")
    def internetaccess(self):
        print("accessing internet on iphone 13 pro")

    def faceid(self):
        print("iphone 13 pro uses face id for security")

    def cameradetails(self):
        print("iphone 13 pro has a 12mp triple-camera system with telephoto lens")

    def chargingtype(self):
        print("this phone uses lightning port for charging")

class samsungm14(phone):
    def call(self):
        print("calling from samsung galaxy m14...")
    def internetaccess(self):
        print("accessing internet on samsung galaxy m14")
    def batteryinfo(self):
        print("samsung galaxy m14 has a 6000mah battery")

    def cameradetails(self):
        print("samsung galaxy m14 has 50mp triple camera setup")

print("redmi note 6 pro")
redmi = redminote6pro()
redmi.chargingtype()
redmi.call()
redmi.internetaccess()
redmi.cameradetails()


print("\niphone 13 pro")
iphone = iphone13pro()
iphone.call()
iphone.internetaccess()
iphone.faceid()
iphone.cameradetails()
iphone.chargingtype()

print("\nsamsung galaxy m14")
samsung = samsungm14()
samsung.call()
samsung.internetaccess()
samsung.batteryinfo()
samsung.cameradetails()
samsung.chargingtype()
