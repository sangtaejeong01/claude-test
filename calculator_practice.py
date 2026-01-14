#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
혼합계산 연습기 (Mixed Calculation Practice)
터미널에서 실행 가능한 대화형 계산 연습 프로그램
"""

import random
import os
import sys

class CalculatorPractice:
    def __init__(self):
        self.correct_count = 0
        self.incorrect_count = 0
        self.difficulty = 'medium'
        self.operators = ['+', '-', '×', '÷']
        self.current_problem = None

    def clear_screen(self):
        """화면 지우기"""
        os.system('clear' if os.name != 'nt' else 'cls')

    def get_random_number(self):
        """난이도에 따른 랜덤 숫자 생성"""
        max_values = {
            'easy': 10,
            'medium': 50,
            'hard': 100
        }
        max_val = max_values.get(self.difficulty, 50)
        return random.randint(1, max_val)

    def generate_problem(self):
        """새로운 문제 생성"""
        if not self.operators:
            print("⚠️  최소 하나의 연산자를 선택해주세요!")
            self.operators = ['+']

        operator = random.choice(self.operators)
        num1 = self.get_random_number()
        num2 = self.get_random_number()
        answer = 0

        if operator == '+':
            answer = num1 + num2
        elif operator == '-':
            # 결과가 양수가 되도록 조정
            if num1 < num2:
                num1, num2 = num2, num1
            answer = num1 - num2
        elif operator == '×':
            # 곱셈은 숫자를 작게 조정
            num1 = num1 // 2 + 1
            num2 = num2 // 2 + 1
            answer = num1 * num2
        elif operator == '÷':
            # 나눗셈은 나누어떨어지도록 조정
            num2 = max(2, num2 // 2)
            answer = random.randint(1, 20)
            num1 = num2 * answer

        self.current_problem = {
            'num1': num1,
            'num2': num2,
            'operator': operator,
            'answer': answer
        }

    def display_stats(self):
        """통계 표시"""
        total = self.correct_count + self.incorrect_count
        accuracy = (self.correct_count / total * 100) if total > 0 else 0

        print("\n" + "="*60)
        print(f"📊 통계")
        print("="*60)
        print(f"✅ 맞은 문제: {self.correct_count}")
        print(f"❌ 틀린 문제: {self.incorrect_count}")
        print(f"📈 정답률: {accuracy:.1f}%")
        print("="*60 + "\n")

    def display_problem(self):
        """현재 문제 표시"""
        p = self.current_problem
        print(f"\n{'='*60}")
        print(f"   {p['num1']} {p['operator']} {p['num2']} = ?")
        print(f"{'='*60}\n")

    def check_answer(self, user_answer):
        """답안 확인"""
        try:
            user_ans = int(user_answer)
            correct_ans = self.current_problem['answer']

            if user_ans == correct_ans:
                self.correct_count += 1
                print(f"\n🎉 정답입니다! ({correct_ans})")
                return True
            else:
                self.incorrect_count += 1
                print(f"\n😢 틀렸습니다. 정답은 {correct_ans}입니다.")
                return False
        except ValueError:
            print("\n⚠️  올바른 숫자를 입력해주세요!")
            return None

    def show_settings_menu(self):
        """설정 메뉴 표시"""
        self.clear_screen()
        print("\n" + "="*60)
        print("⚙️  설정")
        print("="*60)

        # 난이도 설정
        print("\n난이도 선택:")
        print("1. 쉬움 (1-10)")
        print("2. 보통 (1-50)")
        print("3. 어려움 (1-100)")

        difficulty_choice = input("\n선택 (1-3): ").strip()
        if difficulty_choice == '1':
            self.difficulty = 'easy'
        elif difficulty_choice == '2':
            self.difficulty = 'medium'
        elif difficulty_choice == '3':
            self.difficulty = 'hard'

        # 연산자 설정
        print("\n연산자 선택 (스페이스로 구분, 예: 1 2 3):")
        print("1. + (더하기)")
        print("2. - (빼기)")
        print("3. × (곱하기)")
        print("4. ÷ (나누기)")

        op_choice = input("\n선택 (1-4): ").strip()
        op_map = {'1': '+', '2': '-', '3': '×', '4': '÷'}
        selected_ops = []

        for char in op_choice.split():
            if char in op_map:
                selected_ops.append(op_map[char])

        if selected_ops:
            self.operators = selected_ops

        print(f"\n✅ 설정 완료!")
        print(f"   난이도: {self.difficulty}")
        print(f"   연산자: {', '.join(self.operators)}")
        input("\n계속하려면 Enter를 누르세요...")

    def show_main_menu(self):
        """메인 메뉴 표시"""
        self.clear_screen()
        print("\n" + "="*60)
        print("🧮 혼합계산 연습기")
        print("="*60)
        self.display_stats()

        print("메뉴:")
        print("1. 문제 풀기")
        print("2. 설정")
        print("3. 통계 초기화")
        print("4. 종료")

        choice = input("\n선택 (1-4): ").strip()
        return choice

    def reset_stats(self):
        """통계 초기화"""
        confirm = input("\n통계를 초기화하시겠습니까? (y/n): ").strip().lower()
        if confirm == 'y' or confirm == 'yes':
            self.correct_count = 0
            self.incorrect_count = 0
            print("✅ 통계가 초기화되었습니다!")
        else:
            print("❌ 취소되었습니다.")
        input("\n계속하려면 Enter를 누르세요...")

    def practice_mode(self):
        """연습 모드"""
        while True:
            self.clear_screen()
            self.display_stats()
            self.generate_problem()
            self.display_problem()

            print("명령어: [숫자 입력] 또는 'skip'(건너뛰기), 'menu'(메뉴)")
            user_input = input("\n답: ").strip().lower()

            if user_input == 'menu':
                break
            elif user_input == 'skip':
                self.incorrect_count += 1
                print(f"\n정답: {self.current_problem['answer']}")
                input("\n계속하려면 Enter를 누르세요...")
            else:
                result = self.check_answer(user_input)
                if result is not None:
                    input("\n계속하려면 Enter를 누르세요...")

    def run(self):
        """프로그램 실행"""
        try:
            while True:
                choice = self.show_main_menu()

                if choice == '1':
                    self.practice_mode()
                elif choice == '2':
                    self.show_settings_menu()
                elif choice == '3':
                    self.reset_stats()
                elif choice == '4':
                    self.clear_screen()
                    print("\n👋 수고하셨습니다! 안녕히 가세요!\n")
                    break
                else:
                    print("\n⚠️  올바른 번호를 선택해주세요!")
                    input("\n계속하려면 Enter를 누르세요...")
        except KeyboardInterrupt:
            self.clear_screen()
            print("\n\n👋 프로그램을 종료합니다.\n")
            sys.exit(0)


def main():
    """메인 함수"""
    app = CalculatorPractice()
    app.run()


if __name__ == "__main__":
    main()
