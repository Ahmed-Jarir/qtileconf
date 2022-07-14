
from libqtile.lazy import lazy
from libqtile.config import Key, Click, Drag

from runCommands import runc
from groups import groups, groups2
from commonVars import terminal
##modifiers##
mod = "mod4"
alt = "mod1"

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
##mouse key bindings##
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
##end mouse key bindings##

##group keys##

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
