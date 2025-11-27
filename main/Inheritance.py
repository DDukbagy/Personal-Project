'''
# 상속(IS-A 관계) 예시
class Animal:
    def eat(self):
        print("먹는다")

class Dog(Animal):
    pass

# 포함(HAS-A 관계) 예시
class Engine:
    def start(self):
        print("엔진 스타트!")

class Car:
    def __init__(self):
        self.engine = 10  # 초기에는 숫자

class ElectricEngine:
    def start(self):
        print("전기 엔진 ON")

car = Car()
car.engine = ElectricEngine()   # 엔진 객체로 교체

car.engine.start()  # "전기 엔진 ON"
'''

"""
[ 상속, 포함 비교 정리 ]
* 상속 = 큰 덩어리 위에 층층이 쌓는 구조(고정적)
- 밑바닥(부모 구조)이 변하면 위층(자식)이 무너짐, 중간층을 통째로 바꾸는 건 거의 불가능
- 구조가 단단히 고정됨, 부모 기능을 자동 상속 받음, 유연성 낮음, "종류"를 표현하는 방식

* 포함 = 레고 블록처럼 부품을 계속 갈아끼우는 구조(유연함)
- 부품을 끼우고 빼고 다른 모양으로 교체, 새 부품 추가 등 완전 자유로움
- 구조가 유연함, 필요한 객체를 조립, 나중에 교체/추가/삭제 가능, "조립"을 표현하는 방식
"""

# ================================================================================================================ #
