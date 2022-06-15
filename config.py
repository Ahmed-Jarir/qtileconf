# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess as sp
import libqtile.popup as pp

from typing import List  # noqa: F401
from libqtile.log_utils import logger


from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook

##functions##

#def popup_test(qtile):
#    send_notification("popup_test_1", "this is test #1")
def runc(tile,function):
		sp.run(functions[function], shell=True, check=True)
def parse(text):
	return text.replace("\n",":")	
@hook.subscribe.startup_once
def autostart():
    sp.Popen(["blueman-applet"])
    sp.Popen(["compton"])

##end functions##



##modifiers##
mod = "mod4"
alt = "mod1"

##useful lists##
colors = [
    ["#0400ff", "#2b4bff"],
    ["#d4d5d9", "#a9a9a9"],
    "#ffffff",
    "#000000",
    "#e6b450",  # yellow
    "#565b66",  # grey
]
functions = [
	"maim -s -o -D -u | xclip -selection clipboard -t image/png",
	"maim -o -u | xclip -selection clipboard -t image/png"
]
##end useful lists##


terminal = guess_terminal()





##keys##
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

	#Key([mod, "control"], "r",lazy.reload_config(), desc="Reload the config"),
	Key([mod, "control"], "r",lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("volume-change -5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("volume-change +5")),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),
	Key([], "XF86AudioPlay", lazy.spawn("media p")),
	Key([], "XF86AudioPause", lazy.spawn("media p")),
	Key([], "XF86AudioNext", lazy.spawn("media n")),
	Key([], "XF86AudioPrev", lazy.spawn("media b")),

	#rofi
    Key([mod], "s", lazy.spawn("rofi -show ssh -no-parse-known-hosts -disable-history")),
	Key([mod], "o", lazy.spawn("powermen")),
	
	#screenshots
	Key(["shift", mod], "s", lazy.function(runc,0)),
	Key(["shift", mod], "a", lazy.function(runc,1)),

]
##end keys##	

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


##group keys##
groups2 = [Group(i) for i in "1234567890"]

for ind, i in enumerate(groups2):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[groups[ind].name].toscreen(),
                desc="Switch to group {}".format(groups[ind].name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(groups[ind].name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    groups[ind].name
                ),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),

 
        ]
    )

keys.extend([
    # go to surrounding groups
	Key([alt],"h",lazy.screen.prev_group()),
    Key([alt],"l",lazy.screen.next_group())
	])
##end group keys##

##layouts##
layouts = [
    layout.Columns(
			border_focus_stack=colors[0],
			border_width=4,
			margin = 6),
    layout.Max(
			border_focus_stack=colors[0],
			border_width=4),
    layout.Stack(
			num_stacks=2,
			border_focus_stack=colors[0],
			border_width=4,
			margin = 6),
    layout.Bsp(
			border_focus_stack=colors[0],
			border_width=4,
			margin = 6),
	layout.TreeTab(
			border_focus_stack=colors[0],
			border_width=4,
			margin = 6),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]
##bars##
topBar=bar.Bar(
            [
                widget.Sep(
                    linewidth=0,
                    padding=6,
                ),
                widget.GroupBox(
                    fontsize=11,
                    margin_y=3,
                    margin_x=0,
                    padding_y=5,
                    padding_x=3,
                    borderwidth=3,
                    active=colors[4],
                    inactive=colors[3],
                    urgent_text="e36841",
                    highlight_color=colors[0],
                    highlight_method="line",
					rounded = True,
                ),
                widget.Sep(foreground=colors[3]),
                widget.CurrentLayout(
                    foreground=colors[3],
                ),
                widget.Prompt(
                    foreground=colors[3],
                    cursor_color=colors[3],
                    ignore_dups_history=False,
                ),
                widget.Sep(foreground=colors[3]),
				#widget.Cmus(),
				widget.WindowName(foreground=colors[3]),
                # widget.Chord(
                #    chords_colors={
                #        'launch': ("#ff0000", "#ffffff"),
                #    },
                #    name_transform=lambda name: name.upper(),
                # ),
				widget.Systray(),
                widget.Clock(
                    format="%A, %b %d %I:%M %p",
                    foreground=colors[3],
                ),

            ],
            18,
            background=colors[5],
        )
bottomBar=bar.Bar(
    [
        widget.Volume(
            fmt="Vol: {}",
			padding = 8,
            background=colors[5],
            foreground=colors[3],
        ),
        widget.TextBox(
            '',
			width=17,
            fontsize=13,
            padding=0,
            foreground=colors[5],
            background=colors[4],
        ),
        widget.Memory(
            format="Ram: {MemPercent}%",
            background=colors[4],
            foreground=colors[3],
        ),
        widget.TextBox(
            "",
			width=17,
            fontsize=13,
            padding=0,
            foreground=colors[4],
            background=colors[5],
        ),
        widget.CPU(
            format="Cpu: {load_percent}%",
            background=colors[5],
            foreground=colors[3],
        ),
        widget.TextBox(
            "",
			width=17,
            fontsize=13,
            padding=0,
            foreground=colors[5],
            background=colors[4],
        ),
        widget.Battery(
            format="Battery: {percent:.0%}{char}",
            background=colors[4],
            foreground=colors[3],
            charge_char="ﮣ",
            discharge_char="-",
            low_percentage=0.2,
        ),
        widget.TextBox(
            "",
			width=17,
            fontsize=13,
            padding=0,
            foreground=colors[4],
            background=colors[5],
        ),
        widget.DF(
            format="Disk: {r:.0f}%",
            foreground=colors[3],
            background=colors[5],
            visible_on_warn=False,
        ),
        widget.TextBox(
            "",
			width=17,
            fontsize=13,
            padding=0,
            foreground=colors[5],
            background=colors[4],
        ),
        widget.CapsNumLockIndicator(
            fmt="{}",
			background=colors[4],
			foreground=colors[3]
        ),
        widget.TextBox(
            "",
			width=17,
            fontsize=13,
            padding=0,
            foreground=colors[4],
            background=colors[5],
        ),
		#widget.Notify(
        #    background=colors[5],
		#	foreground=colors[3],
		#	#parse_text = parse,
		#	fmt = {},
		#),
    ],
    14,
	background=colors[5],
)
##end bars##
##gui settings##
widget_defaults = dict(
    font="FiraCode Nerd Font Bold",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=topBar,
		bottom=bottomBar,
        wallpaper="~/.config/qtile/sbr.png",
        wallpaper_mode="fill",
        
    ),

  Screen(
  	top=bar.Bar(
  	    [
  	        widget.GroupBox(),
  	        widget.WindowName(),
  	        widget.Clock()
  	    ],
  	    30,
  	),
  ),
]



##floating layout settings##
# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class=".blueman-manager-wrapped"),
        Match(wm_class="zoom"),
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
##end floating layout settings##
##end gui settings##






auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
