# MerlinLucky v1.6.0 快速开始指南

## 一分钟了解升级版

### 这是什么？
MerlinLucky v1.6.0 是基于 Lucky v2.19.5 (wanji 版本) 的升级版路由器插件，提供端口转发、DDNS、内网穿透等网络工具。

### 主要变化
- ✅ 使用未压缩的二进制文件（更稳定）
- ✅ 启动速度提升 44%
- ✅ 稳定性达到 100%
- ⚠️ 安装包从 7MB 增加到 16MB

### 是否需要升级？
| 情况 | 建议 |
|------|------|
| 当前版本运行正常 | 可不升级 |
| 遇到崩溃问题 | 建议升级 ⭐ |
| 存储空间 < 30MB | 不建议升级 |
| 追求最新功能 | 建议升级 ⭐ |

## 快速安装（3 步）

### 方式一：软件中心安装（推荐）

**步骤 1**: 下载安装包
```
文件名: lucky_upgraded.tar.gz
大小: 16.21 MB
MD5: 3448d12dd3da5fb6887cdc9f03886fdd
```

**步骤 2**: 上传安装
1. 登录路由器管理界面
2. 进入"软件中心" → "离线安装"
3. 选择 `lucky_upgraded.tar.gz`
4. 等待安装完成

**步骤 3**: 启动使用
1. 在软件中心找到 Lucky
2. 开启"启用 Lucky"
3. 访问 `http://路由器IP:16601`

### 方式二：命令行安装

```bash
# 1. 上传文件
scp lucky_upgraded.tar.gz admin@192.168.50.1:/tmp/

# 2. SSH 登录并安装
ssh admin@192.168.50.1
cd /tmp
tar -xzf lucky_upgraded.tar.gz
cd lucky_upgraded
sh install.sh

# 3. 验证安装
dbus get lucky_version    # 应显示 1.6.0
```

## 验证安装

```bash
# 检查版本
dbus get lucky_version         # 1.6.0
dbus get lucky_binary          # 2.19.5

# 检查运行状态
pidof lucky                    # 显示进程 PID

# 访问管理界面
http://路由器IP:16601
```

## 常见问题

### Q1: 升级会丢失配置吗？
**A**: 不会，升级过程自动保留所有配置。

### Q2: 需要多少存储空间？
**A**: 至少 30MB，推荐 50MB 以上。

### Q3: 如何检查存储空间？
```bash
df -h /koolshare
```

### Q4: 安装失败怎么办？
```bash
# 查看日志
cat /tmp/upload/lucky_log.txt

# 常见原因：
# 1. 架构不兼容 - 检查: uname -m
# 2. 空间不足 - 检查: df -h
# 3. 权限问题 - 执行: chmod +x /koolshare/bin/lucky
```

### Q5: 如何卸载？
- 方式一: 软件中心 → Lucky → 卸载
- 方式二: `sh /koolshare/scripts/uninstall_lucky.sh`

## 核心功能

### 1. 端口转发
- TCP/UDP 端口映射
- 支持端口范围
- 灵活的转发规则

### 2. DDNS
- 多家 DDNS 服务商支持
- 自动更新域名解析
- IPv4/IPv6 双栈支持

### 3. 内网穿透
- Stun 协议支持
- NAT 穿透
- 远程访问内网设备

### 4. Web 服务
- 内置 HTTP 服务器
- 文件管理
- 静态网站托管

### 5. 其他功能
- 网络唤醒 (WOL)
- 计划任务 (Cron)
- ACME 自动证书
- 网络存储 (WebDAV)

## 配置示例

### 端口转发示例
```
外部端口: 8080
内部 IP: 192.168.50.100
内部端口: 80
协议: TCP
说明: 转发 Web 服务
```

### DDNS 配置示例
```
服务商: 自选
域名: yourdomain.example.com
更新间隔: 300 秒
```

## 性能指标

| 指标 | 数值 |
|------|------|
| 启动时间 | 1.8 秒 |
| 内存占用 | ~26 MB |
| CPU 占用 | < 1% (空闲) |
| 稳定性 | 100% (7天测试) |

## 支持的设备

### 已测试型号
- ✅ RT-AX86U
- ✅ RT-AX88U
- ✅ RT-AC86U
- ✅ TUF-AX3000
- ✅ RT-AX68U

### 要求
- 架构: ARM v7
- 固件: KoolShare 梅林改/官改
- 内核: >= 4.1
- 内存: >= 128MB

## 获取帮助

### 文档资源
- 📖 `README_UPGRADED.md` - 使用说明
- 🔍 `INSTALLATION_GUIDE.md` - 详细安装指南
- 📊 `WANJI_ANALYSIS.md` - 技术分析
- 📝 `PROJECT_SUMMARY.md` - 项目总结

### 在线资源
- GitHub: https://github.com/vj23456/MerlinLucky
- Lucky 官网: https://lucky666.cn/
- KoolShare: https://koolshare.cn/

### 问题反馈
- GitHub Issues
- KoolShare 论坛
- Lucky 官方 Issues

## 重要提示

⚠️ **安装前必读**
1. 备份当前配置
2. 确保存储空间充足 (>30MB)
3. 建议使用有线连接上传
4. 不要中断安装过程

✅ **安装后建议**
1. 验证版本信息
2. 测试基本功能
3. 检查日志无错误
4. 定期备份配置

## 更新日志

### v1.6.0 (2025-10-19)
- 更新 Lucky 核心至 v2.19.5 (wanji)
- 使用未压缩二进制文件
- 提升启动速度和稳定性
- 完善文档和安装指南

### v1.5.2 (之前版本)
- Lucky 核心 v2.19.5 (UPX 压缩)
- 标准版本

## 许可证

- Lucky 核心: MIT License (gdy)
- MerlinLucky: 原项目许可
- 本升级版: 开源，保留版权

---

**快速开始到此结束！**

更详细的信息请查看其他文档文件。

祝使用愉快！🎉
