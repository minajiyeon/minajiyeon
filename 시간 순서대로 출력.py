import calendar

class Schedule: #schedule 클래스는 사용자의 일정을 관리하기 위한 기능을 제공함.

    def __init__(self): #클래서 초기화
        self.schedule = [] #리스트 생성
        
    def show_calendar(self, year, month): # 선택한 월의 달력 
        text_cal = calendar.TextCalendar(firstweekday = 6)
        text_cal.prmonth(year, month)

    def schedule_searching(self, date, time = ""): # 일정 찾기

        filtered_schedule = []
        
        for schedule in self.schedule:
            if time:
                if schedule["date"] == date and schedule["time"] == time:
                    filtered_schedule.append(schedule)
                    
            else:
                if schedule["date"] == date:
                    filtered_schedule.append(schedule)

        if filtered_schedule:
            sorted_schedule = sorted(filtered_schedule, key=lambda x: x.get("time", ""))
            for schedule in sorted_schedule:
                print("일정 : ", schedule["title"]) #일정 제목
                print("시간 : ", schedule["time"]) #일정 시간

            
        else :
            print("해당하는 일정이 없습니다.") #일정 시간

    def remove_event(self, date, time, title):
        
        removed_events = []
        
        for schedule in self.schedule:
            if schedule["date"] == date and schedule["time"] == time and schedule["title"] == title:
                removed_events.append(schedule)
                
        for event in removed_events:
            self.schedule.remove(event)
            
        if removed_events:
            print("다음 일정이 삭제되었습니다:")
            for event in removed_events:
                print("일정:", event["title"])
                print("날짜:", event["date"])
                print("시간:", event["time"])
        else:
            print("해당하는 일정이 없습니다.")
            
my_schedule = Schedule()
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
        my_schedule.show_calendar(year, month)
    elif choice == "2": #일정 추가
        date = input("날짜를 입력하세요 (YYYY-MM-DD): ")
        time = input("시간을 입력하세요 (HH:MM): ")
        title = input("일정 내용을 입력하세요: ")
        my_schedule.schedule.append({"date": date, "time" : time, "title": title})
    elif choice == "3":
        date = input("조회할 날짜를 입력하세요 (YYYY-MM-DD): ")
        my_schedule.schedule_searching(date)
    elif choice == "4":
        date = input("조회할 날짜를 입력하세요 (YYYY-MM-DD): ")
        time = input("조회할 시간을 입력하세요 (HH:MM): ")
        my_schedule.schedule_searching(date, time)
    elif choice == "5":
        date = input("삭제할 일정의 날짜를 입력하세요 (YYYY-MM-DD): ")
        time = input("삭제할 일정의 시간을 입력하세요 (HH:MM): ")
        title = input("삭제할 일정의 제목을 입력하세요: ")
        my_schedule.remove_event(date, time, title)
    elif choice == "6":
        break
    else:
        print("유효하지 않은 선택입니다. 다시 선택해주세요.")
