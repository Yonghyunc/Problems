import sys
input = sys.stdin.readline


def check(np, pt, party):
    know = False
    other = []
    for p in party:
        if p in truth:
            know = True
        else:
            other.append(p)
    if know:
        np += other
    else:
        pt.append(party)


n, m = map(int, input().split())
t, *truth = map(int, input().split())
if not t:
    print(m)
else:
    new_truth = []
    parties = []
    for _ in range(m):
        cnt, *party = map(int, input().split())
        check(new_truth, parties, party)
    truth = new_truth

    while True:
        n_tru = []
        n_party = []
        for party in parties:
            check(n_tru, n_party, party)
        parties = n_party
        truth = n_tru
        if not n_tru or not n_party:
            print(len(n_party))
            break
