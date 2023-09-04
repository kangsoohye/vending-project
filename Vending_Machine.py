###### 약 자판기 종료 메세지 출력 함수 #####
from Close_Message import Close_Message


###### 약 자판기 환영 메세지 출력 함수 #####
from Welcom_Message import Welcome_Message
Welcome_Message()


######   학생 본인확인을 위한 구문   ######


Name_List = {'202068062' : '강수현', '202068040' : '백홍기', 
        '202068044' : '윤민녕', '202025003' : '조민지' }

Medicine_List = {'202068062' : [], 
'202068040' : [], '202068044' : [], '202025003' : [] }

# 학생의 학번을 담을 Student_Number 변수 선언
Student_Number = input("본인 확인을 위해 학번을 입력해주세요. \n\n 99번: 프로그램 종료 \n\n") 


# oo학교 학생인지 확인하는 함수 선언
def Student_DB():
        global Student_Number
        while True :
        #while문을 쓰는 이유는 학번을 잘못 입력했을 경우 다시 입력할 수 있게 반복해야 하므로(대신 99번을 입력하면 프로그램 종료)
                if Student_Number == '99':
                      Close_Message()
                elif Student_Number in Name_List:
                        Student_Name = Name_List[Student_Number]
                        if Student_Number in Name_List and len(Medicine_List[Student_Number]) < 3 :
                                print(f"안녕하세요,{Student_Name}님")
                                break
                
                        elif Student_Number in Name_List and len(Medicine_List[Student_Number]) == 3 :
                                num = input("하루에 구매할 수 있는 약은 최대 3개 입니다.\n다음에 다시 이용해주시기 바랍니다.\n99번: 종료하기 ") #num=종료 변수
                                if num == '99':
                                    print("프로그램이 종료되었습니다.")
                                Close_Message()
                        elif not Student_Number in Name_List:
                                Student_Number = input("입력하신 정보를 찾지 못했습니다\n본인 확인을 위해 학번을 입력해주세요:")


Student_DB()



######### 약 자판기 사용시 주의사항 출력  #########
from Notice import Notice
Notice()



######### 자판기에서 판매 중인 약 리스트   #########


# 각각의 약 수량을 20개로 설정

tylenol = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
ezn = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
brufen = [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
Panpyrin = [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
pancol = [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
bearse = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]


# 판매중인 약 리스트 호출 함수 
#from Medicine_List import Vending_Machine_Medicine_List
#Vending_Machine_Medicine_List()



############### 약 수량 감소 함수 #################

# buy_additional()은 사용자가 선택한 약이 약 리스트에서 수량이 줄어들도록 하는 함수다.
# 타이레놀이 총 20개 있는데 사용자가 타이레놀을 선택했다면
# 타이레놀 수량이 19개로 줄어들도록 한다.

def buy_additional1():
        print("하루 최대 구매하실 수 있는 약은 3개입니다.\n8번: 결제창으로 넘어가기\t99번: 종료하기")
        for buypill in range(2) :
            buypill=input("추가로 구매하실 약의 이름을 입력해 주세요.\n만약 없으시다면 8번을 입력해 주세요. : ")
            if buypill == '타이레놀':
                del tylenol[0] #타이레놀 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(buypill) #리스트에 이름 추가
            elif buypill == '이지엔6':
                del ezn[0] #이지엔6 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(buypill) #리스트에 이름 추가
            elif buypill == '부루펜':
                del brufen[0] #부루펜 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(buypill) #리스트에 이름 추가
            elif buypill == '판피린':
                del Panpyrin[0] #판피린 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(buypill) #리스트에 이름 추가
            elif buypill == '판콜':
                del pancol[0] #판콜 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(buypill) #리스트에 이름 추가
            elif buypill == '베아제':
                del bearse[0] #베아제 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(buypill) #리스트에 이름 추가
            elif buypill == '99':
                Close_Message()
            else:
                break

def buy_additional2():
        print("하루 최대 구매하실 수 있는 약은 3개입니다.\n8번: 결제창으로 넘어가기\t99번: 종료하기")
        for buypill in range(1) :
            buypill=input("추가로 구매하실 약의 이름을 입력해 주세요.\n만약 없으시다면 8번을 입력해 주세요. : ")
            if buypill == '타이레놀':
                del tylenol[0] #타이레놀 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(buypill) #리스트에 이름 추가
            elif buypill == '이지엔6':
                del ezn[0] #이지엔6 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(buypill) #리스트에 이름 추가
            elif buypill == '부루펜':
                del brufen[0] #부루펜 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(buypill) #리스트에 이름 추가
            elif buypill == '판피린':
                del Panpyrin[0] #판피린 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(buypill) #리스트에 이름 추가
            elif buypill == '판콜':
                del pancol[0] #판콜 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(buypill) #리스트에 이름 추가
            elif buypill == '베아제':
                del bearse[0] #베아제 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(buypill) #리스트에 이름 추가
            elif buypill == '99':
                Close_Message()
            else:
                break

def buy_additional3():
        for buypill in range(3) :
            buypill=input("구매하실 약의 이름을 입력해 주세요.\n만약 없으시다면 8번을 입력해 주세요.: ")
            if buypill == '타이레놀':
                del tylenol[0] #타이레놀 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(buypill) #리스트에 이름 추가
            elif buypill == '이지엔6':
                del ezn[0] #이지엔6 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(buypill) #리스트에 이름 추가
            elif buypill == '부루펜':
                del brufen[0] #부루펜 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(buypill) #리스트에 이름 추가
            elif buypill == '판피린':
                del Panpyrin[0] #판피린 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(buypill) #리스트에 이름 추가
            elif buypill == '판콜':
                del pancol[0] #판콜 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(buypill) #리스트에 이름 추가
            elif buypill == '베아제':
                del bearse[0] #베아제 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(buypill) #리스트에 이름 추가
            elif buypill == '99':
                Close_Message()
            else:
                break




############ 구매할 수 있는 약 개수 제한 ###########

# 이 약 자판기는 한 학생이 하루에 3개의 약만 구매할 수 있도록 했다.
# 약을 3개 이하로 구매할 수 있도록 제한하는 기능을 아래에서 구현했다.


#만약 학생이 하루에 약을 1개 구매했을 때 
if Student_Number in Name_List and len(Medicine_List[Student_Number]) == 1 :
        buy_additional1()
                                
#만약 학생이 하루에 약을 2개 구매했을 때 
elif Student_Number in Name_List and len(Medicine_List[Student_Number]) == 2 :
        buy_additional2()

#만약 학생이 하루에 약을 0개 구매했을 때 
elif Student_Number in Name_List and len(Medicine_List[Student_Number]) == 0 :
        buy_additional3()
                
      
def choice():
    print('구매하실 약이 ', Medicine_List.get(Student_Number), '맞습니까?\n') #학번의 리스트안에 구매한 약 이름 출력 & 선택지 출력
    answer = input("11번: 맞습니다 ") 
    if answer == '11' :
        print("결제기능으로 넘어갑니다.")
    
choice()



############### 결제 기능 #################
# 사용자가 구매한 약의 합계를 계산한 후
# 잔돈을 거슬러 주거나 부족한 돈을 추가로 지불할 수 있도록 구현


# 사용자가 선택한 모든 약의 가격을 담는 변수 Total 선언
Total = 0


# 사용자가 선택한 모든 약의 가격을 합하는 함수 선언
def Add_Medicine_Price ():
        global Total    
        if Medicine_List[Student_Number][i] == "타이레놀":
                Total += 3000
        elif Medicine_List[Student_Number][i] == "이지엔6":
                Total += 2500
        elif Medicine_List[Student_Number][i] == "부루펜":
                Total += 6000  
        elif Medicine_List[Student_Number][i] == "판피린":
                Total += 1500
        elif Medicine_List[Student_Number][i] == "판콜":
                Total += 2600
        elif Medicine_List[Student_Number][i] == "베아제":
                Total += 1700


# 1) 학생이 구매한 약이 3개일 경우 실행되는 계산식 
if len(Medicine_List[Student_Number]) == 3:

        for i in range(3):
                Add_Medicine_Price()


# 2) 학생이 구매한 약이 2개인 경우 실행되는 계산식
elif len(Medicine_List[Student_Number]) == 2:

        for i in range(2):
                Add_Medicine_Price()


# 3) 학생이 구매한 약이 1개인 경우 실행되는 계산식
else:
        for i in range(1):
                Add_Medicine_Price()


# 사용자가 지불한 금액을 저장하는 Money 변수 선언

print(f"\n지불하실 금액은 {Total}원 입니다.")
Money = int(input("돈을 투입구에 넣어주세요. \n\n99번. 종료하기\n\n"))


# 사용자가 돈을 지불하지 않고 프로그램을 종료하는 경우
if Money == 99:
        Close_Message()


# 지불해야 할 돈에 딱 맞게 돈을 지불한 경우
elif Money == Total:
        print("\n\n구매가 완료됐습니다. \n투입구에서 약을 받아가 주세요.")
        Close_Message()


# 지불해야 할 돈보다 더 많은 돈을 지불한 경우
elif Money > Total:

        # 거스름돈을 저장할 Change 변수 선언
        Change = Money - Total
        print(f"구매가 완료됐습니다. \n투입구에서 약과 거스름돈 {Change}원을 받아가주세요.")
        Close_Message()


# 부족한 금액을 지불한 경우
else :
        # 얼마나 부족한 금액을 나타내는지 알려주는 lack_money 변수 선언
        # 5000원을 지불해야하는데 사용자가 1000원을 지불했다면 4000원을 덜 지불한 것이니
        # lack_money에는 4000원이 저장된다.
        lack_money = abs(Money - Total)
        print(f"투입하신 돈이 {lack_money}원 부족합니다. \n")

        #사용자가 추가로 지불한 돈을 저장하는 Pay_Extra 변수 선언
        Pay_Extra = int(input("돈을 추가로 투입해주세요. \n\n 99번. 종료하기 \n\n"))

        while True:

                if Pay_Extra == 99:
                        Close_Message()

                elif Pay_Extra == lack_money:
                        print("구매가 완료됐습니다. \n투입구에서 약을 받아가 주세요.")
                        Close_Message()


                # 지불해야 할 돈보다 더 많은 돈을 지불한 경우
                elif Pay_Extra > lack_money:

                        # 거스름돈 변수인 Change 선언
                        
                        Change = lack_money - Pay_Extra
                        print(f"구매가 완료됐습니다. \n 투입구에서 약과 거스름돈 {Change}을 받아가주세요.")
                        Close_Message()
                
                
                #@@@@@@@@@@@ 여기서부터 문제다.
                # 돈을 계속 부족하게 지불할 경우 어떻게 해야할지 설정해야 함.
                else :
                        # lack_money = abs(Money - Total)
                        # print(f"투입하신 돈이 {lack_money}원 부족합니다. \n")


                        continue
