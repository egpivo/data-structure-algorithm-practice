# Definition for polynomial singly-linked list.
class PolyNode:
    def __init__(self, x=0, y=0, next=None):
        self.coefficient = x
        self.power = y
        self.next = next


class Solution:
    """
    Complexity
    ----------
    - TC: O(max(n, m))
    - SC: O(1)
    """
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        head = answer = PolyNode()

        while poly1 and poly2:
            if poly1.power > poly2.power:
                head.next = PolyNode(x=poly1.coefficient, y=poly1.power)
                poly1 = poly1.next
            elif poly1.power < poly2.power:
                head.next = PolyNode(x=poly2.coefficient, y=poly2.power)
                poly2 = poly2.next
            else:
                coefficient = poly1.coefficient + poly2.coefficient
                power = poly1.power
                poly1 = poly1.next
                poly2 = poly2.next
                if coefficient != 0:
                    head.next = PolyNode(x=coefficient, y=power)
                else:
                    continue

            head = head.next

        if poly1:
            head.next = poly1
        if poly2:
            head.next = poly2

        return answer.next


if __name__ == '__main__':
    a, a.next, a.next.next = PolyNode(2, 2), PolyNode(4, 1), PolyNode(3, 0)
    b, b.next, b.next.next = PolyNode(3, 2), PolyNode(-4, 1), PolyNode(-1, 0)
    result = Solution().addPoly(a, b)
    while result:
        print(f"[{result.coefficient},{result.power}]")
        result = result.next
