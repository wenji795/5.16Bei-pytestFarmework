import allure


def allure_init(case):#case是形参
    allure.dynamic.feature(case["feature"])
    allure.dynamic.story(case["story"])
    allure.dynamic.title(f"ID:{case["id"]} -- {case["title"]}")