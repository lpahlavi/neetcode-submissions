class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Idea: greedy
        # Idea: schedule task that occurs most often as soon as possible
        # Idea: min-heap, pop the next element with largest count
        counts = Counter(tasks)
        max_count = max(counts.values())
        num_max_count = len([count for count in counts.values() if count == max_count])
        return max(len(tasks), (max_count - 1) * (n + 1) + num_max_count)