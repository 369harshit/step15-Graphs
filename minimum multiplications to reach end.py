from collections import deque
class Solution:
    def minimumMultiplications(self, arr, start, end):
        # Create a queue for storing the numbers as a result of multiplication
        # of the numbers in the array and the start number.
        q = deque([(start, 0)])

        # Create a dist array to store the no. of multiplications to reach
        # a particular number from the start number.
        dist = [float('inf')] * 100000
        dist[start] = 0
        mod = 100000

        # Multiply the start no. with each of the numbers in the arr
        # until we get the end no.
        while q:
            node, steps = q.popleft()

            for i in arr:
                num = (i * node) % mod

                # If the no. of multiplications are less than before
                # in order to reach a number, we update the dist array.
                if steps + 1 < dist[num]:
                    dist[num] = steps + 1

                    # Whenever we reach the end number
                    # return the calculated steps
                    if num == end:
                        return steps + 1
                    q.append((num, steps + 1))

        # If the end no. is unattainable.
        return -1

# Driver Code
start = 3
end = 30
arr = [2, 5, 7]

obj = Solution()
ans = obj.minimumMultiplications(arr, start, end)
print(ans)
