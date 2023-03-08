if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = sorted(list(set(arr)), reverse=True)
    runner_up_score = arr[1]

print(runner_up_score)



