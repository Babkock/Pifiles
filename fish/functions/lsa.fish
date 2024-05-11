function lsa
	lsd --group-directories-first --git -A --long --color always -h -F --blocks permission,user,size,git,date,name --date relative $argv
end

