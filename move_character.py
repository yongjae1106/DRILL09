import math

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

# 이동 속도 (초당 픽셀)
SPEED = 300

# 애니메이션 속도 (초당 프레임)
ANIMATION_FPS = 12

# 화면 경계 (캐릭터 크기의 절반만큼 안쪽)
MIN_X, MAX_X = FRAME_WIDTH // 2, TUK_WIDTH - FRAME_WIDTH // 2
MIN_Y, MAX_Y = FRAME_HEIGHT // 2, TUK_HEIGHT - FRAME_HEIGHT // 2

# 방향키별 이동 방향 (dx, dy)
KEY_DIRECTIONS = {
    SDLK_RIGHT: (1, 0),
    SDLK_LEFT: (-1, 0),
    SDLK_UP: (0, 1),
    SDLK_DOWN: (0, -1),
}

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key in KEY_DIRECTIONS and event.key not in pressed_keys:
                pressed_keys.append(event.key)
        elif event.type == SDL_KEYUP:
            if event.key in pressed_keys:
                pressed_keys.remove(event.key)

    update_direction()


def update_direction():
    # 좌우, 상하 각각 가장 나중에 누른 방향키를 따른다
    global dir_x, dir_y

    dir_x, dir_y = 0, 0
    for key in pressed_keys:
        dx, dy = KEY_DIRECTIONS[key]
        if dx != 0:
            dir_x = dx
        if dy != 0:
            dir_y = dy


def update_character(dt):
    global x, y, face, frame

    if dir_x != 0:  # 위아래로만 움직일 때는 기존 방향 유지
        face = dir_x
    speed = SPEED
    if dir_x != 0 and dir_y != 0:  # 대각선 이동 시 속도가 √2 배가 되지 않도록 보정
        speed = SPEED / math.sqrt(2)
    x = clamp(MIN_X, x + dir_x * speed * dt, MAX_X)
    y = clamp(MIN_Y, y + dir_y * speed * dt, MAX_Y)
    frame = (frame + ANIMATION_FPS * dt) % FRAME_COUNT


def draw_character():
    if dir_x == 0 and dir_y == 0:
        row = IDLE_RIGHT if face == 1 else IDLE_LEFT
    else:
        row = RUN_RIGHT if face == 1 else RUN_LEFT
    character.clip_draw(int(frame) * FRAME_WIDTH, row, FRAME_WIDTH, FRAME_HEIGHT, x, y)


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dir_x = 0  # 좌우 이동 방향 (-1: 왼쪽, 0: 정지, 1: 오른쪽)
dir_y = 0  # 상하 이동 방향 (-1: 아래, 0: 정지, 1: 위)
face = 1  # 바라보는 방향 (1: 오른쪽, -1: 왼쪽)
pressed_keys = []  # 눌려 있는 방향키 (나중에 누른 키가 뒤쪽)
last_time = get_time()

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    draw_character()
    update_canvas()
    handle_events()
    current_time = get_time()
    dt = current_time - last_time  # 이전 프레임으로부터 경과 시간 (초)
    last_time = current_time
    update_character(dt)
    delay(0.01)

close_canvas()
