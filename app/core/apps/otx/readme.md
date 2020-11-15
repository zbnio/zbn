## APP说明
>查询ioc是否在某个pulse,例如：查询某个IP是否为botnet地址，则ioc为IP地址，如果查询CC
域名则ioc为域名
>
## 动作列表
### 威胁情报匹配
**参数**

| 参数 | 类型 | 必填 | 备注 |
| :---- | :---- | :---- | :---- | 
|**api_key**|string|`Yes`|OTX平台的api_key,需要自己注册|
|**pulse_id**|string|`Yes`|情报的pulseid号，参考https://otx.alienvault.com/browse/global|
|**ioc**|string|`Yes`|需要查询的威胁特征，如可疑的IP,域名、hash|


**返回值**

Bool类型命中返回`True`反之为`False`
