#coding:gbk
import scrapy
class demo(scrapy.Spider):
    name = 'gaoshiqing'
    start_urls = ["http://data.nowgoal.com/OddsCompBasket/284834.html"]
    def parse(self, response):
        class_list1 = response.xpath(".//*[@id='card1']/b/text()").extract()    #��ȡ�̿�����
        class_list2 = response.xpath(".//*[@id='card2']/b/text()").extract()    #��ȡ��������
        company_list1 = response.xpath(".//tr[@class='Leaguestitle']/td[@width='17%']/text()").extract()    #��ȡ������˾����
        updatetime = response.xpath(".//tr[@class='Leaguestitle']/td[@width='15%']/text()").extract()       #��ȡupdatetime
        uptatetime_values = response.xpath(".//tr[@bgcolor='#ffffff']/td[6]/text()").extract()      #��ȡ����ʱ��ֵ
        print '��ȡ��...'
        #print class_list1[0],class_list2[0]
        # for t in uptatetime_values:    # ��������ʱ��
        #     print t
        data_list_Sbobet = response.xpath(".//tr[@bgcolor='#ffffff']/td[1]/font/text()").extract()  # ��ȡfont����
        data_list2_Sbobet = response.xpath(".//tr[@bgcolor='#ffffff']/td[1]/span/text()").extract()  # ��ȡspan����
        data_list3_Sbobet = response.xpath(".//tr[@bgcolor='#ffffff']/td[1]/text()").extract()  # ��ȡtd����
        M = []
        for i in data_list3_Sbobet:
            if i.strip() != '':
                M.append(i.strip())
        print company_list1[0]  # ��ӡSbobet��˾����
        m = 0
        for j in range(len(data_list_Sbobet)):   #������˾����
            if j == 0:
                print class_list1[0]
            if j == 20:
                print class_list2[0]
            print data_list_Sbobet[j].center(8)
            print data_list2_Sbobet[j],M[m]
            m = m + 1

        data_list_Easybet = response.xpath(".//tr[@bgcolor='#ffffff']/td[2]/font/text()").extract()  # ��ȡfont����
        data_list2_Easybet = response.xpath(".//tr[@bgcolor='#ffffff']/td[2]/span/text()").extract()  # ��ȡspan����
        data_list3_Easybet = response.xpath(".//tr[@bgcolor='#ffffff']/td[2]/text()").extract()  # ��ȡtd����

        M1 = []
        for i in data_list3_Easybet:
            if i.strip() != '':
                M1.append(i.strip())
        print company_list1[1]  # ��ӡ��˾����
        m1=0
        for j in range(len(data_list_Easybet)):  # ������˾����
            if j == 0:
                print class_list1[0]
            if j == 8:
                print class_list2[0]
            print data_list_Easybet[j].center(8)
            print data_list2_Easybet[j],M1[m1]
            m1 = m1+1

        data_list_Crown = response.xpath(".//tr[@bgcolor='#ffffff']/td[3]/font/text()").extract()  # ��ȡfont����
        data_list2_Crown = response.xpath(".//tr[@bgcolor='#ffffff']/td[3]/span/text()").extract()  # ��ȡspan����
        data_list3_Crown = response.xpath(".//tr[@bgcolor='#ffffff']/td[3]/text()").extract()  # ��ȡtd����
        M2 = []
        for i in data_list3_Crown:
            if i.strip() != '':
                M2.append(i.strip())
        print company_list1[2]  # ��ӡ��˾����
        m2 = 0
        for j in range(len(data_list_Crown)):  # ������˾����
            if j == 0:
                print class_list1[0]
            if j == 18:
                print class_list2[0]
            print data_list_Crown[j].center(8)
            print data_list2_Crown[j],M2[m2]
            m2 = m2 + 1

        data_list_Bet365 = response.xpath(".//tr[@bgcolor='#ffffff']/td[4]/font/text()").extract()  # ��ȡfont����
        data_list2_Bet365 = response.xpath(".//tr[@bgcolor='#ffffff']/td[4]/span/text()").extract()  # ��ȡspan����
        data_list3_Bet365 = response.xpath(".//tr[@bgcolor='#ffffff']/td[4]/text()").extract()  # ��ȡtd����
        M3 = []
        for i in data_list3_Bet365:
            if i.strip() != '':
                M3.append(i.strip())
        print company_list1[3]  # ��ӡ��˾����
        m3 = 0
        for j in range(len(data_list_Bet365)):  # ������˾����
            if j == 0:
                print class_list1[0]
            if j == 11:
                print class_list2[0]
            print data_list_Bet365[j].center(8)
            print data_list2_Bet365[j],M3[m3]
            m3 = m3 + 1

        data_list_Vcbet = response.xpath(".//tr[@bgcolor='#ffffff']/td[5]/font/text()").extract()  # ��ȡfont����
        data_list2_Vcbet = response.xpath(".//tr[@bgcolor='#ffffff']/td[5]/span/text()").extract()  # ��ȡspan����
        data_list3_Vcbet = response.xpath(".//tr[@bgcolor='#ffffff']/td[5]/text()").extract()  # ��ȡtd����
        M4 = []
        for i in data_list3_Vcbet:
            if i.strip() != '':
                M4.append(i.strip())
        print company_list1[4]  # ��ӡ��˾����
        m4 = 0
        for j in range(len(data_list_Vcbet)):  # ������˾����
            if j == 0:
                print class_list1[0]
            if j == 4:
                print class_list2[0]
            print data_list_Vcbet[j].center(8)
            print data_list2_Vcbet[j],M4[m4]
            m4 = m4 + 1

