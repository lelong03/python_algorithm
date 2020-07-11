def make_readable(seconds):
    hour = seconds // 3600
    minute = seconds % 3600
    if minute % 60 == 0:
        second = 0
    else:
        second = minute % 60
    minute = minute // 60
    return '%02d:%02d:%02d' % (hour, minute, second)

print make_readable(86399)