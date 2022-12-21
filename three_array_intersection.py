# 三个数组的交集
a = [1,2,4,9, 15, 18]
b = [3,5,9,10, 18]
c = [2,4,9,11,15, 18]

# 交集
elements = []

# 三个数组计算交集
index_a = 0
index_b = 0
index_c = 0
print(index_a, index_b, index_c)

# 如果长度不到pass, 则持续
while index_a < len(a) and index_b < len(b) and index_c < len(c):
#   如果相等
    if a[index_a] == b[index_b] and a[index_a]== c[index_c]:
        elements.append(a[index_a])
        index_a += 1
        index_b += 1
        index_c += 1
    else:
        max_element = max([a[index_a], b[index_b], c[index_c]])
#         print(max_element)
#       均匀累加
        while index_a < len(a) and a[index_a] < max_element:
            index_a += 1
        
        while index_b < len(b) and b[index_b] < max_element:
            index_b += 1
            
        while index_c < len(c) and c[index_c] < max_element:
            index_c += 1   

print(elements)
