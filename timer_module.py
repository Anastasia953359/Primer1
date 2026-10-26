import time

class GuessTimer:

    def __init__(self):
        self._start_time = None
        self._end_time = None

    def start(self):
        self._start_time = time.perf_counter()
        self._end_time = None

    def stop(self):
        self._end_time = time.perf_counter()
        return self.elapsed()

    def elapsed(self):
        if self._start_time is None:
            return 0.0
        end = self._end_time if self._end_time is not None else time.perf_counter()
        return end - self._start_time

    @staticmethod
    def format_time(seconds):
        if seconds < 60:
            return f"{seconds:.2f} сек."
        minutes = int(seconds // 60)
        secs = seconds % 60
        return f"{minutes} мин. {secs:.2f} сек."