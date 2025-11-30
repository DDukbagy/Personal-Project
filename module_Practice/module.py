# 같은 폴더의 파일 import
import mod1
mul = mod1.MulCal()
mul.setdata(3,4)
print(mul.mul())


# [ 다른 위치에 있는 파일 import하기 ] ※ 터미널에 pwd를 입력하면 경로가 나옴
# 방법 1. 경로 - 간단하게, import - 자세하게
# 이 후에 더 사용할 파일이 있다면 '최종파일경로.파일이름'로 쉽게 사용 가능
import sys
sys.path.append("/workspaces/Personal-Project") # 경로 : 가장 큰 경로

import example_folder.mod2 as mod               # import : '최종파일경로.파일이름' as '별칭'
a = mod.Math()
print(a.solv(3))

# 방법 2. 경로 - 자세하게, import - 간단하게
# - 코드가 단순해지지만 다른 폴더에 있는 파일을 import하려면 다시 그 경로를 알려줘야 함
import sys
sys.path.append("/workspaces/Personal-Project/module_Practice/example_folder")  #경로 : 최종경로

import mod2                                                                     # import : '파일이름'
b = mod2.Math()
print(b.solv(4))
#-----------------------------------------------------------------------------------------------------------#
