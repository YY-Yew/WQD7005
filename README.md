# WQD7005
This is to compile all the coding and dataset from data crawling to data interpreting. <br/>
https://drive.google.com/open?id=1rQKgs_aVW5TE5Ofkobs5Y894NbcVgRjA<br/>

(1) Data Crawler<br/>

stock_crawl_F.py<br/>
This python code is link to a stockcode list named "Parameter.txt" and crawl the data from https://www.thestar.com.my/business/marketwatch/. <br/>
However no additional steps should be conducted because the py file has inserted a google drive link and it will download the required file automatically.<br/>

TweetCrawler.py<br/>
This python code can be used to crawl information from tweeter. However it has narrow down the scope to United Airlines.<br/>

PDFCrawler.py<br/>
This python code is to auto-download Annual Report in PDF format.<br/>

RSSCrawlwer.py<br/>
This python code is to crawl next trade feed from RSS.<br/>

(2) Covariance Analysis<br/>

Before execute the covariance analysis, data preprocessing is necessarily. Please download all the text files together with below py file and place in same working directory.<br/>

Covariance Analysis.py<br/>

(3) Data Compilation<br/>

File_Merger.py<br/>
Put all the data from different data source into one file, then the clean and complete dataset can be used for data visualization and modelling.<br/>

Example for the output<br/>
"Market_Stock_Data.txt"

