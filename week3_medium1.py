# Simple Text Editor
# https://www.hackerrank.com/challenges/simple-text-editor/submissions/code/27813575

s = ""
stack = []

Q = int(raw_input())
for i in range(0, Q):
    operation = raw_input().split()
    # append
    if operation[0] == "1":
        # append empty string to stack
        # append current string to keep track for undo()
        stack.append(s)
        s += operation[1]

    # delete
    elif operation[0] == "2":
        # append current string to keep track for undo()
        stack.append(s)
        s = s[:len(s)-int(operation[1])]

    # print
    elif operation[0] == "3":
        print s[int(operation[1])-1]

    # undo
    elif operation[0] == "4":
        s = stack.pop()
