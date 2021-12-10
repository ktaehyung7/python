def change_base(num, base):
    nums=''
    while num > 0:
        num, rest=divmod(num, base)
        nums = str(rest) + nums
    return nums