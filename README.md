# 🐳 Entertainment（巨鲸传媒）

> 基于 uni-app x + Vue 3 构建的娱乐直播公会代理管理系统，面向 Android 原生 App。

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Vue](https://img.shields.io/badge/Vue-3.x-brightgreen.svg)](https://vuejs.org/)
[![uni-app x](https://img.shields.io/badge/uni--app%20x-latest-7B68EE.svg)](https://uniapp.dcloud.net.cn/uni-app-x/)
[![Platform](https://img.shields.io/badge/platform-Android-3DDC84.svg)]()

---

## 📖 项目简介

**巨鲸传媒** 是一套专为娱乐直播/语聊公会打造的综合管理平台。公会代理通过该系统可以高效地管理旗下主播资源、追踪平台业绩、结算佣金收益，并实时掌握团队动态。

核心业务流程：代理登陆 → 管理主播入职/绑定 → 查看平台&个人业绩 → 结算佣金 → 提现。

---

## ✨ 核心功能

| 模块 | 功能描述 |
|------|----------|
| 🏠 **首页** | 公告轮播、语聊/直播平台切换、功能入口导航（推广、团队、主播资源、业绩） |
| 🎤 **主播管理** | 主播入职办理、快捷绑定、主播列表、主播资源池（CRUD） |
| 👥 **团队体系** | 多级代理架构（直推代理/间推代理）、团队主播一览 |
| 📊 **业绩系统** | 平台业绩总览、我的业绩明细、佣金记录 |
| 💰 **资金管理** | 余额查询、资金明细、提现申请（支付宝/灵工账户） |
| 📰 **内容中心** | 新闻资讯、系统公告、推广规则、违规公示 |
| 🛠️ **客服支持** | 在线客服接待 |
| 👤 **个人中心** | 用户信息、收益统计、团队统计、退出登录 |

---

## 🛠️ 技术栈

| 类别 | 技术 |
|------|------|
| **框架** | uni-app x（增强版，支持原生渲染） |
| **前端** | Vue 3 (Composition API + `<script setup>`) |
| **开发语言** | UTS（uni-app TypeScript 方言，编译为原生代码） |
| **样式预处理** | SCSS |
| **构建工具** | Vite |
| **路由** | pages.json（uni-app 页面路由） |
| **状态管理** | Composition API + uni.storage |
| **HTTP 请求** | uni.request（封装在 `utils/request.uts`） |
| **目标平台** | Android 原生 App（支持扩展至 iOS / H5 / 小程序） |

---

## 📁 项目结构

```
Entertainment/
├── App.uvue                     # 应用入口组件（生命周期、全局样式）
├── main.uts                     # 应用启动入口
├── index.html                   # SPA 入口 HTML
├── manifest.json                # 应用配置（AppID、版本、平台分发）
├── pages.json                   # 页面路由 & TabBar & 全局样式配置
├── uni.scss                     # 全局 SCSS 变量（主题色、间距、字号）
├── platformConfig.json          # 目标平台配置（当前：APP-ANDROID）
│
├── pages/                       # 业务页面（29个）
│   ├── login/login.uvue                     # 登录页
│   ├── register/register.uvue               # 注册页
│   ├── index/index.uvue                     # 首页（TabBar）
│   ├── news/news.uvue                       # 新闻资讯（TabBar）
│   ├── performance/performance.uvue         # 平台业绩（TabBar）
│   ├── service-tab/service-tab.uvue         # 客服接待（TabBar 中转页）
│   ├── mine/mine.uvue                       # 个人中心（TabBar）
│   ├── app-download/app-download.uvue       # APP 下载
│   ├── app-intro/app-intro.uvue             # 应用介绍
│   ├── quick-bind/quick-bind.uvue           # 快捷绑定主播
│   ├── anchor-list/anchor-list.uvue         # 主播列表
│   ├── anchor-resource/                     # 主播资源管理
│   │   ├── anchor-resource.uvue             #   资源主页
│   │   ├── anchor-resource-form.uvue        #   入职表单
│   │   ├── anchor-resource-list.uvue        #   资源列表
│   │   └── anchor-resource-detail.uvue      #   资源详情
│   ├── team/team.uvue                       # 我的团队
│   ├── promote/promote.uvue                 # 我要推广
│   ├── promotion-rule/promotion-rule.uvue   # 推广规则
│   ├── my-performance/my-performance.uvue   # 我的业绩
│   ├── commission-records/commission-records.uvue # 最近动态/佣金记录
│   ├── finance-detail/finance-detail.uvue   # 资金明细
│   ├── withdraw/withdraw.uvue               # 我要提现
│   ├── withdraw-account/withdraw-account.uvue # 提现账户管理
│   ├── withdraw-history/withdraw-history.uvue # 提现记录
│   ├── notice/notice.uvue                   # 系统公告
│   ├── agreement/agreement.uvue             # 用户协议
│   ├── chat-convention/chat-convention.uvue # 语聊公约
│   ├── rules/rules.uvue                     # 违规公示
│   └── service/service.uvue                 # 联系客服
│
├── components/                  # 公共组件
│   └── custom-tab-bar/custom-tab-bar.uvue   # 自定义底部导航栏
│
├── utils/                       # 工具模块
│   ├── request.uts              #   HTTP 请求封装（Bearer Token、统一错误处理）
│   ├── api.uts                  #   API 接口层（类型定义 + 接口函数）
│   └── auth.uts                 #   认证管理（Token 存取、登录状态检查、路由守卫）
│
├── static/                      # 静态资源
│   ├── logo.png                 # 应用 Logo
│   ├── bg.png                   # 背景图
│   ├── *.svg                    # SVG 图标集（功能入口、性别、支付等）
│   └── svg/                     # SVG 组件图标
│
├── unpackage/                   # 构建输出（已 gitignore）
├── .gitignore                   # Git 忽略规则
└── README.md                    # 本文件
```

---

## 🎨 设计规范

| 属性 | 值 |
|------|-----|
| **品牌色** | `#F0C275`（金色）、`#FFD54F`（TabBar 选中色） |
| **背景色** | `#F5F0E8`（米黄色导航栏/页面背景） |
| **强调色** | `#FF4D4F`（红色，组件选中态） |
| **文字色** | `#333`（主文字）、`#999`（辅助文字） |
| **字体尺寸** | `12px`（小）、`14px`（标准）、`16px`（大） |
| **导航栏风格** | 自定义导航栏（`navigationStyle: custom`）/ 部分页面使用系统导航 |

---

## 🚀 快速开始

### 环境要求

- [HBuilderX](https://www.dcloud.io/hbuilderx.html) 最新版（支持 uni-app x）
- Node.js 16+
- Android Studio（用于 Android 原生打包）

### 安装步骤

1. **克隆仓库**

```bash
git clone https://github.com/Nonver/Entertainment.git
cd Entertainment
```

2. **使用 HBuilderX 打开项目**

   - 启动 HBuilderX
   - 菜单栏：文件 → 打开目录 → 选择项目根目录

3. **配置 API 地址**

   编辑 `utils/request.uts`，修改后端接口基地址：

```js
// 开发环境示例
const BASE_URL = 'http://your-api-server:8000/api/admin'
```

4. **运行调试**

   - HBuilderX 工具栏 → 运行 → 运行到手机或模拟器
   - 选择 Android 基座运行

5. **打包发布**

   - HBuilderX 工具栏 → 发行 → 原生 App-云打包
   - 按向导配置签名证书、图标、启动图等

---

## 📡 后端 API

本项目采用 RESTful API 风格，后端接口位于 `/api/admin/*`。主要接口模块：

| 模块 | 端点 | 说明 |
|------|------|------|
| 登录 | `POST /api/admin/login` | 账号密码登录 |
| 用户 | `GET /api/admin/auth/info` | 获取当前用户信息 |
| 平台 | `GET /api/admin/platforms` | 语聊平台列表 |
| 平台 | `GET /api/admin/live-platforms` | 直播平台列表 |
| 主播 | `GET/POST /api/admin/anchors` | 主播管理 |
| 业绩 | `GET /api/admin/performance/stats` | 业绩统计 |
| 佣金 | `GET /api/admin/commission` | 佣金查询 |
| 团队 | `GET /api/admin/users` | 团队用户 |
| 提现 | `GET/POST /api/admin/withdraw` | 提现管理 |
| 新闻 | `GET /api/admin/news` | 新闻列表 |
| 公告 | `GET /api/admin/notices` | 系统公告 |

> 详细 API 定义见 `utils/api.uts`（含完整的 Type/接口类型定义）。

---

## 📱 平台支持

| 平台 | 状态 |
|------|------|
| Android App | ✅ 当前主要支持（`platformConfig.json` 已配置） |
| H5 (Web) | ✅ 已配置支持（`manifest.json` 中已启用 history 路由模式） |
| iOS App | 🔧 预留扩展（manifest 已配置，待测试） |
| 微信小程序 | 🔧 预留扩展（manifest 已配置） |
| 支付宝小程序 | 🔧 预留扩展（manifest 已配置） |
| 字节跳动小程序 | 🔧 预留扩展（manifest 已配置） |

---

## 📄 TabBar 导航

| 图标 | 名称 | 页面 | 说明 |
|------|------|------|------|
| 📰 | 新闻资讯 | `pages/news/news` | 内容流 |
| 🏠 | 首页 | `pages/index/index` | 核心工作台 |
| 📊 | 平台业绩 | `pages/performance/performance` | 数据看板 |
| 💬 | 客服接待 | `pages/service-tab/service-tab` | 联系客服 |
| 👤 | 个人中心 | `pages/mine/mine` | 账户管理 |

---

## 🔐 认证流程

1. 用户进入应用 → 检查本地 Token
2. Token 存在且在有效期内 → 直接进入首页
3. Token 不存在或过期 → 自动跳转登录页
4. 登录成功 → 存储 Token 和用户信息 → 跳转首页
5. 访问需登录页面时自动校验（白名单机制，见 `utils/auth.uts`）
6. API 请求 401 → 自动清除 Token → 跳转登录

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request。在提交代码前请确保：

- 代码风格与项目保持一致
- 页面文件名使用小写字母和连字符（kebab-case）
- 使用 `uts` 类型声明，避免 `any`
- 请求封装使用 `utils/request.uts` 统一方法

---

## 📜 License

MIT License © 2024 Nonver

---

## 📧 联系方式

- GitHub: [https://github.com/Nonver/Entertainment](https://github.com/Nonver/Entertainment)

---

<p align="center">
  <sub>Built with ❤️ using uni-app x + Vue 3</sub>
</p>
