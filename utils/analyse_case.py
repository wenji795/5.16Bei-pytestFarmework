import allure

from config.config import BASE_URL


@allure.step("1.解析请求数据")#在函数外部用装饰器
def analyse_case(case):
    # 核心步骤1: 解析请求数据
    method = case["method"]  # case 是字典，字典要取某个键的值，必须用 方括号 []  意思是从字典里取指定键对应的值。
    url = BASE_URL + case["path"]
    headers = eval(case["headers"]) if isinstance(case["headers"], str) else None
    params = eval(case["params"]) if isinstance(case["params"], str) else None
    data = eval(case["data"]) if isinstance(case["data"], str) else None
    json = eval(case["json"]) if isinstance(case["json"], str) else None
    files = eval(case["files"]) if isinstance(case["files"], str) else None

    request_data = {
        "method": method,
        "url": url,
        "headers": headers,
        "params": params,
        "data": data,
        "json": json,
        "files": files,
    }
    #需要加上返回值，不然test_runner的request_data报错
    return request_data