n = int(input("Nhập n: "))
s = 0
n = abs(n)
while n > 0:
	s = s + n % 10
	n = int(n / 10)
print("Tổng các chữ số là: ",s)
