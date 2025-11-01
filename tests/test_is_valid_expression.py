from src.application.calculator.calculator_utils import is_valid_expression

def test_is_valid_expression():
	cases = [
		# Empty String
		("", False),

		# Missing components
		("89", False),
		("+", False),
		("()", False),
		("+3", False),
		("-2", False),
		("/8", False),
		("^4", False),
		("*6", False),
		("3+", False),
		("2-", False),
		("8/", False),
		("4^", False),
		("6*", False),

		# Basic Operations
		("3+2", True),
		("2*0", True),
		("1/7", True),
		("9^4", True),
		("3-2", True),
	
		# Single Operation
		("+", False),
		("-", False),
		("/", False),
		("-", False),
		("^", False),

		# Parenthesis testing
		("(+23)", False),
		("(3+)", False),
		("(1+6)+(9*3)", True),
		("1-(4*3)", True),
		("7/(2-1)", True),
		("4(8/2)", False),

		# Parenthesis count
		("(3+2)", True),
		("((3+2)", False),
		("(3+2))", False),
		("(3+2", False),
		("3+2)", False),

		# Decimal testing
		(".4+3", False),
		("5.+3", False),
		("5.2-3.1", True),
		("5..2-3.1", False),
		("(0.4^3.2)+2.9", True),
		("5+.9", False),
		("2+9.", False),

		# Complex Equations
		("2.1^2+(234.32-0)", True),
		("(1.75+0.25)*(3.14-2.9)/(0.3+(1.1^6.7))", True)
	]

	for expr, expected in cases:
		assert is_valid_expression(expr) == expected