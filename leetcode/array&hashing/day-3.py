# Problem: Rotate Array
# Given an array, rotate the array to the right by k steps, where k is non-negative. 
#  K is the number of steps to rotate the array to the right.
def rotate(nums, k):
     k = k % len(nums)
     
     print("k: ", k)
     print("nums[-k:]: ", nums[-k:])
     print("nums[:-k]: ", nums[:-k])
     nums[:] = nums[-k:] + nums[:-k]
     return nums

# print(rotate([1, 2, 3, 4, 5, 6, 7], 9))



def rotate2(nums, k):
     k = k % len(nums)

     def reverse(start, end):
          while start < end:
               nums[start], nums[end] = nums[end], nums[start]
               start += 1
               end -= 1

     reverse(0, len(nums) - 1)
     reverse(0, k - 1)
     reverse(k, len(nums) - 1)
     return nums

# explanation: reverse the entire array, then reverse the first k elements, and then reverse the rest of the elements.
# 1. reverse the entire array
# 2. reverse the first k elements
# 3. reverse the rest of the elements
# 4. return the array
# print(rotate2([1, 2, 3, 4, 5, 6, 7], 3))  # Output: [5, 6, 7, 1, 2, 3, 4]



def containsDuplicate(nums):
     return len(nums) != len(set(nums))

# print(containsDuplicate([1, 2, 3, 1]))  # Output: True




# Problem: Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# 1. XOR operation: XOR of a number with itself is 0. If we XOR all elements in the array, we will be left with the single number.
# 2. XOR operation: XOR of a number with 0 is the number itself. If we XOR all elements in the array, we will be left with the single number.
# 3. XOR operation: XOR of two same numbers is 0. If we XOR all elements in the array, we will be left with the single number.

def singleNumber(nums):
     result = 0
     for num in nums:
          result ^= num # XOR operation
   
          
     return result

# print(singleNumber([2, 2, 1]))  # Output: 1




# Problem: Intersection of Two Arrays
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
def intersection(nums1, nums2):
     return list(set(nums1) & set(nums2))

# print(intersection([1, 2, 2, 1], [1, 3]))  # Output: [2]



# <__main__.ListNode object at 0x0000018C129174D0> is the memory address of the object. 
# The object is an instance of the ListNode class.
# The object is a linked list.

class ListNode:
     def __init__(self, val=0, next=None):
          self.val = val
          self.next = next
          
def singleLinkedList(nums):
     head = None
     for num in nums:
          node = ListNode(num)
          print("node: ", node)
          node.next = head
          
          head = node
     return head



# print(singleLinkedList([1, 2, 3, 4, 5]))  # Output: <__main__.ListNode object at 0x7f8b1c1b5d30>


# Problem: Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# 1. Create a stack variable that will store the elements.
# 2. Create a push function that will add an element to the stack.
# 3. Create a pop function that will remove an element from the stack.
# 4. Create a min function that will return the minimum element in the stack.
def MinStack():
     stack = []

     def push(val):
          stack.append(val)

     def pop():
          return stack.pop() if stack else None

     return push, pop

push, pop= MinStack()

push(3)
push(2)
push(1)

# print(pop())  # Output: 1







# Problem: Best Time to Buy and Sell Stock II
# You are given an array prices where prices[i] is the price of a given stock on the ith day. Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
def maxProfit(prices):
     profit = 0
     for i in range(1, len(prices)):
          if prices[i] > prices[i - 1]:
               profit += prices[i] - prices[i - 1]
     return profit

# print(maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 7



def binarySearch(nums, target):
     left = 0
     right = len(nums) - 1
     while left <= right:
          mid = (left + right) // 2
       
          
          if nums[mid] == target:
               return mid
          elif nums[mid] < target:
               left = mid + 1
          else:
               right = mid - 1
     return -1

# print(binarySearch([-1, 0, 3, 5, 9, 12], 9))  # Output: 4



# Problem: Search in Rotated Sorted Array
# There is an integer array nums sorted in ascending order (with distinct values). Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
def searchMatrix(matrix, target):
     m = len(matrix)
     print("m: ", m)
     n = len(matrix[0])
     print("n: ", n)
     left = 0
     right = m * n - 1
     
     print("right: ", right)
     while left <= right:
          mid = (left + right) // 2
          mid_element = matrix[mid // n][mid % n]
          if mid_element == target:
               return True
          elif mid_element < target:
               left = mid + 1
          else:
               right = mid - 1
     return False


print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))  # Output: True
