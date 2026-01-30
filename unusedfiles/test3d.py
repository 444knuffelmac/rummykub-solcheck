layer1 = []
layer11 = []
layer111 = [1,2,3]
layer112 = [3,8]
layer12 = []
layer121 = [5,9]
layer122 = [9,2]
layer11.append(layer111)
print(layer11)
layer11.append(layer112)
print(layer11)
layer12.append(layer121)
print(layer12)
layer12.append(layer122)
print(layer12)
layer1.append(layer11)
print(layer1)
layer1.append(layer12)
print(layer1)
print(layer1[1][0][0])