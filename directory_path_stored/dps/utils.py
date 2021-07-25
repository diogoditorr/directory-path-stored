def calculate_max_width(iterable: list[str]) -> int:
    max_width = 0

    for item in iterable:
        if len(item) > max_width:
            max_width = len(item)

    return max_width


# It will receive a list of strings. Return the max number of characters found.
# def calculate_max_width(iterable: list[str]) -> int:
#     """
#     Calculate the maximum width of the given string.
#     :param iterable: list[str]
#     :return: int
#     """
#     max_width = 0
#     for string in iterable:
#         max_width = max(max_width, len(string))
#     return max_width