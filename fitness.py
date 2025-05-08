from dateutil import parser
class workout(object):
    def __init__(self,start,end,calories = None):
        self.start = parser.parse(start)
        self.end = parser.parse(end)
        self.calories = calories
        self.icon = '😥'
        self.kind = 'workout'
    def get_calories(self):
        if (calories == None):
            return workout.cal_per_hr*(self.end - self.start).total_seconds()/3600
        else:
            return self.calories
    def get_start(self):
        return self.start
    def get_end(self):
        return self.end
    def set_calories(self,calories):
        self.calories = calories
    def set_start(self,start):
        self.start = start
    def set_end(self, end):
        self.end = end
start = '5/8/2025 7:26 PM'
end = '5/10/2025 7:26 PM'
start_date = parser.parse(start)
end_date = parser.parse(end)
type(start_date)