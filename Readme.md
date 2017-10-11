# CodeCheckerマニュアル

## 対象
このCodeCheckerはC言語(.c, .h)に対応したコードチェックツールです。

## 各Checkerの使い方

### CommentStrChecker.py

#### 使い方
`python CommentStrChecker.py [project dir] ([output csv file path])`
* *[project dir]* : 検査対象のプロジェクトのディレクトリパス。
* [output csv file path] : 検査結果のCSV出力先ファイルのパス。省略した場合はコンソールに出力される。

#### 処理の概要
コメントに禁則文字が含まれていないかチェックするツールです。
チェックする禁則文字を以下に記します。
* `半角カナ`
* `全角英数字`

### VariableChecker.py

#### 使い方
`python VariableChecker.py [project dir] ([output csv file path])`
* *[project dir]* : 検査対象のプロジェクトのディレクトリパス。
* [output csv file path] : 検査結果のCSV出力先ファイルのパス。省略した場合はコンソールに出力される。

#### 処理の概要
変数宣言箇所を抽出し、CSVファイルに出力するツール。
ただし、検索対象の文字列を検索しているだけなので宣言部以外も抽出されます。
検索対象の文字列は以下の通りです。
* `U2`
* `U4`
* `S4`
* `VD`
* `void`
* `VS1`
* `VS2`
* `VS4`
* `VU1`
* `VU2`
* `VU4`
* `BL`
* `F4`

文頭に「#define」、「#ifdef」がついているものは除外しています。

### BasicTypeChecker.py

#### 使い方
`python BasicTypeChecker.py [project dir] ([output csv file path])`
* *[project dir]* : 検査対象のプロジェクトのディレクトリパス。
* [output csv file path] : 検査結果のCSV出力先ファイルのパス。省略した場合はコンソールに出力される。

#### 処理の概要
Ｃ言語の基本型を検索し、結果を出力するツールです。
検索対象の基本型は以下の通りです。
* `char`
* `short`
* `int`
* `long`
* `float`
* `double`
* `BOOL`

### StructChecker.py

#### 使い方
`python StructChecker.py [project dir] ([output csv file path])`
* *[project dir]* : 検査対象のプロジェクトのディレクトリパス。
* [output csv file path] : 検査結果のCSV出力先ファイルのパス。省略した場合はコンソールに出力される。

#### 処理の概要
構造体を検索し、結果を出力するツールです。
ここで使用している"構造体"とは以下のことを指します。
* `struct`
* `union`
* `enum`

### DefineChecker.py

#### 使い方
`python DefineChecker.py [project dir] ([output csv file path])`
* *[project dir]* : 検査対象のプロジェクトのディレクトリパス。
* [output csv file path] : 検査結果のCSV出力先ファイルのパス。省略した場合はコンソールに出力される。

#### 処理の概要
`#define`を使用している行を抽出するツールです。抽出結果はCSVファイルに出力されます。

### ReserviedWordSpaceChecker.py

#### 使い方
`python ReserviedWordSpaceChecker.py [project dir] ([output csv file path])`
* *[project dir]* : 検査対象のプロジェクトのディレクトリパス。
* [output csv file path] : 検査結果のCSV出力先ファイルのパス。省略した場合はコンソールに出力される。

#### 処理の概要
C言語の予約語を確認し、適切なスペースが挿入されているかチェックするツール。
検索でヒットするパターンを以下に記します。
* [予約語]( ： 予約語と"("の間にスペースがない場合
* [予約語]&nbsp;&nbsp;&nbsp;( ： 予約語と"("の間にスペースが二つ以上ある場合
* ){ ： ")"と"{"の間にスペースがない場合
* )&nbsp;&nbsp;&nbsp;{ ： ")"と"{"の間にスペースが二つ以上ある場合

検索対象の予約語を以下に記します。
* `static`
* `const`
* `signed`
* `unsigned`
* `extern`
* `volatile`
* `register`
* `return`
* `goto`
* `if`
* `else`
* `switch`
* `case`
* `default`
* `break`
* `for`
* `while`
* `do`
* `continue`
* `typedef`
* `struct`
* `enum`
* `union`
* `sizeof`

### Preprocessor.py

#### 使い方
`python Preprocessor.py [project dir] ([output csv file path])`
* *[project dir]* : 検査対象のプロジェクトのディレクトリパス。
* [output csv file path] : 検査結果のCSV出力先ファイルのパス。省略した場合はコンソールに出力される。

#### 処理の概要
C言語のプリプロセッサが行先頭で宣言されていない箇所を抽出するツールです。
抽出した結果はCSVに出力されます。

抽出対象のプリプロセッサは以下に記します。
* `#define`
* `#pragma`
* `#ifdef`
* `#endif`
* `#if`
* `#else`
* `#include`
* `#error`
* `#warning`

> 注意：
> 以下のパターンも正規表現にマッチしてしまうため、抽出結果から目視で除外する必要がある。
> #endif /\* #ifdef ※※※ \*/
> ↑"#endif"は行先頭に宣言されているが、コメントの"#ifdef"は行先頭に無いため抽出されてしまう。

### MultiStatementChecker.py

#### 使い方
`python MultiStatementChecker.py [project dir] ([output csv file path])`
* *[project dir]* : 検査対象のプロジェクトのディレクトリパス。
* [output csv file path] : 検査結果のCSV出力先ファイルのパス。省略した場合はコンソールに出力される。

#### 処理の概要
マルチステートメント行を抽出しCSVに出力するツールです。
マルチステートメントの例を以下に記します。
* `int a = 0; char c = 'a';`
* `if (a == 0) break;`
* `while (a == 0) a++;`
* `for (i = 0; i < 10; i++) a++;`

> 注意：
> マルチステートメントは1行に出現する";"の数で検索しています。
> よってfor文の条件式も検索にヒットしてしまうため、抽出後目視で確認してください。
