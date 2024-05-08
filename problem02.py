from collections import deque


def main_problem_02():
    msg = input()
    apd = [" "] * len(msg)
    stk = deque()
    msg_len = len(msg)
    for i in range(msg_len):
        if '(' == msg[i]:
            stk.append(i)
        elif ')' == msg[i]:
            if len(stk) > 0:
                stk.pop()
            else:
                apd[i] = '?'
    while len(stk) > 0:
        idx = stk.pop()
        apd[idx] = 'x'
    print(msg)
    print(''.join(apd))


main_problem_02()
