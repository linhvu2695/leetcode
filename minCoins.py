import sys

coin_set = [156,265,40,280]

coin_dict = {}

def minCoins(coins, amount):
    if amount == 0:
        coin_dict[amount] = 0
        return 0

    if amount < min(coins):
        coin_dict[amount] = -1
        return -1

    #memoization
    if amount in coin_dict.keys():
        return coin_dict[amount]

    #initialize result to MAX INT
    res = sys.maxsize
    for i in range(len(coins)):
        #check through all valid coins
        if coins[i] <= amount:
            sub_res = minCoins(coins, amount-coins[i])

            #update if found a smaller combination (ignore invalid scenarios)
            if sub_res != -1 and sub_res + 1 < res:
                res = sub_res + 1
    #no valid scenarios found if result was never updated
    if res == sys.maxsize:
        coin_dict[amount] = -1
        return -1
    
    print(coin_dict)
    coin_dict[amount] = res
    return res


#most elegant solution
#example: best_minCoins(coins=[2,5], amount=7)
#index: 	0	1	2	3	4	5	6	7
#res array:	0	8	8	8	8	8	8	8
#update:	0	8	1	8	2	1	3	2
#								|_______|
def best_minCoins(coins, amount):
    rs = [amount+1] * (amount+1)
    rs[0] = 0
    for i in range(1, amount+1):
        for c in coins:
            if i >= c:
                rs[i] = min(rs[i], rs[i-c] + 1)

    if rs[amount] == amount+1:
        return -1
    return rs[amount]



print(best_minCoins(coin_set, 9109))
