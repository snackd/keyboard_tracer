# keyboard_tracer

1. What? (做什麼?)
> 目標:製作追蹤按下鍵盤哪個按鍵，
2. Why? (為什麼做)
> 想要有個追蹤按下鍵盤哪些鍵的程式
3. How? (如何運行)
> 使用 pynput 套件，導入 keyboard 類別

[keyboard Reference](https://pynput.readthedocs.io/en/latest/keyboard.html)

## 開發原因

由於自己在玩遊戲 ([Tetris](https://tetr.io/)) 時，想要變得更強，精益求精。

但無奈個人手速上有限制([個人速度紀錄](https://youtu.be/DbAZ0Zf3wJs))，總是被打敗，也在網路上看到機器人很強大 ([Tertis ZZZ_TEST](https://www.youtube.com/watch?v=IuOJPCAZPM0&ab_channel=ICLY))，故有個大膽的想法，想寫出可以像此機器人一樣的程式，來訓練自己或擊敗對手。

當初看到這機器人最直觀的想法，腦中想著這是怎麼做到的呢? 
> 深度學習 (DL) 或是 某些演算法?

有了這些想法後，我就先打造一個最基本的，至少可以讀到我鍵盤按了那些按鍵、快速幫我建立開場、快速地放方塊，儘管初期效率不高，但也遠比人的速度更快。

打算分為三階段開發，先以輔佐自己的輔助程式為先而設計的理念開發此程式。

- [X] 1. 按鍵追蹤程式
- [ ] 2. 開場紀錄、迅速建置開場程式
- [ ] 3. 可自動自發與人對戰的機器人

## 運行結果
![程式運行結果](https://i.imgur.com/gzbPeDo.png)
