# 2023 KAKAO BLIND RECRUITMENT
# My Solution
def solution(today, terms, privacies):
    result = []

    for i in range (len(privacies)):
        date = privacies[i].split()[0].split(".")
        alp = privacies[i].split()[1]

        year = int(date[0])
        month = int(date[1])
        day = int(date[2])
        
        cnt = 0
        for t in terms:
            if t[0] == alp:
                d = int(t.split(" ")[1])
                cnt = d * 28
                continue
        cnt += int(day)-1
        month += cnt // 28
        day = cnt % 28

        if day == 0:
            day = 28
            month -= 1

        if month > 12:
            print(month)
            if (month%12==0):
                year += (month-1) // 12
                month = month - (12 * ((month-1)//12))
            else:
                year += month // 12
                month = month - (12 * (month//12))


        to_date = today.split(".")
        if int(to_date[0]) > year:
            result.append(i+1)
            continue
        elif int(to_date[0]) == year:
            if int(to_date[1]) > month:
                result.append(i+1)
                continue
            elif int(to_date[1]) == month:
                if int(to_date[2]) > day:
                    result.append(i+1)
                    continue

    return result
  
# Solution By Others
def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def others(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    answer = [
        i + 1 for i, j in enumerate(privacies)
        if to_days(j[:-2]) + months[j[-1]] <= today
    ]
    return answer