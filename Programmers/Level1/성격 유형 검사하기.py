# 2022 KAKAO TECH INTERNSHIP
# My Solution
def solution(survey, choices):
    result = "RCJA"
    dic = {'R': 0, 'T' : 0, 'C' : 0, 'F' : 0,
           'J': 0, 'M' : 0, 'A' : 0, 'N' : 0 }

    for i in range(len(choices)):
        if (choices[i] == 4):
            continue
        elif (choices[i] > 4):
            dic[survey[i][1]] += choices[i]-4
        else:
            dic[survey[i][0]] += 4-choices[i]
    if dic["R"] < dic["T"]:
        result = result.replace("R", "T")
    if dic["C"] < dic["F"]:
        result = result.replace("C", "F")
    if dic["J"] < dic["M"]:
        result = result.replace("J", "M")
    if dic["A"] < dic["N"]:
        result = result.replace("A", "N")    

    return result

# Solution By Others
def others(survey, choices):
    dict = {"RT":0,"CF":0,"JM":0,"AN":0}
    
    for i, j in zip(survey, choices):
        if i not in dict.keys():
            i = i[::-1]
            dict[i] -= j-4
        else:
            dict[i] += j-4
    
    result = ""
    for i in dict.keys():
        if dict[i] > 0:
            result += i[1]
        elif dict[i] < 0:
            result += i[0]
        else:
            result += sorted(i)[0]
    return result
  
