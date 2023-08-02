# rab_fastapi_login

### 配置片段
```toml
# 外部模块
[external]
  [external.rab_fastapi_login]
    [external.rab_fastapi_login.user]
    # 表名
    table_name = "fastapi_login_user"
      [external.rab_fastapi_login.user.admin]
      # 管理员用户名
      username = "admin"
      # 管理员密码
      password = "admin"
```

### 流程
1. 通过 `/login` 接口登录，传入 `username` 和 `password`。
  - 成功登录后，会返回 `token`。
  - 登录失败的时候，抛出 
2. 