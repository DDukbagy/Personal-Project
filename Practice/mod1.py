'''
class AddCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

if __name__ == "__main__":
    print("This file is main file!")
else:
    print("This file is \""+__name__+"\" file!")
'''

"""
* __name__
- 모듈 이름을 저장하는 변수
- __name__가 있는 파일에서 직접 실행하면 값이 "__main__"로 저장됨
- 다른 모듈에서 불러와서 실행하면 __name__가 그 파일의 이름으로 저장됨
- 직접 실행용 코드와 import용 코드를 구분할 때 사용함
"""