#!/usr/bin/env python3
"""JavaScript DOM 基礎の Anki デッキを生成するスクリプト。

使い方:
    pip install genanki
    python3 build_deck.py

同じ Front から GUID を生成しているため、再生成して再インポートしても
重複せず既存カードが更新される。
"""

from pathlib import Path

import genanki

DECK_NAME = "The Odin Project::JavaScript"
MODEL_ID = 1743000001
DECK_ID = 1743000002
OUTPUT = Path(__file__).with_name("javascript-basics.apkg")

model = genanki.Model(
    MODEL_ID,
    "Basic (TIL)",
    fields=[
        {"name": "Front"},
        {"name": "Back"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Front}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{Back}}',
        }
    ],
    css="""
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
    "Hiragino Kaku Gothic ProN", "Noto Sans JP", sans-serif;
  font-size: 18px;
  line-height: 1.6;
  text-align: left;
  color: #222;
  background: #fff;
  padding: 12px;
}
.card.nightMode {
  color: #eee;
  background: #2b2b2b;
}
code, pre {
  font-family: "SFMono-Regular", Menlo, Consolas, monospace;
  font-size: 0.9em;
  background: #f2f2f2;
  border-radius: 4px;
}
code { padding: 1px 4px; }
pre { padding: 10px; overflow-x: auto; }
pre code { padding: 0; }
.nightMode code, .nightMode pre { background: #3a3a3a; }
hr#answer {
  border: none;
  border-top: 2px solid #ddd;
  margin: 16px 0;
}
.nightMode hr#answer { border-top-color: #555; }
""",
)

# (Front, Back, Tags)
CARDS = [
    (
        "<code>const</code> と <code>let</code> の違いは？",
        "<code>const</code> は再代入不可、<code>let</code> は再代入可能。"
        "<br>再代入しない値は <code>const</code> を使う。"
        "<br><br>※ <code>const</code> は宣言時の初期化が必須"
        "（<code>const x;</code> はエラー）。",
        "javascript dom the-odin-project",
    ),
    (
        "<code>const</code> で宣言したオブジェクトの中身は変更できる？",
        "はい。<code>const</code> は変数への再代入を禁止するだけで、"
        "オブジェクトや配列の中身は変更できる。"
        '<pre><code>const user = { name: "Shota" };\n'
        'user.name = "Taro"; // OK\n'
        "user = {};          // TypeError</code></pre>",
        "javascript const the-odin-project",
    ),
    (
        "<code>textContent</code> と <code>innerText</code> の"
        "「読み取り」の違いは？",
        "<b>textContent</b>：DOM標準。CSSの影響を受けず、"
        "非表示要素のテキストも含む。レイアウト計算が不要で高速。"
        "<br><b>innerText</b>：画面に表示されているテキストのみを返す。"
        "CSSを反映するためリフローが走り低速。",
        "javascript dom textcontent innertext",
    ),
    (
        "<code>display: none</code> の要素内テキストを取得できるのはどちら？",
        "<code>textContent</code>。<code>innerText</code> は"
        "表示されているテキストのみを返すため、非表示要素のテキストは含まれない。",
        "javascript dom textcontent innertext",
    ),
    (
        "プレーンテキストを要素に書き込むとき推奨されるのは "
        "<code>textContent</code> / <code>innerText</code> のどちら？ 理由は？",
        "<code>textContent</code>。DOM標準で高速、再レイアウトが不要で"
        "挙動が予測しやすい。単純なテキスト書き込みなら "
        "<code>innerText</code> と見た目の結果はほぼ同じ。",
        "javascript dom textcontent innertext",
    ),
    (
        "<code>textContent</code> と <code>innerHTML</code> の違いは？",
        "<code>textContent</code> は文字列をテキストとして扱い、"
        "HTMLタグを解釈しない。<code>innerHTML</code> はHTMLとして解釈する。"
        "ユーザー入力を <code>innerHTML</code> に入れるとXSSの危険がある。",
        "javascript dom textcontent innerhtml security",
    ),
    (
        "<code>element.textContent</code> に "
        "<code>&lt;b&gt;太字&lt;/b&gt;</code> を代入するとどう表示される？",
        "タグは解釈されず、文字列 "
        "<code>&lt;b&gt;太字&lt;/b&gt;</code> がそのまま表示される。",
        "javascript dom textcontent",
    ),
    (
        '<code>document.getElementById("x")</code> が '
        "<code>null</code> を返すのはどんなとき？",
        "指定IDの要素がその時点でDOMに存在しないとき。"
        "スクリプトの実行タイミング（配置や <code>defer</code>）を確認する。",
        "javascript dom getelementbyid",
    ),
    (
        "DOM構築後にスクリプトを実行させる2つの方法は？",
        '① <code>&lt;script src="..." defer&gt;&lt;/script&gt;</code> を付ける'
        "<br>② <code>&lt;/body&gt;</code> の直前に <code>script</code> を置く",
        "javascript dom defer",
    ),
    (
        "テンプレートリテラルの構文は？ "
        '<code>greeting + " " + name</code> を書き換えると？',
        "バッククォートで囲み <code>${式}</code> を埋め込む。"
        "<pre><code>const message = `${greeting} ${name}`;</code></pre>",
        "javascript template-literals",
    ),
    (
        "ブラウザで変数名 <code>name</code> を使うと注意が必要な理由は？",
        "<code>name</code> は <code>window.name</code> という"
        "グローバルプロパティと名前が衝突する。"
        "<code>userName</code> などにすると安全で読みやすい。",
        "javascript browser",
    ),
]


def main() -> None:
    deck = genanki.Deck(DECK_ID, DECK_NAME)
    for front, back, tags in CARDS:
        deck.add_note(
            genanki.Note(
                model=model,
                fields=[front, back],
                tags=tags.split(),
                guid=genanki.guid_for(front),
            )
        )
    genanki.Package(deck).write_to_file(OUTPUT)
    print(f"wrote {OUTPUT} ({len(CARDS)} cards)")


if __name__ == "__main__":
    main()
