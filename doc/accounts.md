用户模块
========

## 通用


1. 不用浏览器自带的 required 校验. 提示信息及体验不友好.
2. 禁止表单重复提交
3. 非个别字段的错误信息, 使用单独的 block 提示.

    1. 登录时, Incorrect username or password.
    2. 注册时, 2 次密码不一致.
4. tabindex
5. autofocus 第一个输入字段

## 登录 login. 后台名字 Signin

模仿 github

1. 前端不做校验. 如果登录失败, 统一回复: Incorrect username or password.

TODO:
- 如果重复登录失败, 页面刷新效果不够明显. UI 上需要优化.
- return to 登录前的页面

## 注册

- email 等字段的友好提示, 比如, github
