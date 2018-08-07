from aip import AipOcr
import configparser  # 获取配置文件

#  文字识别
class ShowService(object):

    def __init__(self):
        # 读取工单配置信息--登录百度云》产品》人工智能》文字识别》立即使用
        target=configparser.ConfigParser()
        target.read('PWconfig.ini',encoding='utf-8')
        AppID=target.get('MyPW','AppID')
        APIKey=target.get('MyPW','APIKey')
        SecretKey=target.get('MyPW','SecretKey')

        # 类内均可调用
        self.client=AipOcr(AppID,APIKey,SecretKey)

    # 读取图片
    @staticmethod  #静态方法
    def getPicture(filepath):
        with open(filepath,'rb') as file:
            return file.read()

    # 识别图片
    def showPicText(self,filepath):
        # 读取图片
        image=self.getPicture(filepath)

        # 识别图片
        text=self.client.basicGeneral(image)
        #print(text)
        content=''
        for item in text['words_result']:
            #print(item['words'])
            content = content+''.join(item['words'])
        return content


# 测试
if __name__=='__main__':
    model = ShowService()
    model.showPicText('cutImg.png')

