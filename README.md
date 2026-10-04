> 特别鸣谢 [ioiio.tv](https://ioiio.tv/) 提供的算力测试支持。

<h1 align="center">Seedance 2.5<br>高燃打斗导演</h1>

<p align="center">一句剧情，编排一场有攻防、有镜头、有特效因果的战斗。</p>
<p align="center"><strong>Codex Skill · 中文提示词 · 五类战斗方向</strong></p>

<p align="center">
  <a href="#快速开始">快速开始</a> ·
  <a href="#五类示例">五类示例</a> ·
  <a href="#安装与更新">安装与更新</a> ·
  <a href="#首次使用">首次使用</a> ·
  <a href="#更多文档">更多文档</a>
</p>

---

为即梦／Dreamina Seedance 2.5 编写打斗提示词与导演脚本。给出角色、场景和结局，Skill 会继续推导攻防节奏、空间路线、受力反馈、运镜与特效，把这场戏写成可复制的文字方案。

| 你想做什么 | 可以得到什么 |
| :--- | :--- |
| 从一句剧情开始 | 动作与镜头连贯的打斗提示词、分镜脚本 |
| 做复杂场面 | 单段直出方案，或带承接状态的分段方案 |
| 加强华丽特效 | 写清来源、轨迹、碰撞、环境反馈与消散 |
| 改善已有提示词 | 对节奏、攻防、镜头、特效和连续性的诊断与修改 |

## 快速开始

**① 在 Codex 对话中安装**

复制下面这段话，交给 Codex 自带的 `skill-installer`：

```text
使用 $skill-installer，安装这个 GitHub 仓库中的 Skill：
https://github.com/liyue-aigc/seedance-2-5-fight-director

SKILL.md 就在仓库根目录，路径为 .，
安装名称为 seedance-2-5-fight-director。
```

此方式使用安装器下载；安装完成后，在下一次消息中调用。若尚未识别到 Skill，重新打开会话。已有同名 Skill 时，请看下方的[更新说明](#更新已安装的版本)。

**② 给出你的打斗需求**

```text
使用 $seedance-2-5-fight-director，
写30秒女刀客对男枪客，从古殿打到云海。
全程高速均势，特效华丽，不要蓄力和慢动作，
结尾长枪脱手，只输出可复制提示词。
```

**③ 将提示词用于视频制作**

按方案在即梦／Dreamina 中添加素材、生成视频；分段方案可逐段制作后衔接。本 Skill 产出文字方案，不直接提交视频生成任务。

## 五类示例

角色、武器、地点、时长和结局都可以替换。展开任意一项即可复制使用。

<details>
<summary><strong>01 · 写实短打</strong> — 近身攻防、重量与打击反馈</summary>

```text
使用 $seedance-2-5-fight-director，
写15秒雨夜窄巷写实短打，女拳手对男拳手。
一镜到底，格挡、落空反击与重击反馈清楚，
不要超自然特效，只输出提示词。
```

</details>

<details>
<summary><strong>02 · 蓄力回合</strong> — 压制、反转与决胜</summary>

```text
使用 $seedance-2-5-fight-director，
写30秒剑修对重甲魔修，场景是云海断桥。
前段受压、中段蓄力对波、最后反推破甲。
3D国漫CG，特效有明确来源和消散，只输出提示词。
```

</details>

<details>
<summary><strong>03 · 高速 1v1</strong> — 连续交锋、追逐与兵器战</summary>

```text
使用 $seedance-2-5-fight-director，
写30秒女刀客对男枪客的高速均势战，穿行于竹林与吊桥。
全程连续攻防，不要蓄力和慢动作。
刀光、枪芒和木屑华丽但不遮接触点，
结尾长枪脱手，只输出提示词。
```

</details>

<details>
<summary><strong>04 · 群战清场</strong> — 敌群密度、范围攻击与突围</summary>

```text
使用 $seedance-2-5-fight-director，
写30秒女将独守城门迎战妖兵潮，一路突围清场。
攻击范围逐级升级，敌群被实际击退、阵型瓦解，
特效华丽且有层次，给直出版和分段版。
```

</details>

<details>
<summary><strong>05 · 科幻机甲</strong> — 推进惯性、护盾与结构受力</summary>

```text
使用 $seedance-2-5-fight-director，
写25秒双机甲在轨道船坞高速缠斗。
推进器喷流、护盾命中、装甲受力与热量变化都清楚，
结尾一方主武器脱手，只输出提示词。
```

</details>

还可以直接说：**“诊断这段提示词”**、**“攻防再紧一点”**、**“保留剧情，换成机甲”**，或指定角色图、武器图与动作参考的用途。更多输出范例见[完整示例](references/examples.md)。

## 安装与更新

使用 Codex，并准备 Python 3.10 或更新版本运行首次引导脚本。上方推荐的 `skill-installer` 可直接下载；以下手动安装方式另需 Git，以及可访问 GitHub 的终端网络。

### 手动安装

下列命令用于**首次安装**，目标目录应尚不存在。命令会读取自定义 `CODEX_HOME`；未设置时使用用户目录下的 `.codex`。

<details>
<summary><strong>Windows · PowerShell</strong></summary>

```powershell
$codexDir = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE ".codex" }
$skillDir = Join-Path $codexDir "skills\seedance-2-5-fight-director"
New-Item -ItemType Directory -Force -Path (Split-Path $skillDir) | Out-Null
git clone https://github.com/liyue-aigc/seedance-2-5-fight-director.git "$skillDir"
```

安装完成后，可以确认入口文件：

```powershell
Test-Path (Join-Path $skillDir "SKILL.md")
```

返回 `True` 表示文件已放到目标目录。

</details>

<details>
<summary><strong>macOS / Linux · 终端</strong></summary>

```bash
codex_dir="${CODEX_HOME:-$HOME/.codex}"
skill_dir="$codex_dir/skills/seedance-2-5-fight-director"
mkdir -p "$(dirname "$skill_dir")"
git clone https://github.com/liyue-aigc/seedance-2-5-fight-director.git "$skill_dir"
```

安装完成后，可以确认入口文件：

```bash
test -f "$skill_dir/SKILL.md" && echo "Skill files installed"
```

</details>

### 更新已安装的版本

**通过 Git 安装的版本**可以使用下面的更新命令。若有自己的修改，先保存或提交；`--ff-only` 不会自动合并分叉历史。

<details>
<summary><strong>展开 Git 更新命令</strong></summary>

Windows PowerShell：

```powershell
$codexDir = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE ".codex" }
$skillDir = Join-Path $codexDir "skills\seedance-2-5-fight-director"
git -C "$skillDir" pull --ff-only
```

macOS / Linux：

```bash
codex_dir="${CODEX_HOME:-$HOME/.codex}"
git -C "$codex_dir/skills/seedance-2-5-fight-director" pull --ff-only
```

</details>

**通过安装器下载的版本**通常不包含 Git 历史，不能直接 `git pull`。可让 Codex“从上述仓库更新此 Skill，先备份现有目录并保留本地自定义”；安装器本身会拒绝覆盖已有同名目录。

<details>
<summary><strong>常见安装问题</strong></summary>

| 提示或现象 | 处理方法 |
| :--- | :--- |
| `git` 或 `python` 找不到 | 安装相应工具后重新打开终端；Windows 的 Python 也可尝试 `py -3` |
| 目标目录已存在 | 已安装时走更新流程；不要重复 `git clone` 到同一目录 |
| GitHub 连接超时、域名解析失败 | 检查终端网络与代理；浏览器能访问不代表 Git 已使用系统代理，可先尝试上方 Codex 安装方式 |
| 文件已安装但没有识别到 | 在下一次消息中显式调用 Skill；必要时重新打开 Codex 会话 |

</details>

## 首次使用

第一次实际调用会展示一条简短教学，随后继续完成你的请求。**同一台机器、同一 Codex 配置下，换对话、重开应用或更新 Skill，都不会自动重播。**

需要再看说明时，直接说“再教我怎么用”即可。

<details>
<summary>查看状态保存位置</summary>

首次状态保存在 Skill 仓库之外：

```text
CODEX_HOME/skill-state/seedance-2-5-fight-director/first-run-v1.json
```

未设置 `CODEX_HOME` 时，根目录为用户目录下的 `.codex`。不同机器或不同 Codex 配置分别记录状态。

在 Skill 目录中执行以下命令，可以查询状态而不消耗首次机会：

```bash
python scripts/first_run.py status
```

</details>

## 更多文档

| 文档 | 内容 |
| :--- | :--- |
| [新手说明](references/getting-started.md) | 输出类型、需求描述与反馈方式 |
| [完整示例](references/examples.md) | 多题材提示词与分镜范例 |
| [诊断方法](references/diagnose.md) | 排查节奏、动作、镜头与特效问题 |
| [平台适配](references/seedance-adaptation.md) | 参考素材、分段、续写与规格边界 |
| [Skill 入口](SKILL.md) | 完整调用规则与资料索引 |

视频规格与可用模式以即梦／Dreamina 当前实际入口为准。
