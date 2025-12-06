try:                                # 오류가 있는지 확인할 코드를 입력
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:      # try문 수행 중 오류 발생 시 실행
    print(e)
except IndexError:                  # except문은 여러번 사용 가능, 여러 오류가 발생해도 처음 except문만 실행됨
    print("인덱싱 할 수 없습니다.")
except:                             # 오류 변수는 생략 가능, 발생 오류가 생략된 except문은 except문의 마지막에 위치해야함
    print("오류 발생!!!")
else:                               # 오류가 발생하지 않으면 실행
    print("d")
finally:                            # try문 수행 도중 예외 발생 여부 상관없이 무조건 실행
    print("d")
