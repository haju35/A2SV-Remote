
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact_words = set(wordlist)

        case_map = {}
        vowel_map = {}

        def devowel(word):
            word = word.lower()
            result = ""

            for char in word:
                if char in "aeiou":
                    result += "*"
                else:
                    result += char

            return result

        for word in wordlist:
            lower_word = word.lower()
            vowel_word = devowel(word)

            if lower_word not in case_map:
                case_map[lower_word] = word

            if vowel_word not in vowel_map:
                vowel_map[vowel_word] = word

        answer = []

        for query in queries:
            if query in exact_words:
                answer.append(query)

            elif query.lower() in case_map:
                answer.append(case_map[query.lower()])

            elif devowel(query) in vowel_map:
                answer.append(vowel_map[devowel(query)])

            else:
                answer.append("")

        return answer