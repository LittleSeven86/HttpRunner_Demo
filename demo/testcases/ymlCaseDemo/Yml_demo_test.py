# NOTE: Generated By HttpRunner v4.3.0
# FROM: testcases/ymlCaseDemo/Yml_demo.yml
from httprunner import HttpRunner, Config, Step, RunRequest


class TestCaseYmlDemo(HttpRunner):

    config = (
        Config("请求测试用例")
        .variables(
            **{
                "mobile_phone": 13300000096,
                "pwd": "Aa123456",
                "sql": 'SELECT COUNT(*) FROM member WHERE mobile_phone = "13300000100"',
            }
        )
        .base_url("${ENV(base_url)}")
    )

    teststeps = [
        Step(
            RunRequest("登录接口")
            .with_variables(**{"mobile_phone": 13300000100, "pwd": "Aa123456"})
            .setup_hook("${connect_database('demo/config.yml',$sql)}")
            .setup_hook("${hook_print(hello)}")
            .post("/member/login")
            .with_headers(
                **{
                    "X-Lemonban-Media-Type": "lemonban.v2",
                    "Content-Type": "application/json",
                }
            )
            .with_json({"mobile_phone": "$mobile_phone", "pwd": "$pwd"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("connect_database('demo/config.yml'", "$sql)")
        ),
    ]


if __name__ == "__main__":
    TestCaseYmlDemo().test_start()
