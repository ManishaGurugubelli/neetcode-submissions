class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""

        for s in strs:
            ans += str(len(s)) + "#" + s

        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i

            # Find #
            while s[j] != '#':
                j += 1

            # Get length
            length = int(s[i:j])

            # Move after #
            j += 1

            # Get the actual string
            word = s[j:j + length]
            ans.append(word)

            # Move to next string
            i = j + length

        return ans

