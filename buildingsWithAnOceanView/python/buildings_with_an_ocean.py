from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_height = heights[-1]

        buildings = [len(heights) - 1]

        for index, height in enumerate(heights[::-1]):
            if height > max_height:
                max_height = height
                buildings.append(len(heights) - index - 1)

        return buildings[::-1]


if __name__ == "__main__":
    heights = [4, 2, 3, 1]
    print(Solution().findBuildings(heights))
