from Hero import HeroAgility, HeroIntelligent
import os 

lindy = HeroIntelligent("Lindy")
zex = HeroAgility("Zex")

os.system('cls')

lindy.view_info()
zex.view_info()

lindy.gainExp = 130
zex.gainExp = 130

lindy.view_info()
zex.view_info()





