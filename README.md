特别鸣谢 [ioiio.tv](https://ioiio.tv/) 提供的算力测试支持。

# Seedance 2.5 高燃打斗导演 Skill

面向 Codex 的中文打斗导演 Skill：把一句剧情推导成可复制的即梦／Dreamina Seedance 2.5 打斗提示词或导演执行脚本。支持写实近战、蓄力回合、高速 1v1、群战清场，以及机甲科幻等题材；按角色、兵器、空间和胜负关系设计动作、镜头、受力反馈与特效，不把同一个时间轴反复套用到不同故事。

本仓库只生成文字方案，不提交视频生成任务。完整规则见 [SKILL.md](SKILL.md)，创作与诊断参考资料在 [references](references)；[完整示例](references/examples.md) 可用于判断输出粒度。

## 安装

需要 Git、Codex，以及用于一次性教学状态脚本的 Python 3。默认 Skill 安装目录为 `~/.codex/skills/`；如果设置了 `CODEX_HOME`，请将下文的安装目录改为 `CODEX_HOME/skills/`。

Windows PowerShell：

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
git clone https://github.com/liyue-aigc/seedance-2-5-fight-director.git "$env:USERPROFILE\.codex\skills\seedance-2-5-fight-director"
```

macOS / Linux：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/liyue-aigc/seedance-2-5-fight-director.git ~/.codex/skills/seedance-2-5-fight-director
```

已有同名目录时，先保留自己的修改并检查目录来源，不要直接覆盖。通过上述 `git clone` 安装的版本，日后可在 Skill 目录运行 `git pull` 更新。安装后在 Codex 中使用 `$seedance-2-5-fight-director` 调用；如果当前会话没有识别到新 Skill，重新打开一个会话。

## 怎么用

只需说清“谁和谁／和什么打、在哪里、期望节奏与特效、时长、结尾”。缺项可由 Skill 用合理默认补齐。你可以指定“只输出提示词”“给分段版”“诊断现有提示词”，也可以附角色、武器、场景或动作参考素材。

以下是五种可直接复制、自由改题材与场景的调用示例：

```text
使用 $seedance-2-5-fight-director，写15秒雨夜窄巷写实短打，女拳手对男拳手，一镜到底，格挡、落空反击与重击反馈清楚，不要超自然特效，只输出提示词。

使用 $seedance-2-5-fight-director，写30秒剑修对重甲魔修，云海断桥，前段受压、中段蓄力对波、最后反推破甲；3D国漫CG，特效有明确来源和消散，只输出提示词。

使用 $seedance-2-5-fight-director，写30秒女刀客对男枪客的高速均势战，从古殿打到云海，全程连续攻防，不要蓄力和慢动作；刀光、枪芒、石屑和云浪要华丽但不遮接触点，结尾长枪脱手，只输出提示词。

使用 $seedance-2-5-fight-director，写30秒女将独守城门迎战妖兵潮，一路突围清场，攻击范围逐级升级，敌群被实际击退、阵型瓦解，特效华丽且有层次，给直出版和分段版。

使用 $seedance-2-5-fight-director，写25秒双机甲在轨道船坞高速缠斗，推进器喷流、护盾命中、装甲受力与热量账本都清楚，结尾一方主武器脱手，只输出提示词。
```

例如第三条会推导“古殿内近身交错 → 借殿门外移 → 云海上继续攻防 → 枪脱手”的空间与胜负变化，并将刀光、枪芒、碎石、云浪写成有触发点和消散过程的特效，而不是只堆形容词。实际时间轴和镜头随你的角色与约束重新推导，不固定照搬这条顺序。

## 首次调用教学只展示一次

第一次**实际调用**时，Skill 会先给一条简短上手提示，然后继续完成你当次的创作或诊断。`scripts/first_run.py claim` 以原子方式创建用户级标记；后续调用会跳过教学，**新对话、重开 Codex 和更新 Skill 都不会被当作第一次**。仅阅读、审查或发布 Skill 不会触发标记。

标记位于 `CODEX_HOME/skill-state/seedance-2-5-fight-director/first-run-v1.json`；未设置 `CODEX_HOME` 时位于用户主目录下的 `.codex/skill-state/seedance-2-5-fight-director/first-run-v1.json`。它不在本仓库内，`git pull` 不会清除它。这个保证覆盖**同一台机器、同一 Codex 用户配置**；其他机器或独立用户配置各有自己的首次状态。随时可明确要求“再教我怎么用”，这不会重置自动教学次数。

你可以只查看状态而不消耗首次机会：

```powershell
python scripts/first_run.py status
```

开发测试请传独立的 `--state-dir`，不要用正常配置执行 `claim`。

## 文档入口

- [新手完整说明](references/getting-started.md)：输出类型、参数和反馈方式。
- [完整示例](references/examples.md)：多题材调用与提示词示范。
- [平台适配](references/seedance-adaptation.md)：素材职责、分段、续写及规格边界。
- [诊断方法](references/diagnose.md)：已有提示词或成片反馈的定位与修正。

平台可用规格会变化，请以当前即梦／Dreamina 实际入口为准。
