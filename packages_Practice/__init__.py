
from .graphic.render import render_test # __init__.py파일에 패키지 내의 다른 모듈을 미리 import하여 패키지를 사용하는 코드에서 간편하게 사용 가능

VERSION = 3.5

def print_version_info():
    print(f"The version of this game is {VERSION}.")

print("Initializing game...")   # 패키지 초기화 코드(패키지를 처음 불러올 때 실행되는 코드), 처음 한번만 실행됨


"""
[ "__init__.py"의 역할 ]
- 이 폴더는 파이썬 패키지야! 라고 표시하는 깃발 같은 역할
ex ) game/
     ├─ player.py
     ├─ monster.py
     └─ item.py
- 위의 예시는 그냥 폴더일 뿐, 파이썬은 이걸 "묶음"으로 보지 않음
- 폴더 내부의 파일들을 ex) import game.player 처럼 import 할 수 없음
- 이 폴더를 패키지로 인정시키기 위해 필요한 파일이 "__init__.py"
- "__init.py__"에는 내용이 없어도 됨

※ "__init.py__" 파일이 없어도 실행이 잘 되는 이유
- 파이썬 3.3 이후, “네임스페이스 패키지(namespace package)”라는 기능을 만들어서 init.py가 없어도 폴더를 패키지처럼 취급할 수 있게 바뀜
- 네임스페이스 패키지가 동작하는 조건
    1. 폴더가 실제 파이썬 패스 안에 있을 때
    2. 그 폴더가 다른 패키지와 충돌하지 않을 때
    3. 단순한 구조일 때
- 하위 버전호환을 위해 왠만하면 "__init.py__"를 추가하는 것을 권장함

※ 패키지란?
- 폴더(디렉터리)를 “모듈 묶음”으로 만들기 위한 것
"""