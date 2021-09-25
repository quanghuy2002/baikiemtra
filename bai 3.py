print("Nhập giá trị n: ",end='')
n=int(input())
if n > 0:
    giaithua=1
    for i in range(1,n+1):
        giaithua=giaithua*i
    print(n,"giai thừa bằng:",giaithua)
else:
    print("Vui lòng nhập n > 0")