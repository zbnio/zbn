## APP说明

连接指定服务器并运行指定命令

## 动作列表

### 链接服务器并执行

**参数**

| 参数 | 类型 | 必填 | 备注 |
| :---- | :---- | :---- | :---- | 
|target|string|`Yes`|要连接的服务器地址，ip，域名均可|
|port|string|`Yes`|服务器地址端口号|
|command_str|string|`Yes`|要执行的命令|
|user|string|`Yes`|服务器用户名|
|passwd|string|`Yes`|服务器密码|

**返回值**

命令执行结果
