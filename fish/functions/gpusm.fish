function gpusm
	eval ssh-agent &
	ssh-add "$HOME/.ssh/github_pi"
	git push origin main
end

