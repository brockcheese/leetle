def solve(arr):
    from collections import Counter
    count = Counter(arr)
    lucky = [n for n in count if count[n] == n]
    return max(lucky) if lucky else -1