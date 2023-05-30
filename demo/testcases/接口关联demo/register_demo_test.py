# NOTE: Generated By HttpRunner v4.3.0
# FROM: testcases/接口关联demo/register_demo.yml
from httprunner import HttpRunner, Config, Step, RunRequest


class TestCaseRegisterDemo(HttpRunner):

    config = Config("注册接口").base_url("${ENV(base_url)}").export(*["code"])

    teststeps = [
        Step(
            RunRequest("注册接口")
            .post("/member/register")
            .with_headers(
                **{
                    "Content-Type": "application/json",
                    "X-Lemonban-Media-Type": "lemonban.v2",
                }
            )
            .with_json({"mobile_phone": "$mobile_phone", "pwd": "$pwd"})
            .extract()
            .with_jmespath("body.code", "code")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.msg", "账号已存在")
        ),
    ]


if __name__ == "__main__":
    TestCaseRegisterDemo().test_start()
