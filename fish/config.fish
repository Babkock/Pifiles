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
end

