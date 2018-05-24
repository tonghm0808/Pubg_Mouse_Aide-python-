#简介：
用python2.7写的一款纯软件压枪辅助工具，也用Tkinter简单做了个小界面
原理也很简单，用pyHook来监听鼠标键盘，然后用的user32.dll里面的
SendInput()函数控制鼠标，鼠标主要的修正算法也都比较简陋。参考aid.py
里面的Mouse_fix()函数。其中利用random.randint(9, 11) / 100.0来生成
随机偏移的定时时间。

#使用方法：
1. 小键盘"+" "-"号控制偏移量
2. 小键盘"Enter"控制开启关闭
3. 先打开游戏，然后用管理员模式运行

#编译所需额外ODLUE:
1. pythoncom
2. pyHook
3. pyinstaller