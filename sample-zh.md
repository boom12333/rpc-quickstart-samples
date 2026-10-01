# 在接入 EVM 服务前，先确认链 ID

**Pep.Liu 独立演示样稿，使用 AI 辅助撰写和核查。不是客户案例，也不是安全审计。**

本例只读取链 ID，不连接钱包，不签名，不发送交易。演示端点 `http://127.0.0.1:8765` 在本机模拟响应，不是区块链节点。实际接入时应使用服务商提供的端点，并检查目标网络和套餐限制。

## 发出请求

```sh
curl --fail-with-body --silent --show-error \
  --max-time 10 \
  -H 'Content-Type: application/json' \
  --data '{"jsonrpc":"2.0","id":1,"method":"eth_chainId","params":[]}' \
  http://127.0.0.1:8765
```

如果 curl 版本不支持 `--fail-with-body`，升级 curl，或者改用 `--fail` 并单独检查错误。真实服务端点可能包含 API 密钥，不要放进公开仓库、截图或支持工单。

本地演示会返回：

```json
{"jsonrpc":"2.0","id":1,"result":"0x1"}
```

`0x1` 是十六进制的 1，对应以太坊主网的链 ID。这里的结果是模拟数据。真实响应必须与准备接入的网络核对。链 ID 正确不代表端点支持所有方法，也不代表历史数据完整。

## HTTP 成功不等于 RPC 成功

HTTP 状态码反映传输或服务网关状态；JSON-RPC 响应里的 `error` 反映请求本身的错误。即使 HTTP 返回 200，也可能有 RPC 错误。使用结果前核对响应 `id`，并分别处理这两种情况。

| 英文术语 | 推荐中文 | 使用说明 |
|---|---|---|
| endpoint | 服务端点 | 指请求发送到的服务地址，不译为“钱包地址” |
| chain ID | 链 ID | 区分网络；与区块高度不同 |
| read-only request | 只读请求 | 不签名、不发交易，不保证服务免费 |
| rate limit | 请求频率限制 | 与额度耗尽区分；遵循服务商规则 |
| bounded backoff | 有上限的退避重试 | 同时限制间隔和次数 |
| JSON-RPC error | JSON-RPC 错误 | 不能只检查 HTTP 状态码 |
| API credential | API 凭据 | 不出现在对外材料中 |
| simulated response | 模拟响应 | 明确标识，不能当实时链上数据 |

## 排障说明

- 401/403：检查凭据、来源限制和账户权限，不把密钥发给第三方。
- 429：检查频率和套餐规则，采用有上限的退避，不无限重试。
- 超时：检查网络和服务状态，设置明确的请求超时时间。
- Method not found：核对方法名、网络与服务商支持范围。
- 链 ID 不符：先停止接入测试，选择正确端点，不发送交易来试错。

## 本地化核查记录

保留 `eth_chainId`、`params`、`id` 和代码原样；将 endpoint 与钱包地址明确区分；保留“模拟数据”和成功范围限制；把 error 处理写成可执行检查，避免误译成“状态码 200 即成功”。本样稿展示试译方法，不宣称代表任何项目的官方中文版。

原文独立样稿见 sample-en.md。文本采用 CC BY 4.0，代码采用 MIT。第三方方法语义参考 https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_chainid 。
