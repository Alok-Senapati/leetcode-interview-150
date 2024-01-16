class Solution:
    def climbStairs(self, n: int) -> int:
        no_of_ways = [0] * (n + 1)
        no_of_ways[0] = 1
        no_of_ways[1] = 1
        for i in range(2, n + 1):
            no_of_ways[i] = no_of_ways[i - 1] + no_of_ways[i - 2]
        return no_of_ways[n]


if __name__ == '__main__':
    print(Solution().climbStairs(5))