class Solution:
    def palindromePairs(self, words):
        def isPal(s):
            return s == s[::-1]

        pos = {w: i for i, w in enumerate(words)}
        ans = []

        for i, word in enumerate(words):
            m = len(word)

            for j in range(m + 1):
                left = word[:j]
                right = word[j:]

                # reverse(right) + word
                if isPal(left):
                    rev = right[::-1]
                    if rev in pos and pos[rev] != i:
                        ans.append([pos[rev], i])

                # word + reverse(left)
                # j != m avoids duplicate when right is ""
                if j != m and isPal(right):
                    rev = left[::-1]
                    if rev in pos and pos[rev] != i:
                        ans.append([i, pos[rev]])

        return ans