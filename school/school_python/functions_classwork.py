def factorial(num):
	fact=1
	while num >= 1:
		fact=num*fact
		num = num - 1
	return fact

print(factoria(5))

def area_perimeter(length, width):
	perimeter = (2*length + 2*width)
	area = length*width
	return (f'area: {area},perimeter: {perimeter}')


