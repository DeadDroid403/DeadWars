#! /usr/bin/env python3
from src import decorations as dc , lastchar, asking

class DeadWords:
    def __init__(self):
        self.game = 0
        self.ch_one = 0
        self.ch_two = 0
        self.ch_three = 0

    def menu(self):
        dc.logo()
        dc.rocket()
        self.ch_one = asking.firstmenu()
        dc.rocket()
        if self.ch_one == 1:
            self.ch_two = asking.secondmenu()
            dc.rocket()
            if self.ch_two == 1:
                self.ch_three = asking.thirdmenu()
                lastchar.last_char_single(self.ch_three)
            elif self.ch_two == 2:
                self.ch_three = asking.thirdmenu()
                lastchar.Last_char(self.ch_three)


if __name__ == '__main__':
        obj = DeadWords()
        obj.menu()
        