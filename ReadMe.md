# 自动更新七牛证书
利用Github Action，通过acme.sh（自动）更新七牛cdn的let's encrypt证书。目前仅支持Namesilo域名。

## 运行
 - 在Github上Fork[本repo](https://github.com/dzhuang/qiniu-cdn-ssl-autoupdate-via-github-action)
 - 在Github Action中激活上一步所fork的repo
 - 配置Github Action运行的环境变量
    - DOMAIN: 你七牛cdn的域名
    - ACCESS_KEY: 七牛api ACCESS_KEY
    - SECRET_KEY: 七牛api SECRET_KEY
    - Namesilo_Key: [Namesilo API key](https://www.namesilo.com/account_api.php)

## 致谢
  - [qiniu-cdn-ssl-autoupdate](https://github.com/daozzg/qiniu-cdn-ssl-autoupdate)，Python代码来源
  - [acme.sh](https://github.com/Neilpang/acme.sh)

## 代码许可

The MIT License (MIT).详情见 [License文件](https://github.com/qiniu/python-sdk/blob/master/LICENSE).
