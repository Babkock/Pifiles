function lstl
	lsd --group-directories-first --git -A --tree --git --long --color always -F --blocks permission,user,size,date,name --date relative $argv
end

