import allure
import jsonpath
from utils.send_request import send_jdbc_request


def json_extractor(case, all, res):#传进来全局变量all
    if case["jsonExData"]:
        with allure.step("4.JSON提取"):
            # 首先把jsonExData的key和value拆开
            for key, value in eval(case["jsonExData"]).items():  # 这里case["jsonExData"]从excel拿出来是string，eval()转成字典
                v = jsonpath.jsonpath(res.json(), value)[0]  # value重新赋值！
                # print(value)
                # 现在全局属性all在测试函数外面
                all[key] = v
                # print(all)


def jdbc_extractor(case, all):
    if case["sqlExData"]:
        with allure.step("4.JDBC提取"):
            for key, q_value in eval(case["sqlExData"]).items():
                v = send_jdbc_request(q_value)
                all[key] = v