# Balanced Brackets
# https://www.hackerrank.com/challenges/balanced-brackets


import sys
def is_balance(str):
    openers = "({["
    closers = ")}]"
    stack = []

    for a in str:
        if a in openers:
            stack.append(a)
        elif a in closers:
            if not len(stack):
                return False
            else:
                stack_top = stack.pop()
                balance_bracket = openers[closers.index(a)]
                if stack_top != balance_bracket:
                    return False
        else:
            return False
    return not len(stack)

t = int(raw_input().strip())
for a0 in xrange(t):
    s = raw_input().strip()
    if is_balance(s):
        print "YES"
    else:
        print "NO"
