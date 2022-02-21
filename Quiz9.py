class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg
chicken = 10
waiting = 1
try :
    while(True):
        print("[남은 치킨 ; {0}".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order < 1:
            ValueError()
        if order > chicken: # 남은 치킨보다 주문량이 많을때
            print("재료가 부족합니다")
            raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다")



        else :
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다." \
                .format(waiting, order))
            waiting += 1
            chicken -= order


except ValueError:
    print("잘못된 값을 입력하였습니다")
    
except SoldOutError as err:
    #print("재고가 소진되어 더 이상 주문을 받지 않습니다1")
    print(err)