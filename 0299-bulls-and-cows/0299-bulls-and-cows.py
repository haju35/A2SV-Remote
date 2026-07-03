from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        remain_secret = []
        remain_guess = []

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                remain_secret.append(s)
                remain_guess.append(g)

        counter = Counter(remain_secret)

        cows = 0
        for ch in remain_guess:
            if counter[ch] > 0:
                cows += 1
                counter[ch] -= 1

        return f"{bulls}A{cows}B"