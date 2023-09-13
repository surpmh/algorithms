# 여행경로
def solution(tickets):
    answer = []
    tickets.sort()
    visited = [False] * len(tickets)

    def dfs(departure, pathway):
        if len(pathway) == len(tickets)+1:
            answer.append(pathway)
            return

        for idx, ticket in enumerate(tickets):
            if ticket[0] == departure and not visited[idx]:
                visited[idx] = True
                dfs(ticket[1], pathway+[ticket[1]])
                visited[idx] = False

    dfs('ICN', ['ICN'])
    return answer[0]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))