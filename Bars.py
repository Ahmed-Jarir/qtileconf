from libqtile import bar, widget
from commonVars import colors
widget_defaults = dict(
    font="FiraCode Nerd Font Bold",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

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
            padding=-2,
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
            padding=-2,
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
            padding=-2,
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
            padding=-2,
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
            padding=-2,
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
            padding=-2,
            foreground=colors[4],
            background=colors[5],
        ),
    ],
    14,
	background=colors[5],
)
##end bars##
