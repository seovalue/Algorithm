def solution(name_list):
    for i in range(len(name_list)):
        size = len(name_list[i])
        for j in range(i+1, len(name_list)):
            if len(name_list[j]) == size:
                if name_list[i] == name_list[j]:
                    return True
            elif len(name_list[j]) > size:
                if name_list[i] in name_list[j]:
                    return True
    else:
        return False

name_list = ["너굴","너a","굴b","Aa너a굴"]
#name_list = ["Ab", "aa", "bb", "Aa"]
if solution(name_list) == True:
    print("True")
else:
    print("False")