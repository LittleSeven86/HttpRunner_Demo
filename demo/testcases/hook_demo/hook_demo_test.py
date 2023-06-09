# NOTE: Generated By HttpRunner v4.3.0
# FROM: testcases\hook_demo\hook_demo.yml
import pytest

from httprunner import HttpRunner, Config, Step, RunRequest
from httprunner import Parameters


class TestCaseHookDemo(HttpRunner):
    @pytest.mark.parametrize(
        "param", Parameters({"mobile_phone-pwd": "${P(csv_data/mobile_phone-pwd.csv)}"})
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("关联测试用例").base_url("${ENV(base_url)}")

    teststeps = [
        Step(
            RunRequest("注册接口")
            .setup_hook("${hook_print('这是函数级别测试夹具--1')}")
            .setup_hook("${setup_hook_add_kwargs($request)}")
            .post("/member/register")
            .with_headers(
                **{
                    "Content-Type": "application/json",
                    "X-Lemonban-Media-Type": "lemonban.v2",
                }
            )
            .with_json({"mobile_phone": "$mobile_phone", "pwd": "$pwd"})
            .teardown_hook("${hook_print('这是函数级别测试夹具--2')}")
            .extract()
            .with_jmespath("body.code", "code")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.msg", "账号已存在")
        ),
    ]


if __name__ == "__main__":
    TestCaseHookDemo().test_start()
