


def angryProfessor(k, a):
     
     
     # a is a list of integers containing the arrival time of each student
     # k is the minimum number of students required to start the class
     # if the number of students who arrived on time is less than k, the class is cancelled
     # return "YES" if the class is not cancelled, otherwise return "NO"
     
     count = 0
     for i in range(len(a)):
          if a[i] <= 0:
               count += 1
     return "NO" if count >= k else "YES"


# [-1, -3, 4, 2] => 2 students arrived on time, 2 < 3, so the class is cancelled
# [0, -1, 2, 1] => 2 students arrived on time, 2 >= 2, so the class is not cancelled
#[-1, -3, 4, 2, 0 ] => 3 students arrived on time, 3 >= 3, so the class is not cancelled
# test cases
# print(angryProfessor(3, [-1, -3, 4, 2])) # YES
# print(angryProfessor(2, [0, -1, 2, 1])) # NO 
# print(angryProfessor(3, [-1, -3, 4, 2, 0])) # YES




def designerPdfViewer(h, word):
     # h is a list of integers containing the heights of each letter of the alphabet
     # word is a string containing the word to be typed
     # return the height of the tallest letter in the word
     
     
     # create a dictionary to store the height of each letter
     # create a variable to store the height of the tallest letter
     # loop through the word
     # get the height of the letter from the dictionary
     # update the height of the tallest letter if the current letter is taller
     # return the height of the tallest letter
     # 97 `a` to 122 `z`
     # h[0] = height of `a`
     # h[1] = height of `b`
     # h[i - 97] = height of `i`
     # h[25] = height of `z`
     height = {}
     for i in range(97, 123):
          
       
          height[chr(i)] = h[i - 97]
     tallest = 0
     for letter in word:
          if height[letter] > tallest:
               tallest = height[letter]
     return tallest

# test cases
# print(designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], "gadj"))




