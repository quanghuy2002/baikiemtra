A = [1,1,2,3,5,8,13,21,34,55,88]
B = [1,3,5,4,7,88,66,59,40,54]
C = []
for x in A:
	for s in B:
		if x == s:
			print(x)
			C.append(x)

print("List C sau khi luu tru cac so trung nhau ben list A,B: ",C)
for x in C:
	for s in B:
		if x == s:
			B.remove(s)
for x in C:
	for s in A:
		if x == s:
			A.remove(s)
print("List A sau khi xoa: ",A)
print("List B sau khi xoa: ",B)