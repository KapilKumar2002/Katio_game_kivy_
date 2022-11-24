[app]

# (str) Title of your application
title =  Katio
package.name = kapil
package.domain = org.kapil
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,wav
version = 0.1
requirements = python3,kivy,kivymd,pillow,ffpyplayer
# (str) Presplash of the application
presplash.filename = %(source.dir)s/assets/image.png
# (str) Icon of the application
icon.filename = %(source.dir)s/assets/image1.png
orientation = portrait
fullscreen = 0
# (string) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
android.presplash_color = #FFFFFF
# (str) Adaptive icon of the application (used if Android API level is 26+ at runtime)
#icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
#icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png
android.permissions = INTERNET
android.api = 33
android.sdk_path = ~/Android/Sdk
android.skip_update = False
android.logcat_filters = *:S python:D
android.archs = armeabi-v7a
# armeabi-v7a
[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
