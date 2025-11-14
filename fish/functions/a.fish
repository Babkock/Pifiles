function a
	yt-dlp --format "best[height=1080]" --remux-video 'mkv' --embed-metadata --embed-subs --embed-chapters --sleep-requests 2 --limit-rate 9M "$argv[1]"
end

