class Employee:
    def __init__(self, first_name, last_name, avail_start, avail_end):
        self.first_name = first_name
        self.last_name = last_name
        self.avail_start = avail_start
        self.avail_end = avail_end
    
    def set_first_name(self, name):
        self.first_name = name

    def set_last_name(self, name):
        self.last_name = name

    def set_avail_start(self, start_time):
        self.avail_start = start_time

    def set_avail_end(self, end_time):
        self.avail_end = end_time
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name

    def get_avail_start(self):
        return self.avail_start

    def get_avail_end(self):
        return self.avail_end