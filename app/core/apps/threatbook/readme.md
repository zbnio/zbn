## APP说明
>查询单个IP在X情报社区中的情报
>
## 动作列表
### IP地址威胁分析
**参数**

| 参数 | 类型 | 必填 | 备注 |
| :---- | :---- | :---- | :---- | 
|**api_key**|string|`Yes`|X社区平台的api_key,需要自己注册|
|**ip**|string|`Yes`|需要分析的IP地址|


**返回值**

返回威胁类型，参考https://x.threatbook.cn/api_docs#/appendix/threat_type
