if status is-interactive
	set hydro_color_pwd brred
	set hydro_color_prompt green
	set hydro_color_duration cyan
	set hydro_color_git yellow
	set fish_prompt_pwd_dir_length 0
	set hydro_cmd_duration_threshold 2000
	set fish_color_autosuggestion white
	set fish_color_command green
	export LS_COLORS="$(vivid generate one-dark)"
	export FZF_DEFAULT_OPTS="--border=horizontal --prompt='\$ ' --pointer='->' --highlight-line --color=bg+:black,fg+:bright-green:italic,gutter:-1,hl:blue,hl+:bright-blue,query:bright-yellow,prompt:bright-yellow,pointer:black:dim,info:magenta,preview-bg:black,border:black:dim"
	source /home/pi/.config/fish/fzf.fish
	cowsay "$(fortune)" | lolcat
end

