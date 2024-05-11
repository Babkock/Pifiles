function t
	if not set -q argv[1]
		tremc -X -r
		true
	else if not set -q argv[2]
		printf "Starting %s...\n" "$argv[1]"
		tremc -c "$argv[1]" > /dev/null
		rm "$argv[1]" 2> /dev/null
		tremc -X -r
		true
	end
end

