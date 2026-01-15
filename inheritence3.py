class bird:
    def __init__(self):
        print("bird is ready")

        def whoisthis(self):
            print("bird")
        
        def swim(self):
            print("swim faster")

class penguine(bird):
    def __init__(self):
        super().__init__()
        print("Penguine is ready")

    def whoisthis(self):
        print("penguine")
    def run(self):
        print("run faster")
peggy=penguine()
peggy.whoisthis()
peggy.swim()
peggy.run()