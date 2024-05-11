function lsl
	lsd --group-directories-first --git --long --color always -h -F --blocks permission,user,size,git,date,name --date relative $argv
end

