import lxml.html as lh
import requests
import datetime

#Stockcode (keyID) list read from google drive
from google_drive_downloader import GoogleDriveDownloader as gdd

gdd.download_file_from_google_drive(file_id='1A5R2WdXp5pETRRK_xPOoFOetSyE27IWE',
                                    dest_path='./Parameter.txt')

now = datetime.datetime.now()

#Crawl information from webpage and write it into text file
class AppCrawler:
    def __init__(self, starting_url, depth):
        self.starting_url = starting_url
        self.depth = depth
        self.apps = []

    def crawl(self):
        self.get_app_from_link(self.starting_url)
        return

    def get_app_from_link(self, link):
        start_page = requests.get(link)
        tree = lh.fromstring(start_page.text)
        try:
            name = tree.xpath('//h1[@class="stock-profile f16"]/text()')[0]
            code = tree.xpath('//li[@class="f14"]/text()')[1]
            Open = tree.xpath('//td[@id="slcontent_0_ileft_0_opentext"]/text()')[0]
            High = tree.xpath('//td[@id="slcontent_0_ileft_0_hightext"]/text()')[0]
            Low = tree.xpath('//td[@id="slcontent_0_ileft_0_lowtext"]/text()')[0]
            Last = tree.xpath('//td[@id="slcontent_0_ileft_0_lastdonetext"]/text()')[0]
            ChgPer = tree.xpath('//td[@id="slcontent_0_ileft_0_chgpercenttrext"]/text()')[0]
            Vol = tree.xpath('//td[@id="slcontent_0_ileft_0_voltext"]/text()')[0]
            BuyVol = tree.xpath('//td[@id="slcontent_0_ileft_0_buyvol"]/text()')[0]
            SellVol = tree.xpath('//td[@id="slcontent_0_ileft_0_sellvol"]/text()')[0]
            Time = tree.xpath('//span[@id="slcontent_0_ileft_0_timetxt"]/text()')[0]
        except IndexError:
            return
        with open(filename, 'a') as file_object:
            file_object.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s/%s/%s\t%s\t%s\n'
                              % (name, code[3:], Open, High, Low, Last, ChgPer, Vol, BuyVol[:BuyVol.find("/")-1], 
                                 BuyVol[BuyVol.find("/")+2:], SellVol[:SellVol.find("/")-1], SellVol[SellVol.find("/")+2:], 
                                 now.month, now.day, now.year , Time, now.strftime('%A')))   
        return    
    
class App:
    def __init__(self, name, code, Open, High, Low,	Last, ChgPer, Vol, BuyVol, SellVol, Time, links):
        self.name = name
        self.code = code
        self.Open = Open
        self.High = High
        self.Low = Low
        self.Last = Last
        self.ChgPer = ChgPer
        self.Vol = Vol
        self.BuyVol = BuyVol
        self.SellVol = SellVol
        self.Time = Time
        self.links = links

    def ____(self):
        return ("Name: " + self.name.encode('UTF-8') +
        "\r\nCode: " + self.developer.encode('UTF-8') +
        "\r\nOpen: " + self.Open.encode('UTF-8')  +
        "\r\nHigh: " + self.High.encode('UTF-8')  +
        "\r\nLow: " + self.Low.encode('UTF-8') +
        "\r\nLast: " + self.Last.encode('UTF-8') +
        "\r\nChgPer: " + self.ChgPer.encode('UTF-8') +
        "\r\nVol: " + self.Vol.encode('UTF-8') +
        "\r\nBuyVol: " + self.BuyVol.encode('UTF-8') +
        "\r\nSellVol: " + self.SellVol.encode('UTF-8') + 
        "\r\nTime: " + self.Time.encode('UTF-8') + "\r\n")
        
#Define the url        
stock_url = "https://www.thestar.com.my/business/marketwatch/"

#create a new text file and append all the information in this file               
full_list = []
with open(r'./Parameter.txt') as f:
    for line in f:
        full_list.append(line.replace("\r","").replace("\n",""))

filename = "Market Watch %s-%s-%s.txt" % (now.day, now.month, now.year)

with open(filename, 'w') as file_object:
    file_object.write("Company\tStock_Code\tOpen\tHigh\tLow\tLast\tChg_Perc\tVol_in'00\tBuy\tBuy_Vol_in'00\tSell\tSell_Vol_in'00\tDate\tTime\tDay\n")

for list in full_list:
    crawler = AppCrawler("https://www.thestar.com.my/business/marketwatch/stocks/?qcounter=%s" % (list), 0)
    crawler.crawl()
    for app in crawler.apps:
        print(app)