from pico2d import *

# 화면 크기 (배경 TUK_GROUND.png 크기와 동일)
TUK_WIDTH, TUK_HEIGHT = 1280, 1024

# 스프라이트 시트 정보 (한 프레임 100 x 100, 한 줄에 8프레임)
FRAME_WIDTH, FRAME_HEIGHT = 100, 100
FRAME_COUNT = 8

# 스프라이트 시트의 줄 위치 (clip_draw 의 bottom 값)
IDLE_RIGHT = 300
IDLE_LEFT = 200
RUN_RIGHT = 100
RUN_LEFT = 0

# 이동 속도 (프레임당 픽셀)
SPEED = 10

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running, dir_x, dir_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dir_x = 0  # 좌우 이동 방향 (-1: 왼쪽, 0: 정지, 1: 오른쪽)
dir_y = 0  # 상하 이동 방향 (-1: 아래, 0: 정지, 1: 위)
face = 1  # 바라보는 방향 (1: 오른쪽, -1: 왼쪽)

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if dir_x == 0:
        row = IDLE_RIGHT if face == 1 else IDLE_LEFT
    else:
        row = RUN_RIGHT if face == 1 else RUN_LEFT
    character.clip_draw(frame * FRAME_WIDTH, row, FRAME_WIDTH, FRAME_HEIGHT, x, y)
    update_canvas()
    handle_events()
    if dir_x != 0:
        face = dir_x
    x += dir_x * SPEED
    frame = (frame + 1) % FRAME_COUNT
    delay(0.05)

close_canvas()
