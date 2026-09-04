class TimeMap:

    def __init__(self):
        self.time_based_ds = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_based_ds:
            self.time_based_ds[key] = []

        self.time_based_ds[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_based_ds:
            return ""

        values = self.time_based_ds[key]

        left = 0
        right = len(values) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2

            if values[mid][0] <= timestamp:
                result = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return result
