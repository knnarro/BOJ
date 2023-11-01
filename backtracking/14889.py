import sys
input = sys.stdin.readline

n = int(input())
s = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    s[i] = list(map(int, input().split()))

team_start = [0] # 스타트팀에는 0번째 선수가 항상 있는 것으로 가정
answer = 1e10

def get_total_ability(team):
    total_ability = 0
    for i in range(1, len(team)):
        for j in range(0, i+1):
            total_ability += s[team[i]][team[j]]
            total_ability += s[team[j]][team[i]]
    return total_ability

def get_team_link(team_start):
    team_link = []
    for member in range(0, n):
        if member not in team_start:
            team_link.append(member)
    return team_link

def dfs(depth, start):
    global team_start, team_link, answer

    if depth >= (n//2):
        team_link = get_team_link(team_start)
        gap = abs(get_total_ability(team_start)-get_total_ability(team_link))
        if gap < answer:
            answer = gap
        return

    for member in range(start, n):
        if member not in team_start:
            team_start.append(member)
            dfs(depth+1, member+1)
            team_start = team_start[:-1]

dfs(1, 1)
print(answer)