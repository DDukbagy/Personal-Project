from fpdf import FPDF

# PDF 생성
pdf = FPDF()
pdf.add_page()

# 한글 폰트 등록 (NanumGothic Regular & Bold)
# Codespaces(Linux) 기준 폰트 경로
pdf.add_font('NanumGothic', '', '/usr/share/fonts/truetype/nanum/NanumGothic.ttf', uni=True)
pdf.add_font('NanumGothic', 'B', '/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf', uni=True)

# PDF 제목 (Bold)
pdf.set_font('NanumGothic', 'B', 16)
pdf.cell(0, 10, "오키나와 둘째 날 상세 일정", ln=True, align="C")
pdf.ln(10)

# 일정 내용 (Regular)
pdf.set_font('NanumGothic', '', 12)

schedule = [
    ("오리엔탈 호텔 출발", "09:00", "오리엔탈 호텔에서 출발"),
    ("비세 후쿠기 가로수길 산책", "09:40-10:40", "사진, 산책"),
    ("J's Kitchen 브런치", "10:50-11:50", "식사, 웨이팅 포함"),
    ("만좌모 이동", "11:50-12:50", "북부 이동, 사진 촬영"),
    ("츄라우미 수족관 관람", "12:50-14:50", "주요 전시 관람, 사진"),
    ("류쿠 온천 세나가지마 호텔 이동", "14:50-15:50", "북부 → 남부 이동"),
    ("호텔 체크인 / 휴식", "15:50-16:20", "체크인 + 온천 준비"),
    ("얏빠리 스테이크 3호점 저녁 식사", "16:40-17:40", "저녁 식사"),
    ("국제거리 관광 / 쇼핑", "17:40-20:05", "저녁 식사 후 바로 관광 가능"),
]

for item in schedule:
    pdf.multi_cell(0, 8, f"{item[0]} ({item[1]}): {item[2]}")
    pdf.ln(2)

# PDF 저장
pdf.output("Okinawa_Day2_Schedule.pdf")
print("PDF 생성 완료: Okinawa_Day2_Schedule.pdf")
