import sys
import os
from jinja2 import Template

from utils.allure_utils import allure_init
from utils.analyse_case import analyse_case
from utils.asserts import http_assert, jdbc_assert
from utils.extractor import json_extractor, jdbc_extractor
from utils.send_request import send_http_request

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import jsonpath
# import pymysql
import pytest
# import requests
from utils.excel_utils import read_excel



class TestRunner:


    # TODO:读取测试用例文件中的全部数据，用属性保存
    data = read_excel()

    # TODO:提取后的数据要初始化成一个全局的属性，可以用{}空字典存
    all = {}

    @pytest.mark.parametrize("case", data)
    def test_case(self, case):

            # 引用全局的all
            all = self.all

            #根据all的值，渲染case
            case = eval(Template(str(case)).render(all))
            #case是实参
            # 渲染前：原本的数据源excel是列表，每一条用例是一个case是字典，先转成字符串str(case)，方便渲染
            # {"Authorization": "{{TOKEN}}"}     "{{TOKEN}}"：字典的 值，这里不是最终文本，而是 Jinja2 占位符（模板变量）
            # {{ ... }} 是 Jinja2 的语法，表示“把里面这个变量的值渲染进来”
            # 放在引号里是为了让渲染后的结果仍是一个“合法的字符串值”
            # 渲染时：render()是Template包的渲染函数
            # 渲染后：再用eval()转成字典
            # 外层花括号是字典，占位符要双大括；值是字符串要引号，渲染之后再反序列。

            #初始化allure报告
            allure_init(case=case)#形参=实参  参数只有一个时形参可以不写
            # allure.dynamic.feature(case["feature"])
            # allure.dynamic.story(case["story"])
            # allure.dynamic.title(f"ID:{case["id"]} -- {case["title"]}")


            # 核心步骤1: 解析请求数据
            request_data = analyse_case(case)

            #核心步骤2: 发起请求，得到响应结果
            # res = requests.request(**request_data)  # **字典 的意思是 参数解包，会把字典里的 key/value 当作函数的参数传进去。
            # print("🔹核心步骤2json:",res.json())
            #核心步骤2: 发起请求，得到响应结果
            res = send_http_request(**request_data)

            #核心步骤3: 处理断言
            #http响应断言
            http_assert(case, res)

            #数据库断言
            jdbc_assert(case)

            #核心步骤4: 提取
            #JSON 提取
            json_extractor(case, all, res)

            #SQL提取
            jdbc_extractor(case, all)

