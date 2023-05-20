import calendar

def show_calendar(year, month):
    # 선택한 월의 달력 출력
    text_cal = calendar.TextCalendar(firstweekday = 6)
    text_cal.prmonth(year, month)


def schedule_searching(date, time = ""):
    # 일정 찾기
    for schedule in schedules.values():
        if time:
            if schedule["date"] == date and schedule["time"]:
                print("일정 : ", schedule["title"]) #일정 제목
                print("시간 : ", schedule["time"]) #일정 시간
    
        else:
            if schedule["date"] == date:
                print("일정 : ", schedule["title"]) #일정 제목
                print("시간 : ", schedule["time"]) #일정 시간


# 프로그램 실행
while True:
    print("\n===== 일정 관리 프로그램 =====")
    print("1. 달력 보기")
    print("2. 일정 추가")
    print("3. 일정 조회 (날짜)")
    print("4. 일정 조회 (날짜 및 시간)")
    print("5. 일정 삭제")
    print("6. 종료")
    choice = input("원하는 기능을 선택하세요: ")

    if choice == "1":
        year = int(input("년도를 입력하세요: "))
        month = int(input("월을 입력하세요: "))
        show_calendar(year, month)

        
    elif choice == "3":
        date = input("조회할 날짜를 입력하세요 (YYYY-MM-DD): ")
        schedule_searching(date)
    elif choice == "4":
        date = input("조회할 날짜를 입력하세요 (YYYY-MM-DD): ")
        time = input("조회할 시간을 입력하세요 (HH:MM): ")
        schedule_searching(date, time)

        

