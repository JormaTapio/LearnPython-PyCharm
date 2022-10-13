class albhaChange:
    def __init__(self,alpha:str):
        self.alpha = alpha

    def alphaNumber(self,alpha:str):
        orderNumber = alpha.isdigit()
        while orderNumber > 10:
            orderNumber -= 10
            return orderNumber

    def alphaNumber2(self,alpha:str):
        orderNumber = ord(alpha)-96
        while orderNumber > 10:
            orderNumber -= 10
            return orderNumber

    def alphaNumber3(self,alpha:str):
        albhas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y", "z", "å", "ä", "ö"]
        orderNumber = albhas.index(alpha)
        while orderNumber > 10:
            orderNumber -= 10
            return orderNumber