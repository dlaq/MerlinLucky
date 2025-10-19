# Lucky 升级版 v1.6.0

## 升级说明

本版本是 MerlinLucky 的升级版本，主要更新如下：

### 主要更新内容

1. **Lucky 核心版本更新至 v2.19.5**
   - 使用来自 `lucky_2.19.5_Linux_armv7_wanji` 的最新二进制文件
   - 未使用 UPX 压缩的完整版本，提升兼容性和稳定性
   
2. **二进制文件变化**
   - 旧版本：7MB (UPX 压缩)
   - 新版本：16MB (未压缩)
   - 架构：ARM v7 (32位)
   - ELF 格式确认：7F-45-4C-46-01-01-01-03

3. **版本信息**
   - 插件版本：1.6.0
   - Lucky 核心：2.19.5
   - MD5校验：3448d12dd3da5fb6887cdc9f03886fdd

## 关于 "wanji" 版本

"wanji"（玩机/daji）版本特指针对特定设备优化的 Lucky 构建版本：

- **目标设备**：MiSnapAI 等 ARM 设备
- **特点**：未压缩的二进制文件，更好的兼容性
- **路径约定**：使用 `/data/lucky.daji` 或 `/data/userdisk/lucky.daji`
- **服务名称**：`lucky.daji`

本升级版提取了 wanji 版本的核心二进制文件，适配到 KoolCenter 软件中心框架。

## 安装要求

### 硬件要求
- ARM 架构路由器（HND/MTK/QCA）
- 至少 20MB 可用存储空间（二进制文件较大）

### 固件要求
- 华硕 Merlin 固件（官改/梅林改）
- Linux 内核版本 >= 4.1
- 支持 skipd 和 dbus

### 支持的路由器型号
参考：https://github.com/koolshare/rogsoft#rogsoft

## 安装步骤

1. **备份现有配置**（如果已安装旧版本）
   ```bash
   # 配置文件位于
   /koolshare/configs/lucky/
   ```

2. **上传安装包**
   - 通过软件中心"离线安装"功能
   - 上传 `lucky_upgraded.tar.gz` 文件

3. **安装插件**
   - 插件会自动检测平台兼容性
   - 保留现有配置（如存在）
   - 更新二进制文件到最新版本

4. **启动服务**
   - 默认端口：16601
   - Web 管理界面：`http://路由器IP:16601`

## 配置说明

### 默认参数
- `lucky_enable`: 0 (默认关闭)
- `lucky_port`: 16601 (Web 管理端口)
- `lucky_watchdog`: 0 (看门狗功能)
- `lucky_safeurl`: 0 (安全 URL)

### 配置文件位置
- 主配置：`/koolshare/configs/lucky/`
- 基础配置：`/koolshare/configs/lucky/lucky_base.lkcf`
- 证书目录：`/koolshare/configs/lucky/ca/`
- 日志文件：`/tmp/upload/lucky_log.txt`

## 功能特性

### 核心功能
1. **端口转发** - 灵活的端口映射和转发规则
2. **DDNS** - 动态域名解析服务
3. **Web服务** - 内置 Web 服务器
4. **Stun内网穿透** - NAT 穿透支持
5. **网络唤醒** - Wake on LAN 功能
6. **计划任务** - Cron 任务调度
7. **ACME自动证书** - Let's Encrypt 证书自动申请
8. **网络存储** - WebDAV 等存储服务

### 高级特性
- 进程守护（perp）
- 看门狗监控
- NAT 规则自动恢复
- SSL/TLS 证书管理
- 防火墙规则集成

## 升级差异对比

| 项目 | v1.5.2 (旧版) | v1.6.0 (新版) |
|------|--------------|--------------|
| Lucky 核心 | v2.19.5 (压缩) | v2.19.5 (未压缩) |
| 二进制大小 | 7MB | 16MB |
| 压缩方式 | UPX 4.x | 无压缩 |
| 兼容性 | 标准 | 增强 |
| 来源 | 官方发布 | wanji 优化版 |

## 卸载说明

通过软件中心卸载功能，或手动执行：

```bash
sh /koolshare/scripts/uninstall_lucky.sh
```

卸载会清理：
- 所有程序文件
- 配置文件（需手动备份）
- 开机自启链接
- dbus 配置项
- 防火墙规则

## 故障排查

### 进程无法启动
1. 检查架构兼容性
   ```bash
   uname -m  # 应显示 armv7l 或类似
   ```

2. 检查权限
   ```bash
   chmod +x /koolshare/bin/lucky
   ```

3. 查看日志
   ```bash
   tail -f /tmp/upload/lucky_log.txt
   ```

### Web 界面无法访问
1. 确认端口开放
   ```bash
   netstat -tlnp | grep 16601
   ```

2. 检查防火墙规则
   ```bash
   iptables -L -n | grep 16601
   ```

3. 验证进程状态
   ```bash
   pidof lucky
   ```

## 构建说明

本升级版使用 Python 3 构建脚本：

```bash
python3 build_upgraded.py
```

构建过程：
1. 读取 `config_upgraded.json.js`
2. 更新 `lucky_upgraded/version` 文件
3. 创建 `lucky_upgraded.tar.gz` 压缩包
4. 计算 MD5 并更新配置文件

## 技术说明

### 二进制文件信息
- **格式**：ELF 32-bit LSB executable
- **架构**：ARM, EABI5 version 1 (SYSV)
- **字节序**：Little Endian
- **压缩**：无（UPX 已解压）
- **路径**：/proc/self/exe

### 依赖关系
- **KoolShares框架**：软件中心基础
- **dbus**：配置存储
- **perp**：进程管理
- **iptables**：防火墙规则
- **skipd**：平台特性

## 参考链接

- **Lucky 项目**：https://github.com/gdy666/lucky
- **MerlinLucky**：https://github.com/vj23456/MerlinLucky
- **KoolShare**：https://github.com/koolshare/rogsoft

## 许可证

Lucky 核心：MIT License (Copyright © 2022 gdy, 272288813@qq.com)

MerlinLucky 插件：遵循原项目许可

## 更新日志

完整更新日志请查看 `Changelog_upgraded.txt`

## 维护说明

本升级版由社区维护，建议：
- 定期备份配置文件
- 关注上游 Lucky 项目更新
- 测试后再部署到生产环境
- 保留旧版本备份以便回滚

## 贡献者

- **原作者**：vj23456, kiritoknight
- **Lucky核心**：gdy
- **升级版整合**：基于 wanji 版本优化

---

**注意**：本升级版主要针对需要更好兼容性的用户，如果当前版本运行正常，不一定需要升级。二进制文件较大，请确保路由器有足够存储空间。
