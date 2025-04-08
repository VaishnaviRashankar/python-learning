class car():
    def set_details(self,brand,color):
        self.brand = brand
        self.color = color
        
    def show_details(self):
        print(f'This is a {self.color}{self.brand}')
car1=car()
car1.set_details('BMW','black')

car2 = car()
car2.set_details('Marcedies','black')

car1.show_details()
car2.show_details()
