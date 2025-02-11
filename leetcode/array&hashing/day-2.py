
# Problem: Meeting Rooms
# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
def canAttendMeetings(intervals):
     if len(intervals) == 0:
          return True

     intervals.sort(key=lambda x: x[0]) # sort the intervals by start time
     
     for i in range(1, len(intervals)):
      
          # if the start time of the current interval is greater than or equal to the end time of the previous interval, return False to print
          if intervals[i][0] < intervals[i - 1][1]:
               return False

     return True

# print(canAttendMeetings([[0, 30], [5, 10], [15, 20]]))  # Output: False


# Problem: Meeting Rooms II
# Given an array of meeting time intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.     

def minMeetingRooms(intervals):
     if len(intervals) == 0:
          return 0

     intervals.sort(key=lambda x: x[0]) # sort the intervals by start time
     rooms = []

     for i in range(len(intervals)):
          print("i: ", i)
     
          # if the start time of the current interval is greater than or equal to the end time of the previous interval, add 1 to the rooms variable
          if len(rooms) == 0 or intervals[i][0] >= rooms[-1]:
               rooms.append(intervals[i][1])
          else:
               rooms.sort()
               rooms[0] = intervals[i][1]

     return len(rooms)

# print(minMeetingRooms([[10, 30], [5, 10], [15, 20]]))  # Output: 2


# Problem: Jump Game
# Given an array of non-negative integers nums, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you can reach the last index.
def canJump(nums):
     if len(nums) == 1:
          return True

     max_reach = 0
     for i in range(len(nums)):
          print("i: ", i)
          if i > max_reach:
               return False
          max_reach = max(max_reach, i + nums[i])
          
          print("max_reach: ", max_reach)

     return True

# print(canJump([2, 3, 1, 1, 4]))  # Output: True



def jump(nums):
     if len(nums) == 1:
          return 0

     max_reach = 0
     jumps = 0
     for i in range(len(nums)):
        
          if i > max_reach:
               return -1
          max_reach = max(max_reach, i + nums[i])
          print("max_reach: ", max_reach)
          if i == max_reach:
               jumps += 1

     return jumps

# print(jump([2, 3, 1, 1, 4]))  # Output: 2



# Problem: Merge Intervals
# Given an array of intervals where intervals[i] = [si, ei], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input. 

def merge(intervals):
     if len(intervals) == 0:
          return []

     intervals.sort(key=lambda x: x[0]) # sort the intervals by start time
     
     merged = []
     for i in range(len(intervals)):     
          if len(merged) == 0 or intervals[i][0] > merged[-1][1]:
               merged.append(intervals[i])
          else:
               merged[-1][1] = max(merged[-1][1], intervals[i][1])

     return merged



# print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # Output: [[1, 6], [8, 10], [15, 18]]


def reverseString(s):
     left = 0
     right = len(s) - 1
 
     while left < right:
          s[left], s[right] = s[right], s[left]
          print("left: ", left)
          print("right: ", right)
          left += 1
          print("left+1: ", left)
          right -= 1
          print("right-1: ", right)

     return s


# print(reverseString(["h", "e", "l", "l", "o"]))  # Output: ["o", "l", "l", "e", "h"]


