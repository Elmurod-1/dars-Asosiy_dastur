"""Assalomu alekum"""

import pygame, pygame.gfxdraw, json, os
# from math import sqrt
# from time import sleep


"""o'zgarmaslar"""

# ranglar
oq = (255, 255, 255)
qora = (0, 0, 0)
qizil = (220, 0, 0)
kok = (0, 0, 220)

# o'lchamlar
balandlik = 800
kenglik = 1200

pygame.init()

pks = 60
aa = pygame.time.Clock()
qq = pygame.time
rt = [".jpg", ".jpeg", ".png", ".gif", ".pcx", ".tga", ".tif", ".pbm", ".xpm", ".JPG"]
keys = [23, 4, 6, 8, 24, 20, 28, 88888798878787, 58, 59, 60, 61, 62]

mm = os.getcwd()
# son, vaqt, bosh = False, 100, True
pygame.display.set_caption("Zarrin nihol", "rasm.jpg")
d = pygame.image.load("rasm.jpg")
pygame.display.set_icon(d)


class asosiy_oyna(object):
    def __init__(self):
        self.b = pygame.mixer.music
        self.b.load("Audio.wav")
        # self.soniya = 0
        self.biri = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.chizma_oyna = pygame.Surface((1200, 800))
        self.mn = [(0, 0), (0, 0)]
        self.qalinligi = 1
        self.rasmlar = [i for i in os.listdir(mm) if (i[i.index("."):] if "." in i else "4") in rt]
        self.rasm_j = [len(self.rasmlar), 0, 0]
        self.yuklandi = list()
        self.qalams = 0, 0
        self.oyna = pygame.display.set_mode((kenglik, balandlik), flags=0|pygame.RESIZABLE)
        self.oldingi_rasm = pygame.Surface((10, 10))
        self.oldingi_rasm.fill("white")
        self.ortga = []
        self.ort1 = 0
        self.soniya = qq.get_ticks()

    def asosiy(self):
        self.oyna.fill(oq)
        self.chizma_oyna.fill(oq)
        ww = True
        k = 0
        with open("dars.json","r") as e:
            self.s = json.loads(e.read())
        while ww:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    self.b.stop()
                    ww = False

                """elif i.type == pygame.KEYDOWN:
                    elif i.mod & pygame.KMOD_ALT:
                    if not son:
                        self.soniya = pygame.time.get_ticks()-vaqt
                        son = True
                        self.yon_o()
                    else:
                        vaqt = pygame.time.get_ticks()
                        son = False
                        self.yon_o()
                    
                    if i.scancode in (29, 26) and i.mod == 4160:
                        try:
                            if i.scancode == 29 and self.ort1 > 0:
                                self.ort1 = (self.ort1 - 1)
                                self.saqlash.append(("ort", True))
                            elif i.scancode == 26 and self.ort1 < len(self.ortga):
                                self.ort1 = (self.ort1 + 1)
                                self.saqlash.append(("ort", False))
                            self.chizma_oyna.blit(self.ortga[self.ort1], (0, 0))
                        except:
                            pass

                    if self.biri[6] == 1 and 'z' >= i.unicode >= ' ':
                        self.satr += i.unicode

                elif i.type == pygame.MOUSEWHEEL:
                    if pygame.mouse.get_pos()[0] >= 1100:
                        if i.y == 1 and (self.rasm_j[0]-self.rasm_j[1]) >= 9:
                            self.rasm_j[1] += 1 if self.rasm_j[2] == -100 else 0
                            self.rasm_j[2] = -25 if (self.rasm_j[2] == -100) else (self.rasm_j[2]-25)

                        elif i.y == -1 and ((self.rasm_j[1] > 0) or self.rasm_j[2] < 0):
                            self.rasm_j[1] -= 1 if self.rasm_j[2] == 0 else 0
                            self.rasm_j[2] = -75 if (self.rasm_j[2] == 0) else (self.rasm_j[2]+25)

                        self.rasm()"""
            self.oyna.fill(oq)
            self.oyna.blit(self.chizma_oyna, (0, 0))
            d = qq.get_ticks() - self.soniya
            try:

                if (s:=self.s[k])[-1] <= d:
                    print(s)
                    if s[0] == "yuklash":
                        self.yuklash(s[1])
                    elif s[0] == "rasm_chiqarish":
                        self.rasm_chiqarish(s[1])
                    elif s[0] == "yozish":
                        self.yozish(s[1], s[2], s[3], s[4], a=False)
                    elif s[0] == "yozish1":
                        self.yozish(s[1], s[2], s[3], s[4])
                    elif s[0] == "chizma":
                        self.chizma(s[1], s[2], s[3])
                    elif s[0] == "qalam":
                        self.qalam(s[1], s[2], s[3])
                    elif s[0] == "play":
                        self.b.play()
                    elif s[0] == "toza":
                        self.oyna.fill(oq)
                    elif s[0] == "ort":
                        pass
                        # self.ort()
                    k += 1
            except:
                print(255)
                pass

            pygame.display.flip()
            aa.tick(pks)

    def yozuv_yozish(self, text, olcham, rang=qora):
        z = pygame.font.Font('C:\Windows\Fonts\courbd.ttf', olcham)
        return pygame.font.Font.render(z, text, True, rang)

    def shakl_chizish(self, oyna, a, rang, qalin):
        if a[0] == 0:
            pygame.draw.rect(oyna, rang, (a[1][0], a[1][1], a[2][0] - a[1][0], a[2][1] - a[1][1]), qalin)
        elif a[0] == 1:
            pygame.draw.circle(oyna, rang, (a[1][0], a[1][1]), (pygame.Vector2(a[1]).distance_to(pygame.Vector2(a[2]))), qalin)
        elif a[0] == 2:
            pygame.draw.line(oyna, rang, (a[1][0], a[1][1]), (a[2][0], a[2][1]), qalin)
        elif a[0] == 3:
            pygame.draw.ellipse(oyna, rang, (a[1][0], a[1][1], int((a[2][0]-a[1][0])), int((a[2][1]-a[1][1]))), qalin)
        elif a[0] == 4:
            pygame.gfxdraw.trigon(oyna, a[1][0], a[1][1], int(a[1][0]+(a[2][0]-a[1][0])/2), int(a[1][1] -
                                                                        (a[2][0]-a[1][0])/2), a[2][0], a[2][1], rang)
    def chizma(self, a, rang, qalinlik):
        self.shakl_chizish(self.chizma_oyna, a, rang, qalinlik)

    def yozish(self, satr, olcham, rang, xy, a = True):
        if a:
            self.oyna.blit(self.yozuv_yozish(satr, olcham, rang), xy)
        else:
            self.chizma_oyna.blit(self.yozuv_yozish(satr, olcham, rang), xy)

    def rasm_chiqarish(self, rasm_j):
        try:
            zz = self.yuklandi[rasm_j]
        except:
            zz = self.yuklandi[0]
        self.chizma_oyna.blit(pygame.transform.rotozoom(self.oldingi_rasm, 0.0, 0.8), (400, 100))
        self.chizma_oyna.blit(pygame.transform.rotozoom(zz, 0.0, 0.8), (400, 100))
        self.oldingi_rasm = zz.copy()
        self.oldingi_rasm.fill("white")
        # if son:
            # self.ort()

    def yuklash(self, rasmlar):
        for i in rasmlar:
            try:
                self.yuklandi.append(pygame.image.load(str(i)))
            except:
                pass
        self.yuklandi.append(pygame.Surface((1, 1)))

    def qalam(self, rang, joy, qalinligi):
        pygame.draw.polygon(self.chizma_oyna, rang,(pygame.Vector2(joy[0]),pygame.Vector2(joy[1])), qalinligi)


    def ort(self):
        if self.ort1 != len(self.ortga) - 1:
            self.ortga = self.ortga[:self.ort1]
        d = pygame.Surface((1200, 800))
        d.blit(self.oyna, (0, 0))
        self.ortga.append(d)
        self.ort1 = (len(self.ortga) - 1)
        #print(self.ort1)
        if self.ort1 > 100:
            self.ortga = self.ortga[1:]


def main():
    ss = os.listdir()
    if "dars.json" in ss and "Audio.ogg" in ss:
        a = asosiy_oyna()
        a.asosiy()

if __name__ == '__main__':
    main()