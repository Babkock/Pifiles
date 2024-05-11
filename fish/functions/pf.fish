function pf
	if not set -q argv[1]
		printf "pf needs a process name to search for\n" > /dev/stderr
		false
	else
		ps -aux | rg "$argv[1]"
	end
end

