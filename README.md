# ArkLogTime
Arkのプレイ時間をRCONログファイルから算出するプログラムです。
プライベート用に制作しましたが、どの環境でも動作すると思います。

ログの入退出を判定して計算しているので、RCONを途中で閉じたりしていると計算が正しくなくなるので注意してください。

気が向いたらきれいにかきなおします

This program calculates Ark's login time from RCON log files.
I created this for private use, but I believe it will work in any environment.

Note that the calculations are based on judging log entry and exit, so if you close RCON in the middle of a log, the calculations will not be correct.

# 使い方(Use)
1. ファイルを展開してから`logFile`フォルダに計算したい期間のlogファイルを全てコピーしてください。  
  (フォルダがない場合はArk_RCONLog_inTime.pyを実行すると生成されます)  
  
    Extract the files and then copy all log files for the period you want to calculate to `logFile`.  
  (If it is not there, it is generated by executing ArkLogTime.py)  

2. `Ark_RCONLog_inTime.py`を実行すると、計算結果が表示されます。   

   Running `Ark_RCONLog_inTime.py` will display the results of the calculation.

![image](File/run.png)

# 注意(attention)
Steam名を変更して入室すると、入出時は以前の名前でログに記録され退出時新しい名前で退出されるのでエラーを出します。
解決法としてログファイルを直接書き換えると正常に計算できるようになります。

ArkApiでUnicodeRconを利用した環境を想定して開発したので、文字化けした状態での動作は保証しません。

早く寝たいっていう気持ち95％で構成されてます。

この作成物および同梱物を使用したことによって生じたすべての障害・損害・不具合等に関しては一切の責任を負いません。各自の責任においてご使用ください。

If you change your steam name and enter a room, you will get an error because when you enter the room, you will be logged under your old name and when you leave, you will leave under your new name.
The solution is to rewrite the log file directly so that it can be calculated correctly.

Since we developed this application assuming an environment using UnicodeRcon with ArkApi, we do not guarantee that it will work with garbled characters.

We assume no responsibility whatsoever for any damage, loss, or malfunction resulting from the use of this work or any of its contents. Use at your own risk.


# 動作環境(operating environment)
ASM v1.1.439.1   
Ark v357.3   
UnicodeRcon v1.2   

# 変更履歴(ChangeLog)  

1.0.2 - 細部のコードの間違いを修正 、整理  
1.0.1 - コードが適当すぎたのを整理  
1.0 - 初版
