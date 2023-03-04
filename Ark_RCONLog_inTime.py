import os
import glob
import datetime

def Timecount(join, left):
    djoin = datetime.datetime.strptime(join, '%H:%M:%S')
    dleft = datetime.datetime.strptime(left, '%H:%M:%S')
    dtime = dleft - djoin
    return dtime

# Log格納用フォルダがなければ生成する
if os.path.isdir('./logFile') == False:
    os.mkdir('./logFile')

# logFileに入ってるファイル名の取得、リスト化
path_List = glob.glob('./logFile/*')
Namelist = []
Player = []
joinTimeList = []
TimeList = []
incheck = []

j = 0

for i in path_List:
    file = os.path.basename(i)
    Namelist.append(i)

i = 0
for Name in Namelist:
    with open(Name, encoding="utf-8") as f:
        for line in f:

            # 参加時間取得
            if 'joined' in line:
                join = line[0:8]

                # 参加者取得
                start = line.index("] ") + 2
                end = line.index(" joined")
                PName = line[start:end]

                # リストにプレイヤーが格納されているか
                if PName in Player:
                    PlayerNum = Player.index(PName)
                    joinTimeList[PlayerNum] = join
                    incheck[PlayerNum] = 1
                # 格納されていれば格納して続行
                else:
                    Player.append(PName)
                    TimeList.append(datetime.timedelta(seconds=0))
                    joinTimeList.append(join)
                    incheck.append('1')

            # 退出時間取得
            if 'left' in line:
                left = line[0:8]

            # 退出者取得
                start = line.index("] ") + 2
                end = line.index(" left")
                PName = line[start:end]

                PlayerNum = Player.index(PName)
                TimeList[PlayerNum] += Timecount(joinTimeList[PlayerNum], left)
                incheck[PlayerNum] = 0

        # 日付をまたいだ場合の処理
        PlayerNum = 0
        for check in incheck:
            if incheck[PlayerNum] == 0:
                PlayerNum += 1
            # またいだ場合は24:00:00に退出し、00:00:00に入出した扱い
            else:
                left = '23:59:59'
                TimeList[PlayerNum] += Timecount(join, left)
                joinTimeList[PlayerNum] = '00:00:00'
                incheck[PlayerNum] = 1
                PlayerNum += 1

# Output
i = 0
for Players in Player:
    totaltime = TimeList[i]

    print(f'{Player[i]} : {totaltime}')
    i += 1

os.system('PAUSE')
