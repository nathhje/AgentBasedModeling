class StrategiesBasic():

    def __init__(self):
        self.threshold_low_price = 8
        self.threshold_high_price = 12
        self.n_time = 5

    """"Basic strategies""" #With old boolean
    def random_strat(self,history_self,history_all, stock):
        self.choice = math.floor(random.random()*2)
        if stock > 0:
            self.choice *= -1
        return self.choice

    """Choice: -1 sell, 0 do nothing, 1 buy"""
    #self.history.append(self.choice) add this to agent!
    def do_nothing_strat(self, history_self, history_all):
        self.choice = 0
        return self.choice