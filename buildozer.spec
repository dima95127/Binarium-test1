[app]
title = Trading Helper
package.name = tradinghelper
package.domain = org.tradinghelper
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,ccxt,requests,pandas,numpy,matplotlib,ta,yfinance,multitasking
pure_python_modules = ta,yfinance,multitasking
orientation = portrait
fullscreen = 0
icon.filename = icon.png
android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.archs = arm64-v8a,armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 0
