


def getMoneySpent(keyboards, drives, b):
     # keyboards is a list of integers containing the prices of each keyboard
     # drives is a list of integers containing the prices of each drive
     # b is the budget
     # return the maximum amount of money that can be spent on a keyboard and a drive
     # max_value = -1 means no combination of keyboard and drive can be bought with the budget
     max_value = -1
     for keyboard in keyboards:
          print('keyboard:', keyboard)
          for drive in drives:
               print('drive:', drive)
               if keyboard + drive <= b and keyboard + drive > max_value:
                    print('keyboard + drive:', keyboard + drive)
                    max_value = keyboard + drive
     return max_value


print(getMoneySpent([1, 2, 3], [1, 2, 8], 11))