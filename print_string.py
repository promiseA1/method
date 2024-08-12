class Sex:
    def __init__(self , height , quality , gender):
        self.height = height
        self.quality = quality
        self.gender = gender

    def printString(self):
        print(f"{self.height} {self.quality} {self.gender}")
    

my_sex = Sex("Tall" , "Beautiful" , "Lady")
(my_sex.printString())