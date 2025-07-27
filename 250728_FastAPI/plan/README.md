# FastAPI 初學者 Web API 專案教學

## 專案概述

這是一個使用 [FastAPI](https://fastapi.tiangolo.com/) 框架建立的簡單 Web API 範例。你將學會：

- 如何建立 FastAPI 應用程式
- 如何設計 GET 與 POST 路由
- 如何回應純文字訊息

本專案適合 Python 與 Web API 初學者，能幫助你快速上手 FastAPI 的基本用法。

---

## 安裝說明

1. **安裝 Python 3.8 以上版本**
2. **安裝依賴套件**

在終端機執行：

```bash
pip install -r requirements.txt
```

3. **啟動伺服器**

```bash
uvicorn main:app --reload
```

伺服器啟動後，預設會在 [http://127.0.0.1:8000](http://127.0.0.1:8000) 提供服務。

---

## 工作原理

### 1. 建立 FastAPI 應用程式

```python
app = FastAPI()
```
這行程式碼建立了一個 FastAPI 應用實例，所有 API 路由都會掛載在這個實例上。

### 2. GET 路由 `/`

```python
@app.get("/")
def get_greeting() -> PlainTextResponse:
    return PlainTextResponse("Hello, World!")
```
當你用瀏覽器或工具（如 curl）GET 請求根目錄 `/`，會收到純文字回應 `Hello, World!`。

### 3. POST 路由 `/data`

```python
@app.post("/data")
async def post_data(request: Request) -> PlainTextResponse:
    return PlainTextResponse("Received")
```
當你對 `/data` 發送 POST 請求（可附帶 JSON 資料），伺服器會回應 `Received`。

---

## 範例用法

### 1. 取得歡迎訊息

```bash
curl http://127.0.0.1:8000/
# 或直接用瀏覽器開啟 http://127.0.0.1:8000/
```

### 2. 傳送資料到 /data

```bash
curl -X POST http://127.0.0.1:8000/data -H "Content-Type: application/json" -d '{"key": "value"}'
```

---

## 範例輸出

### GET /
```
Hello, World!
```

### POST /data
```
Received
```

---

## 測試

本專案已內建 pytest 測試，執行下列指令可驗證 API 是否正常：

```bash
pytest test_main.py
```

---

## 參考資源

- [FastAPI 官方文件](https://fastapi.tiangolo.com/)
- [Uvicorn 文件](https://www.uvicorn.org/)
