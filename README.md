# yang_app_work

Python 编写的 Android 应用，使用 Kivy 框架 + Buildozer 打包成 APK。

## 📥 下载 APK

前往 [Releases 页面](https://github.com/yanghuangluo/yang_app_work/releases) 下载最新版本 APK，安装到 Android 手机即可使用。

> 当前为占位演示版本，正式 APK 会在 Release 中发布。

## 📁 项目结构

```
yang_app_work/
├── main.py          # 应用主代码（Kivy）
├── buildozer.spec   # Buildozer 打包配置
└── README.md        # 说明文档
```

## 🔧 本地构建 APK

### 环境要求
- Linux 系统（Ubuntu/Debian）
- Python 3.8+

### 安装依赖
```bash
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
pip install buildozer
```

### 打包命令
```bash
buildozer android debug
```

构建完成后，APK 文件会生成在 `bin/` 目录下。

## 📤 发布到 GitHub Release

1. 打标签：`git tag -a v0.1 -m "第一个版本"`
2. 推送标签：`git push origin v0.1`
3. 在 GitHub 网页端进入 Releases → Draft a new release
4. 上传生成的 APK 文件作为附件
5. 发布后用户即可从 Release 页面下载
