
class Interval:

    def __init__(self, start=None, end=None):

        self.start = start
        self.end = end

def merge_overlap_intervals(intervals):

    result = []
    intervals.sort(key=lambda x:x.start)

    start = intervals[0].start
    end = intervals[0].end


    for i in range(1, len(intervals)):
        interval = intervals[i]

        if interval.start <= end:
            end =  max(interval.end, end)
        else:
            new_interval = Interval(start, end)
            result.append(new_interval)
            start = interval.start
            end = interval.end

    new_interval = Interval(start, end)
    result.append(new_interval)

    return result
    
result = merge_overlap_intervals([Interval(5, 7), Interval(4, 10), Interval(8, 12)])
# result = result.remove(result[len(result)-1])
for res in result:

    print(f"{res.start} -> {res.end}")




