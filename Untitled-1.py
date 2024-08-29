
def test():
   num = str(input("input the binary Number : "))
   dec = 0
   po = len(num) - 1
   for i in num:
       dec += int(i) * 2 ** po
       po -= 1
   return dec 

print(test())
