# .bashrc

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

export PATH=$PATH:/home/pi/bin

alias ..="cd .."
alias .config="cd ~/.config"
alias Downloads="cd ~/Downloads"
alias Pictures="cd ~/Pictures"
alias d="cd"
alias df="duf"
alias g="rg"
alias gh="rg --context=4"
alias h="htop"
alias m="mpv"
alias c="cvlc"
alias v="vim"
alias o="pkill -x"
alias r="ranger"
alias s="ssh -i '$HOME/.ssh/pi2comp' babkock@192.168.0.9"
alias x="sudo bash"
alias ls="lsd --group-directories-first --git -F"
alias lsl="lsd --group-directories-first --git --long --color always -h -F --blocks permission,user,size,git,date,name --date relative"
alias lsa="lsd --group-directories-first -A --git --long --color always -h -F --blocks permission,user,size,git,date,name --date relative"
alias lst="lsd --group-directories-first -A --tree --git --long --color always -h -F --blocks permission,user,size,git,date,name --date relative"

function pf() {
	if [ -z "$1" ]; then
		printf "pf needs a process name to search for\n"
		false
	else
		ps -au | rg "$1"
	fi
}

function t() {
	if [ -z "$1" ]; then
		tremc -X -r
		true
	elif [ -z "$2" ]; then
		printf "Starting %s...\n" "$1"
		tremc "$1" > /dev/null
		rm "$1" 2> /dev/null
		tremc -X -r
		true
	elif [ -z "$3" ]; then
		printf "Starting %s with speed %s kbps....\n" "$1" "$2"
		tremc "$1" > /dev/null
		transmission-remote -asd "$2"
		rm "$1" 2> /dev/null
		tremc -X -r
		true
	else
		printf "Too many arguments\n" > /dev/stderr
		false
	fi
}

PS1='\[\e[1;31m\]\u@\h\] \[\e[1;34m\]\W\[\e[m\] \[\e[1;32m\]\$\[\e[m\] '
#PS1='[\u@\h \W]\$ '
