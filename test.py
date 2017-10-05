def main(num1,num2):
	summ = summation(num1, num2)
	subb = subtraction(num1, num2)
	return subb, summ

def summation(n1, n2):
	return n1 + n2

def subtraction(n1, n2):
	return n1 - n2

main(int(input()), int(input()))
