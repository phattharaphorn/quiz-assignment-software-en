def is_perfect_square(number):
    if number < 0:
        return False
    if number == 0:
        return True

    root = 1
    while root * root <= number:
        if root * root == number:
            return True
        root += 1
    return False

def count_perfect_square (numbers):
	
	result = 0
	for i in range(len(numbers)):
		for j in range(i+1, len(numbers)):	
			if is_perfect_square(numbers[i] + numbers[j]):
				result += 1
	return result 