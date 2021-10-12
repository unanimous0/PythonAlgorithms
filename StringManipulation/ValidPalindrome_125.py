"""
    문자열 조작 (String Manipulation)
    LeetCode 125 - Valid Palindrome
    https://leetcode.com/problems/valid-palindrome/
"""

# 풀이 1 - 리스트로 변환
class Solution1:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():                  # isalnum() - 영문자, 숫자 여부를 판별 -> True/False로 반환
                strs.append(char.lower())

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():       # pop() - 맨 뒤의 요소 추출
                return False                    # 파이썬의 리스트는 pop() 함수에서 인덱스 지정할 수 있으므로, 인덱스를 인자로 받는 경우 해당 인덱스 위치의 요소를 추출함
        
        return True


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    # s = "race a car"

    sol1 = Solution1()
    print(sol1.isPalindrome(s))


# 풀이 2 - Deque 자료형을 이용한 최적화
import collections

class Solution2:
    def isPalindrome(self, s: str) -> bool:
        # 자료형 데크로 선언
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():        # list의 pop(0)는 O(n)인 데 반해, 데크의 popleft()는 O(1) 이므로 훨씬 빠름
                return False                        # n번씩 반복하면 리스트 구현은 O(n^2)이고, 데크 구현은 O(n) 으로 성능차이가 큼

        return True


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    # s = "race a car"

    sol2 = Solution2()
    print(sol2.isPalindrome(s))


# 풀이 3 - 슬라이싱 사용
import re

class Solution3:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)          # 문자열 전체를 한 번에 영숫자만 걸러내도록 정규식으로 처리
                                                # (위에서는 isalnum()으로 모든 문자를 일일이 점검함)
        # 슬라이싱
        return s == s[::-1]                     # 파이썬은 문자열을 배열이나 리스트처럼 슬라이싱할 수 있는 기능을 제공 ([::-1] -> 뒤집기)
                                                # 코드가 줄어듦은 물론, 내부적으로 C로 구현되어 있어 더 빠른 속도로 구현 가능
                                                ## 대부분의 문자열 작업은 슬라이싱으로 처리하는 편이 가장 빠름
if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"        ## 파이썬의 문자열 슬라이싱은 내부적으로 빠르게 동작함
    # s = "race a car"                          ### 위치를 지정하면 해당 위치의 배열 포인터를 얻게 되며, 이를 통해 연결된 객체를 찾아
                                                ### 실제 값을 찾아내는데, 이 과정은 매우 빠르게 진행되므로 문자열을 조작할 때는 슬라이싱을
    sol3 = Solution3()                          ### 우선으로 사용하는 편이 속도 개선에 유리함
    print(sol3.isPalindrome(s))