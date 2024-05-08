def is_sub_seq(src, sub):
    i, j = 0, 0
    src_len = len(src)
    while i < src_len:
        if j == len(sub):
            break
        if src[i] == sub[j]:
            j += 1
        i += 1
    return j == len(sub)


def min_concat_sub_seq(src, tgt):
    if len(tgt) < 1:
        return 0
    end_idx = len(tgt)
    is_find = False
    while end_idx >= 1:
        sub = tgt[: end_idx]
        if is_sub_seq(src=src, sub=sub):
            is_find = True
            break
        end_idx -= 1
    if is_find:
        return 1 + min_concat_sub_seq(src, tgt[end_idx:])
    else:
        raise Exception("ERROR: The task is impossible")


def main_problem_01():
    source = input()
    target = input()

    try:
        cnt = min_concat_sub_seq(src=source, tgt=target)
        print(cnt)
    except Exception as _:
        print(-1)


main_problem_01()
