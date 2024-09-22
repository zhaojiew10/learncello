转自https://blog.csdn.net/weixin_42046751/article/details/110520560

中央C在钢琴上是小字一组c1，但也有的说是C3、C4、C5。那么，c1为什么会等于C3、C4、C5 ？先解释一下“中央C”：中央C（Middle C）为西洋音乐术语，代表位于五线谱大谱表（Grand staff）正中间的音值。

第一点，要明白这个问题的前提：首先要搞清楚是用的哪种“标记音高的方法” ，不同的标记方法对同一个音的命名可能不同，比如：

- 中央C在赫尔姆霍茨音调记号法（Helmholtz pitch notation）中，被标记为“小字一组的c (c1)”，
- 但中央C在科学音调记号法（Scientific pitch notation）中，被标记为“C4”。

![img](https://i-blog.csdnimg.cn/blog_migrate/ce08be98767867f1e79fa3cb93425ae4.jpeg)

> 1: MIDI编号（MIDI numbering）
> 2: 八度编号 (Japanese, Yamaha, Encore)
> 3: 八度编号 (scientific, MusicXML, and others)
> 4: 赫尔姆霍茨

科学音高记谱法（scientific pitch notation）的概念，为了标示同名（在同一个音高集合中）但不同高度的音符，科学音调记号法（ scientific pitch notation）用字母及一个用来表示所在八度的阿拉伯数字，明确指出音符的位置。

- 八度 0-9 表示八度区。C-D-E-F-G-A-B 为 C 大调七个主音：do re mi fa so la si（简谱记为 1 到 7）。科学音调记号法（scientific pitch notation）就是将上面这两者合在一起表示一个音，比如 A4 就是中音 la，频率为 440 Hz。C5 则是高音 do（简谱是 1 上面加一个点）。

- 升一个八度也就是把频率翻番。A5 频率 880 Hz，正好是 A4 的两倍。一个八度区有 12 个半音，就是把这两倍的频率间隔等比分为 12，所以两个相邻半音的频率比是 2 开 12 次方，也即大约 1.05946。这种定音高的办法叫做 twelve-tone equal temperament，简称 12-TET。

- 两个半音之间再等比分可以分 100 份，每份叫做一音分（cent）。科学音调记号加上音分一般足够表示准确的音高了。比如 A4 +30 表示比 440 Hz 高 30 音分，可以算出来具体频率是 447.69 Hz。

- A4 又称 “标准音” A440，是国际标准音高。钢琴调音师或者大型乐队乐器之间调音都用这个频率。
  C4 又称 “中央C”（Middle C），是中音八度的开始。有一种音高标定方法是和 C4 比较相隔的半音数，比方 B4 就是 +11，表示比 C4 高 11 个半音。

- MIDI note number p 和频率 f 转换关系：p = 69 + 12 x log2(f/440)。这实际上就是把 C4 定为 MIDI note number 60，然后每升降一个半音就加减一个号码。

- 可以看到 E-F 和 B-C 的间隔是一个半音，而七个主音别的间隔都是两个半音，也叫一个全音。

- 标准钢琴琴键有大有小，大的白色琴键是主音，小的黑色琴键是主音升降一个半音后的辅音（图）。一般钢琴是 88 个琴键，从 A0 到 C8。知道了上面这些，看到钢琴键盘应该就马上能找到 Middle C 了，如下：

  ![img](https://i-blog.csdnimg.cn/blog_migrate/a6724375ddb520551f10bd42543197f0.jpeg)