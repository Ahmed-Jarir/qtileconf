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


def popup_test(qtile):
    send_notification("popup_test_1", "this is test #1")


@hook.subscribe.startup_once
def autostart():
    sp.Popen(["blueman-applet"])


mod = "mod4"
alt = "mod1"
colors = [
    ["#0400ff", "#2b4bff"],
    ["#d4d5d9", "#a9a9a9"],
    "#ffffff",
    "#000000",
    "#e6b450",  # yellow
    "#565b66",  # grey
]
terminal = guess_terminal()

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
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
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
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("volume-change -5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("volume-change +5")),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),
]

groups = [
    Group("DEV", spawn=terminal, layout="bsp"),
    Group("UNI", spawn="nautilus Documents/pr/uni"),
    Group("NET", spawn="google-chrome-stable"),
    Group("SYS"),
    Group("DOC"),
    Group("VRM",spawn="virt-manager",matches=[Match(wm_class=["virt-manager"])],layout="max"),
    Group("CHT", spawn="discord", matches=[Match(wm_class=["discord"])]),
    Group("MUS"),
    Group("VID"),
]


groups2 = [Group(i) for i in "123456789"]
groupdict = {
		"DEV":0,
		"UNI":1,
		"NET":2,
		"SYS":3,
		"DOC":4,
		"VRM":5,
		"CHT":6,
		"MUS":7,
		"VID":8
		}

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
	Key([alt, "shift"],"h",lazy.screen.prev_group()),
    Key([alt, "shift"],"l",lazy.screen.next_group())
	])
	


layouts = [
    layout.Columns(border_focus_stack=colors[0], border_width=4),
    layout.Max(border_focus_stack=colors[0], border_width=4),
    # Try more layouts by unleashing below layouts.
    layout.Stack(num_stacks=2, border_focus_stack=colors[0], border_width=4),
    layout.Bsp(border_focus_stack=colors[0], border_width=4),
	layout.TreeTab(border_focus_stack=colors[0], border_width=4),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="FiraCode Nerd Font Bold",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
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
            24,
            background=colors[5],
        ),
        wallpaper="~/.config/qtile/sbr.png",
        wallpaper_mode="fill",
        bottom=bar.Bar(
            [
                widget.Volume(
                    fmt="Vol: {}",
                    background=colors[5],
                    foreground=colors[3],
                ),
                widget.TextBox(
                    "",
                    width=29,
                    padding=0,
                    fontsize=23,
                    foreground=colors[5],
                    background=colors[4],
                ),
                widget.Memory(
                    format="Memory: {MemPercent}%",
                    background=colors[4],
                    foreground=colors[3],
                ),
                widget.TextBox(
                    "",
                    width=23,
                    padding=0,
                    fontsize=23,
                    foreground=colors[4],
                    background=colors[5],
                ),
                widget.CPU(
                    format="Cpu: {load_percent}%",
                    background=colors[5],
                    foreground=colors[3],
                ),
                widget.TextBox(
                    "",
                    width=23,
                    padding=0,
                    fontsize=23,
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
                    "",
                    width=23,
                    padding=0,
                    fontsize=23,
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
                    "",
                    width=23,
                    padding=0,
                    fontsize=23,
                    foreground=colors[5],
                    background=colors[4],
                ),
                widget.CapsNumLockIndicator(
                    fmt="{}", background=colors[4], foreground=colors[3]
                ),
                widget.TextBox(
                    "",
                    width=23,
                    padding=0,
                    fontsize=23,
                    foreground=colors[4],
                    background=colors[5],
                ),
                widget.Notify(),
            ],
            24,
            background=colors[5],
        ),
    ),
]

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
