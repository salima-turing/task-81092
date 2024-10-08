import pdb

def calculate_sum(a, b):
	if a == 0 or b == 0:
		pdb.set_trace()  # Set a conditional breakpoint here
	temp_sum = a + b
	result = temp_sum * 2
	return result

if __name__ == "__main__":
	num1 = 0
	num2 = 0
	final_result = calculate_sum(num1, num2)
	print("Final Result:", final_result)
