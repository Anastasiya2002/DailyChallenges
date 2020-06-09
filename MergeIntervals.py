#Given a collection of intervals, merge all overlapping intervals.

def merge(intervals):
    previous = intervals[0]
    result = []
    for i in intervals:
        if i[0] <= previous[1]:
            result = result[:-1]
            result.append([min(previous +i), max(previous +i)])
        else:
            result.append(i)
    return result

print(merge([[1,4],[4,5]]))
print(merge([[1,3],[2,6],[8,10],[15,18]]))

