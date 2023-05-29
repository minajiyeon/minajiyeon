import calendar

class Schedule: #클래스 정의
    def __init__(self):
        self.schedule = []

    def show_calendar(self, 년도, 월): #달력보기
        달력 = calendar.TextCalendar(firstweekday=6) #달력생성
        달력을_문자로 = 달력.formatmonth(날짜, 월) #달력을 문자열로 저장

        for 날 in range(1, calendar.monthrange(년도, 월)[1] + 1):#일정 유무 확인
            events = [이벤트 for 이벤트 in self.schedule if 이벤트["날짜"] == f"{년도}-{월:02d}-{날:02d}"] #events 리스트에 모든 일정의 제목만 저장
            if events:
                달력을_문자로 = 달력을_문자로.replace(f"{날} ", f"{날}*") # 일정 있는 날에 * 추가

        print(달력을_문자로)

        내림차_스케쥴 = sorted(self.schedule, key=lambda 이벤트: (이벤트["날짜"], 이벤트["시간"])) #일정들 시간 순서대로 정렬

        for 이벤트 in 내림차_스케쥴: #일정 출력
            날짜 = 이벤트["날짜"]
            시간 = 이벤트["시간"]
            일정 = 이벤트["일정"]
            print(f"{날짜} {시간}: {일정}")

Myschedule = Schedule()
