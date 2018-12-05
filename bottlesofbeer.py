class Song:


    def beerbottles(self, amount):
        bottles = amount
        for i in range(amount):
            if amount != 1:
                print(str(amount) + " bottles of beer on the wall, " + str(amount) + " bottles of beer! \n "
                                    "Take one down and pass it around, " + str(amount - 1) + " bottles of beer on the wall.")
                amount = amount - 1
            else:
                print(str(amount) + " bottle of beer on the wall, " + str(amount) + " bottle of beer! \n "
                                    "Take one down and pass it around, no more bottles of beer on the wall. \n"
                                    "No more bottles of beer on the wall, no more bottles of beer. \n"
                                    "Go to the store and buy some more, " + str(bottles) + " bottles of beer on the wall.")


# amount = Song()
# amount.beerbottles(99)


class Song2:


    def beerbottles2(self, amounttwo):
        def __init__(self, amounttwo):
            self.bottles = amounttwo
            self.amount = amounttwo
            for i in range(self.amount):
                if amounttwo != 1:
                    f"{self.amount} bottles of beer on the wall, {self.amount} bottles of beer! \n"
                    f"Take one down and pass it around, {self.amount-1} bottles of beer on the wall."
                    self.amount = self.amount-1
                else:
                    f"{self.amount} bottle of beer on the wall, {self.amount} bottle of beer! \n"
                    f"Take one down and pass it around, {self.amount - 1} bottles of beer on the wall."
                    f"No more bottles of beer on the wall, no more bottles of beer. \n"
                    f"Go to the store and buy some more, {self.bottles} bottles of beer on the wall."


amounttwo = Song2()
amounttwo.beerbottles2(99)
