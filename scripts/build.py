import json,html
from pathlib import Path
root=Path(__file__).resolve().parents[1];db=json.loads((root/'data/study.json').read_text());e=html.escape
concept_examples=json.loads((root/'data/concept-examples.json').read_text())
def ruby(parts):
 return ''.join('<ruby>'+e(p['text'])+'<rt>'+e(p['reading'])+'</rt></ruby>' if p.get('reading') else e(p['text']) for p in parts)
def example_html(x):
 return '<div class="example"><span lang="ja">'+ruby(x['exampleParts'])+'</span><div class="translation" lang="zh-Hant">'+e(x['translation'])+'</div></div>'
concepts=[('01',
  '必要條件：沒有 A，就沒有 B',
  '先判斷句子是在說「不可或缺」，還是在說一般原因。',
  [('N あっての N', '人や基盤があって初めて成立', 0), ('N なくしては＋否定', '沒有前項便無法完成', 1), ('V ないことには＋否定', '先滿足條件才有辦法判斷', 2), ('普通形＋以上（は）', '既成前提→責任、決心', 3)]),
 ('02',
  '讓步：承認之後，要轉到哪裡？',
  'ものの、反面、つつも都有轉折，但結構與焦點不同。',
  [('～ものの', '雖然成立，結果不如預期', 4), ('～反面', '同一事物同時存在的兩面', 5), ('V ます語幹＋つつも', '知道／承認，行動仍相反', 6), ('～くらいなら', '前項不想接受，寧選後項', 7)]),
 ('03',
  '時間：立即發生，還是逐漸改變？',
  '注意辭書形、た形和ている形；差一個形，意思可能不同。',
  [('V 辭書形＋なり', '一做 A 就發生 B', 8), ('V ます語幹＋次第', 'A 完成後立即做 B', 9), ('～うちに', '過程中逐漸、自然變化', 10), ('～てからというもの', '轉捩點後持續的改變', 11)]),
 ('04',
  '不能、不得、不肯：不是同一件事',
  '先區分能力、完成量、意志及社會責任，才能排除選項。',
  [('～きれない', '不能全部完成', 12), ('～ようがない', '沒有可行手段', 13), ('～ようとしない', '不願意採取行動', 14), ('～わけにはいかない', '基於立場、責任不能做', 15)]),
 ('05',
  '相乘、交換、契機：因果的不同方向',
  '看到「兩個因素」時，先問它們是合作加強，還是有得有失。',
  [('～と相まって', 'A 與 B 一起增強結果', 16), ('～と引きかえに', '獲得 A，同時失去 B', 17), ('～を機に', '一次事件帶來轉變', 18), ('～を皮切りに', '以 A 為一連串事件的開端', 19)]),
 ('06',
  '推測與評價：語氣有多強？',
  '不要只把中文翻成「一定／最好」；比較說話者的確信與要求程度。',
  [('～見込みだ', '依資料預測未來', 20), ('～兆しがある', '已能看到的跡象', 21), ('～に越したことはない', '理想的選擇', 22), ('～ざるを得ない', '迫於情況只好做', 23)]),
 ('07',
  '授受與敬語：先找「誰做」',
  '把主語、受惠者與動作方向畫清楚，再選尊敬語或謙讓語。',
  [('おいでくださる', '對方來，我方受惠', 24), ('お越しいただく', '我方承蒙對方來', 25), ('伺う', '我去／我問的謙讓語', 26), ('お越しになる', '對方來的尊敬語', 27)]),
 ('08',
  '詞彙用法：換成近義詞為何會錯？',
  'N1 常用題靠的是典型賓語與語境，不能只記中文字義。',
  [('運用／使用／起用', '資金・制度／工具／人員', 28), ('補填／補充／記入', '缺損／不足數量／表格', 29), ('手先／手際／手腕', '操作靈巧／步驟效率／辦事能力', 30), ('改修／改正／修正', '設施／法律規則／錯誤資料', 31)])]
concept_html=''.join('<article class="concept"><div class="step">'+num+' / 觀念比較</div><h3>'+title+'</h3><p>'+desc+'</p><div class="table-scroll"><table><thead><tr><th>形式</th><th>核心與例子</th></tr></thead><tbody>'+''.join('<tr><td lang="ja">'+e(t)+'</td><td>'+e(meaning)+example_html(concept_examples[ex])+'</td></tr>' for t,meaning,ex in rows)+'</tbody></table></div></article>' for num,title,desc,rows in concepts)
cov=''.join(f'<tr><td>{e(x["name"])}</td><td>前 {x["pages"]} 頁</td><td>{e(x["quality"])}</td><td>依年份對照私人題本</td></tr>' for x in db['coverage'])
static=''.join('<article class="card"><h3 lang="ja">'+e(x['term'])+'</h3><div class="reading">'+e(x['reading'])+'</div><p>'+e(x['meaning'])+'</p><p>'+e(x['connection'] or x['usage'])+'</p><p>'+e(x['pitfall'])+'</p>'+example_html(x)+'<p class="small">檢出 '+str(x['count'])+' 場</p></article>' for x in db['items'])
v=sum(x['type']=='vocab' for x in db['items']);g=len(db['items'])-v
s='''<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="JLPT N1 歷年語彙與文法學習筆記：2010–2025 前段題面檢出、近義辨析、文法比較、主動回想與學習進度。"><title>JLPT 考古題與文法筆記</title><link rel="stylesheet" href="styles.css"><link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='12' fill='%2317614e'/%3E%3Ctext x='32' y='46' font-size='42' text-anchor='middle' fill='white'%3E日%3C/text%3E%3C/svg%3E"></head><body><a href="#study" class="skip">跳至學習條目</a><div class="wrap"><header class="top"><div class="brand"><span class="seal">日</span>N1 STUDY NOTES</div><nav aria-label="頁面導覽"><a href="#study">字詞・文法</a><a href="#concepts">觀念比較</a><a href="#review">主動回想</a><a href="#sources">來源</a></nav></header><section class="hero"><div><div class="eyebrow">2010 — 2025 / Japanese Language Proficiency Test</div><h1>JLPT 考古題與文法筆記</h1><a class="start" href="#study">開始今天的學習 ↓</a></div><aside class="hero-side"><div class="numbers"><div><b>__V__</b><br><small>詞彙條目</small></div><div><b>__G__</b><br><small>文法條目</small></div><div><b>31</b><br><small>場次來源</small></div></div><p class="range">2022–2025 新題已整合<br>每個考點，都回到用法與辨析。</p></aside></section>
<section aria-labelledby="path-title"><div class="section-head"><h2 id="path-title">每天一小段，讀懂考點</h2><span class="label">建議 20–30 分鐘 / 自訂步調</span></div><div class="plan"><article><div class="step">01 / 先抓反覆出現的線索</div><h3>選 10 個跨年詞彙</h3><p>篩選「至少 2 場」，記一個搭配，再說明它與近義詞的差異。</p></article><article><div class="step">02 / 用對比理解句型</div><h3>讀一組文法觀念</h3><p>依序確認接續、前後關係、語氣限制；用自己的情境造句。</p></article><article><div class="step">03 / 蓋住解說再回想</div><h3>今天學，隔天再說一次</h3><p>收藏不熟條目，練到能說出意思和搭配，再標記「已掌握」。</p></article></div></section>
<div class="note"><b>檢出場次 ≠ 正解考次。</b>數字是目前前段題面／選項的跨卷檢出下限，每場最多一次；不是全卷詞頻或官方出題機率。來源展開後可區分「重點整理」和「文字檢出」。部分來源為民間重建版，OCR 可能漏字；例句與比較表為自編教學。<a href="#sources">查看範圍</a></div>
<section id="study"><div class="section-head"><h2>字詞・文法資料庫</h2><span id="progress" class="small"></span></div><div id="storage-note" class="storage-note" hidden>瀏覽器無法儲存進度；本次仍可使用，請匯出備份。</div><div class="filters"><label class="skip" for="q">搜尋詞彙、讀音、中文或用法</label><input id="q" class="search" type="search" placeholder="搜尋詞彙、讀音、中文或用法，例如：相まって、回饋、まぎらわしい…"><div class="filter-row"><label>年份<select id="year"><option value="">全部年份</option></select></label><label>重現程度<select id="freq"><option value="0">全部條目</option><option value="2">至少 2 場</option><option value="3">至少 3 場</option><option value="4">至少 4 場</option></select></label><label>觀念分類<select id="category"><option value="">全部分類</option></select></label><label>學習範圍<select id="scope"><option value="all">全部</option><option value="recent">2022 後有檢出</option><option value="unlearned">尚未掌握</option></select></label><label>排序<select id="sort"><option value="freq">總檢出場次</option><option value="recent">近年檢出場次</option><option value="alpha">日文字序</option></select></label></div></div><div class="tabs" aria-label="條目類型"><button data-type="all" aria-pressed="true">全部</button><button data-type="vocab" aria-pressed="false">單字與搭配</button><button data-type="grammar" aria-pressed="false">文法與接續</button><button id="fav" aria-pressed="false">★ 我的收藏</button><button id="reset">清除篩選</button></div><div class="result"><span id="count" role="status" aria-live="polite"></span><div><button id="begin-review">用目前篩選練回想</button> <button id="print">列印篩選結果</button></div></div><div id="cards" class="cards"></div><noscript><p>未啟用 JavaScript：以下可直接閱讀全部條目；互動篩選需要 JavaScript。</p><div class="cards">__STATIC__</div></noscript><div class="more"><button id="more">再看 30 筆 ↓</button></div></section>
<section id="concepts"><div class="section-head"><h2>把容易混淆的觀念，一次分清楚</h2><span class="label">8 組比較 / 含延伸補充，不另外計入考頻</span></div><div class="concepts">__CONCEPTS__</div></section>
<section id="review"><div class="section-head"><h2>主動回想</h2><span class="small">套用上方篩選；自我評估，不是模擬考分數</span></div><div id="recall" class="recall"><div class="label">先想，再看，再造句</div><h3>你能不看解說說出用法嗎？</h3><p class="small">每張卡先只顯示詞語或句型，展開後核對意思與使用限制。</p><button id="review-start">開始回想</button></div><p class="small">進度儲存在目前瀏覽器；換裝置前可匯出，匯入會合併收藏與已掌握條目。</p><button id="export">匯出學習進度</button> <label class="small">匯入進度 <input id="import" type="file" accept="application/json,.json"></label><span id="import-status" class="small" role="status"></span></section>
<section id="sources"><div class="section-head"><h2>來源與統計方法</h2><span class="label">更新 __DATE__</span></div><div class="note"><b>本次整合 31 場來源，並非 31 套完整逐題驗證卷。</b><br>2010–2021：沿用 23 份舊版前段檢出與筆記，主要前 3 頁，部分前 5 頁；2020.07 無來源。2022–2025：新增 8 場，整理重點為文字・語彙與文法問題 1–6；下表頁碼以 PDF 頁序計算，可能與頁腳不同。未把閱讀文章、聽解或答案重複計入。舊、新資料辨識範圍不同，不適合直接解讀成年別出題趨勢。<br>重點整理條目按題目語境整理適切用法；文字檢出可能是題幹、選項或干擾選項，不代表正解。未出現在筆記的項目不等於沒考過。來源為民間整理，2024.12 為早期版本、2025.12 含作答註記，沒有宣稱官方認證。網站不重新上傳原題 PDF；僅公開場次與 PDF 頁碼，請在自己的題本對照，不公開私人檔案連結。</div><div class="table-scroll"><table><thead><tr><th>場次</th><th>整理／檢出範圍</th><th>來源狀況</th><th>對照方式</th></tr></thead><tbody>__COVERAGE__</tbody></table></div></section><footer>JLPT N1 / 學習筆記 · 自編解說與例句，原題權利屬各權利人。<br><a href="https://github.com/smartleo123/JLPT-Learning">GitHub 專案 ↗</a> · <a href="data/study.json">結構化學習資料</a> · <a href="METHOD.md">整理方法與限制</a></footer></div><script id="study-data" type="application/json">__DB__</script><script src="app.js" defer></script></body></html>'''
for key,value in {'__V__':str(v),'__G__':str(g),'__STATIC__':static,'__CONCEPTS__':concept_html,'__COVERAGE__':cov,'__DATE__':db['updated'],'__DB__':json.dumps(db,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')}.items():s=s.replace(key,value)
(root/'index.html').write_text(s);print('Built',len(db['items']),'items')
