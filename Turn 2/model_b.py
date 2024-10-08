def calculate_sum(a, b):
	temp_sum = a + b
	if temp_sum > 100:  # Set a conditional breakpoint here
		breakpoint()
	result = temp_sum * 2
	return result

# Rest of the code remains the same
if __name__ == "__main__":
	num1 = 10
	num2 = 20
	final_result = calculate_sum(num1, num2)
	print("Final Result:", final_result)
