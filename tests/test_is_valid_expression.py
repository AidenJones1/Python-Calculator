from src.application.calculator.calculator_utils import is_valid_expression

def test_is_valid_expression():
	assert is_valid_expression("") == False
	assert is_valid_expression("+") == False
	assert is_valid_expression("-4") == False
	assert is_valid_expression("8+") == False
	assert is_valid_expression("2-19") == True
	assert is_valid_expression("(10-5))") == False
	assert is_valid_expression("3^(2+1)") == True
	assert is_valid_expression("(5/3)+4^(9*1)") == True
	assert is_valid_expression("(9^2)/((4-1)") == False
	assert is_valid_expression("42-5+") == False
	assert is_valid_expression("(42-)") == False
	assert is_valid_expression("((((5-3))))") == True
	assert is_valid_expression("((((5-3)-1)))") == True
	assert is_valid_expression("((((5-3))*9))") == True
	assert is_valid_expression("((((5-3))))/2") == True
	assert is_valid_expression("(((8-(5-3))))") == True
	assert is_valid_expression("((1*((5-3))))") == True
	assert is_valid_expression("18+((((5-3))))") == True
	assert is_valid_expression("((((5-3))))/((((9-0))))") == True
	assert is_valid_expression("2^2^2") == True