"""
1. Filter out the names that are above 18,
try using list comp instead of filter

Output: ['BOB', 'CHARLIE']
"""

people = [('Alice', 17), ('Bob', 20), ('Charlie', 19)]

new_list = [x.upper() for x,y in people if y>18]

print(new_list)

"""
2. Sum of squares in the list

Output: 55
"""

from functools import reduce

numbers = [1, 2, 3, 4, 5]

sumOfSquares = reduce(lambda x,y: (x**2 if x==numbers[0] else x)+(y**2), numbers)
print(sumOfSquares)
#This works but python allows you to set the starting value for reduce function
#Look into that

"""
3. Find transpose using list comp only

Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
"""

matrix = [    [1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]


list2 = [[matrix[j][i] for j in range(len(matrix[0]))]for i in range(len(matrix))]

# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         list2[i][j] = matrix[j][i]

print(list2)

"""
4. Find the anagrams and group them, return list of lists

Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
"""

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(words)
temp =[]
for word in words:
    dict_ = {}
    for letters in word:
        if letters in dict_.keys():
            dict_[letters]+=1
        else:
            dict_[letters]=1
    temp.append([word, dict_])

#print(temp)

answer = []
for i in temp:
    list_=[]
    for j in temp:
        if i[1]==j[1]:
            list_.append(j[0])
            del j
    del i
    if list_ not in answer:
        answer.append(list_)

print(answer)

words = list(map(lambda x: sorted(x), words))
# Much easier method^