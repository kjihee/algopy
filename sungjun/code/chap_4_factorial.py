
# # 1부터 n까지 합 재귀
# def n_hap(n):
#     if n==1:
#         return 1
#     return n+n_hap(n-1)
#
# print(n_hap(10))


# # 팩토리얼
# def fact(n):
#     f = 1
#     for i in range(1,n+1):
#         f = f * i
#     return f
#
# print(fact(4))



# 팩토리얼 재귀
def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)

print(fact(4))


def max(x,y):                                       #큰 값 비교
    if x>y:
        return x
    else:
        return y

def find_max(list,k):                               #변수가 되는 list와 k는 리스트의 크기
                                                    #list = [10,23,467,45,1]일 때, k=5
    if k==1:                                        #종료조건
        return list[0]
    else:
        return max(list[k-1],find_max(list,k-1))

list=[10,23,467,45,1]

print(find_max(list,len(list)))
