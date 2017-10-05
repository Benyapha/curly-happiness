def main(num1,num2):
	summ = summation(num1, num2)
	subb = subtraction(num1, num2)
	return subb, summ

def subtraction(n1, n2):
	return n1 - n2

def summation(n1, n2):
	return n1 + n2

def test():
	print('giveeiei')

main(int(input()), int(input()))
