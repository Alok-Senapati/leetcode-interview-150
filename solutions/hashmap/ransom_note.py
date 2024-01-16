import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counter = collections.Counter(magazine)
        for c in ransomNote:
            if not magazine_counter.get(c) or magazine_counter.get(c) <= 0:
                return False
            magazine_counter[c] -= 1
        return True


if __name__ == '__main__':
    print(Solution().canConstruct("aabbc", "aabc"))
    print(Solution().canConstruct("aabbc", "aacbb"))