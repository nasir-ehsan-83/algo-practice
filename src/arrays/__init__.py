from .advanced import kth_largest, max_subarray_sum, top_k_freq
from .basics import (
    largest_element,
    largest_smallest,
    second_largest,
    smallest_element,
    sum_elements,
)
from .compare import arr_eq
from .intervals import intersection, merge_intervals
from .matrix import multiply_matrix, set_zeroes
from .rearrange import is_rotation, rearrange_even_odd, rotate_right
from .search import contains, count_occurrences, find_missing_number
from .unique import is_unique, remove_duplicates, unique_elements

__all__: list[str] = [
    "arr_eq",
    "contains",
    "count_occurrences",
    "find_missing_number",
    "intersection",
    "is_rotation",
    "is_unique",
    "kth_largest",
    "largest_element",
    "largest_smallest",
    "max_subarray_sum",
    "merge_intervals",
    "multiply_matrix",
    "rearrange_even_odd",
    "remove_duplicates",
    "rotate_right",
    "second_largest",
    "set_zeroes",
    "smallest_element",
    "sum_elements",
    "top_k_freq",
    "unique_elements",
]
