class User:
    def __init__(self):
        self.pos = 0
        self.progress = 0
        self.rankArr = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
        self.rank = self.rankArr[self.pos]

    def inc_progress(self, lv):
        idx = self.rankArr.index(lv)
        if idx == self.pos:
            self.progress += 3
        elif idx < self.pos:
            if abs(idx-self.pos) == 1:
                self.progress += 1
        else:
            self.progress += 10 * abs(idx-self.pos) ** 2
            
        if self.progress >= 100:
            self.pos += self.progress // 100
            self.progress = self.progress % 100
        if self.pos >= 15:
            self.pos = 15
            self.progress = 0
        self.rank = self.rankArr[self.pos]
