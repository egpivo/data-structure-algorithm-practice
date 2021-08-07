from collections.abc import Generator
LIMIT = 1000


def square_number_digits(num: int) -> Generator:
    for char in str(num):
        yield int(char) ** 2


class HappyNumber:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        for _ in range(LIMIT):
            total = sum(square_number_digits(n))
            if total == 1:
                return True
            else:
                n = total
        return False


class HappyNumber2:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        first = second = n
        while True:
            first = sum(square_number_digits(first))
            second = sum(square_number_digits(second))
            second = sum(square_number_digits(second))
            if first == second:
                break
        return first == 1


if __name__ == "__main__":
    instance = HappyNumber()
    instance2 = HappyNumber2()

    print("Test answer")
    assert instance.isHappy(19), "Wrong Answer."
    assert not instance.isHappy(2), "Wrong Answer."
    assert instance2.isHappy(19), "Wrong Answer."
    assert not instance2.isHappy(2), "Wrong Answer."
