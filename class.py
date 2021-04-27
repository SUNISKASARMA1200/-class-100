class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.model=model
        self.company=company
        self.color=color
        self.speed_limit=speed_limit

    def start(self):
        print("started")  

    def stop(self):
        print("stopped")

    def accelarate(self):
        print("accelarated")

    def change_gear(self,gear_type):
        print("gear changed")


audi= Car ("A6","white","Audi",90)

print (audi.start())


                     