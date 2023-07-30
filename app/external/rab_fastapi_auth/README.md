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