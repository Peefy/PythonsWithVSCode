
class Solution:
    def solve(self, nums, M, K):
        n = len(nums)
        r = -99999
        for i in range(n - M * K):
            r = max(r, sum(nums[i: i + M * K + 1: K + 1]))
        return r

    def solve2(self, N, R, points):
        M = len(R)
        S = len(points)
        R.sort(reverse=True)
        points.sort()
        count = 0
        gap = 0
        i = 0
        while i < M:
            if count >= M:
                return -1
            if points[i] > R[count] * 2 + gap:
                count += 1 
                gap = points[i]      
            elif points[i] == R[count] * 2 + gap:
                count += 1
                i += 1
                gap = points[i]
            i += 1
        return count

def main():
    solution = Solution()
    print(solution.solve([-6, -5, -2, 0, -1], 2, 1))
    print(solution.solve([0, -5, -2, 0, -1], 2, 1))
    print(solution.solve2(10, [2, 2, 3], [0, 3, 7]))
    print(solution.solve2(12, [2, 2, 3], [0, 2, 3, 8, 12]))
    print(solution.solve2(12, [2, 4], [0, 2, 3, 8, 12]))
    print(solution.solve2(12, [2, 2, 5], [0, 2, 3, 8, 12]))
    print(solution.solve2(12, [2, 2, 3], [0, 2, 3, 8, 14]))
    print(solution.solve2(12, [3], [0, 2, 3, 8, 14]))
if __name__ == "__main__":
    main()