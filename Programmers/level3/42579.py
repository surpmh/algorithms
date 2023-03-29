# 베스트앨범
def solution(genres, plays):
    answer = []
    total = {}
    dict = {}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre in total:
            total[genre] += play
            dict[genre].append([play, i])
        else:
            total[genre] = play
            dict[genre] = [[play, i]]

    total = sorted(total.items(), key = lambda x: x[1], reverse=True)
    
    for genre in total:
        list = sorted(dict[genre[0]], key=lambda x: x[0], reverse=True)
        for i in range(len(list)):
            answer.append(list[i][1])
            if i == 1:
                break

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))