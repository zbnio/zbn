## APP说明
>识别指定端口信息

**本机需要安装 nmap 工具**

## 动作列表

### 端口识别

**参数**

| 参数 | 类型 | 必填 | 备注 |
| :---- | :---- | :---- | :---- | 
|**IP**|string|`Yes`|需要扫描的目标地址|
|**Port**|string|`Yes`|需要扫描的端口号，支持单个端口，逗号分隔和范围`53,80 or 1-3 or 80`|
|**Protocol**|string|`Yes`|扫描的协议类型【tcp/udp】默认为tcp|

**返回值**

下面是分别扫描53和80端口的扫描结果，`n/a`代表未取到值。
```json
{
	'data': {
		'port': "['53', '80']",
		'state': "['filtered', 'open']",
		'reason': "['no-response', 'syn-ack']",
		'name': "['domain', 'http']",
		'service': "['n/a', 'Apache httpd']"
	}
}
```
json格式的扫描结果
