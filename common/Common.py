
# 是否素数
def sushu(i):
    if i == 1:
        return False
    for num in range(2, i):
        if i % num == 0:
            return False
    else:
        return True


print(sushu(7))