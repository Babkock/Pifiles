function gpulm
	pkill -x ssh-agent
	eval ssh-agent &
	ssh-add "$HOME/.ssh/github_pi"
	git pull -u origin main
end

