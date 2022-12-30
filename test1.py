def __init__(self, name):
    self.foodapp_name = name
    self.food = {}  # self.food= {1 : {---self.item--}, 2 : {------}, 3 : {------}}
    self.foodid = len(self.food) + 1
    self.admin_details = {}
    self.user_details = {}
    self.ordered_item = []