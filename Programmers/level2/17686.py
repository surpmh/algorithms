# [3차] 파일명 정렬
import re

def solution(files):
    answer =[re.split(r"([0-9]+)", s) for s in files]

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))

    return [''.join(file) for file in answer]

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))