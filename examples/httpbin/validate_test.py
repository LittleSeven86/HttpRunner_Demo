# NOTE: Generated By HttpRunner v4.1.4
# FROM: validate.yml
from httprunner import HttpRunner, Config, Step, RunRequest


class TestCaseValidate(HttpRunner):

    config = Config("basic test with httpbin").base_url("https://httpbin.org/")

    teststeps = [
        Step(
            RunRequest("validate response with json path")
            .get("/get")
            .with_params(**{"a": 1, "b": 2})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.args.a", "1")
            .assert_equal("body.args.b", "2")
        ),
        Step(
            RunRequest("validate response with python script")
            .get("/get")
            .with_params(**{"a": 1, "b": 2})
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseValidate().test_start()