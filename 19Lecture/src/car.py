class Car:
    def __init__(self,name,model):
        self.name = name
        self.model = model 
    def display_info(self):
        print(f"Name: {self.name}")