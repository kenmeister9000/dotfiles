local wezterm = require 'wezterm'  
local config = wezterm.config_builder() 
config.color_scheme = 'Everforest Dark Medium (Gogh)'
config.window_background_opacity = 0.7 
config.hide_tab_bar_if_only_one_tab = true 
config.keys = {
    { 
        key = '|',  
        mods = "CTRL|SHIFT",   
        action = wezterm.action.SplitVertical { domain = 'CurrentPaneDomain' }, 
    }, 
    {
        key = '|', 
        mods = "ALT|SHIFT", 
        action = wezterm.action.SplitHorizontal { domain = 'CurrentPaneDomain' },
    },
} 

return config
