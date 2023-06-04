# ImayoColor
This is short code to discribe new definition of imayo (color name). 
Imayo is a Japanese color name. 
That name means color of "trend". 
This means actual color of imayo shold be changed by passing time. 

For some reason, it's not. 
Imayo is considered as one of the traditional color of Japan and its color code is #D0576B (cite: [HTMLカラーコード](https://www.colordic.org/colorsample/2017)). 

This code re-define Imayo as a UNIX time based color. 
Now, we can use proper defined imayo. 



# 日本語による説明
今様色、と言う色がある。
この色は字義的には「今、流行している色」の意味で相違ないと考えられる。

つまり、本来的には色の定義は時間の経過によって変遷するべきと考えられる。
しかし、この色は日本の伝統色のひとつとして捉えられており、[HTMLカラーコード](https://www.colordic.org/colorsample/2017)によれば#D0576Bでコードされる色である。

つまり、時間の経過によって変遷するべきにも関わらず、上記の「今様」とは10世紀頃で固定されてしまっている状態である。
この状態は実態が定義から乖離しており、不健全である。

従って、新たに今様色を定義し直すことによって定義と実態を一致させる。
この色はUnixTimeの上位桁をカラーコードと見なすことで定義される。

（一見、流行の色ではないため定義からはずれるように見えるが、字義的に考えて「今」の「様」（様式）の意味であるから、その意味でしばらくの間は定義に合うし、「今」の「様」（ありさま）と捉えれば定義に適う。）

具体的定義はコードを見よ。

## 元の定義の曖昧さ
今様色の定義は人や文献によって元々異なる。

## コードの不具合
このコードは明らかにいくつかの不都合を含んでいる。
コードは任意で修正可能であるが、筆者は積極的な修正を予定していない。
概念が重要であり、コードそのものは重要でないからである。


## 定義の可塑性
今流行している色を確実・効率的な方法で取得する方法があれば、それを利用した定義が上記の定義を書き換える。
