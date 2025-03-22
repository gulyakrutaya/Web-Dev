n = int(input())
scores = list(map(int, input().split()))

unique_scores = sorted(set(scores))

runner_up = unique_scores[-2]

print(runner_up)
