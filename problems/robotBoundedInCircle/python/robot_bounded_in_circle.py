class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: 0(1)
    """
    def isRobotBounded(self, instructions: str) -> bool:
        # north -> east -> south -> west
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        x = y = 0
        index = 0

        for instruction in instructions:
            if instruction == "R":
                index = (index + 1) % 4
            elif instruction == "L":
                index = (index + 3) % 4
            else:
                x += directions[index][0]
                y += directions[index][1]

        # back to the original point or not face north
        return (x == 0 and y == 0) or index != 0


if __name__ == "__main__":
    instructions = "GLRLLGLL"
    print(f"The solution to {instructions} is {Solution().isRobotBounded(instructions)}")
