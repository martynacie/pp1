
class TV():
    def __init__(self,):
      self.ison = False
      self.channel = 1
    def turn_on(self):
        self.ison = True
    def turn_off(self):
        self.ison = False
    def show_stat(self):
        if self.ison:
            print("is on")
            print("channel is ",self.channel)
        else:
            print("is off")
    def channel_no(self, no):
        self.channel = no

tv_set = TV()
tv_set.turn_on()
tv_set.show_stat()
tv_set.channel_no(4)
tv_set.show_stat()
