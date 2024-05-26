import requests as re
from bs4 import BeautifulSoup
import datetime
date = datetime.date.today()
year = str(int(date.strftime("%Y"))-1911)
month = date.strftime("%m")
day = date.strftime("%d")
weekday = datetime.date.today().weekday()
if month == "01" or month == "02" or (month == "03" and int(day) < 25):
    year = str(int(year)-1)
    month = "11"
elif int(month) % 2 == 0:
    month = "0" + str(int(month) - 3)
elif int(month) % 2 != 0 and int(day) > 25:
    month = "0" + str(int(month) -2)
else:
    month = "0" + str(int(month)-4)
url = "https://www.etax.nat.gov.tw/etw-main/ETW183W2_"+year+month
print(url)
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"}
response = re.get(url,headers=headers)
response.encoding = 'utf-8'
root = BeautifulSoup(response.text,'lxml')
td = root.select("#tenMillionsTable tbody tr td div div.col-12.mb-3")
prizeli = [prize.text.strip() for prize in td]
prizetable = {
    "SuperSpecialPrize":prizeli[0],
    "SpecialPrize":prizeli[1],
    "Jackpot1":prizeli[2],
    "Jackpot2":prizeli[3],
    "Jackpot3":prizeli[4]
}
while True:
    lastThrNums = input("請輸入發票後三碼：")
    if len(lastThrNums) != 3:
        raise ValueError("輸入的號碼長度有誤")
    if lastThrNums == prizetable.get("Jackpot1")[5:8]:
        frontfiveNums = input("恭喜你中獎了，請繼續輸入前五碼：")
        if len(frontfiveNums) !=5:
            raise ValueError("輸入的長度有誤")
        if frontfiveNums[0:5] == prizetable.get("Jackpot1")[0:5]:
            print("恭喜你中了頭獎！")
        elif frontfiveNums[1:5] == prizetable.get("Jackpot1")[1:5]:
            print("恭喜你中了二獎！")
        elif frontfiveNums[2:5] == prizetable.get("Jackpot1")[2:5]:
            print("恭喜你中了三獎！")
        elif frontfiveNums[3:5] == prizetable.get("Jackpot1")[3:5]:
            print("恭喜你中了四獎！")
        elif frontfiveNums[4:5] == prizetable.get("Jackpot1")[4:5]:
            print("恭喜你中了五獎！")
    elif lastThrNums == prizetable.get("SuperSpecialPrize")[5:8]:
        frontfiveNums = input("恭喜你可能中了特別獎，請輸入前五碼：")
        if frontfiveNums[0:5] == prizetable.get("SuperSpecialPrize")[0:5]:
            print("你中了特別獎！")
    elif lastThrNums == prizetable.get("SpecialPrize")[5:8]:
        frontfiveNums = input("恭喜你可能中了特獎，請輸入前五碼：")
        if frontfiveNums[0:5] == prizetable.get("SpecialPrize")[0:5]:
            print("你中了特獎！")
    else:
        print("銘謝惠顧，請繼續加油！")