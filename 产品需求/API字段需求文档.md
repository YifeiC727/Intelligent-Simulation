# API 字段需求文档

> 本文档定义前端所需的后端接口字段，供后端团队设计 API 参考。

---

## 1. 用户模块

### 1.1 用户信息

**使用场景**：所有页面顶部（如后续加用户头像/昵称展示），排行榜列表中展示其他玩家信息

| 字段 | 类型 | 说明 |
|------|------|------|
| user_id | string | 用户唯一标识 |
| nickname | string | 用户昵称 |
| avatar_url | string | 头像地址 |
| created_at | timestamp | 注册时间 |

### 1.2 用户进度（前端首页需要）

**使用场景**：首页右侧「世界探索进度」卡片 + 进度环 + 时间线 + 左侧关卡卡片的解锁/完成状态，页面加载时请求一次

| 字段 | 类型 | 说明 |
|------|------|------|
| user_id | string | 用户 ID |
| total_completed | int | 已完成关卡总数 |
| total_levels | int | 关卡总数 |
| current_chapter | string | 当前所在章节（desk / table / office / cbd） |
| unlocked_levels | string[] | 已解锁的关卡 ID 列表 |

---

## 2. 场景与关卡模块

### 2.1 场景列表

**使用场景**：首页左侧关卡面板的场景切换 + 右侧时间线中每个 Chapter 的进度展示

| 字段 | 类型 | 说明 |
|------|------|------|
| scene_id | string | 场景标识（desk / table / office / cbd） |
| scene_name | string | 场景名称（书桌场景 / 茶几场景…） |
| chapter | string | 章节编号（Chapter 01 / 02…） |
| status | enum | locked / unlocked / completed |
| level_count | int | 该场景下关卡总数 |
| completed_count | int | 该场景下已完成关卡数 |

### 2.2 关卡详情

**使用场景**：首页关卡卡片列表（名称、难度、状态）+ onboarding 引导页（物体数、时间限制、预览图）+ 游戏页初始化（时间、物体数、AI 用时）

| 字段 | 类型 | 说明 |
|------|------|------|
| level_id | string | 关卡唯一标识（desk-tutorial / table-toycar…） |
| scene_id | string | 所属场景 |
| level_name | string | 关卡名称（新手教学 / 玩具车…） |
| level_type | enum | tutorial / normal | 教学关 / 正式关 |
| object_count | int | 物体数量 |
| time_limit | int | 时间限制（秒），0 = 不限时 |
| status | enum | locked / open / completed |
| difficulty | string | 难度标签（初级 / 中级 / 高级） |
| description | string | 关卡描述 |
| preview_image | string | 预览图 URL |
| best_time | int \| null | 用户该关卡最佳用时（秒），未玩过为 null |
| ai_reference_time | int | AI 参考用时（秒），用于结果页对比 |

---

## 3. 游戏会话模块

### 3.1 开始游戏（前端请求）

**使用场景**：用户从 onboarding 页进入游戏页时调用，创建一局游戏会话，获取 AI 参考用时

| 字段 | 类型 | 说明 |
|------|------|------|
| user_id | string | 用户 ID |
| level_id | string | 关卡 ID |

**返回：**

| 字段 | 类型 | 说明 |
|------|------|------|
| session_id | string | 本局游戏唯一 ID |
| ai_reference_time | int | AI 本局参考用时 |

### 3.2 结束游戏（前端提交）

**使用场景**：游戏结束时（完成/超时/放弃）前端提交本局数据，返回值用于渲染结果页（是否刷新最佳、排名、是否解锁新关卡）

| 字段 | 类型 | 说明 |
|------|------|------|
| session_id | string | 游戏会话 ID |
| user_id | string | 用户 ID |
| level_id | string | 关卡 ID |
| elapsed_time | int | 用户用时（秒） |
| objects_placed | int | 成功归位物体数 |
| total_objects | int | 物体总数 |
| completed | bool | 是否全部完成 |
| result | enum | win / lose / timeout |

**返回：**

| 字段 | 类型 | 说明 |
|------|------|------|
| is_new_best | bool | 是否刷新个人最佳 |
| rank | int \| null | 当前排名（如有排行榜） |
| next_level_unlocked | string \| null | 本局是否解锁了新关卡，返回关卡 ID |

---

## 4. 排行榜模块（预留）

### 4.1 获取排行榜

**使用场景**：排行榜页面（预留），展示某关卡 Top N 玩家

**请求参数：**

| 字段 | 类型 | 说明 |
|------|------|------|
| level_id | string | 关卡 ID |
| top_n | int | 获取前 N 名，默认 10 |

**返回列表每项：**

| 字段 | 类型 | 说明 |
|------|------|------|
| rank | int | 排名 |
| user_id | string | 用户 ID |
| nickname | string | 用户昵称 |
| avatar_url | string | 头像 |
| best_time | int | 最佳用时（秒） |
| completed_at | timestamp | 完成时间 |

### 4.2 用户自身排名

**使用场景**：排行榜页面底部"你的排名"卡片 + 游戏结果页展示当前排名

| 字段 | 类型 | 说明 |
|------|------|------|
| rank | int | 当前排名 |
| best_time | int | 个人最佳用时 |
| gap_to_top3 | int | 距离第 3 名差距（秒） |

---

## 5. 接口总览

| 接口 | 方法 | 说明 |
|------|------|------|
| /api/user/profile | GET | 获取用户信息 + 进度 |
| /api/scenes | GET | 获取场景列表（含解锁状态） |
| /api/scenes/{scene_id}/levels | GET | 获取某场景下所有关卡 |
| /api/game/start | POST | 开始游戏，创建会话 |
| /api/game/end | POST | 结束游戏，提交结果 |
| /api/leaderboard/{level_id} | GET | 获取某关卡排行榜 |
| /api/leaderboard/{level_id}/me | GET | 获取用户自身排名 |

---

## 6. 关卡配置表

> 由产品定义，后端录入数据库。后续修改任意数值只需更新数据库记录，无需改代码。

| level_id | 场景 | 关卡名称 | 类型 | 物体数 | 时间限制 | AI参考用时 | 实机成功率 | 解锁条件 |
|----------|------|---------|------|--------|---------|-----------|-----------|---------|
| desk-tutorial | 书桌 | 垃圾收纳（新手教学） | tutorial | 1 | 正计时 · 不限时 | — | 100% | 默认解锁 |
| table-toycar | 茶几 | 玩具车 · 初级 | normal | 1 | 待定 | 待定 | 80% | 完成 desk-tutorial |
| desk-1 | 书桌 | 文具盒 · 初级 | normal | 1 | 待定 | 待定 | 100% | 完成 desk-tutorial |
| table-1 | 茶几 | 纸巾盒 · 中级 | normal | 1 | 待定 | 待定 | 70% | 完成 table-toycar |
| desk-2 | 书桌 | 涂改液 · 中级 | normal | 1 | 待定 | 待定 | 80% | 完成 desk-1 |

---

## 备注

- 本文档不涉及操作轨迹数据回传，仅覆盖游戏状态与用户数据
- 登录/鉴权方式由后端决定，前端按 token 方式对接即可
- 排行榜为预留模块，优先级低于前 4 个模块
- 关卡配置存在数据库，产品调整数值时后端改数据库即可，无需发版
