class MathDojo:
    def __init__(self):
        self.result = 0

    def sumar(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self

    def restar(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self



# crear una instancia:
md = MathDojo()

""" x = md.sumar(2, 3).result
print(x)  # Imprimirá 5 

x = md.sumar(4, 5, 6).result
print(x)  # Imprimirá 20 

x = md.sumar(1, 2, 3, 4, 5).result
print(x)  # Imprimirá 35  """


x = md.restar(2, 3).result
print(x)  # Imprimirá -5 (-2 - 3)

x = md.restar(4, 5, 6).result
print(x)  # Imprimirá -20 (-5 - 4 - 5 - 6)

x = md.restar(1, 2, 3, 4, 5).result
print(x)  # Imprimirá -35 (-20 - 1 - 2 - 3 - 4 - 5)




md = MathDojo()

x = md.sumar(2).restar(1, 3).sumar(5).result
print(x)  # Imprimirá 3 (0 + 2 - 1 - 3 + 5)
