def count_evens(start, end):
    # By using `while` loop calculate even numbers from `start` to `end`.
    # `start` and `end` are included.
    # Example:
    # >>> count_evens(1, 4)
    # 2
    result = 0
    # --> Add code here
    while (start +1) < end:
        result +=1
        start +=1
    return result

print(count_evens(1,1))
