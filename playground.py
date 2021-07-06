# https://www.acmicpc.net/problem/15652

def find_seq(remains, pre_seq, count):
    if count == 1:
        for r in remains:
            if len(pre_seq) != 0:
                if r < pre_seq[-1]:
                    continue
            print(' '.join(map(str,pre_seq + [r])))
    else:
        for r in remains:
            if len(pre_seq) != 0:
                if r < pre_seq[-1]:
                    continue
            find_seq(remains, pre_seq+[r],count-1)

n, m = map(int, input().split())

start = [i+1 for i in range(n)]
find_seq(start,[],m)