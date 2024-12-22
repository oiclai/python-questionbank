kmLargura, kmComprimento, moedasExtras = map(int, input().split())

while moedasExtras > 0:
    if kmLargura <= kmComprimento:
        kmLargura += 1
    else:
        kmComprimento += 1
    moedasExtras -= 1

print(kmLargura * kmComprimento)




# 2 3 9
# 3 * 4 = 12 | 7
# 4 * 5 = 20 | 5
# 5 * 6 = 30 | 3
# 6 * 7 = 42 | 1
# 7 * 7 = 49 | 0
