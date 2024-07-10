def optimal_earnings(n, earnings, prev, cache):
    earnings_cache = {
        "T": 1500,
        "P": 1000,
        "C": 3000
    }

    time_cache = {
        "T": 5,
        "P": 4,
        "C": 10
    }

    keys_list = list(time_cache.keys())

    if n < 4:
        return

    for key in time_cache:
        if n >= time_cache[key]:
            time_left = n - time_cache[key]
            profits = earnings + earnings_cache[key]*time_left
            curr = list(prev)
            curr[keys_list.index(key)] += 1
            if profits not in cache:
                cache[profits] = [curr]
            else:
                cache[profits].append(curr)
            optimal_earnings(time_left, profits, curr, cache)


def main():
    prev = [0, 0, 0]
    cache = {}
    n = int(input("Input:"))
    optimal_earnings(n, 0, [0, 0, 0], cache)
    maxi = -1
    for key in cache:
        if key > maxi:
            maxi = key
    print(maxi)


if __name__ == "__main__":
    main()
