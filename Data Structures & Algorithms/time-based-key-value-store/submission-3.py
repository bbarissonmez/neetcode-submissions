class TimeMap:

    def __init__(self):
        self.tmap = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values_list = self.tmap.get(key, [])

        l = 0
        r = len(values_list) - 1
        res = ""

        while (l <= r):
            mid = l + (r - l) // 2

            if values_list[mid][0] <= timestamp:
                l = mid + 1
                res = values_list[mid][1]
            else:
                r = mid - 1
        
        return res