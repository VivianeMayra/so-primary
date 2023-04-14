from cgenerator import color

class Process:
    def __init__(self, pid, burst_time):
        self.initial_burst_time = burst_time
        self.burst_time = burst_time
        self.pid = pid
        self.completion_time = 0
        self.waiting_time = 0
        self.response_time = 0
        self.return_time = 0
        self.color = color()

    def __str__(self):
        return f'P{self.pid}'

    def set_completion_time(self, ct):
        self.completion_time = ct
        
    def set_turnaround_time(self, tt):
        self.turnaround_time = tt

    def set_waiting_time(self, wt):
        self.waiting_time = wt

    def set_response_time(self, rt):
        self.response_time = rt

    def set_return_time(self, rt):
        self.return_time = rt