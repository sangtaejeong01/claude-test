#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
초등학교 6학년 수준 최대공약수, 최소공배수 계산 프로그램
"""

def gcd(a, b):
    """
    최대공약수(GCD, Greatest Common Divisor)를 구하는 함수
    유클리드 호제법을 사용합니다.

    예시:
    gcd(12, 18) = 6
    gcd(24, 36) = 12
    """
    # 두 수 중 작은 수부터 1까지 거꾸로 확인하는 방법 (이해하기 쉬운 방법)
    # 하지만 유클리드 호제법이 더 효율적입니다

    # 유클리드 호제법: 큰 수를 작은 수로 나눈 나머지로 계속 반복
    while b != 0:
        remainder = a % b  # a를 b로 나눈 나머지
        a = b
        b = remainder

    return a


def gcd_simple(a, b):
    """
    최대공약수를 구하는 간단한 방법 (이해하기 더 쉬움)
    두 수의 공약수 중 가장 큰 수를 찾습니다.
    """
    # 두 수 중 작은 수를 찾기
    smaller = min(a, b)

    # 작은 수부터 1까지 거꾸로 확인
    for i in range(smaller, 0, -1):
        if a % i == 0 and b % i == 0:  # 둘 다 나누어떨어지면 최대공약수
            return i

    return 1


def lcm(a, b):
    """
    최소공배수(LCM, Least Common Multiple)를 구하는 함수

    공식: 최소공배수 = (두 수의 곱) ÷ 최대공약수

    예시:
    lcm(12, 18) = 36
    lcm(4, 6) = 12
    """
    return (a * b) // gcd(a, b)


def print_calculation_steps(a, b):
    """
    계산 과정을 단계별로 보여주는 함수
    """
    print(f"\n=== {a}와 {b}의 최대공약수와 최소공배수 구하기 ===\n")

    # 최대공약수 계산
    result_gcd = gcd(a, b)
    print(f"1단계: 최대공약수 구하기")
    print(f"   {a}와 {b}의 최대공약수 = {result_gcd}")

    # 최소공배수 계산
    result_lcm = lcm(a, b)
    print(f"\n2단계: 최소공배수 구하기")
    print(f"   공식: 최소공배수 = (두 수의 곱) ÷ 최대공약수")
    print(f"   최소공배수 = ({a} × {b}) ÷ {result_gcd}")
    print(f"   최소공배수 = {a * b} ÷ {result_gcd}")
    print(f"   최소공배수 = {result_lcm}")

    print(f"\n✓ 결과:")
    print(f"  최대공약수(GCD) = {result_gcd}")
    print(f"  최소공배수(LCM) = {result_lcm}")
    print()


def main():
    """
    메인 프로그램
    """
    print("=" * 50)
    print("최대공약수와 최소공배수 계산 프로그램")
    print("=" * 50)

    # 예제 실행
    print("\n📚 예제들:")
    examples = [
        (12, 18),
        (24, 36),
        (15, 25),
        (8, 12)
    ]

    for a, b in examples:
        print_calculation_steps(a, b)

    # 사용자 입력 받기
    print("\n" + "=" * 50)
    print("직접 계산해보기")
    print("=" * 50)

    try:
        num1 = int(input("\n첫 번째 숫자를 입력하세요: "))
        num2 = int(input("두 번째 숫자를 입력하세요: "))

        if num1 <= 0 or num2 <= 0:
            print("❌ 양의 정수를 입력해주세요!")
            return

        print_calculation_steps(num1, num2)

    except ValueError:
        print("❌ 숫자만 입력해주세요!")
    except KeyboardInterrupt:
        print("\n\n프로그램을 종료합니다.")


if __name__ == "__main__":
    main()
