from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


# @ 글로벌 메모리 저장 heap
running = True


def handle_events():
    global running
    # @ ^^ 위를 선언하지 않을 시
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            # @ 로컬 메모리 stack
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


frame = 0
for x in range(0, 800, 5):

    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    update_canvas()

    # fill here
    handle_events()
    if not running:
        break


    frame = (frame + 1) % 8
    delay(0.05)


close_canvas()
