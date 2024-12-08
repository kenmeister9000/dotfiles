# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
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
import re 
import os 
import subprocess
from libqtile import bar, layout, qtile, hook  
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal, send_notification
from qtile_extras import widget 
from qtile_extras.widget.decorations import PowerLineDecoration, RectDecoration

# Startup Script 
@hook.subscribe.startup_once
def autostart(): 
    home = os.path.expanduser('~/.config/qtile/autostart.sh') 
    subprocess.call(home) 

mod = "mod4"
terminal = "alacritty" 

# Key Bindings
keys = [
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.reset()),
    Key([mod, "shift"], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "s", lazy.layout.toggle_auto_maximize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
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
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
   ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Rofi Launches stuff"),
    Key([mod], "p", lazy.spawn("flameshot gui"), desc="Flameshot screenshot"), 
  #  Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 set Master 5-")), 
  #  Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 set Master 5+")), 
  #  Key([], "XF86AudioMute", lazy.spawn("amixer -c 0 Master toggle")), 
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    ) 

layouts = [
   # layout.Columns(border_focus=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
     layout.MonadTall(border_focus=['#e69138', "#bcbcbc"], border_width=3, margin=8),
     layout.MonadWide(border_focus=['#D3C6AA', "#bcbcbc"], border_width=3, margin=8),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

# Powerline Decorations
arrow_right = {
        "decorations": [ 
            PowerLineDecoration(path="arrow_right") 
        ]
}
arrow_left = {
        "decorations": [ 
            PowerLineDecoration(path="arrow_left") 
        ]
    }
round_right = {
        "decorations": [ 
            PowerLineDecoration(path="rounded_right") 
        ]
    }
round_left = {
        "decorations": [ 
            PowerLineDecoration(path="rounded_left") 
        ]
    }
for_slash = {
        "decorations": [ 
            PowerLineDecoration(path="forward_slash") 
        ]
    }

# Qtile Bar and Widgets
screens = [
    Screen(
        wallpaper = '/usr/share/backgrounds/archlinux/simple.png',  
        wallpaper_mode = 'fill',
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(),
                widget.GroupBox(
                    this_current_screen_border = '#DBBC7F' 
                    ),
                widget.Prompt(), 
#                widget.Notify(), 
                
                widget.Spacer( 
                    length = 1, 
                    background = None, **round_right 
                ), 
                
                widget.WindowName(
                    fmt = '<b>{}</b>', 
                    foreground = '#4c4f69',  
                    background = '#e67e80', **round_left 
                    ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Spacer(
                    length = 20, 
                    background = None, **round_right
                ), 
                widget.CheckUpdates(
                    fmt = '<b>{}</b>', 
                    distro= 'Arch_checkupdates',
                    no_update_string = '  No Updates  ', 
                    background = '#dbbc7f', **for_slash,  
                    update_interval = 1800, 
                    display_format = '   {updates}   ',  
                    colour_have_updates = '#4c4f69', 
                   colour_no_updates = '#4c4f69' 
                    ), 
                widget.Volume(
                    fmt = '<b>{}</b>', 
                    background = '#a7c080', **for_slash,  
                    unmute_format = '   {volume}%   ', 
                    mute_format = '   Muted  ', 
                    foreground = '#4c4f69', 
                   # emoji = True, 
                   # emoji_list = [' ', ' ', ' ', ' ']       
                    ), 
                widget.CPU(
                    fmt = '<b>{}</b>', 
                    format = '  {load_percent}%   ', 
                    foreground = '#4c4f69',
                    background = '#7fbbb3', **for_slash
                    ),  
                widget.Memory(
                    fmt = '<b>{}</b>', 
                    format = '  {MemPercent}%   ', 
                    foreground = '#4c4f69',
                    background = '#d699b6', **for_slash
                    ),  
                widget.UPowerWidget(
                    text_displaytime = 30, 
                    percentage_critical = 0.3, 
                    percentage_low = 0.4,   
                    border_charge_colour = '#439660', 
                    border_colour = '#f1c232', 
                    battery_width = 25, 
                    background = '#b4a7d6', **for_slash 
                    ), 
                widget.Clock(
                        fmt = '<b>{}</b>', 
                        format="  %m/%d/%Y    %r", 
                        foreground = '#4c4f69', 
                        background = '#d3c6aa', **round_left
                        ), 
                widget.Systray() 
            ],
            24,
           # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
           #border_color=["418913", "000000", "418913", "000000"]  # Borders are magenta
           background = '#232634'  
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = [] 
# Workspaces and applications assigned
groups = [ 
   Group ("1", label=" ", matches=[Match(wm_class=re.compile(r"^(alacritty)$"))]) , 
   Group ("2", label=" ", matches=[Match(wm_class=re.compile(r"^(firefox|discord)$"))]),
   Group ("3", label=" ", matches=[Match(wm_class=re.compile(r"^(heroic|steam)$"))]),        
   Group ("4", label=" ", matches=[Match(wm_class=re.compile(r"^(keepassxc)$"))]),  
   Group ("5", label=" " )
]
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
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

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
