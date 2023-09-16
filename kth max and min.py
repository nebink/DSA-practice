from typing import List




class Solution:
    def kth_Largest_And_Smallest_By_AscendingOrder(self, arr: List[int], k: int) -> None:
        arr.sort()
        n = len(arr)


        print(
            f"kth Largest element {arr[n - k]}, kth Smallest element {arr[k - 1]}")




if __name__ == "__main__":
    arr = [6,5,1,2,4,8]
    k=int(input("Enter the value for K"))
    Solution().kth_Largest_And_Smallest_By_AscendingOrder(arr, k)