def solve(phone):
    import re
    digits = re.sub(r'\D', '', phone)
    return len(digits) == 10
