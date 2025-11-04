# 최대공약수와 최소공배수 계산기
# 초등학교 6학년용

def gcd(a, b):
    """최대공약수(GCD)를 구하는 함수"""
    # 유클리드 호제법 사용
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """최소공배수(LCM)를 구하는 함수"""
    # 최소공배수 = (a × b) ÷ 최대공약수
    return (a * b) // gcd(a, b)

# 프로그램 시작
print("=" * 50)
print("🔢 최대공약수와 최소공배수 계산기 🔢")
print("=" * 50)
print()

# 사용자로부터 두 숫자 입력받기
try:
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))

    # 양수인지 확인
    if num1 <= 0 or num2 <= 0:
        print("⚠️ 양수만 입력해주세요!")
    else:
        # 결과 계산
        result_gcd = gcd(num1, num2)
        result_lcm = lcm(num1, num2)

        # 결과 출력
        print()
        print("-" * 50)
        print(f"📊 계산 결과:")
        print(f"   입력한 숫자: {num1}, {num2}")
        print(f"   최대공약수(GCD): {result_gcd}")
        print(f"   최소공배수(LCM): {result_lcm}")
        print("-" * 50)

except ValueError:
    print("⚠️ 숫자만 입력해주세요!")
