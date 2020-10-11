from datetime import datetime
import time

play_time = "50:00:00"
adv_time ="50:00:00"
logs =["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]

def calc_time(start,end):
    end_sec = int(end[0]) * 3600 + int(end[1]) * 60 + int(end[2])
    start_sec = int(start[0]) * 3600 + int(start[1]) * 60 + int(start[2])
    return end_sec-start_sec

    if play_time == adv_time:
        return "00:00:00"

stack = list()
logs_list = list()
for log in logs:
    split_idx = log.index("-")
    start = log[:split_idx]
    end = log[split_idx+1:]
    logs_list.append([list(map(str,start.split(':'))),True])
    logs_list.append([list(map(str,end.split(':'))),False])
logs_list = sorted(logs_list)

cum_list = list()
for i in range(len(logs_list)):
    is_start = logs_list[i][1]
    if is_start == True:  # 시작점
        stack.append(logs_list[i])
    elif is_start == False:
        start_time = stack[-1][0]
        end_time = logs_list[i][0]
        cumsum = calc_time(start_time,end_time) * len(stack)
        stack.pop()
        cum_list.append([cumsum, ":".join(start_time)])

cum_list = sorted(cum_list, reverse=True)
maximum = cum_list[0][0]
res_time = cum_list[0][1]
for i in range(1,len(cum_list)):
    if maximum <= cum_list[i][0] and res_time > cum_list[i][1]:
        res_time = cum_list[i][1]
    else:
        break

