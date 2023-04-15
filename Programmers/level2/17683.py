# [3차] 방금그곡
def solution(m, musicinfos):
    answer = "(None)"
    playtime = 0
    m = m.replace("C#", "H").replace("D#", "I").replace("F#", "J").replace("G#", "K").replace("A#", "M")
    
    for musicinfo in musicinfos:
        musicinfo = musicinfo.replace("C#", "H").replace("D#", "I").replace("F#", "J").replace("G#", "K").replace("A#", "M")
        
        start, end, title, melody = musicinfo.split(",")
        
        start_h, start_m = map(int, start.split(":"))
        end_h, end_m = map(int, end.split(":"))
        time = (end_h * 60 + end_m) - (start_h * 60 + start_m)
        
        melody = melody * (time // len(melody)) + melody[:time % len(melody)]

        if m in melody and playtime < time:
            answer = title
            playtime = time

    return answer

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))