function start
	export GTK_THEME="Sunset-Dark"
	export GDK_BACKEND="wayland,x11"
	export XDG_CURRENT_DESKTOP="sway"
	export XDG_SESSION_DESKTOP="sway"
	export XDG_SESSION_TYPE="wayland"
	export QT_QPA_PLATFORM="wayland-egl"
	export QT_QPA_PLATFORMTHEME="qt6ct"
	export QT_WAYLAND_DISABLE_WINDOWDECORATION=1
	export XCURSOR_THEME="Adwaita"
	export XCURSOR_SIZE=35
	export MOZ_ENABLE_WAYLAND=1
	export MOZ_WEBRENDER=1
	pgrep pipewire | xargs kill 2> /dev/null
	pgrep pulseaudio | xargs kill 2> /dev/null
	echo "Starting Sway..."
	gsettings set org.gnome.desktop.interface cursor-theme Adwaita
	gsettings set org.gnome.desktop.interface cursor-size 35
	dbus-launch --exit-with-session sway
	true
end

