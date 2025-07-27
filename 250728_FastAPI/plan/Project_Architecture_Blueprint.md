# 專案架構藍圖

> 產生日期：2025年7月28日

---

## 1. 架構偵測與分析

### 技術堆疊自動偵測
- 本專案為 Python 專案，主要使用 FastAPI 框架建構 Web API。
- 依據 `requirements.txt` 及 `main.py`，未偵測到其他大型框架或 ORM。
- 依據目錄結構，屬於單體應用（Monolithic）架構，無明顯分層或微服務劃分。

### 架構模式偵測
- 採用 Layered（分層）+ Monolithic（單體）架構。
- 主要分為 API 路由層與應用邏輯層，尚未明確拆分資料存取層。
- 依據 FastAPI 慣例，路由與業務邏輯可進一步拆分於多個模組。

---

## 2. 架構總覽
- 採用 FastAPI 建立 RESTful API，簡潔明瞭。
- 以函式為單位設計路由，易於擴充。
- 目前僅有單一檔案，建議未來依功能拆分模組。

---

## 3. 架構視覺化
- 高階架構：
  - Client → FastAPI 應用（main.py）→ 回應
- 元件互動：
  - 路由函式處理請求，回傳純文字。
- 資料流：
  - POST /data 接收 JSON，GET / 回傳文字。

---

## 4. 核心架構元件
- **FastAPI 應用實例**：API 進入點，負責路由註冊與請求分派。
- **路由函式**：處理 HTTP 請求，回應資料。
- **Request/Response 物件**：負責請求資料解析與回應格式化。

---

## 5. 架構分層與依賴
- 目前僅有 API 層，無明確分層。
- 建議未來拆分 service、repository 層，強化維護性。
- 無循環依賴。

---

## 6. 資料架構
- 尚未有明確的資料模型。
- POST /data 可擴充為接收/驗證複雜 JSON 結構。
- 建議未來導入 Pydantic Model 處理資料驗證。

---

## 7. 橫切關注點實作
- **認證授權**：目前未實作，可用 FastAPI OAuth2/JWT 擴充。
- **錯誤處理**：未自訂例外處理，建議加入全域 exception handler。
- **日誌監控**：未實作，建議導入 logging。
- **驗證**：未實作，建議用 Pydantic Model 驗證輸入。
- **組態管理**：可用 .env 或 config.py 管理環境變數。

---

## 8. 服務通訊模式
- 單體應用，僅 HTTP RESTful API。
- 無服務間通訊。

---

## 9. Python 架構模式
- 模組組織簡單，建議依功能拆分多個 py 檔。
- 依賴管理以 requirements.txt 為主。
- 可支援同步與非同步程式設計。

---

## 10. 實作模式
- 路由函式直接處理請求，建議未來抽離 service 層。
- 可用依賴注入（Depends）管理複雜依賴。
- 建議導入 repository/service pattern。

---

## 11. 測試架構
- 已有 test_main.py，建議撰寫單元測試覆蓋所有路由。
- 可用 pytest 進行單元與整合測試。
- 測試資料可用 fixture 管理。

---

## 12. 部署架構
- 可用 uvicorn/gunicorn 部署。
- 建議撰寫 Dockerfile，支援容器化。
- 組態可用 .env 管理。

---

## 13. 擴充與演進模式
- 新增功能建議：
  - 新增 py 檔案，依功能命名。
  - 路由、service、repository 分層。
  - 依賴注入管理新元件。
- 修改建議：
  - 先撰寫測試，確保相容性。
  - 重要變更可用 deprecation warning。
- 整合外部系統：
  - 可用 requests/httpx 呼叫外部 API。
  - 導入 adapter pattern。

---

## 14. 架構模式範例
```python
from fastapi import APIRouter, Depends
from pydantic import BaseModel

router = APIRouter()

class Item(BaseModel):
    name: str
    value: int

@router.post("/items")
def create_item(item: Item):
    # 這裡可呼叫 service 層
    return {"msg": f"Item {item.name} created."}
```

---

## 15. 架構決策記錄
- 選用 FastAPI：因其輕量、易於擴充、支援 async。
- 單體架構：適合小型專案，易於部署。
- 未導入 ORM：因目前無資料庫需求。
- 依賴管理採 requirements.txt，簡單明瞭。

---

## 16. 架構治理
- 目前無自動化檢查，可用 flake8/black 強化一致性。
- 建議定期 code review，維持架構一致。
- 文件建議集中於 docs/。

---

## 17. 新功能開發藍圖
- 建議流程：
  1. 於 routes/、services/、models/ 建立新檔案。
  2. 撰寫 Pydantic Model 定義資料結構。
  3. 路由呼叫 service 層，service 處理業務邏輯。
  4. 撰寫/更新測試。
- 標準檔案組織：
  - main.py（進入點）
  - routes/（路由）
  - services/（業務邏輯）
  - models/（資料結構）
- 常見陷阱：
  - 路由與邏輯未分層，導致維護困難。
  - 忽略測試，降低品質。
  - 忽略型別註記與文件。

---

> 本藍圖由自動化工具產生，建議每次重大架構調整後重新產生並審查。
