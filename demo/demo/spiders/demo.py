#coding:gbk
import scrapy
class demo(scrapy.Spider):
    name = 'gaoshiqing'
    start_urls = ["http://data.nowgoal.com/OddsCompBasket/284834.html"]
    def parse(self, response):
        class_list1 = response.xpath(".//*[@id='card1']/b/text()").extract()    #获取盘口赔率
        class_list2 = response.xpath(".//*[@id='card2']/b/text()").extract()    #获取升降赔率
        company_list1 = response.xpath(".//tr[@class='Leaguestitle']/td[@width='17%']/text()").extract()    #获取各个公司名称
        updatetime = response.xpath(".//tr[@class='Leaguestitle']/td[@width='15%']/text()").extract()       #获取updatetime
        uptatetime_values = response.xpath(".//tr[@bgcolor='#ffffff']/td[6]/text()").extract()      #获取更新时间值
        print '爬取中...'
        #print class_list1[0],class_list2[0]
        # for t in uptatetime_values:    # 遍历更新时间
        #     print t
        data_list_Sbobet = response.xpath(".//tr[@bgcolor='#ffffff']/td[1]/font/text()").extract()  # 获取font数据
        data_list2_Sbobet = response.xpath(".//tr[@bgcolor='#ffffff']/td[1]/span/text()").extract()  # 获取span数据
        data_list3_Sbobet = response.xpath(".//tr[@bgcolor='#ffffff']/td[1]/text()").extract()  # 获取td数据
        M = []
        for i in data_list3_Sbobet:
            if i.strip() != '':
                M.append(i.strip())
        print company_list1[0]  # 打印Sbobet公司名称
        m = 0
        for j in range(len(data_list_Sbobet)):   #遍历公司数据
            if j == 0:
                print class_list1[0]
            if j == 20:
                print class_list2[0]
            print data_list_Sbobet[j].center(8)
            print data_list2_Sbobet[j],M[m]
            m = m + 1

        data_list_Easybet = response.xpath(".//tr[@bgcolor='#ffffff']/td[2]/font/text()").extract()  # 获取font数据
        data_list2_Easybet = response.xpath(".//tr[@bgcolor='#ffffff']/td[2]/span/text()").extract()  # 获取span数据
        data_list3_Easybet = response.xpath(".//tr[@bgcolor='#ffffff']/td[2]/text()").extract()  # 获取td数据

        M1 = []
        for i in data_list3_Easybet:
            if i.strip() != '':
                M1.append(i.strip())
        print company_list1[1]  # 打印公司名称
        m1=0
        for j in range(len(data_list_Easybet)):  # 遍历公司数据
            if j == 0:
                print class_list1[0]
            if j == 8:
                print class_list2[0]
            print data_list_Easybet[j].center(8)
            print data_list2_Easybet[j],M1[m1]
            m1 = m1+1

        data_list_Crown = response.xpath(".//tr[@bgcolor='#ffffff']/td[3]/font/text()").extract()  # 获取font数据
        data_list2_Crown = response.xpath(".//tr[@bgcolor='#ffffff']/td[3]/span/text()").extract()  # 获取span数据
        data_list3_Crown = response.xpath(".//tr[@bgcolor='#ffffff']/td[3]/text()").extract()  # 获取td数据
        M2 = []
        for i in data_list3_Crown:
            if i.strip() != '':
                M2.append(i.strip())
        print company_list1[2]  # 打印公司名称
        m2 = 0
        for j in range(len(data_list_Crown)):  # 遍历公司数据
            if j == 0:
                print class_list1[0]
            if j == 18:
                print class_list2[0]
            print data_list_Crown[j].center(8)
            print data_list2_Crown[j],M2[m2]
            m2 = m2 + 1

        data_list_Bet365 = response.xpath(".//tr[@bgcolor='#ffffff']/td[4]/font/text()").extract()  # 获取font数据
        data_list2_Bet365 = response.xpath(".//tr[@bgcolor='#ffffff']/td[4]/span/text()").extract()  # 获取span数据
        data_list3_Bet365 = response.xpath(".//tr[@bgcolor='#ffffff']/td[4]/text()").extract()  # 获取td数据
        M3 = []
        for i in data_list3_Bet365:
            if i.strip() != '':
                M3.append(i.strip())
        print company_list1[3]  # 打印公司名称
        m3 = 0
        for j in range(len(data_list_Bet365)):  # 遍历公司数据
            if j == 0:
                print class_list1[0]
            if j == 11:
                print class_list2[0]
            print data_list_Bet365[j].center(8)
            print data_list2_Bet365[j],M3[m3]
            m3 = m3 + 1

        data_list_Vcbet = response.xpath(".//tr[@bgcolor='#ffffff']/td[5]/font/text()").extract()  # 获取font数据
        data_list2_Vcbet = response.xpath(".//tr[@bgcolor='#ffffff']/td[5]/span/text()").extract()  # 获取span数据
        data_list3_Vcbet = response.xpath(".//tr[@bgcolor='#ffffff']/td[5]/text()").extract()  # 获取td数据
        M4 = []
        for i in data_list3_Vcbet:
            if i.strip() != '':
                M4.append(i.strip())
        print company_list1[4]  # 打印公司名称
        m4 = 0
        for j in range(len(data_list_Vcbet)):  # 遍历公司数据
            if j == 0:
                print class_list1[0]
            if j == 4:
                print class_list2[0]
            print data_list_Vcbet[j].center(8)
            print data_list2_Vcbet[j],M4[m4]
            m4 = m4 + 1

