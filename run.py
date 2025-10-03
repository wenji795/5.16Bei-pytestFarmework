import pytest
import os

if __name__=="__main__":
        pytest.main([
                "-vs",
                "./testcases/test_runner.py", #指定要运行的测试文件
                "--alluredir", "./report/json_report", #把测试结果保存为 Allure 能识别的 JSON 文件，存到 ./report/json_report/ 目录
                "--clean-alluredir" #在写入 JSON 之前清空目录，避免旧的测试结果干扰
        ])

        os.system("allure generate ./report/json_report -o ./report/html_report --clean")
