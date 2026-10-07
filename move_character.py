from pico2d import *

# 화면 크기 (배경 TUK_GROUND.png 크기와 동일)
TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')

clear_canvas()
tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
update_canvas()
delay(2)

close_canvas()
