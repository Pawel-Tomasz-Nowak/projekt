import pygame as pg
from typing import Tuple, List
import sys
import Klasy


# Kolory
Color = Tuple[int, int, int]
WHITE: Color = (255, 255, 255)
MEDIUM_GRAY: Color = (100, 100, 100)
ORANGE: Color = (255, 131, 32)
BLACK: Color = (0, 0, 0)

# Zadeklaruj szerokość i wysokość okna.
screen_width: int = 400
screen_height: int = 750
window_size: tuple[int, int] = (screen_width, screen_height)



## ------------------------  SEKCJA DOTYCZĄCA EKRANU STARTOWEGO ------------------------
# Inicjalizacja Pygame
pg.init()

# Stworzenie okna. Ten obiekt jest ważny, ponieważ jest on klasy Surface, czyli powierzchni, na którą można dodawać figury.
intro_screen: pg.Surface = pg.display.set_mode(window_size)
font: pg.font.Font = pg.font.SysFont('Arial', 64)
small_font: pg.font.Font = pg.font.SysFont('Arial', 28)
mini_font: pg.font.Font = pg.font.SysFont('Arial', 18)

pg.display.set_caption("Moja Gra")   # Tytuł okna

def pokaz_ekran_startowy():
    start: bool = True
    tytul_text: pg.Surface = font.render("Nazwa gry", True, WHITE)
    graj_text: pg.Surface = font.render("GRAJ", True, WHITE)
    graj_rect: pg.Rect = graj_text.get_rect(center=(screen_width // 2, screen_height // 2))
    polecenie_text: pg.Surface = small_font.render("Kliknij GRAJ aby rozpocząć grę", True, MEDIUM_GRAY)
    polecenie_rect: pg.Rect = polecenie_text.get_rect(center=(screen_width // 2, screen_height // 2 + 100))
    instrukcja_lines: List[str] = [
        "Ustaw armatę pod odpowiednim kątem.",
        "Wystrzel piłkę klikając lewy przycisk myszy.",
        "Pamiętaj, że piłka może odbić się tylko dwa razy!",
        "Powodzenia!"
    ]

    instrukcja_texts: List[pg.Surface] = [mini_font.render(line, True, BLACK) for line in instrukcja_lines]
    instrukcja_rects: List[pg.Rect] = [instrukcja_text.get_rect(center=(screen_width // 2, screen_height // 2 + 200 + i * 30)) for i, instrukcja_text in enumerate(instrukcja_texts)]

    while start:
        for zdarzenie in pg.event.get():
            if zdarzenie.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif zdarzenie.type == pg.MOUSEBUTTONDOWN:
                if zdarzenie.button == 1 and graj_rect.collidepoint(zdarzenie.pos):
                    start = False

        intro_screen.fill(ORANGE)
        intro_screen.blit(tytul_text, (screen_width // 2 - tytul_text.get_width() // 2, 150))
        intro_screen.blit(graj_text, graj_rect)

        intro_screen.blit(polecenie_text, polecenie_rect)
        for instrukcja_text, instrukcja_rect in zip(instrukcja_texts, instrukcja_rects):
            intro_screen.blit(instrukcja_text, instrukcja_rect)

        pg.display.update()

pokaz_ekran_startowy()




# # ------------------------ SEKCJA GŁÓWNA GRY ------------------------
screen: pg.Surface = pg.display.set_mode(window_size)
running = True

screen.fill(color = ORANGE, )



#Narysuj pierwszą armatę wypionizowaną.
Prostokat1 =Klasy.Cannon(window_size[0]/2, window_size[1]-125, 50, 100,)
Prostokat1.NarysujArmatę(surface = screen, color = [0, 0,0])




while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
                #Poniższa linijka "usuwa" stare działo.
                Prostokat1.NarysujArmatę(surface = screen, color = ORANGE)

                #Tworzenie nowego działa.
                Prostokat1 = Klasy.Cannon(window_size[0]/2, window_size[1]-125, 50, 100)

                kat =  Klasy.Cannon.PoliczKąt(Prostokat1.x0, Prostokat1.y0)
                
                if kat is not False:
                    Prostokat1.slope = kat

                Prostokat1.NarysujArmatę(surface = screen, color = [0,0,0])



        pg.display.update()


