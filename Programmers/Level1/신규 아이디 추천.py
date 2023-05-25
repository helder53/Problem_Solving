# 2021 KAKAO BLIND RECRUITMENT
# My Solution
def solution(new_id):
    
    answer = ''
    new_id = new_id.lower()                     # 1

    for i in new_id:                            # 2
        if i.isalnum() or i in '-_.':
            answer += i

    while '..' in answer:                       # 3
        answer = answer.replace('..', '.')

    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer # 4
    answer = answer[:-1] if answer[-1] == '.' else answer
    
    answer = 'a' if answer == '' else answer                                # 5
    
    if len(answer) >= 16:                       # 6
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    if len(answer) <= 2:                        # 7
        answer = answer + answer[-1] * (3-len(answer))
        
    return answer
  
# Solution By Others
import re

def others(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st