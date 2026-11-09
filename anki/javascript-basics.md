# JavaScript DOM 基礎 Anki デッキ

`javascript-basics.apkg` を Anki で「ファイル → インポート」すると、
デッキ「The Odin Project::JavaScript」に 11 枚のカードが追加されます。

再生成する場合:

```bash
pip install genanki
python3 build_deck.py
```

## カード一覧

1. **`const` と `let` の違いは？**
   - `const` は再代入不可、`let` は再代入可能。再代入しない値は `const` を使う。
   - `const` は宣言時の初期化が必須（`const x;` はエラー）。

2. **`const` で宣言したオブジェクトの中身は変更できる？**
   - はい。`const` は変数への再代入を禁止するだけで、オブジェクトや配列の中身は変更できる。

3. **`textContent` と `innerText` の「読み取り」の違いは？**
   - `textContent`：DOM標準。CSSの影響を受けず、非表示要素のテキストも含む。高速。
   - `innerText`：画面に表示されているテキストのみ。CSSを反映するためリフローが走り低速。

4. **`display: none` の要素内テキストを取得できるのはどちら？**
   - `textContent`。`innerText` は表示中のテキストのみのため含まれない。

5. **プレーンテキストを書き込むとき推奨されるのはどちら？ 理由は？**
   - `textContent`。DOM標準で高速、再レイアウト不要で予測しやすい。

6. **`textContent` と `innerHTML` の違いは？**
   - `textContent` はHTMLタグを解釈しない。`innerHTML` は解釈する。ユーザー入力ではXSSに注意。

7. **`element.textContent` に `<b>太字</b>` を代入すると？**
   - タグは解釈されず、文字列 `<b>太字</b>` がそのまま表示される。

8. **`document.getElementById("x")` が `null` を返すのは？**
   - 指定IDの要素がその時点でDOMに存在しないとき。実行タイミングを確認する。

9. **DOM構築後にスクリプトを実行させる2つの方法は？**
   - `<script src="..." defer></script>` を付ける。
   - `</body>` の直前に `script` を置く。

10. **テンプレートリテラルの構文は？ `greeting + " " + name` を書き換えると？**
    - バッククォートで囲み `${式}` を埋め込む。`` `${greeting} ${name}` ``

11. **ブラウザで変数名 `name` を使うと注意が必要な理由は？**
    - `name` は `window.name` と名前が衝突する。`userName` などが安全。
