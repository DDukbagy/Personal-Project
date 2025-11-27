import mod1
add = mod1.MulCal()
add.setdata(3,4)
print(add.add())

import sys
sys.path.append("/workspaces/Personal-Project")

import example_folder.mod2 as mod
a= mod.Math()
print(a.solv(3))

"""
[ 다른 위치에 있는 파일 import하기 ] 
* 방법 1. 경로 : 가장 큰 경로, 코드 : import '최종파일경로.파일이름' as '별칭'
- 경로는 가장 큰 곳으로 하고 '최종파일경로.파일이름'으로 위치와 사용할 폴더명을 입력
- 이 후에 더 사용할 파일이 있다면 '최종파일경로.파일이름'로 쉽게 사용 가능

* 방법 2. 경로 : 최종경로, 코드 : import '파일이름'
- 경로를 가장 가까운 곳으로 해주어 바로 찾을 수 있게함
- 코드가 단순해지지만 다른 폴더에 있는 파일을 import하려면 다시 그 경로를 알려줘야 함

※ 터미널에 pwd를 입력하면 경로가 나옴
"""