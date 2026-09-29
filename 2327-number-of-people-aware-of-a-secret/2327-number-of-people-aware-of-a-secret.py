class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7

        # dp[i] = number of people who learn the secret on day i
        dp = [0] * (n + 1)
        dp[1] = 1

        # Number of people who can currently share the secret
        sharers = 0

        for day in range(2, n + 1):

            # People who learned `delay` days ago can start sharing
            if day - delay >= 1:
                sharers += dp[day - delay]
                sharers %= MOD

            # People who learned `forget` days ago forget today
            # and can no longer share.
            if day - forget >= 1:
                sharers -= dp[day - forget]
                sharers %= MOD

            # Every active sharer tells one new person
            dp[day] = sharers

        # Count people who still remember the secret on day n
        answer = 0

        for day in range(max(1, n - forget + 1), n + 1):
            answer += dp[day]
            answer %= MOD

        return answer
