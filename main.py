import pygame as pg
import random

s_width = 800
s_height = 700
play_width = 300
play_height = 600
block_size = 30
top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height
number_screen = 0

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 51, 51)
GRAY = (192, 192, 192)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
LBLUE = (30, 144, 255)

S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
blocks_colors = ["block_colors/S.png", "block_colors/Z.png", "block_colors/I.png", "block_colors/O.png",
                 "block_colors/J.png", "block_colors/L.png", "block_colors/T.png"]
blocks = ["block/S.png", "block/Z.png", "block/I.png", "block/O.png", "block/J.png", "block/L.png", "block/T.png"]
play_button_pos = ((s_width - 150) // 2 + 75, 230 + 75, 75)
ranking_button_pos = (490, 500, 50)
information_button_pos = (670, 500, 50)
level_button_pos = (300, 500, 50)
setting_button_pos = (130, 500, 50)
button_pos = [play_button_pos, setting_button_pos, level_button_pos, ranking_button_pos, information_button_pos, ]
button_pause = {(pg.image.load('pause/play.png'), pg.image.load('pause/play_effect.png')): False,
                (pg.image.load('pause/sound.png'), pg.image.load('pause/sound_effect.png'),
                 pg.image.load('pause/no_sound.png'), pg.image.load('pause/no_sound_effect.png')): False,
                (pg.image.load('pause/home.png'), pg.image.load('pause/home_effect.png')): False}
button_pause_pos = [(15 + 40, 90 + 40, 40), (110 + 40, 90 + 40, 40), (205 + 40, 90 + 40, 40)]

button_lose = {(pg.image.load('lose/undo.png'), pg.image.load('lose/undo_effect.png')): False,
               (pg.image.load('lose/home.png'), pg.image.load('lose/home_effect.png')): False}
button_lose_pos = [(15 + 40, 200 + 40, 40), (110 + 40, 200 + 40, 40)]
rank_list = [int(i) for i in open('score_txt', 'r').read().split()]
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((s_width, s_height))
pg.display.set_caption('T E T I S')
pg.mixer.init()
pg.mixer.music.load("sound/nen.wav")
pg.mixer.music.play(-1, 0.0)
yes_volume = True


def check_pos_in_circle(cir_pos, mouse_pos):
    return (mouse_pos[0] - cir_pos[0]) ** 2 + (mouse_pos[1] - cir_pos[1]) ** 2 <= cir_pos[2] ** 2


class OptionBox:

    def __init__(self, x, y, w, h, choose, list_level, option_list, pos_option_list=(), selected=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.circle_pos = (x + 50, y + 50, 50)
        self.level_list = list_level
        self.option_list = option_list
        self.selected = selected
        self.choose = choose
        self.rect = pg.Rect(self.x - 10, self.y + self.choose[0].get_height() - 20, 180 + len(self.option_list) * 80,
                            160)
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1
        self.pos_clicked = (x + 50, y + 50)
        self.pos_option_list = pos_option_list
        self.effect = False

    def draw(self, surface):
        index = 1 if self.effect else 0
        re = 0 if index == 0 else 10
        surface.blit(self.choose[index], (self.x + re, self.y + re))
        if self.draw_menu:
            pg.draw.rect(surface, WHITE,
                         (self.x, self.y + self.choose[0].get_height(), 180 + len(self.option_list) * 80, 160))
            for i, value in enumerate(self.option_list, 0):
                surface.blit(value, (self.pos_option_list[i]))

    def update(self, list_event):
        mouse_pos = pg.mouse.get_pos()
        self.menu_active = check_pos_in_circle(self.circle_pos, mouse_pos)
        self.active_option = -1
        if self.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
            self.menu_active = True if check_pos_in_circle((self.x + 50, self.y + 50, 50), self.pos_clicked) else False
            for i in range(len(self.option_list)):
                if check_pos_in_circle((self.pos_option_list[i][0] + 40, self.pos_option_list[i][1] + 40, 40),
                                       mouse_pos):
                    self.active_option = i
                    break

        if not self.menu_active and self.active_option == -1:
            self.draw_menu = False

        for event_item in list_event:
            if event_item.type == pg.MOUSEMOTION:
                if check_pos_in_circle(level_button_pos, pg.mouse.get_pos()):
                    self.effect = True
                else:
                    self.effect = False
            elif event_item.type == pg.MOUSEBUTTONDOWN:
                if self.draw_menu and self.active_option >= 0:
                    self.selected = self.active_option
                    self.draw_menu = False
                    self.choose[0] = self.level_list[self.active_option]
                    return self.active_option
                if self.menu_active:
                    self.draw_menu = not self.draw_menu
            elif event_item.type == pg.MOUSEBUTTONUP:
                self.pos_clicked = pg.mouse.get_pos()
        return -1


def draw_rank(surface, score_list):
    score_list.sort(reverse = True)
    pg.draw.rect(surface, WHITE, (0, 0, s_width, s_height))
    rank = pg.image.load('rank/ranking.png')
    rank_title = pg.font.Font('font/pridib.ttf', 50).render('Bảng xếp hạng', True, BLACK)
    surface_title = pg.Surface((rank.get_width() + rank_title.get_width() + 20, rank.get_height()))
    surface_title.fill(WHITE)
    surface_title.blit(rank, (0, 0))
    surface_title.blit(rank_title, (rank.get_width() + 10, surface_title.get_height() - rank_title.get_height()))
    surface.blit(surface_title, ((s_width - surface_title.get_width()) // 2, 30))

    surface_list = pg.Surface((rank.get_width() + rank_title.get_width() + 20, 500))
    surface_list.fill(WHITE)
    h_format = 70
    for i in range(5):
        rank_item = pg.image.load('rank/number-' + str(i + 1) + '.png')
        score = pg.font.Font('font/pridib.ttf', 40).render(str(score_list[i]), True, BLACK)
        surface_list.blit(rank_item, (0, h_format * i + 20 * i))
        surface_list.blit(score, (
            rank_item.get_width() + 20, rank_item.get_height() // 2 + h_format * i - score.get_height() // 2 + 20 * i))

    surface.blit(surface_list, ((surface.get_width() - surface_list.get_width()) // 2, 200))


def draw_information_game(surface):
    pg.draw.rect(surface, WHITE, (0, 0, s_width, s_height))
    ptit_logo = pg.image.load('picture_start/ptitlogo.png')
    name_vi = pg.font.Font('font/pridib.ttf', 25).render('Học viện Công Nghệ Bưu Chính Viễn Thông'.upper(), True, BLACK)
    name_en = pg.font.Font('font/pridil.ttf', 20).render('Posts and Telecommunications Institute of Technology', True, RED)
    name_project = pg.font.Font('font/pridil.ttf', 30).render('Đồ án :', True, BLACK)
    name_game = pg.font.Font('font/monoton.ttf', 80).render('GAME  TETRIS', True, BLACK)
    name_teacher = pg.font.Font('font/pridib.ttf', 20).render('Giảng viên hướng dẫn :', True, BLACK)
    name_info_teacher = pg.font.Font('font/pridil.ttf', 20).render('TS. Nguyễn Thị Tuyết Hải', True, BLACK)
    name_student = pg.font.Font('font/pridib.ttf', 20).render('Sinh viên thực hiện :', True, BLACK)
    name_info_student1 = pg.font.Font('font/pridil.ttf', 20).render('Nguyễn Hữu Trưởng - N19DCCN221', True, BLACK)
    name_info_student2 = pg.font.Font('font/pridil.ttf', 20).render('Nguyễn Nhật Thanh - N19DCCN190', True, BLACK)
    day_info = pg.font.Font('font/pridil.ttf', 20).render('TP Hồ Chí Minh Ngày 24 Tháng 12 Năm 2021', True, BLACK)
    surface_ptit = pg.Surface((ptit_logo.get_width() + name_vi.get_width() + 20, ptit_logo.get_height()))
    surface_infor = pg.Surface((max(name_game.get_width() + 20,
                                    name_teacher.get_width() + name_info_teacher.get_width() + 20),
                                name_game.get_height() * 5 + name_project.get_height() + name_game.get_height() + 30))
    x_format = (surface_infor.get_width() - name_teacher.get_width() - name_info_student1.get_width()) // 2
    y_format = (
                       surface_infor.get_width() - name_teacher.get_width() - name_info_student1.get_width()) // 2 + name_teacher.get_width() + 10
    h_format = 0
    surface_infor.fill(WHITE)
    surface_infor.blit(name_project, ((surface_infor.get_width() - name_project.get_width()) // 2, h_format))
    h_format += name_project.get_height()
    surface_infor.blit(name_game, ((surface_infor.get_width() - name_game.get_width()) // 2, h_format))
    h_format += name_game.get_height() + 50
    surface_infor.blit(name_teacher, (x_format, h_format))
    surface_infor.blit(name_info_teacher, (y_format, h_format))
    h_format += name_info_teacher.get_height()
    surface_infor.blit(name_student, (x_format, h_format))
    surface_infor.blit(name_info_student1, (y_format, h_format))
    h_format += name_info_student1.get_height()
    surface_infor.blit(name_info_student2, (y_format, h_format))
    h_format += 150
    surface_infor.blit(day_info, ((surface_infor.get_width() - day_info.get_width()) // 2, h_format))

    surface_ptit.fill(WHITE)
    surface_ptit.blit(ptit_logo, (0, 0))
    surface_ptit.blit(name_vi, (ptit_logo.get_width() + 10, ptit_logo.get_height() // 2 - name_vi.get_height()))
    surface_ptit.blit(name_en, (ptit_logo.get_width() + 10, ptit_logo.get_height() // 2))
    surface.blit(surface_ptit, ((s_width - surface_ptit.get_width()) // 2, 30))

    surface.blit(surface_infor, ((surface.get_width() - surface_infor.get_width()) // 2, 200))


class Piece(object):
    rows = 20
    columns = 10

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shapes.index(shape)
        self.rotation = 0


def create_grid(locked_positions={}):
    grid = [[-1 for _ in range(10)] for _ in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                c = locked_positions[(j, i)]
                grid[i][j] = c
    return grid


def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions


def valid_space(shape, grid):
    accepted_positions = []
    for i in range(20):
        for j in range(10):
            if grid[i][j] == -1:
                accepted_positions.append((j, i))
    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False

    return True


def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False


def get_shape():
    global shapes
    return Piece(5, 0, random.choice(shapes))


def draw_grid(surface, row, col):
    sx = top_left_x
    sy = top_left_y
    for i in range(row):
        pg.draw.line(surface, GRAY, (sx, sy + i * 30), (sx + play_width, sy + i * 30))
        for j in range(col):
            pg.draw.line(surface, GRAY, (sx + j * 30, sy), (sx + j * 30, sy + play_height))


def clear_rows(grid, locked):
    inc = 0
    ind_delete_row = []
    for i in range(len(grid) - 1, -1, -1):
        row = grid[i]
        # Clear if there is no white pixels in the row
        if -1 not in row:
            inc += 1
            ind_delete_row.append(i)
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    if inc > 0:
        clear_row_sound = pg.mixer.Sound("sound/clear.wav")
        clear_row_sound.play()
        for ind in ind_delete_row[::-1]:
            for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
                x, y = key
                if y < ind:
                    newKey = (x, y + 1)
                    locked[newKey] = locked.pop(key)
    return ind_delete_row


def draw_right_side(shape, surface):
    x_next_shape = top_left_x + play_width + 25
    y_next_shape = top_left_y
    surface.blit(pg.image.load('picture_start/paper.png'), (x_next_shape, y_next_shape))
    shape_pic = pg.image.load(blocks[shapes.index(shape.shape)])
    surface.blit(shape_pic, (
        x_next_shape + (200 - shape_pic.get_width()) // 2, y_next_shape + (200 - shape_pic.get_height()) // 2 + 10))


def draw_score_board(surface, score):
    surface_score = pg.Surface((200, 170))
    surface_score.fill(WHITE)
    black_board = pg.image.load('picture_start/blackboard.png')
    teacher = pg.image.load('picture_start/teacher.png')
    surface_score.blit(black_board, (50, 0))
    surface_score.blit(teacher, (0, 70))
    score_text = pg.font.SysFont('comicsans', 30).render(str(score), True, WHITE)
    surface_score.blit(score_text, (50 + (150 - score_text.get_width()) // 2, 30))
    surface.blit(surface_score, (20, top_left_y + 25))


def draw_window(surface, score):
    pg.draw.rect(surface, WHITE, (0, 0, s_width, s_height // 2))
    draw_score_board(surface, score)
    title = pg.image.load('picture_start/tetris.png')
    screen.blit(title, (top_left_x + play_width / 2 - (title.get_width() / 2), 17))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == -1:
                pg.draw.rect(surface, (96, 96, 96), (top_left_x + j * 30, top_left_y + i * 30, 30, 30), 0)
            else:
                image = pg.image.load(blocks_colors[grid[i][j]])
                image = pg.transform.scale(image, (30, 30))
                surface.blit(image, (top_left_x + j * 30, top_left_y + i * 30))
    draw_grid(surface, 20, 10)
    pg.draw.rect(surface, (96, 96, 96), (top_left_x - 2, top_left_y - 2, play_width + 5, play_height + 5), 5)


def effect_del_rows(surface, ind_del_rows, effect, score):
    ind_del_rows.sort()
    pg.draw.rect(surface, WHITE, (0, 0, s_width, s_height // 2))
    draw_score_board(surface, score)
    title = pg.image.load('picture_start/tetris.png')
    surface.blit(title, (top_left_x + play_width / 2 - (title.get_width() / 2), 17))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == -1:
                pg.draw.rect(surface, (96, 96, 96), (top_left_x + j * 30, top_left_y + i * 30, 30, 30), 0)
            else:
                image = pg.image.load(blocks_colors[grid[i][j]])
                image = pg.transform.scale(image, (30, 30))
                surface.blit(image, (top_left_x + j * 30, top_left_y + i * 30))
    for i in ind_del_rows:
        surface.blit(pg.transform.scale(effect, (play_width, 30)),
                     ((s_width - play_width) // 2, top_left_y + 30 * i))
    draw_grid(surface, 20, 10)
    pg.draw.rect(surface, (96, 96, 96), (top_left_x - 2, top_left_y - 2, play_width + 5, play_height + 5), 5)


def calculate_level_and_fall_speed(score, level_start):
    speed_up = int(score / 100)
    fall_speed = 0
    level = 0
    if level_start == 0:
        level = 0
        fall_speed = 0.35 - (speed_up * 0.01)
        if fall_speed <= 0.25:
            level = 1
        elif fall_speed <= 0.15:
            level = 2
    elif level_start == 1:
        level = 1
        fall_speed = 0.25 - (speed_up * 0.01)
        if fall_speed <= 0.15:
            level = 2
    elif level_start == 2:
        level = 2
        fall_speed = 0.15 - (speed_up * 0.01)
    if fall_speed < 0.05:
        level = 2
        fall_speed = 0.05
    return fall_speed, level


def pause_screen():
    global yes_volume
    text = pg.image.load('pause/text.png')
    background = pg.image.load('picture_start/frame.png')
    surface_pause = pg.Surface((background.get_width(), background.get_height()))
    surface_pause.fill(WHITE)
    pause = True
    while pause:
        surface_pause.blit(background, (0, 0))
        surface_pause.blit(text, ((300 - text.get_width()) // 2, 20))
        for i, button_item in enumerate(button_pause, 0):
            idx = 1 if button_pause.get(button_item) else 0
            r = 0 if idx == 0 else 5
            surface_pause.blit(button_item[idx + 2 if not yes_volume and i == 1 else idx],
                               (button_pause_pos[i][0] - 40 + r, button_pause_pos[i][1] - 40 + r))
        for event_item in pg.event.get():
            if event_item.type == pg.QUIT:
                pg.quit()
                quit()
            if event_item.type == pg.KEYDOWN:
                if event_item.key == pg.K_c:
                    pause = False
                if event_item.key == pg.K_q:
                    return False
            if event_item.type == pg.MOUSEMOTION:
                for i, button_item in enumerate(button_pause, 0):
                    if check_pos_in_circle((button_pause_pos[i][0] + (s_width - 300) // 2,
                                            button_pause_pos[i][1] + (s_height - 300) // 2, 40), pg.mouse.get_pos()):
                        button_pause[button_item] = True
                    else:
                        button_pause[button_item] = False
            if event_item.type == pg.MOUSEBUTTONDOWN:
                for i, button_item in enumerate(button_pause, 0):
                    if check_pos_in_circle((button_pause_pos[i][0] + (s_width - 300) // 2,
                                            button_pause_pos[i][1] + (s_height - 300) // 2, 40), pg.mouse.get_pos()):
                        if i == 0:
                            for item in button_pause:
                                button_pause[item] = False
                            pause = False
                        elif i == 1:
                            yes_volume = not yes_volume
                            pg.mixer.music.set_volume(1.0 if yes_volume else 0.0)
                        else:
                            return 0
        screen.blit(surface_pause, ((s_width - 300) // 2, (s_height - 300) // 2))
        pg.display.update()

    for button_item in button_pause:
        button_pause[button_item] = False
    return -1


def lose_screen(surface, score):
    pg.mixer.music.stop()
    loose_sound = pg.mixer.Sound("sound/game_over.wav")
    loose_sound.play()
    pause = True
    surface_lose = pg.Surface((210, 300))
    background = pg.transform.scale(pg.image.load('lose/background.png'), (210, 300))
    title = pg.image.load('lose/text.png')
    score_text = pg.font.SysFont('comicsans', 50).render(str(score), True, BLACK)

    while pause:
        for event_item in pg.event.get():
            if event_item.type == pg.QUIT:
                pg.quit()
                quit()
            if event_item.type == pg.MOUSEMOTION:
                for i, button_item in enumerate(button_lose, 0):
                    if check_pos_in_circle((button_lose_pos[i][0] + (s_width - 210) // 2,
                                            button_lose_pos[i][1] + (s_height - 300) // 2, 40), pg.mouse.get_pos()):
                        button_lose[button_item] = True
                    else:
                        button_lose[button_item] = False
            if event_item.type == pg.MOUSEBUTTONDOWN:
                for i, button_item in enumerate(button_pause, 0):
                    if check_pos_in_circle((button_lose_pos[i][0] + (s_width - 210) // 2,
                                            button_lose_pos[i][1] + (s_height - 300) // 2, 40), pg.mouse.get_pos()):
                        if i == 0:
                            return 3
                        else:
                            return 0

        surface_lose.blit(background, (0, 0))
        surface_lose.blit(title, ((210 - title.get_width()) // 2, 20))
        surface_lose.blit(score_text, ((210 - score_text.get_width()) // 2, 100))
        for i, button_item in enumerate(button_lose, 0):
            index = 1 if button_lose.get(button_item) else 0
            r = 0 if index == 0 else 5
            surface_lose.blit(button_item[index],
                              (button_lose_pos[i][0] - 40 + r, button_lose_pos[i][1] - 40 + r))
        screen.blit(surface_lose, ((s_width - 210) // 2, (s_height - 300) // 2))
        pg.display.update()

    for button_item in button_lose:
        button_lose[button_item] = False
    return 3


def play_game(level_start):
    global grid, x, rank_list
    score = 0
    locked_positions = {}
    grid = create_grid(locked_positions)
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pg.time.Clock()
    fall_time = 0
    fall_speed, level = calculate_level_and_fall_speed(score, level_start)
    effect = False
    pause_button = pg.image.load('pause/pause.png')
    pause_button_effect = pg.image.load('pause/pause_effect.png')
    check_out = -1
    while run:
        pg.draw.rect(screen, WHITE, (s_width - 120, s_height - 120, 120, 120))
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()
        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event_item in pg.event.get():
            if event_item.type == pg.QUIT:
                run = False
                pg.display.quit()
                quit()
            if event_item.type == pg.MOUSEMOTION:
                if check_pos_in_circle((s_width - 80 - 20 + 40, s_height - 80 - 20 + 40, 40), pg.mouse.get_pos()):
                    effect = True
                else:
                    effect = False
            if event_item.type == pg.MOUSEBUTTONDOWN:
                if check_pos_in_circle((s_width - 80 - 20 + 40, s_height - 80 - 20 + 40, 40), pg.mouse.get_pos()):
                    effect = False
                    check_out = pause_screen()
                    if check_out == 0:
                        return 0
            if event_item.type == pg.KEYDOWN:
                if event_item.key == pg.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1

                elif event_item.key == pg.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                elif event_item.key == pg.K_UP:
                    # rotate shape
                    current_piece.rotation = (current_piece.rotation + 1) % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = (current_piece.rotation - 1) % len(current_piece.shape)
                elif event_item.key == pg.K_DOWN:
                    # move shape down
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1

        shape_pos = convert_shape_format(current_piece)

        for index in range(len(shape_pos)):
            x, y = shape_pos[index]
            if y > -1:
                grid[y][x] = current_piece.color
        ind_del_rows = []
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            ind_del_rows = clear_rows(grid, locked_positions)
            score += 10 * len(ind_del_rows)
            fall_speed, level = calculate_level_and_fall_speed(score, level_start)

        if len(ind_del_rows) > 0:
            t = pg.time.get_ticks()
            while t + 250 >= pg.time.get_ticks():
                effect_del_rows(screen, ind_del_rows, pg.image.load('picture_start/e1.png'), score)
                draw_right_side(next_piece, screen)
                pg.display.update()
            while t + 500 >= pg.time.get_ticks():
                effect_del_rows(screen, ind_del_rows, pg.image.load('picture_start/e2.png'), score)
                draw_right_side(next_piece, screen)
                pg.display.update()
            while t + 750 >= pg.time.get_ticks():
                effect_del_rows(screen, ind_del_rows, pg.image.load('picture_start/e1.png'), score)
                draw_right_side(next_piece, screen)
                pg.display.update()
        draw_window(screen, score)
        draw_right_side(next_piece, screen)
        screen.blit(pause_button_effect if effect else pause_button,
                    (s_width - pause_button.get_width() - 20 + (5 if effect else 0),
                     s_height - pause_button.get_height() - 20 + (5 if effect else 0)))
        pg.display.update()

        if check_lost(locked_positions):
            run = False
    rank_list.sort(reverse=True)
    rank_list[-1] = score if score > rank_list[-1] else rank_list[-1]
    str_rank_list = " ".join([str(item) for item in rank_list])
    with open('score_txt', 'w+') as f:
        f.write(str_rank_list)
    check_out = lose_screen(screen, score)
    pg.display.update()
    pg.mixer.music.play()
    if check_out == 0:
        return 0
    else:
        return 3


if __name__ == '__main__':
    score = 0
    yes_level = False
    init_level = 0
    move = 0
    count = 0
    select_level = 0
    label = pg.image.load('picture_start/tetris_big.png')

    button_list = {(pg.image.load('picture_start/play.png'), pg.image.load('picture_start/play_effect.png')): False,
                   (pg.image.load('picture_start/volume_on.png'), pg.image.load('picture_start/volume_on_effect.png'),
                    pg.image.load('picture_start/volume_off.png'), pg.image.load('picture_start/volume_off_effect.png')): False,
                   (pg.image.load('level/level.png'), pg.image.load('level/level_effect.png')): False,
                   (pg.image.load('rank/ranking.png'), pg.image.load('rank/ranking_effect.png')): False,
                   (pg.image.load('picture_start/information.png'), pg.image.load(
                       'picture_start/information_effect.png')): False}

    level_list = OptionBox(250, 450, 100, 100,
                           [pg.image.load('level/level.png'), pg.image.load('level/level_effect.png')], (
                               pg.image.load('level/easy.png'), pg.image.load('level/medium.png'),
                               pg.image.load('level/hard.png')),
                           (pg.image.load('level/easy1.png'), pg.image.load('level/medium1.png'),
                            pg.image.load('level/hard1.png')), ((305, 570), (430, 570), (555, 570)))
    pg.time.set_timer(pg.USEREVENT, 40)

    while True:
        clock.tick(120)
        event_list = pg.event.get()
        for event in event_list:
            if event.type == pg.QUIT:
                pg.display.quit()
                quit()

            if event.type == pg.MOUSEMOTION:
                for i, button in enumerate(button_list, 0):
                    if check_pos_in_circle(button_pos[i], pg.mouse.get_pos()):
                        button_list[button] = True
                    else:
                        button_list[button] = False

            if event.type == pg.MOUSEBUTTONDOWN:
                if check_pos_in_circle(play_button_pos, pg.mouse.get_pos()):
                    number_screen = 3
                elif check_pos_in_circle(ranking_button_pos, pg.mouse.get_pos()) and number_screen == 0:
                    number_screen = 2
                elif check_pos_in_circle(information_button_pos, pg.mouse.get_pos()) and number_screen == 0:
                    number_screen = 1
                elif check_pos_in_circle(setting_button_pos, pg.mouse.get_pos()):
                    yes_volume = not yes_volume
                    pg.mixer.music.set_volume(1.0 if yes_volume else 0.0)
                else:
                    number_screen = 0

            if event.type == pg.USEREVENT:
                if count == 0:
                    move += 1
                    if move == 10:
                        count = 1
                else:
                    move -= 1
                    if move == 0:
                        count = 0
        screen.fill(WHITE)
        screen.blit(label, ((s_width - label.get_width()) // 2, 30 + move))

        selected_level = level_list.update(event_list)
        if selected_level >= 0:
            init_level = selected_level
        level_list.draw(screen)
        if number_screen == 0:
            for i, button in enumerate(button_list, 0):
                if i == 2:
                    continue
                idx = 1 if button_list.get(button) else 0
                radius = 75 if i == 0 else 50
                radius_effect = 0 if idx == 0 else 5
                screen.blit(button[idx + 2 if not yes_volume and i == 1 else idx],
                            (button_pos[i][0] - radius + radius_effect, button_pos[i][1] - radius + radius_effect))

        elif number_screen == 1:
            draw_information_game(screen)
        elif number_screen == 2:
            draw_rank(screen, rank_list)
        elif number_screen == 3:
            number_screen = play_game(init_level)
        pg.display.update()
