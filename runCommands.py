import subprocess as sp
def runc(tile,function):
	sp.run(functions[function], shell=True, check=True)
functions = [
	"maim -s -o -D -u | xclip -selection clipboard -t image/png",
	"maim -o -u | xclip -selection clipboard -t image/png"
]
