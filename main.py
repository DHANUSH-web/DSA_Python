# Time complexity
def reverse_str(string: str) -> str:
    if len(string) <= 1:
        return string

    return reverse_str(string[1:]) + string[0]


print(reverse_str("hello"))
