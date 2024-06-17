c.colors.completion.fg = '#88fdfdfd'
c.colors.completion.odd.bg = '#77000000'
c.colors.completion.even.bg = '#77000000'

c.colors.completion.category.fg = '#ee87efe8'
c.colors.completion.category.bg = '#77000000'
c.colors.completion.category.border.top = '#77e09690'
c.colors.completion.category.border.bottom = '#77ddff78'
c.colors.completion.item.selected.fg = '#ee000000'
c.colors.completion.item.selected.bg = '#eefbc1f9'
c.colors.completion.item.selected.border.top = '#eed8b0c1'
c.colors.completion.item.selected.border.bottom = '#eed8b0c1'
c.colors.completion.item.selected.match.fg = '#eefefefe'
c.colors.completion.match.fg = '#ee87efe8'
c.colors.completion.scrollbar.fg = '#aaffe379'
c.colors.completion.scrollbar.bg = '#77101010'

c.colors.tooltip.bg = '#aa000000'
c.colors.tooltip.fg = '#eeffffff'

c.colors.contextmenu.disabled.bg = '#77000000'
c.colors.contextmenu.disabled.fg = '#eee09690'
c.colors.contextmenu.menu.bg = '#88000000'
c.colors.contextmenu.menu.fg = '#eefefefe'
c.colors.contextmenu.selected.bg = '#eefbc1f9'
c.colors.contextmenu.selected.fg = '#ee000000'

c.colors.downloads.bar.bg = '#77000000'
c.colors.downloads.start.fg = '#ee87efe8'
c.colors.downloads.start.bg = '#00010101'
c.colors.downloads.stop.fg = '#eeddff78'
c.colors.downloads.stop.bg = '#00010101'
c.colors.downloads.error.fg = '#eee09690'
c.colors.downloads.system.bg = 'hsv'

c.colors.messages.error.fg = '#ffe09690'
c.colors.messages.error.bg = '#66000000'
c.colors.messages.error.border = '#eec75646'
c.colors.messages.warning.fg = '#ffffe379'
c.colors.messages.warning.bg = '#66000000'
c.colors.messages.warning.border = '#eee0c04c'
c.colors.messages.info.fg = '#ffffffff'
c.colors.messages.info.bg = '#66000000'
c.colors.messages.info.border = '#99000000'

c.colors.statusbar.normal.fg = '#eeace9ff'
c.colors.statusbar.normal.bg = '#66000000'
c.colors.statusbar.insert.fg = '#ee000000'
c.colors.statusbar.insert.bg = '#aa9ec64b'
c.colors.statusbar.passthrough.fg = '#ee000000'
c.colors.statusbar.passthrough.bg = '#aafbc1f9'
c.colors.statusbar.private.fg = '#eeace9ff'
c.colors.statusbar.private.bg = '#ee000000'
c.colors.statusbar.command.fg = '#eee09690'
c.colors.statusbar.command.bg = '#66000000'
c.colors.statusbar.progress.bg = '#eeffe379'

c.colors.statusbar.url.fg = '#eeffe379'
c.colors.statusbar.url.error.fg = '#eee09690'
c.colors.statusbar.url.hover.fg = '#eefbc1f9'
c.colors.statusbar.url.success.http.fg = '#eeddff78'
c.colors.statusbar.url.success.https.fg = '#eeddff78'
c.colors.statusbar.url.warn.fg = '#eee09690'

c.colors.tabs.bar.bg = '#10000000'
c.colors.tabs.indicator.start = '#eeffe379'
c.colors.tabs.indicator.stop = '#aae0c04c'
c.colors.tabs.indicator.error = '#eee09690'
c.colors.tabs.odd.fg = '#eeddff78'
c.colors.tabs.odd.bg = '#66000000'
c.colors.tabs.even.fg = '#eeddff78'
c.colors.tabs.even.bg = '#66000000'
c.colors.tabs.pinned.even.bg = '#66000000'
c.colors.tabs.pinned.even.fg = '#eefefefe'
c.colors.tabs.pinned.odd.bg = '#66000000'
c.colors.tabs.pinned.odd.fg = '#eefefefe'

c.colors.tabs.selected.odd.fg = '#eeffe379'
c.colors.tabs.selected.odd.bg = '#77000000'
c.colors.tabs.selected.even.fg = '#eeffe379'
c.colors.tabs.selected.even.bg = '#77000000'

c.colors.webpage.bg = '#ffffffff'

config.load_autoconfig()

c.auto_save.session = True
c.completion.height = "50%"
c.downloads.location.directory = "/home/pi"
c.downloads.location.prompt = False
c.prompt.filebrowser = False
c.prompt.radius = 20
c.input.insert_mode.auto_load = True
c.input.insert_mode.auto_leave = True
c.downloads.prevent_mixed_content = True
c.downloads.position = "bottom"
c.window.transparent = True
c.completion.scrollbar.width = 30
c.content.cookies.accept = 'all'
c.content.media.video_capture = True
c.content.media.audio_capture = True
c.content.media.audio_video_capture = True
c.content.notifications.enabled = True
c.content.notifications.presenter = "libnotify"
c.content.webgl = True
c.content.pdfjs = True
c.content.xss_auditing = False
c.content.local_content_can_access_remote_urls = True
c.content.plugins = True
c.content.tls.certificate_errors = "load-insecurely"
c.content.geolocation = False
c.content.javascript.clipboard = "access"
c.hints.radius = 20
c.scrolling.bar = "always"
c.scrolling.smooth = False
c.qt.args = ["enable-gpu-rasterization", "ignore-gpu-blocklist", "use-gl=egl", "enable-accelerated-video-decode"]
c.qt.highdpi = True
c.qt.chromium.experimental_web_platform_features = "always"

c.fonts.default_family = "Space Mono Nerd Font"
c.fonts.default_size = "16pt"
c.fonts.messages.error = "16pt Space Mono Nerd Font"
c.fonts.messages.info = "16pt Space Mono Nerd Font"
c.fonts.messages.warning = "16pt Space Mono Nerd Font"
c.fonts.statusbar = "16pt Space Mono Nerd Font"
c.fonts.downloads = "16pt Space Mono Nerd Font"
c.fonts.prompts = "16pt Victor Mono Nerd Font"
c.fonts.keyhint = "16pt Space Mono Nerd Font"
c.fonts.contextmenu = "16pt Space Mono Nerd Font"
c.fonts.completion.category = "bold 16pt Victor Mono Nerd Font"
c.fonts.tooltip = "16pt Victor Mono Nerd Font"
c.fonts.completion.entry = "16pt Space Mono Nerd Font"
c.fonts.tabs.selected = "italic 16pt Space Mono Nerd Font"
c.fonts.tabs.unselected = "16pt Space Mono Nerd Font"
c.fonts.messages.info = "italic 16pt Space Mono Nerd Font"
c.fonts.messages.error = "italic 16pt Space Mono Nerd Font"
c.fonts.messages.warning = "italic 16pt Space Mono Nerd Font"

c.url.start_pages = ["http://192.168.0.9:8000/pi.html"]
c.url.searchengines = { 'DEFAULT': 'https://duckduckgo.com/?ia=web&q={}', '!a': 'https://wiki.archlinux.org/index.php?title=Special%3ASearch&search={}', '!g': 'https://google.com/search?hl=en&q={}', '!i': 'https://google.com/search?hl=en&tbm=isch&q={}', '!m': 'https://google.com/maps?q={}', '!w': 'https://en.wikipedia.org/w/index.php?title=Special%3ASearch&search={}', '!h': 'https://github.com/search?q={}', '!y': 'https://youtube.com/results?search_query={}', '!n': 'https://yandex.ru/search/?text={}', '!v': 'https://voidlinux.org/packages/?arch=aarch64&q={}' }

c.tabs.padding = {
    "left": 5,
    "right": 4,
    "top": 4,
    "bottom": 4
}

c.tabs.title.format = "{audio}{current_title}"
c.tabs.title.format_pinned = "{audio}{index}"
c.window.title_format = "{perc}{current_title}"
c.tabs.show = "multiple"
c.tabs.last_close = "close"
c.tabs.mode_on_change = "restore"
c.tabs.indicator.width = 0
c.tabs.favicons.scale = 1.3
c.tabs.show_switching_delay = 600
c.tabs.pinned.frozen = False
c.completion.shrink = True
c.url.open_base_url = True

c.fileselect.handler = "external"
c.fileselect.single_file.command = ["alacritty", "-e", "ranger", "--choosefile={}"]
c.fileselect.multiple_files.command = ["alacritty", "-e", "ranger", "--choosefiles={}"]

