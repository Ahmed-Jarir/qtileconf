from libqtile.config import Group, Match
from commonVars import terminal 
##Groups##
groups = [
    Group("SYS", spawn=terminal, layout="bsp"),
    Group("NET", spawn="google-chrome-stable"),
    Group("UNI", spawn="nautilus Documents/pr/uni"),
    Group("DOC"),
    Group("GDV",spawn="unityhub",matches=[Match(wm_class=["unityhub","Unity"])],layout="treetab"),
    Group("VRM",spawn="virt-manager",matches=[Match(wm_class=["virt-manager"])],layout="max"),
    Group("CHT", spawn="discord", matches=[Match(wm_class=["discord","whatsapp"])]),
    Group("MUS",spawn = "google-chrome-stable youtube.com"),
    Group("VID"),
	Group("ANI",spawn = "google-chrome-stable zoro.to",layout = "max"),
]
##end keys##	
groups2 = [Group(i) for i in "1234567890"]

