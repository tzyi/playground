from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

# ===============================
# FastAPI 基礎 Web API 範例
# ===============================
# 本檔案展示如何使用 FastAPI 建立簡單的 Web API。
# 你將學會：
# - 如何建立 FastAPI 應用程式
# - 如何設計 GET 與 POST 路由
# - 如何回應純文字訊息

# 建立 FastAPI 應用程式實例
# 這是整個 API 的進入點
app = FastAPI()

# -------------------------------
# 路由 1：根目錄 ('/')
# -------------------------------
@app.get("/")
def get_greeting() -> PlainTextResponse:
    """
    當用戶端以 GET 方法存取根目錄時，回傳一段歡迎訊息。
    回傳型態為純文字（PlainTextResponse）。
    """
    # 回應一段簡單的歡迎訊息
    return PlainTextResponse("Hello, World!")

# -------------------------------
# 路由 2：/data (POST)
# -------------------------------
@app.post("/data")
async def post_data(request: Request) -> PlainTextResponse:
    """
    當用戶端以 POST 方法傳送資料到 /data 時，伺服器會接收 JSON 資料，
    並回傳確認訊息。

    參數：
        request (Request): FastAPI 的 Request 物件，包含用戶端傳來的資料。
    回傳：
        PlainTextResponse: 簡單的確認訊息。
    """
    # 你可以透過下行取得傳來的 JSON 資料：
    # data = await request.json()
    # 但本範例僅回應固定訊息
    return PlainTextResponse("Received")
