# run_args: -n
# statcheck: 1 <= stats['slowpath_binop'] <= 5
def i():
    return 0

n = 10000
while n:
    n = n - 1
    i() + i()
