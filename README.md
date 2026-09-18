# 完整物料包 v3 — 含二维码预约表单

> 生成日期：2026-09-18  
> 版本：v3（基于 v2 修改）  
> 本文件夹为**全新生成**，未改动任何原文件。

## v3 变更内容

| 变更项 | 说明 |
|--------|------|
| 海外留学海报文字 | "不挑体系不挑年级" → "无缝衔接不同体系" |
| 海外留学海报文字 | "全程同一个老师带" → "全程陪伴" |
| 海外留学海报文字 | "选课规划、预估分策略" → "同时提供选课规划、择校指导" |
| 科目徽章颜色 | 带过学生栏中的科目颜色改为突出的白色（HTML+PPTX） |
| 最小字体加大 | 两个海报版本所有字体加大 2 号（HTML+PPTX） |
| PPTX 同步 | 海外留学 PPTX 同步文字修改，可编辑无乱码 |

* * *

## 文件夹结构

```
完整物料包-含二维码-20260918/
├── form.html              ← 预约表单（扫码后打开的页面）
├── index.html             ← 入口页（自动跳转到 form.html）
├── README.md              ← 本说明文件
├── .gitignore             ← Git 忽略文件（推 GitHub 用）
├── assets/                ← 海报背景图
│   ├── big-ben.jpg
│   └── graduation.jpg
├── posters/               ← 海报（已嵌入二维码）
│   ├── 海报-展架60x160-海外留学.html
│   ├── 海报-展架60x160-海外留学.pptx
│   ├── 海报-展架60x160-国内高考.html
│   └── 海报-展架60x160-国内高考.pptx
├── qr-codes/              ← 二维码图片
│   └── qr-booking.png     ← 预约表单二维码（370×370px）
└── tools/                 ← 工具脚本
    ├── generate_qr.py     ← 生成二维码
    ├── embed_qr_pptx.py   ← 将二维码嵌入 PPTX
    └── regenerate_all.py  ← 一键重新生成（改 URL 后用）















```

* * *

## 整体流程

```
家长扫海报上的二维码
      ↓
打开 GitHub Pages 上的 form.html
      ↓
填写预约信息并提交
      ↓
Formsubmit.co 自动发送到你的邮箱
      ↓
你在邮箱中查看/搜索/导出所有预约记录















```

**邮箱就是你的"数据库"** — 所有提交记录都在邮箱里，可搜索、可导出 CSV。

* * *

## 部署步骤（约 15 分钟）

### 第 1 步：注册 GitHub 账号（3 分钟）

1.  打开 [https://github.com/signup](https://github.com/signup)
2.  注册一个账号（用户名即你的 GitHub 用户名，后面要用）

### 第 2 步：创建仓库并上传文件（5 分钟）

1.  登录 GitHub → 点右上角 **+** → **New repository**
2.  仓库名填 `edu-booking`，选 **Public**，点 **Create repository**
3.  点 **uploading an existing file**
4.  把本文件夹中的 `form.html` 和 `index.html` 拖进去
5.  点 **Commit changes**

### 第 3 步：开启 GitHub Pages（2 分钟）

1.  进入仓库 → **Settings** → 左侧 **Pages**
    
2.  **Source** 选 `Deploy from a branch`
    
3.  **Branch** 选 `main`，文件夹选 `/ (root)`
    
4.  点 **Save**
    
5.  等约 1 分钟，页面顶部会显示你的网址：
    
    ```
    https://你的用户名.github.io/edu-booking/
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ```
    

### 第 4 步：配置邮箱 + 重新生成二维码（5 分钟）

#### 4a. 修改 form.html 中的邮箱

用文本编辑器打开 `form.html`，找到这一行（约第 165 行）：

```javascript
var BOOKING_API = "https://formsubmit.co/YOUR_EMAIL@example.com";















```

把 `YOUR_EMAIL@example.com` 改成你的真实邮箱，例如：

```javascript
var BOOKING_API = "https://formsubmit.co/wanglaoshi@gmail.com";















```

保存后重新上传到 GitHub 仓库（覆盖原文件）。

#### 4b. 重新生成二维码

打开命令行（PowerShell / CMD），进入本文件夹，运行：

```bash
python tools/regenerate_all.py https://你的用户名.github.io/edu-booking/















```

这会自动：

-   用新 URL 重新生成 `qr-codes/qr-booking.png`
-   重新生成两张海报 PPTX（嵌入新二维码）

> 海报 HTML 中的二维码是引用 `qr-codes/qr-booking.png` 图片文件，  
> 重新生成 PNG 后 HTML 自动更新，无需重新生成。

### 第 5 步：激活 [Formsubmit.co](http://Formsubmit.co)（首次提交时）

1.  用手机扫海报上的二维码，打开表单
2.  随便填一条测试数据，点提交
3.  **第一次提交时**，[Formsubmit.co](http://Formsubmit.co) 会发一封确认邮件到你的邮箱
4.  点邮件中的确认链接，激活该邮箱
5.  之后每次有人提交，数据都会自动发到你的邮箱

* * *

## 查看预约记录

| 方式 | 说明 |
| --- | --- |
| **邮箱查看** | 所有提交会以表格格式发到你邮箱，可搜索/筛选/导出 |
| **本机查看** | 表单页面底部有"查看已填记录（本机）"按钮，可查看当前设备上的提交记录 |

### 邮件内容示例

每封邮件包含：

-   称呼、孩子年级、学校类型、英语现状
-   意向国家、想了解的内容
-   联系方式、预约日期、时间段
-   补充问题

* * *

## 常见问题

### Q: 二维码扫出来是占位网址怎么办？

A: 说明还没运行第 4b 步。请按部署步骤重新生成二维码。

### Q: 提交后没收到邮件？

A: 第一次提交需要点确认链接激活。检查垃圾邮件文件夹。

### Q: 不想用 GitHub Pages，可以用别的吗？

A: 可以。任何能托管静态 HTML 的服务都行（腾讯云 COS、阿里云 OSS、Vercel 等）。  
只需把 `form.html` 和 `index.html` 上传到托管服务，拿到 URL 后重新生成二维码即可。

### Q: 想改成发到企业微信/飞书怎么办？

A: 修改 `form.html` 中的 `BOOKING_API`，换成企业微信机器人 webhook 或飞书机器人地址，  
并调整 `submitLead` 函数中的提交格式。

* * *

## 工具脚本说明

### generate\_qr.py — 生成二维码

```bash
python tools/generate_qr.py [URL]
# 不传 URL 则用占位 URL















```

### embed\_qr\_pptx.py — 嵌入二维码到 PPTX

```bash
python tools/embed_qr_pptx.py
# 读取 qr-codes/qr-booking.png，嵌入到 posters/ 下的两个 PPTX















```

### regenerate\_all.py — 一键重新生成

```bash
python tools/regenerate_all.py https://你的用户名.github.io/edu-booking/
# 重新生成 QR + PPTX















```

* * *

## 依赖

-   Python 3.8+
-   `qrcode` 库：`pip install qrcode`
-   `Pillow` 库：`pip install Pillow`
-   `python-pptx` 库：`pip install python-pptx`（仅 PPTX 嵌入需要）