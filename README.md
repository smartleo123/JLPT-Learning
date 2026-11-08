# JLPT 考古題與文法筆記

[開啟學習網站](https://smartleo123.github.io/JLPT-Learning/)

整理 2010–2025 共 31 場前段題面來源，包含 301 個詞彙、96 個文法條目及 8 組觀念比較。2022–2025 的 8 場新增資料已與舊筆記整合。

- 讀音、繁體中文解說、固定搭配、接續、易混辨析與自編例句。
- 年份、檢出場次、語意分類、近年與尚未掌握篩選。
- 收藏、遮答回想、已掌握進度；可匯出／匯入進度。
- 每條來源可展開場次與 PDF 頁碼，對照私人題本；不公開 Drive 檔案連結。
- 手機版、鍵盤操作、列印與無 JavaScript 閱讀備援。

**檢出場次不是正解考次。** 統計包含題幹與選項，OCR 有漏字；各年整理範圍不同，不代表全卷詞頻或官方出題機率。詳見 [METHOD.md](METHOD.md)。

## 更新內容

編輯 `data/study.json` 與 `scripts/build.py` 中的比較表後執行：

```bash
python3 scripts/build.py
python3 scripts/check.py
node --check app.js
```

把產生的 `index.html` 一起提交。GitHub Pages 從 main 根目錄提供靜態網站，不需要 npm 安裝。原始考題 PDF 不在 repository 中。

例句已附繁體中文翻譯與漢字上方的假名標音（HTML ruby），同步用於閱讀卡片、回想解說、列印與無 JavaScript 閱讀。卡片只顯示總檢出場次。觀念比較表的 32 組例句亦附翻譯與標音。
