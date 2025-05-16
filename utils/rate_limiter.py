import time
from datetime import datetime
from collections import deque


class RateLimiter:
    def __init__(self, max_tokens_per_minute=4_000_000, max_requests_per_minute=5000):
        self.token_log = deque()
        self.request_log = deque()
        self.max_tokens = max_tokens_per_minute
        self.max_requests = max_requests_per_minute
        self.last_report_time = time.time()

    def _prune(self, log):
        now = datetime.utcnow()
        while log and (now - log[0][1]).total_seconds() > 60:
            log.popleft()

    def can_send(self, tokens):
        self._prune(self.token_log)
        self._prune(self.request_log)

        token_used = sum(t for t, _ in self.token_log)
        req_count = len(self.request_log)

        now = time.time()
        if now - self.last_report_time > 5:
            print(f"📊 Used: {token_used:,} tokens / {req_count} requests in last 60s")
            print(f"🔄 Remaining: {self.max_tokens - token_used:,} tokens | {self.max_requests - req_count} requests")
            self.last_report_time = now

        return (
            token_used + tokens <= self.max_tokens and
            req_count < self.max_requests
        )

    def consume(self, tokens):
        now = datetime.utcnow()
        self.token_log.append((tokens, now))
        self.request_log.append((1, now))