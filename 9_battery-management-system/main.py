class Mobile:

    #  customize decorator in the class
    def decorators(my_func):
        def wrapper(self):
            print("Showing Battery Percentage")

            result = my_func(self)

            print("Session Ended....\n")
            return result

        return wrapper




    def __init__(self):
        self.__battery = 100
        self.__sign = "%"

    def set_bat(self, battery):
        if 0 <= battery <= 100:
            self.__battery = battery
        else:
            print("Invalid Battery Percentage")

    @decorators
    def get_bat(self):
        print("Battery percentage read by this unseen method")
        print(f"{self.__battery}{self.__sign}")
        return self.__battery


m = Mobile()

m.set_bat(78)
m.get_bat()

m.set_bat(98)
m.get_bat()