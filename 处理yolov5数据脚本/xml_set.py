# #对比xml文件是否有漏框
# import os
# from xml.dom.minidom import parse
#
# def readXML():
#     for i in os.listdir("Annotations"):
#         domTree = parse("Annotations/"+i)
#         # 文档根元素
#         rootNode = domTree.documentElement
#         # print(rootNode.nodeName)
#         customers = rootNode.getElementsByTagName("name")
#         a = 0
#         for customer in customers:
#             a += 1
#         if a == 20 or a == 16:
#             pass
#         else:
#             print(i)
#
# if __name__ == '__main__':
#     readXML()

#修改xml节点名称
import os
from xml.dom.minidom import parse

def readXML():
    for i in os.listdir("Annotations"):
        domTree = parse("Annotations/"+i)
        s = "Annotations/"+i
        # 文档根元素
        rootNode = domTree.documentElement
        # print(rootNode.nodeName)
        customers = rootNode.getElementsByTagName("name")
        for i in range(len(customers)):
            if str(customers[i].firstChild.data) == "FengBan":
                print(customers[i].firstChild.data)
                customers[i].firstChild.data = "HaoZao"

        with open(s, 'w') as fh:
            rootNode.writexml(fh)
if __name__ == '__main__':
    readXML()