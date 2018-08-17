"""
本案例用来测试scrapy框架
参考文献:https://zhuanlan.zhihu.com/p/26854842
"""

from scrapy.selector import Selector

body_xml = """
<html>
    <body>
        <class>
            <name>王尼玛</name>
            <sex>男</sex>
            <age>80</age>
            <favouite>开车</favouite>
        </class>
        <class>
            <name>陈一发</name>
            <sex>母</sex>
            <age>28</age>
            <favouite>开che</favouite>
        </class>
        <class>
            <name>狗贼叔叔</name>
            <sex>公</sex>
            <age>18</age>
            <favouite>土豪战</favouite>
        </class>
    </body>
</html>
"""


def scrapy_test():
    body = body_xml
    print(body)
    print(Selector(text=body).xpath('/html/body/class[1]').extract())

scrapy_test()