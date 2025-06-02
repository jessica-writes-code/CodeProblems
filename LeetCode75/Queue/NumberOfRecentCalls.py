class RecentCounter:

    def __init__(self):
        self._queue = []

    def ping(self, t: int) -> int:
        self._queue.append(t)

        for i, entry in enumerate(self._queue):
            if t - 3000 <= entry:
                break

        self._queue = self._queue[i:]

        return len(self._queue)
