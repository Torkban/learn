class User:
    def __init__(self, first_name, last_name):
        self.self_first_name = first_name
        self.self_last_name = last_name
        
        
    def get_first_name(self):
        print(self.self_first_name)
        
        
    def get_last_name(self):
        print(self.self_last_name)
        
    def get_both_names(self):
        print(self.self_first_name, self.self_last_name)