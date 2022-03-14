def solution(fees, records):
    def cal_time(in_time, out_time):
        time_minute = 0
        in_hour, in_minute = map(int,in_time.split(':'))
        out_hour, out_minute = map(int,out_time.split(':'))
        return (out_hour - in_hour) * 60 + out_minute - in_minute
    answer = []
    log = {}
    for record in records:
        time, num, direction = record.split()
        if direction == "IN":
            if num in log:
                log[num][2] += cal_time(log[num][0], log[num][1])
                log[num][0], log[num][1]= time, ""
            else:
                log[num] = [time, "", 0]
        elif direction == "OUT":
            log[num][1] = time
        
    def cal_fee(time, fees):
        fee = fees[1]
        time -= fees[0]
        if time > 0:
            q, r = divmod(time, fees[2])
            fee += q * fees[3]
            if r:
                fee += fees[3]
        return fee
        
    for _, value in sorted(log.items()):
        if not value[1]:
            answer.append(cal_fee(cal_time(value[0], "23:59") + value[2], fees))
        else:
            answer.append(cal_fee(cal_time(value[0], value[1]) + value[2], fees))
    return answer