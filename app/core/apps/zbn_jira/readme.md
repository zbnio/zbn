## APP说明
>jira系统相关操作，目前只有创建问题功能
## 动作列表
### 创建问题
**参数**

| 参数 | 类型 | 必填 | 备注 |
| :---- | :---- | :---- | :---- | 
|**server**|string|`Yes`|jira服务器地址，ex：http://localhost:2920|
|**user**|string|`Yes`|登录jira的用户名|
|**passwd**|string|`Yes`|登录jira的密码|
|**project_name**|string|`Yes`|需要创建的项目名称|
|**summary**|string|`Yes`|问题标题|
|**desc**|string|`Yes`|问题描述|
|**types**|string|`Yes`|问题类型|

**返回值**

问题编号

