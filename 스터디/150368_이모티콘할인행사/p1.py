import itertools


def solution(users, emoticons):
    num = len(emoticons)
    percents = [40, 30, 20, 10]
    # 중복 순열
    discounts = list(itertools.product(percents, repeat=len(emoticons)))
    max_users = 0
    max_costs = 0
    for discount in discounts:
        now_users = 0
        now_costs = 0
        for user in users:
            sum_costs = 0
            for i in range(num):
                if discount[i] >= user[0]:
                    sum_costs += emoticons[i] * ((100 - discount[i]) / 100)
                if sum_costs >= user[1]:
                    now_users += 1
                    break
            else:
                now_costs += sum_costs

                
        if now_users > max_users:
            max_users = now_users
            max_costs = now_costs
        elif now_users == max_users:
            max_costs = max(now_costs, max_costs)
        # print('변경', max_users, max_costs)


    answer = [max_users, int(max_costs)]

    return answer









print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))