'''
# setdata 예시
class AddCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    
add = AddCal()
add.setdata(3,4)
print(add.add())

#__init__ 예시
class SubCal:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    
    def sub(self):
        result = self.first - self.second
        return result
    
sub = SubCal(5,2)
print(sub.sub())
'''

"""
[ setdata , '__init__ 차이]
* 1. setdata
- 객체는 미리 만들어 두고 값은 나중에 설정 가능
- 여러 번 다른 값으로 재설정 가능
- 초기값 없이도 객체 생성 가능 → 더 유연

* 2. __init__
- 객체와 값이 동시에 생성
- 값이 없으면 생성 불가
- 여러 메서드에서 객체 상태 재사용 가능
- 객체를 새로 선언하지 않고도 인스턴스 변수 수정 가능 ex) a = add(3,4) -> a,first = 10
"""

# ================================================================================================================ #
