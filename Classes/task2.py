class Human:
    def __init__(self, has_head):
        self.has_head = has_head

    def check_head(self):
        if self.has_head == True:
            print('homo sapiens')

    def speak(self):
        print('hello')

    def walk(self):
        print('walk')

class Patient(Human):
    medical_insurance = True

    def __init__(self, budget, has_head=True):
        self.budget = budget
        self.has_left_leg = True
        self.has_right_leg = True
        super().__init__(has_head)

    def remove_leg(self, side, price):
        if not self.medical_insurance and self.budget < price:
            print('sorry')
            return None
        if side == 'left':
            self.has_left_leg = False
        else:
            self.has_right_leg = False

        self.budget -= price

    # def check_head(self):
    #     if self.has_head == True:
    #         print('he is alive!')

patient1 = Patient(10000)
patient1.remove_leg('left', 9999)
patient1.remove_leg('right', 9999)
patient1.check_head()


