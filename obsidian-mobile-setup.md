# Obsidian 手机端 Git 同步完整配置指南

本指南针对 llm-wiki 知识库在手机端的同步设置。

---

## 前提条件

- 手机已安装 Obsidian App
- 知识库地址: `https://github.com/Macrohegder/llm-wiki` (公开仓库)

---

## 第一步：安装 Obsidian Git 插件

1. 打开手机 Obsidian
2. 底部工具栏点击 **设置** (齿轮图标)
3. 选择 **第三方插件** → **浏览社区插件**
4. 搜索框输入 `Obsidian Git`
5. 点击安装，安装完成后点击 **启用**

> 若无法访问社区插件市场（国内网络），可以先在 PC 端安装好插件，然后将 .obsidian/plugins 目录同步到手机。

---

## 第二步：配置 Git 身份（只看不改可跳过）

如果仅需要在手机上**查看**，无需配置身份（公开仓库可直接拉取）。

如果需要在手机上**修改并推送**回 GitHub，需要配置 token：

### 获取 GitHub Personal Access Token

1. 手机浏览器访问 `github.com/settings/tokens`
2. 点击 **Generate new token (classic)**
3. 选择有效期（建议 90 天或 No expiration）
4. 勾选权限：`repo` (完整仓库访问权限）
5. 生成 token 后，**立即复制保存**（只显示一次）

### 在 Obsidian Git 中配置

1. Obsidian 设置 → 插件选项 → 找到 **Obsidian Git**
2. 找到 **Authentication/Commit Author**部分：
   - **Username**: `Macrohegder`
   - **Password/Token**: 粘贴刚才复制的 GitHub token
   - **Author name**: `你的名字`
   - **Author email**: `你的邮箱`
3. 保存设置

---

## 第三步：首次 Clone 仓库

1. 在手机上创建一个新的空文件夹（例如 `Documents/llm-wiki` 或 `下载/llm-wiki`）
2. 打开 Obsidian，选择 **打开文件夹作为知识库**，选择刚才创建的空文件夹
3. 进入这个空知识库后，按下 **Ctrl/Cmd + P** (或底部呼出命令面板)
4. 搜索并选择命令：**`Obsidian Git: Clone an existing remote repo`**
5. 填写信息：
   - **Remote URL**: `https://github.com/Macrohegder/llm-wiki.git`
   - 如果是私有仓库或需要 push，用带 token 的地址：
     `https://<TOKEN>@github.com/Macrohegder/llm-wiki.git`
   - **Save in directory**: `/`（表示放在知识库根目录）
6. 等待 clone 完成（文件较多，可能需要 1-3 分钟）
7. Clone 完成后，重启 Obsidian

---

## 第四步：配置自动拉取（建议）

1. 设置 → 插件选项 → Obsidian Git
2. 找到 **Auto pull/commit/push**部分：
   - **Auto pull interval**: 设置为 `10` 分钟（每 10 分钟自动拉取最新内容）
   - **Auto pull on startup**: 勾选 ✅（每次打开 Obsidian 时自动拉取）
   - **Pull on startup**: 勾选 ✅
3. 如果不希望自动推送（仅查看）：
   - **Auto commit interval**: 设为 `0` 或取消勾选
   - **Auto push interval**: 设为 `0` 或取消勾选
4. 保存设置

---

## 日常使用流程

### 仅查看模式（最简单）

- 打开 Obsidian → 自动拉取最新内容
- 浏览 wiki/sources/ 目录下的策略文章
- 查看复现状态和评分

### 编辑+同步模式（需要 token）

- 修改文件后，命令面板 → `Obsidian Git: Commit all changes`
- 然后命令面板 → `Obsidian Git: Push`
- 或等待自动提交/推送间隔触发

---

## 常见问题排除

| 问题 | 解决方案 |
|------|---------|
| Clone 失败，提示权限不足 | 检查 token 是否有 `repo` 权限，或 URL 是否正确 |
| 自动拉取不生效 | 确保给了 Obsidian 后台运行权限（手机设置 → 应用管理 → Obsidian → 允许后台运行） |
| 文件同步冲突 | 手动执行 `Obsidian Git: Pull`，然后解决冲突（保留两者或覆盖） |
| 文件太多卡顿 | 关闭 Obsidian 的 **安全模式**，安全模式下插件不运行 |

---

## 备选方案（如果 Obsidian Git 不好用）

### 方案 A: GitJournal (Android)

1. 安装 GitJournal App
2. 配置 GitHub 仓库: `Macrohegder/llm-wiki`
3. 使用 GitJournal 编辑 Markdown，它自带 Git 同步

### 方案 B: Working Copy (iOS)

1. App Store 安装 Working Copy
2. Clone 仓库 `https://github.com/Macrohegder/llm-wiki`
3. 在 Working Copy 中编辑文件
4. Obsidian 打开 Working Copy 的文件夹作为知识库

### 方案 C: 简单下载查看（无需 Git）

1. 手机浏览器访问 `https://github.com/Macrohegder/llm-wiki/tree/master/wiki/sources`
2. 点击具体文章直接阅读（GitHub 手机端 Markdown 渲染效果不错）
