ten = input("Nhập tên của bạn: ");
print(ten);
print("Độ dài tên: ",len(ten.replace(' ','')));
n = len(ten.replace(' ',''));
tong = 0;
while(n>0):
	tong = tong + n%10;
	n = int(n / 10);
print("Tổng các chữ số: ",tong)