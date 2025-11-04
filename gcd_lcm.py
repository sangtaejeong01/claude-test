"""
최대공약수(GCD)와 최소공배수(LCM)를 구하는 프로그램
"""

def gcd(a, b):
    """
    유클리드 호제법을 사용하여 최대공약수(GCD)를 구합니다.

    Args:
        a (int): 첫 번째 정수
        b (int): 두 번째 정수

    Returns:
        int: 두 수의 최대공약수
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)


def lcm(a, b):
    """
    최소공배수(LCM)를 구합니다.
    LCM = (a * b) / GCD(a, b)

    Args:
        a (int): 첫 번째 정수
        b (int): 두 번째 정수

    Returns:
        int: 두 수의 최소공배수
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def main():
    """메인 함수 - 사용 예제"""
    print("=== 최대공약수(GCD)와 최소공배수(LCM) 계산 ===\n")

    # 예제 1
    num1, num2 = 48, 18
    print(f"숫자 1: {num1}")
    print(f"숫자 2: {num2}")
    print(f"최대공약수(GCD): {gcd(num1, num2)}")
    print(f"최소공배수(LCM): {lcm(num1, num2)}")
    print()

    # 예제 2
    num1, num2 = 100, 35
    print(f"숫자 1: {num1}")
    print(f"숫자 2: {num2}")
    print(f"최대공약수(GCD): {gcd(num1, num2)}")
    print(f"최소공배수(LCM): {lcm(num1, num2)}")
    print()

    # 예제 3
    num1, num2 = 17, 19
    print(f"숫자 1: {num1}")
    print(f"숫자 2: {num2}")
    print(f"최대공약수(GCD): {gcd(num1, num2)}")
    print(f"최소공배수(LCM): {lcm(num1, num2)}")
    print()

    # 사용자 입력
    print("=== 직접 계산해보기 ===")
    try:
        num1 = int(input("첫 번째 숫자를 입력하세요: "))
        num2 = int(input("두 번째 숫자를 입력하세요: "))
        print(f"\n최대공약수(GCD): {gcd(num1, num2)}")
        print(f"최소공배수(LCM): {lcm(num1, num2)}")
    except ValueError:
        print("올바른 정수를 입력해주세요.")
    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다.")


if __name__ == "__main__":
    main()
