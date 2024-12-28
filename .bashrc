#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias li='eza --icons'
alias lia='eza -a --icons'
alias lil='eza --icons -al'
alias svim='sudo -E vim'
alias mpva='mpv --no-audio-display' 
alias kb0='brightnessctl --device='tpacpi::kbd_backlight' set 0 | ~/.local/bin/backlit.sh'
alias kb1='brightnessctl --device='tpacpi::kbd_backlight' set 1 | ~/.local/bin/backlit.sh'
alias kb2='brightnessctl --device='tpacpi::kbd_backlight' set 2 | ~/.local/bin/backlit.sh'
alias pl="yay -Qq | fzf --preview 'pacman -Qil {}' --layout=reverse --bind 'enter:execute(pacman -Qil {} | less)'"
alias ch='checkupdates' 
eval "$(zoxide init bash)"
eval "$(starship init bash)"
export STARSHIP_CONFIG=~/.config/starship/starship.toml 
export FZF_DEFAULT_COMMAND="fd --type f"
export EDITOR=/usr/bin/vim
export PATH=$HOME/bin:$HOME/.local/bin:$PATH
PS1='[\u@\h \W]\$ '
