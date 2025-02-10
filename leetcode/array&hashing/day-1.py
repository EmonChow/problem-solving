


def contain_duplicate(nums):

    for i in range(len(nums)):
        
        print("i: ", i)
        
        for j in range(i+1, len(nums)):
            
            print("j: ", j)
           
            if nums[i] == nums[j]:
                return True
    return False



# print(contain_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 9]))





def valid_anagram(s, t):
    if len(s) != len(t):
        return False

    char_count = {}

    for s_char in s:
  
      
        char_count[s_char] = char_count.get(s_char, 0) + 1
      
    for t_char in t:
        if t_char in char_count:
            char_count[t_char] -= 1
            if char_count[t_char] < 0:
                return False
        else:
            return False

    return all(value == 0 for value in char_count.values())

# print(valid_anagram("anagram", "nagaram"))  # Output: True


# anagram means the word is same but the order of the characters is different





def group_anagrams(strs):
    def count_key(s):
        """Create a unique key for an anagram using character frequency."""
        char_count = [0] * 26  
      
        for char in s:
            
            char_count[ord(char) - ord('a')] += 1 
            
        return tuple(char_count)  

    anagram_groups = {}

    for s in strs:
        key = count_key(s) 
    
       
        if key in anagram_groups:
          
            anagram_groups[key].append(s)
            
      
            
        else:
            anagram_groups[key] = [s]

    return list(anagram_groups.values())

# print(group_anagrams(["eat", "tea"]))






# top k frequent


def topKFrequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
        freq[count[n]].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
            
# print(topKFrequent([1, 3, 3, 2, 2, 3], 2)) 


def sum_of_two_numbers(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# print(sum_of_two_numbers([2, 7, 11, 15], 9))




def rotate_image(matrix):
    n = len(matrix)
    print("range: ", range(n // 2))
    for i in range(n // 2):
        
     
        for j in range(i, n - i - 1):
           
            temp = matrix[i][j]
          
            matrix[i][j] = matrix[n - 1 - j][i]
        
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
          
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
        
            matrix[j][n - 1 - i] = temp
          
    return matrix


print(rotate_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))