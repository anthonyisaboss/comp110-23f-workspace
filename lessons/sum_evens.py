"""Practice summing over lissts."""""

def sum_evens_of_list(input_list: list[int]) -> int:
    """loop over lists"""
    sum_total: int = 0
    idx: int = 0
    while idx < len(input_list):
        if input_list[idx] % 2 == 0:
            sum_total = sum_total + input_list[idx]
        idx += 1
    return sum_total