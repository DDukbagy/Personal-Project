import svgwrite
import cairosvg

# SVG 전체 캔버스 크기
WIDTH, HEIGHT = 1800, 1200
dwg = svgwrite.Drawing('architecture.svg', profile='full', size=(WIDTH, HEIGHT))

# 색상 정의
APP_COLOR = '#FFDDAA'
SUPABASE_COLOR = '#AAEEFF'
FASTAPI_COLOR = '#DDEEFF'
ADMIN_COLOR = '#CCFFCC'
EXTERNAL_COLOR = '#FFEEDD'
TEXT_COLOR = 'black'

# 박스 자동 크기 계산 함수
def calculate_box_size(title, items, min_width=350, padding=20, line_height=22):
    """텍스트 길이에 맞춰 width/height 자동 계산"""
    all_lines = [title] + items
    max_chars = max(len(line) for line in all_lines)
    
    # 글자 수 기반 width 추정
    width = max(min_width, padding * 2 + max_chars * 8)   # 약 1글자 = 8px
    
    # 줄 수 기반 height 계산
    height = padding * 2 + line_height * (len(all_lines) + 1)
    
    return width, height

# 박스 그리는 함수
def draw_box(x, y, color, title, items=None):
    if items is None:
        items = []

    width, height = calculate_box_size(title, items)
    
    dwg.add(dwg.rect(insert=(x, y), size=(width, height), fill=color, stroke='black', stroke_width=2))
    dwg.add(dwg.text(title, insert=(x+10, y+25), font_size='18px', fill=TEXT_COLOR, font_weight='bold'))
    
    for i, item in enumerate(items):
        dwg.add(dwg.text(f'• {item}', insert=(x+15, y+50 + i*20), font_size='14px', fill=TEXT_COLOR))

    return width, height  # 화살표 연결용

# 화살표 마커 추가
marker = dwg.marker(id="arrow", insert=(10,5), size=(10,10), orient="auto")
marker.add(dwg.polygon(points=[(0,0),(10,5),(0,10)], fill="black"))
dwg.defs.add(marker)

def draw_arrow(start, end):
    dwg.add(dwg.line(start=start, end=end, stroke='black', stroke_width=2, marker_end="url(#arrow)"))


# --------- 박스 배치 ---------

# 고객 앱
app_w, app_h = draw_box(
    50, 50, APP_COLOR,
    '고객 모바일 앱 (React Native / Expo)',
    [
        '로그인 / 회원가입 (Supabase Auth)',
        '예약 조회 / 생성 / 취소',
        '정액제(수업권) 조회',
        '개인 피드백 확인',
        '결제 페이지 이동 (Toss / KG)',
        '푸시 알림 수신 (FCM / APNs)'
    ]
)

# Supabase
sb_w, sb_h = draw_box(
    50, 300, SUPABASE_COLOR,
    'Supabase (Auth / Postgres / Storage)',
    [
        'Auth: 이메일/휴대폰/OAuth 로그인',
        'DB: 회원, 예약, 결제, 정액제, 피드백 관리',
        'Storage: 영상 / 이미지 파일 저장',
        'Edge Functions: 필요 시 서버 로직'
    ]
)

# FastAPI
fastapi_x, fastapi_y = 500, 200
fastapi_w, fastapi_h = draw_box(
    fastapi_x, fastapi_y, FASTAPI_COLOR,
    'FastAPI 백엔드 (Python)',
    [
        '예약 관리: 생성/조회/변경/취소, 중복 확인, 예약 알림',
        '정액제/구독 관리: 차감/갱신/만료, 자동 알림',
        '결제 처리: 요청 전송 / 상태 관리',
        '알림/푸시: 예약, 정액제, 개인 알림',
        'DB 읽기/쓰기',
        'Storage URL 발급',
        'Background Worker / Scheduler'
    ]
)

# FastAPI 내부 하위 박스 (External API)
ext_w, ext_h = draw_box(
    fastapi_x + 20, fastapi_y + fastapi_h - 150,
    EXTERNAL_COLOR,
    '외부 서비스 연동',
    [
        'Toss / KG 결제',
        'KakaoTalk / SMS 알림',
        'FCM / APNs 푸시'
    ]
)

# 관리자 웹
admin_w, admin_h = draw_box(
    500, fastapi_y + fastapi_h + 50,
    ADMIN_COLOR,
    '관리자 웹 (Next.js / Vercel)',
    [
        '고객 관리: 회원 정보, 이용 내역',
        '예약 관리: 스케줄 확인 / 수정 / 취소',
        '정액제 / 결제 관리',
        '피드백 업로드 (영상/사진)',
        '대시보드 / 통계 확인'
    ]
)

# ---------- 화살표 연결 ----------
draw_arrow((50 + app_w, 150), (fastapi_x, 300))    # 앱 → FastAPI
draw_arrow((250, 300), (250, 350))                 # 앱 → Supabase
draw_arrow((50 + sb_w, 390), (fastapi_x, 390))     # Supabase → FastAPI
draw_arrow((fastapi_x + fastapi_w/2, fastapi_y + fastapi_h), (fastapi_x + fastapi_w/2, fastapi_y + fastapi_h + 50))  # FastAPI → 관리자

# 저장
dwg.save()
cairosvg.svg2png(url='architecture.svg', write_to='architecture.png')

print("자동 크기 조절된 SVG/PNG 생성 완료!")
