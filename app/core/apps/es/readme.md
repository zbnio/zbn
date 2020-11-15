## APP说明
>通过dsl语句查询ES服务器中的数据
## 动作列表
### 创建问题
**参数**

| 参数 | 类型 | 必填 | 备注 |
| :---- | :---- | :---- | :---- | 
|**ip**|string|`Yes`|Elasticsearch服务器IP|
|**index**|string|`Yes`|要查询的索引名称|
|**port**|string|`Yes`|Elasticsearch端口号|
|**query_str**|string|`Yes`|查询语句，目前支持支DSL格式，参考：https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html#query-dsl|


**返回值**

json格式查询结果


