def duration_to_second(duration):
    hour, minute, second = duration.split(":")
    return int(hour) * 3600 + int(minute) * 60 + int(second)


def build_phone_log_dict(calls):
    logs = {}
    for call in calls:
        duration, phone_num = call.split(",")
        if not phone_num:
            continue
        if phone_num not in logs:
            logs[phone_num] = duration_to_second(duration)
        else:
            logs[phone_num] += duration_to_second(duration)
    return logs


def get_free_phone_number(logs):
    max_duration = 0
    free_phone_number = None
    for phone_num in logs:
        if logs[phone_num] > max_duration:
            max_duration = logs[phone_num]
            free_phone_number = phone_num
        elif logs[phone_num] == max_duration:
            if phone_num < free_phone_number:
                free_phone_number = phone_num
    return free_phone_number


def solution(S):
    calls = S.splitlines()
    if len(calls) == 0:
        return 0

    logs = build_phone_log_dict(calls)
    free_phone_number = get_free_phone_number(logs)
    amount = 0
    for call in calls:
        duration, phone_num = call.split(",")
        if not phone_num:
            continue
        if phone_num == free_phone_number:
            continue
        seconds = duration_to_second(duration)
        if seconds < 300:
            amount += 3 * seconds
        else:
            minutes = (seconds // 60) + (1 if seconds % 60 else 0)
            amount += 150 * minutes
    return amount


S = """00:01:07,400-234-090
00:05:01,701-080-080
00:05:00,400-234-090
00:01:07,300-234-090
00:03:01,888-080-080
00:05:00,300-234-090"""

print(solution(S))