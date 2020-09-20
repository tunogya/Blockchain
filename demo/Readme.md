# REST API参考

## 1.使用REST-API
您可以通过 REST API 调用智能合约，写入或查询链上信息，也可以查询区块及交易信息，并监听区块链事件。区块链 REST-API 使用 Bearer Token 的认证方
式，在调用API时，您需要额外指定 HTTP 头 “Authorization: Bearer <Your Access Token>” 来提供您的 Access Token。

## 2.生成 Access Token
### API 路径
POST /api/auth/token/

### 请求参数
**Body**


## 3.刷新 Access Token
### API 路径
POST /api/auth/refresh/

### 请求参数
**Body**


## 4.验证 Access Token
### API 路径
POST /api/auth/vertify/

### 请求参数
**Body**



## 5.发起上链交易
向区块链网络发送交易, 交易通过节点验证并被成功写入账本后返回。

### API 路径
POST /api/demo/transactions/

### 请求参数
**URL Query**

| URL Query 参数 | 类型    | 是否必选 | 描述                                 |
|---------------|---------|--------|-------------------------------------|
| timeout       | Integer | 否     | 等待交易完成的超时时间，单位秒，默认值 180。|
| content_check | String  | 否     | 内容合规检查，并根据检测结果拒绝该笔交易上链。默认值空，表示不检测。 |

**返回结果**
| 名称     | 类型      | 描述       |
|---------|----------|------------|
| Success | Boolean  | 请求是否成功 |
| Error   | Error    |            |
| Result  | Response |            |

Error
| 名称        | 类型      | 描述         |
|------------|----------|--------------|
| code       | Integer  | 错误码        |
| message    | String   |  错误描述信息  |
| request_id | String   |  请求ID       |

Response
| 名称        | 类型      | 描述         |
|------------|----------|--------------|
| id       | String  | 交易ID        |
| status    | String   |  状态码  |
| event | List<Event>   |  交易所产生的区块链事件列表       |
| data   | String | 经过Base64编码的链码返回数据 |

## 6.发起查询交易
查询区块链账本中的数据。

### API 路径
GET /api/demo/transactions/

## 7.查询区块
查询某一区块的信息

### API 路径
GET /api/demo/blocks/\<pk\>/

    <pk>表示区块块高， “latest” 表示当前最新的区块

## 8.查询交易信息
查询某一交易的信息。

### API 路径
GET /api/demo/transactions/\<pk\>/

    <pk>为交易ID

### 返回结果
Transaction
| 名称        | 类型      | 描述         |
|------------|----------|--------------|
| id       | String  | 交易ID        |
| state    | String   |  交易状态，”VALID” 表示合法交易，其它值表示非法交易  |
| from | String   | 交易的发起者，格式为 <组织MSP>.<用户名>       |
| to   | String | 交易调用的目标名称  |
| input | String | 经过 Json 编码的链码调用参数 |
| events | List<Event> | 交易所产生的区块链事件列表 |
| data  | Object    | 交易的详细内容，数据结构为交易中的 common.Payload |



