'''
import pygame as pg
import table as tb
import blocks as bk
import colors as col

GAME_SPEED     = 500
SPEED_INC_TICK = 50
LINES_INC_TICK = 10
LEVEL          = 1
REMOVED_LINES  = 0
MAX_LEVEL      = 10
FPS            = 100

def delay(ticks):
    return (ticks % GAME_SPEED) >= GAME_SPEED-10
def incSpeed(remlines):
    global GAME_SPEED
    global LEVEL

    if LEVEL < MAX_LEVEL:
        if remlines / (LEVEL*LINES_INC_TICK) == 1:
            LEVEL += 1
            GAME_SPEED -= SPEED_INC_TICK
            return True
        return False

def updateInfo(nb):
    global LEVEL_NUM_TEXT
    global LINES_NUM_TEXT
    global infosurface

    LEVEL_NUM_TEXT = font.render(str(LEVEL),True,col.WHITE)
    LINES_NUM_TEXT = font.render(str(REMOVED_LINES),True,col.WHITE)
    infosurface.fill(col.GREY_DARK)
    infosurface.blit(LEVEL_TEXT,LEVEL_TEXT_OFFSET)
    infosurface.blit(LEVEL_NUM_TEXT,LEVEL_NUM_TEXT_OFFSET)
    infosurface.blit(LINES_TEXT,LINES_TEXT_OFFSET)
    infosurface.blit(LINES_NUM_TEXT,LINES_NUM_TEXT_OFFSET)
    nb.show(infosurface,NEXT_BLOCK_OFFSET,20,INF_BLOCK_SIZE)

pg.init()
pg.mixer.init()
sndblockplaced = pg.mixer.Sound("sounds/block_placed.wav")
sndblockrotate = pg.mixer.Sound("sounds/block_rotate.wav")
sndremovelines = pg.mixer.Sound("sounds/remove_lines.wav")
sndlevelup     = pg.mixer.Sound("sounds/level_up.wav")
sndgameover    = pg.mixer.Sound("sounds/game_over.wav")
clock          = pg.time.Clock()
pg.display.set_caption("yat - yet another tetris")
pg.key.set_repeat(10,50)

INFO_SURFACE_HEIGHT   = 105
FONT_SIZE             = 30
FONT_SIZE_GAME_OVER   = 60
UPPER_OFFSET          = 20
LEFT_OFFSET           = 10
INF_BLOCK_SIZE        = 20
font                  = pg.font.SysFont(pg.font.get_default_font(),FONT_SIZE)
font_game_over        = pg.font.SysFont(pg.font.get_default_font(),
                                        FONT_SIZE_GAME_OVER)
LEVEL_TEXT            = font.render("Level : ",True,col.WHITE)
LINES_TEXT            = font.render("Lines : ",True,col.WHITE)
LEVEL_TEXT_OFFSET     = (LEFT_OFFSET,UPPER_OFFSET)
LEVEL_NUM_TEXT_OFFSET = (70+LEFT_OFFSET,UPPER_OFFSET)
LINES_TEXT_OFFSET     = (LEFT_OFFSET,INFO_SURFACE_HEIGHT-40)
LINES_NUM_TEXT_OFFSET = (70+LEFT_OFFSET,INFO_SURFACE_HEIGHT-40)
NEXT_BLOCK_OFFSET     = tb.BLOCK_SIZE*tb.WIDTH - INF_BLOCK_SIZE * 5

GAME_OVER_TEXT        = font_game_over.render("GAME OVER",True,col.WHITE)
GAME_OVER_TEXT_OFFSET = ((tb.BLOCK_SIZE*tb.WIDTH/2)-120,(tb.BLOCK_SIZE*tb.
                                                         HEIGHT/2)-50)
screen         = pg.display.set_mode((tb.BLOCK_SIZE*tb.WIDTH,tb.
                                      BLOCK_SIZE*tb.HEIGHT+INFO_SURFACE_HEIGHT))
tablesurface   = screen.subsurface((0,INFO_SURFACE_HEIGHT,tb.BLOCK_SIZE*tb.
                                    WIDTH,tb.BLOCK_SIZE*tb.HEIGHT))
infosurface    = screen.subsurface((0,0,tb.BLOCK_SIZE*tb.WIDTH,
                                    INFO_SURFACE_HEIGHT))

BLOCK_SPAWN_POS = (0,(tb.WIDTH/2)-1)

t     = tb.table(tablesurface)
b     = bk.block(BLOCK_SPAWN_POS)
nextb = bk.block(BLOCK_SPAWN_POS)

updateInfo(nextb)

running = True
while running:
    clock.tick_busy_loop(FPS)
    t.adBlock(b.getPosList(),b.getType())
    t.show()

    if delay(pg.time.get_ticks()):
        if b.canMovDown(t.getHeight(),t.getOcupPosList(b.getPosList())):
            t.adBlock(b.getPosList(),bk.E)
            b.movDown()
        else:
            t.adBlock(b.getPosList(),b.getType())
            sndblockplaced.play()
            retval = t.delFullLines()
            if retval != 0:
                sndremovelines.play()
                REMOVED_LINES += retval
                if incSpeed(REMOVED_LINES):
                    sndlevelup.play()
            b.__init__(BLOCK_SPAWN_POS,nextb.getType())
            nextb = bk.block(BLOCK_SPAWN_POS)
            updateInfo(nextb)

            if t.gameOver(b.getPosList()):
                t.adBlock(b.getPosList(),b.getType())
                t.show()
                running = False
'''


