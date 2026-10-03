from .arithmetic import add_numbers, compound_interest, power, simple_interest, swap
from .calculator import calculator
from .comparison import is_even, max_of_three, min_of_three
from .digits import count_digits, reverse_number, sum_of_digits
from .geometry import rectangle_area_perimeter, triangle_type
from .math_helpers import decimal_to_binary, gcd, lcm, primes_up_to
from .properties import (
    factorial,
    factorial_recursive,
    factors,
    is_armstrong,
    is_palindrome,
    is_prime,
    number_type,
)
from .sequences import (
    collatz_sequence,
    even_numbers,
    fibonacci,
    list_of_nth_numbers,
    sum_of_nth_natural_number,
)

__all__: list[str] = [
    "add_numbers",
    "calculator",
    "collatz_sequence",
    "compound_interest",
    "count_digits",
    "decimal_to_binary",
    "even_numbers",
    "factorial",
    "factorial_recursive",
    "factors",
    "fibonacci",
    "gcd",
    "is_armstrong",
    "is_even",
    "is_palindrome",
    "is_prime",
    "lcm",
    "list_of_nth_numbers",
    "max_of_three",
    "min_of_three",
    "number_type",
    "power",
    "primes_up_to",
    "rectangle_area_perimeter",
    "reverse_number",
    "simple_interest",
    "sum_of_digits",
    "sum_of_nth_natural_number",
    "swap",
    "triangle_type",
]
