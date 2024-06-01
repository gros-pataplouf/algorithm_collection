#https://skilled.dev/course/interview-scheduler

def is_overlapping(slot1, slot2):
    if slot1["end"] > slot2["start"]:
        return True
    return False


def merge_overlapping_intervals(intervals):
    intervals.sort(key=lambda interval: interval["start"])
    merged_intervals = []
    for i in range(1, len(intervals)):
        if is_overlapping(intervals[i-1], intervals[i]):
            print("overlapping", intervals[i-1], intervals[i])
            merged_interval = {"start": intervals[i-1]["start"], "end": intervals[i]["end"] if intervals[i]["end"] > intervals[i-1]["end"] else intervals[i-1]["end"]}
            
            if merged_intervals and is_overlapping(merged_intervals[-1], merged_interval):
                    merged_intervals[-1]["end"] = merged_interval["end"]
            else:
                merged_intervals.append(merged_interval)
            
    return merged_intervals






intervals = [
  { "start": 9 , "end": 11.5 },
  { "start": 19, "end": 19.5 },
  { "start": 19.5, "end": 20.30 },
  { "start": 10 , "end": 11 },
  { "start": 20, "end": 21 },
  
  { "start": 13.5, "end": 15 }
]
print(merge_overlapping_intervals(intervals))
# [{ "start": 9, "end": 11.5 }, { "start": 13, "end": 15 }]

#solution

def merge_overlapping_intervals_solution(intervals):
    if len(intervals) == 0:
        return []

    # Sort by start time to get the meetings in the order they occur throughout the day
    intervals.sort(key = lambda x: x["start"])

    # The combined intervals array is initialized to the first meeting
    merged_intervals = [intervals[0]]

    for current_interval in intervals:
        # Get the latest end-time since they overlap and set it as the end time of the combined interval
        latest_merged_interval = merged_intervals[-1]
        is_overlapping = current_interval["start"] <= latest_merged_interval["end"]

        if is_overlapping:
            latest_merged_interval["end"] = max(current_interval["end"], latest_merged_interval["end"])
        else:
            """
            Since current_interval had the earliest start time of the remaining items,
            no additional items can overlap the latestMergedInterval interval we compared current_interval to.

            Add the current_interval as the last item to the merged interval's output since it did not overlap.
            This will be the latest merged interval on the next iteration that we compare against.
            """

            merged_intervals.append(current_interval)
            
    return merged_intervals
