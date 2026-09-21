class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)              # set lookup is fast
        max_len = max(len(w) for w in wordDict)
        memo = {}                          # start index -> list of sentences

        def helper(start):
            if start == len(s):
                return [""]                # one way to finish: nothing left
            if start in memo:
                return memo[start]

            result = []
            for end in range(start + 1, min(len(s), start + max_len) + 1):
                word = s[start:end]
                if word in words:
                    for rest in helper(end):
                        # join word and the rest with a space, unless nothing is left
                        result.append(word + (" " + rest if rest else ""))

            memo[start] = result
            return result

        return helper(0)