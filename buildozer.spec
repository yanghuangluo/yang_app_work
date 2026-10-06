[app]

# 应用信息
title = Yang Python App
package.name = yangapp
package.domain = org.yanghuangluo

# 源码目录
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# 版本
version = 0.1

# 依赖
requirements = python3,kivy

# Android 配置
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 24

# 应用图标（可选）
# icon.filename = %(source.dir)s/data/icon.png

[buildozer]
log_level = 2
