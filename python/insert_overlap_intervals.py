

def insert_overlap_intervals(sorted_intervals, new_interval):
    """ Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6] """

    merged_intervals = []
    i, start, end = 0, 0, 1

    "get proper index of new interval by merging interval not overlapping with new interval"

    while i < len(sorted_intervals) and sorted_intervals[i][end] < new_interval[start]:

        merged_intervals.append(sorted_intervals[i])
        i+=1

    # print(merged_intervals)

    "insert new interval into specific index in merge intervals"

    while i < len(sorted_intervals) and sorted_intervals[i][start] <= new_interval[end]:
        new_interval[start] = min(sorted_intervals[i][start], new_interval[start])
        new_interval[end] = max(sorted_intervals[i][end], new_interval[end])
        i+=1

    # print(new_interval)
    "add new interval into its index"
    merged_intervals.append(new_interval)

    "copy remaining interval from sorted intervals given to merge intervals"

    while i < len(sorted_intervals):
        merged_intervals.append(sorted_intervals[i])
        i+=1
    
    return merged_intervals


print(insert_overlap_intervals([[1,3], [5,7], [8,12]], [4, 6]))

