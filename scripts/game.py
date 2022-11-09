import pygame as pg

HEIGHT = 256
WIDTH = 256
FPS = 60

def main():
    pg.init()
    clock = pg.time.Clock()
    displaysurface = pg.display.set_mode((WIDTH, HEIGHT), pg.SCALED)
    pg.display.set_caption("Reverse Asteroids")

     # Main Loop
    updating = True
    while updating:
        clock.tick(FPS)

        # Handle Input Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                updating = False

        displaysurface.fill((0, 0, 0))

        pg.display.flip()

    pg.quit()

# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()