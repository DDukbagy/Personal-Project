
import packages_Practice

# packages_Practice.sound안의 echo모듈을 import하여 실행하는 방법 3가지
import packages_Practice.sound.echo
packages_Practice.sound.echo.echo_test()

from packages_Practice.sound import echo
echo.echo_test()

from packages_Practice.sound.echo import echo_test
echo_test()
#----------------------------------------------------------------------#

from packages_Practice.sound import *   # * : 앞에 불러온 모듈의 모든 것을 import함, 해당 모듈의 __inin__.py파일에 __all__변수 있어야 실행됨
echo.echo_test()