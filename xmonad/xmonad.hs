import XMonad 
import XMonad.Util.EZConfig 
import XMonad.Layout.ThreeColumns 
import XMonad.Layout.Spacing
import XMonad.Hooks.EwmhDesktops
import XMonad.Hooks.DynamicLog 
import XMonad.Hooks.StatusBar 
import XMonad.Hooks.StatusBar.PP 
import XMonad.Util.Loggers
main :: IO () 
main = xmonad 
     . ewmhFullscreen 
     . ewmh 
     . withEasySB (statusBarProp "xmobar ~/.config/xmobar/xmobarrc" (pure myXmobarPP)) defToggleStrutsKey
     $ myConfig 

myConfig = def 
    { modMask = mod4Mask 
    , layoutHook = smartSpacing 3 $ myLayout 
    , workspaces = myWorkspaces 
    , focusedBorderColor = "#83C092"    
    , normalBorderColor  = "#000000" 
    } 
   `additionalKeysP` 
     [ ("M-q",                    spawn "wezterm")
     , ("M-r",                    spawn "rofi -show drun") 
     , ("M-p",                    spawn "if type xmonad; then xmonad --recompile && xmonad --restart; else xmessage xmonad not in \\$PATH: \"$PATH\"; fi") 
     , ("<XF86AudioMute>",        spawn "/usr/bin/pulseaudio-ctl mute")
     , ("<XF86AudioRaiseVolume>", spawn "/usr/bin/pulseaudio-ctl up")
     , ("<XF86AudioLowerVolume>", spawn "/usr/bin/pulseaudio-ctl down") 
     ]
myLayout = tiled ||| Mirror tiled ||| Full ||| ThreeColMid 1 (3/100) (1/2) 
  where 
    threecol = ThreeColMid nmaster delta ratio 
    tiled    = Tall nmaster delta ratio 
    nmaster  = 1        -- Default number of windows in master pane  
    ratio    = 1/2      -- Default proportion of screen occupied by master pane 
    delta    = 3/100    -- Percent of screen to increment when resizing panes  
myWorkspaces = ["\xf489", "\xf0ac", "\xf11b", "\xf02d", "\xf17c"]
myXmobarPP :: PP 
myXmobarPP = def 
    { ppCurrent =  xmobarBorder "Bottom" "#7FBBB3" 2 
    , ppSep = aqua " : "
    , ppUrgent          = red . wrap (yellow "!") (yellow "!")
    , ppOrder           = \[ws, l, _, wins] -> [ws, l, wins]
    , ppExtras          = [logTitles formatFocused formatUnfocused]  
    , ppHidden          = gray 
    }
    where 
    formatFocused   = wrap (white    "[") (white    "]") . green . ppWindow
    formatUnfocused = wrap (gray "[") (gray "]") . blue    . ppWindow
    
    ppWindow :: String -> String
    ppWindow = xmobarRaw . (\w -> if null w then "" else w) . shorten 50
    
    red, orange, yellow, green, blue, aqua, purple, white, gray :: String -> String 
    red    = xmobarColor "#E67E80" "" 
    orange = xmobarColor "#E69875" "" 
    yellow = xmobarColor "#DBBC7F" "" 
    green  = xmobarColor "#A7C080" "" 
    blue   = xmobarColor "#7FBBB3" "" 
    aqua   = xmobarColor "#83C092" "" 
    purple = xmobarColor "#D699B6"  "" 
    white  = xmobarColor "#D3C6AA"  "" 
    gray   = xmobarColor "#859289"  "" 
        

