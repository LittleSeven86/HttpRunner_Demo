# 官方文档
## 设计理念

- 约定大于配置:测试用例是标准结构化的，格式统一，方便协作和维护标准开放: 
- 基于开放的标准，支持与 HAR/Postman/Swagger/Curl/JMeter 等工具对接，轻松实现用例生成和转换次投入多维复用:
- 一套脚本可同时支持接口自动化测试、性能测试、数字体验监测等多种 API 测试需求融入最佳工程实践:
- 不仅仅是一款测试工具，在功能中融入最佳工程实践，实现面向网络协议的一站式测试解决方案

## 核心特征

- 网络协议：完整支持 HTTP(S)/1.1 和 HTTP/2，可扩展支持 WebSocket/TCP/RPC 等更多协议
- 多格式可选：测试用例支持 YAML/JSON/go test/pytest 格式，并且支持格式互相转换
- 双执行引擎：同时支持 golang/python 两个执行引擎，兼具 go 的高性能和 [pytest](https://docs.pytest.org/) 的丰富生态
- 录制 & 生成：可使用 [HAR](https://en.wikipedia.org/wiki/HAR_(file_format))/Postman/Swagger/curl 等生成测试用例；基于链式调用的方法提示也可快速编写测试用例
- 复杂场景：基于 variables/extract/validate/hooks 机制可以方便地创建任意复杂的测试场景
- 插件化机制：内置丰富的函数库，同时可以基于主流编程语言（go/python/java）编写自定义函数轻松实现更多能力
- 性能测试：无需额外工作即可实现压力测试；单机可轻松支撑 1w+ VUM，结合分布式负载能力可实现海量发压
- 网络性能采集：在场景化接口测试的基础上，可额外采集网络链路性能指标（DNS 解析、TCP 连接、SSL 握手、网络传输等）
- 一键部署：采用二进制命令行工具分发，无需环境依赖，一条命令即可在 macOS/Linux/Windows 快速完成安装部署

## 前言
HttpRunner4 历经近5年的迭代已经进入到4.0版本，简短的概括HR2用例执行是unitest，HR4采用pvtest执行，yml格式用例执行时会解析为"`xx_test.py`"文件最终通过HR框架封装的方法解析为pytest可执行的用例，同时也原生支持pytest用例编写时更加灵活，在用例编写和断言方面更加便捷

## V4和历史版本对比
| 版本 | v1 | v2 | v3 | HttpRunner+ | v4 |
| --- | --- | --- | --- | --- | --- |
| 发布时间 | 2018.03.07 | 2019.01.01 | 2020.03.10 | 2021.11.18 | 2022.05.01 |
| 开发语言 | Python | Python | Python | Golang | Golang + Python |
| 版本号规范（semver） | ❌ | ✅ | ✅ | ✅ | ✅ |
| 网络协议 | HTTP(S)/1.1 | HTTP(S)/1.1 | HTTP(S)/1.1 | HTTP(S)/1.1 | **多协议** HTTP(S)/HTTP2/WebSocket/_TCP/RPC_ |
| 脚本转换工具 | HAR | HAR | HAR | HAR | HAR/_Postman/Swagger/Curl_ |
| 工程脚⼿架 | ❌ | ✅ | ✅ | ✅ | ✅ |
| 测试⽤例（集）格式 | v1 | v2 | v2 | v2 | v2 |
| 测试⽤例分层机制 | v1 | v2 | v2 | v2 | v2 |
| 脚本格式类型 | YAML/JSON | YAML/JSON | YAML/JSON/**pytest** | YAML/JSON | YAML/JSON/**pytest**/**gotest** |
| 脚本格式校验 | ❌ | [jsonschema](https://github.com/python-jsonschema/jsonschema) | ❌ | ❌ | _TODO_ |
| 脚本编写语法提示 | ❌ | ❌ | pytest 链式调用 | gotest 链式调用 | gotest 链式调用 + pytest 链式调用 |
| 脚本执行引擎 | Python unittest | Python unittest | Python **pytest** | Go 自研 | Go 自研 + Python **pytest** |
| 插件化语言（debugtalk.xx） | Python | Python | Python | **多语言**（Go/Python） | **多语言**（Go/Python/_Java/etc._） |
| 参数提取机制 | regex + 点分隔符 | jmespath + regex + 点分隔符 | jmespath | jmespath + regex | jmespath + regex |
| skip 机制 | ✅ | ❌ | ❌ | ❌ | _TODO_ |
| 接口测试报告 | html 自研（jinja2） | html 自研（jinja2） | pytest-html/allure | html 自研（Go template） | html 自研（Go template） + _pytest-html/allure_ |
| 性能测试引擎 | Python Locust | Python Locust | Python Locust | Go Boomer | Go Boomer |
| 运行环境依赖 | Python 2.7/3.3+ | Python 2.7/3.5+ | Python 3.7+ pytest | 无需依赖 | Go 引擎无需依赖<br />pytest 引擎依赖 Python 3.7+ |
| 网络性能采集 | ❌ | ❌ | ❌ | ❌ | ✅ |
| 安装部署方式 | pip | pip | pip | curl/wget | curl/wget |

注：v4 中 _斜体_ 代表当前还未支持，但计划会实现。<br />从上面的表格可以看出，HttpRunner v4 颇有点**金刚葫芦娃**的意思，囊括了之前所有版本的功能，并且增加了很多新特性。

## v4 版本的 Go & Python 功能对比
HttpRunner v4.0 同时采用了 Golang/Python 两种编程语言，底层会有两套相对独立的执行引擎，目标是兼具 Golang 的高性能和 pytest 的丰富生态。<br />关键差异点对比如下：

| 引擎 | Go | Python |
| --- | --- | --- |
| 脚本类型 | YAML/JSON/gotest | YAML/JSON/pytest |
| 网络协议 | **多协议** HTTP(S)/HTTP2/WebSocket/_TCP/RPC_ | HTTP(S) |
| 脚手架工具 | hrp startproject | / |
| 用例生成工具 | hrp har2case | / |
| 脚本转换工具 | hrp convert | / |
| 插件化语言 | **多语言**（Go/Python/_Java/etc._） | Python |
| 运行环境依赖 | 与插件语言相关，详见[依赖环境说明](https://httprunner.com/docs/user-guide/installation/#%E4%BE%9D%E8%B5%96%E7%8E%AF%E5%A2%83%E8%AF%B4%E6%98%8E) | Python 3.7+ |
| 脚本编写语法提示 | gotest 链式调用 | pytest 链式调用 |
| 运行接口测试 | hrp run | hrp pytest |
| 运行性能测试 | hrp boom | / |
| 网络性能采集 | hrp run –http-stat | / |
| 接口测试报告 | html 自研（Go template） | pytest-html/allure |

<a name="smhNT"></a>
# 环境配置

1. 首先在虚拟环境中安装httprunner
```python
pip install httprunner==4.3.3
```

   - 踩坑日记--20230311
      - 因为V4.x版本 安装HttpRunner4.x后，还不能使用 hrp 命令行工具，这一步需要手动配置，噩梦的开始！！---mac调试环境过程
```python
1、需要先下载安装部署hrp，这里考虑可能权限不够，直接使用sudo
sudo bash -c "$(curl -ksSL https://httprunner.com/script/install.sh)"
```

      - 在安装过程中，抛出了一系列异常信息

![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1678543478598-5abad173-c68a-4822-a3b2-7eb4f707b8d4.png#averageHue=%23303030&clientId=u714e62cf-4662-4&from=paste&height=196&id=udd0a2c53&originHeight=754&originWidth=2096&originalType=binary&ratio=1&rotation=0&showTitle=false&size=153503&status=done&style=none&taskId=ua120961d-2ccc-4d44-ab51-1c1b2c92ca4&title=&width=546)

      - 解决方案
```python
1、创建local/bin目录
	sudo mkdir -p /usr/local/bin/
2、手动将命令移到目标目录
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1678543748777-21f29abe-808e-4306-b1df-0e5915ef41bb.png#averageHue=%235a5a3b&clientId=u714e62cf-4662-4&from=paste&height=170&id=u616fddf4&originHeight=421&originWidth=1450&originalType=binary&ratio=1&rotation=0&showTitle=false&size=195123&status=done&style=none&taskId=ua0885a97-d72f-4c17-b148-fdf65a58b98&title=&width=585)

      - 修复后效果

![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1678543813951-10145902-1b7d-423f-968f-04ebe7202aaa.png#averageHue=%23393939&clientId=u714e62cf-4662-4&from=paste&height=337&id=u3ce6de90&originHeight=1366&originWidth=1618&originalType=binary&ratio=1&rotation=0&showTitle=false&size=137773&status=done&style=none&taskId=uaeabb3fd-f322-4ca4-b754-fc06f9f866c&title=&width=399)		

2. 其次在终端控制台使用创建项目脚手架
```python
hrp startproject 脚手架名称
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1678543869815-28b33bcf-28fc-4eb0-82f1-b5c98c6c237e.png#averageHue=%23303030&clientId=u714e62cf-4662-4&from=paste&height=349&id=u4a1cbfc1&originHeight=1324&originWidth=2910&originalType=binary&ratio=1&rotation=0&showTitle=false&size=381805&status=done&style=none&taskId=ua3f4891a-f9f3-4ffa-b201-da3afa093d1&title=&width=767)![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1678543912339-a2ada599-38c0-441c-bcc4-9583025c455e.png#averageHue=%233b4042&clientId=u714e62cf-4662-4&from=paste&height=345&id=u2f430766&originHeight=1272&originWidth=790&originalType=binary&ratio=1&rotation=0&showTitle=false&size=150378&status=done&style=none&taskId=uade86d72-1ce2-4b0e-bf17-834aad11c22&title=&width=214)
<a name="pOCK2"></a>
# 框架拆解
![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1684763975593-c4a49e6e-c9fd-448f-a80f-baa7273860c8.png#averageHue=%235c644b&clientId=u9adb9089-ee3d-4&from=paste&height=826&id=u84eb993a&originHeight=924&originWidth=821&originalType=binary&ratio=1&rotation=0&showTitle=false&size=81414&status=done&style=none&taskId=ua65f07bb-6aa3-4ffc-badc-ddcf5c3526d&title=&width=734)

- 将HttpRunner源码嵌套在本地项目内，便于我们可以直接对源码进行补充和修改，
- 项目脚手架内创建具体的测试用例，将测试用例和用例依赖的参数化文件进行分离，实现数据和代码的分离，便于我们更好的管理和维护测试用例
- 脚手架内，可以根据`pytest`或者`YML`测试用例，在`utils`中定义插件函数，`YML`在`debugtalk.py`文件中定义，引用`$函数名（foo1,foo2）`，原生`pytest`测试用例在脚手架目录下的`conftest.py`文件中定义测试夹具
- 再根目录下创建启动项`main-debug.py`和`run-test.py`文件：
   - 两者区别在于：`main-debug.py`可以对单个测试用例进行调试，`run test.py`是批量运行case
   - `main-debug.py`文件通过命令行的方式入参调用HR4框架内部api完成测试用例加载和执行操作
```shell
#!/usr/bin/env python
# -*- coding=utf-8 -*-
 
import sys
from httprunner.cli import main
 
cmd = sys.argv.pop(1)
if cmd in ["hrp", "httprunner", "ate"]:
    main()
```

      - 在解释器配置中，配置使用脚本配置，参数为`python main-debug.py hrp run 测试用例 --alluredir=报告路径`

![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1685343216084-4a8fedda-f35f-4dda-aa62-6cf44ac2e90f.png#averageHue=%233e4245&clientId=ud3816294-ecfe-4&from=paste&height=329&id=u9f486de1&originHeight=512&originWidth=1293&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=47441&status=done&style=none&taskId=ufed5600d-d2cd-4ca2-a524-8a70318406b&title=&width=830.4000244140625)<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1685348065307-8c8f9023-a2bb-48ad-9552-36ccd6ba3e4d.png#averageHue=%235d7d68&clientId=ud3816294-ecfe-4&from=paste&height=243&id=ucf4a0775&originHeight=417&originWidth=1907&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=62315&status=done&style=none&taskId=uf8db842a-6401-49ea-87b1-a016a6ae3af&title=&width=1109.4000244140625)

   - `run test.py` 文件则提前定义数据后再调用HR4架内部的api完成侧用例的加载和执行操作
```shell
from httprunner.cli import main_run
if __name__ == '__main__':

    # -v 参数：debug模式打印出具体执行过程和请求响应出入参
    # main_run(['test/demo/testcases/测试1.yml',
    #       '-v',
    #       ])

# 可直接运行，如果想定位问题，可直接debug模式运行
    main_run([r"D:\Python\Httprunner_Demo\demo\testcases\pytestCaseDemo",  # case路径
              '-v',
              # '-s',
              '--report=hhhhhh.html',
              '--title=【酒旅-质量保障部】自动化报告',
              '--tester=【酒旅-质量保障部】',
              '--desc=报告描述信息【酒旅-质量保障部】',
              '--template=2'])
```
<a name="bfSRE"></a>
# HttpRunner依赖文件内容
```shell
colorama==0.4.5
filetype==1.1.0
funppy==0.5.0
loguru==0.6.0
pydantic==1.10.2
pymysql==1.0.2
requests_toolbelt==0.9.1
sentry_sdk==1.9.9
SQLAlchemy==1.4.41
thriftpy2==0.4.14
toml==0.10.2
tweepy==4.10.1
urllib3==1.26.12
allure-pytest==2.10.0
allure-python-commons==2.10.0
attrs==22.1.0
black==22.8.0
Brotli==1.0.9
certifi==2022.9.24
charset-normalizer==2.1.1
click==8.1.3
colorama==0.4.5
idna==3.4
iniconfig==1.1.1
Jinja2==3.1.2
jmespath==0.9.5
jsonpath==0.82
MarkupSafe==2.1.1
mypy-extensions==0.4.3
packaging==21.3
pathspec==0.10.1
platformdirs==2.5.2
pluggy==1.0.0
py==1.11.0
pydantic==1.8.2
pyparsing==3.0.9
pytest==7.1.3
pytest-html==3.1.1
pytest-metadata==2.0.2
pytest-testreport==1.1.5
PyYAML==5.4.1
requests==2.28.1
sentry-sdk==0.14.4
six==1.16.0
tomli==2.0.1
typing-extensions==4.3.0
urllib3==1.26.12
black==22.10.0
websocket-client==1.4.2
```
<a name="vI9zv"></a>
# 源码解析
<a name="gF1dM"></a>
## 项目本地结构
![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1684849053393-ef2357b1-cc98-4a08-a237-8a8148ae66af.png#averageHue=%233a444e&clientId=u5b3b93c0-8d0a-4&from=paste&height=220&id=ue4363276&originHeight=440&originWidth=744&originalType=binary&ratio=1&rotation=0&showTitle=false&size=49277&status=done&style=none&taskId=ue8c4ac34-5317-4fcd-905c-c2f36afbf9d&title=&width=372)
<a name="TwpZW"></a>
## HttpRunner 源码目录结构
![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1684850613613-d40b41ad-6af4-4d48-a49e-46d42f164934.png#averageHue=%2344484b&clientId=u5b3b93c0-8d0a-4&from=paste&height=700&id=u1bebce19&originHeight=1400&originWidth=1482&originalType=binary&ratio=1&rotation=0&showTitle=false&size=599234&status=done&style=none&taskId=ubb84785c-a9ba-471e-ab78-83f809d580e&title=&width=741)
<a name="B3GdU"></a>
# hrp命令
```bash
adb          simple utils for android device management			# adb 链接工具
boom         run load test with boomer											# 用boomer 进行负载测试
build        build plugin for testing												# 为测试构建插件
completion   Generate the autocompletion script for the specified shell		# 为指定的shell生成自动完成脚本
convert      convert multiple source format to HttpRunner JSON/YAML/gotest/pytest cases	# 将多个源格式转换为HttpRunner JSON/YAML/gotest/pytest案例
dns          DNS resolution for different source and record types	#不同源和记录类型的DNS解析
help         Help about any command													# 获取帮助
ios          simple utils for ios device management					# IOS链接帮助
ping         run integrated ping command										# 执行综合ping命令
pytest       run API test with pytest												# 用pytest运行接口测试
run          run API test with go engine										# 用go 引擎执行接口测试
startproject create a scaffold project											# 创建项目脚手架
```
<a name="Aqhh0"></a>
# 测试用例
<a name="PSKpY"></a>
## 用例配置项名称
测试脚本与测试数据分离后，就可以比较方便地实现数据驱动测试，通过对测试脚本传入一组测试数据，实现同一业务功能在输入不同业务数据情况下的测试验证。那么测试数据是如何传入测试脚本中的呢？这就需要用到测试数据与测试脚本之间的桥梁——用例配置（config），测试脚本除了包含多个有序的测试步骤之外，还包含针对当前测试用例的用例配置项

- `verify`客户端是否进行 SSL 校验（todo）
- `headers`定义测试用例级别的请求头
- `variables`定义测试用例级别的变量
- `parameters`配置参数驱动的数据源
- `parameters_setting`配置参数驱动的具体策略
- `think_time`配置思考时间的具体策略、超时时间限制等
- `websocket`配置 WebSocket 断开重连的最大次数和间隔等（todo）
- `export`导出当前测试用例中的变量
- `path`当前测试用例所在路径（通常不需要手工填写）
<a name="bqtIF"></a>
## 测试用例结构
通过查阅官方文档，HttpRunner目前支持三种测试用例格式，`pytest、YAML、JSON`三种格式，但是作者的角度出发时非常建议使用`pytest`格式，而不是使用`YAML/JSON`格式 <br />说明：

- 在每个测试用例中，都必须具备两个属性：`config`和`teststeps`
- `config`中可以进行测试用例级别的设置
   - `name`-- 必填	定义当前测试用例的名称，配合`allure`生成测试报告时会生成，在执行日志中也会显示

![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1685199733145-ff164892-8c1c-4ac7-990b-57793bb8bf2d.png#averageHue=%2350564f&clientId=u14b5bdf7-438b-4&from=paste&height=271&id=u15d1ccbe&originHeight=712&originWidth=2570&originalType=binary&ratio=1&rotation=0&showTitle=false&size=410848&status=done&style=none&taskId=ub746bcef-6087-4dff-93d5-07b11ac1b95&title=&width=977)

   - `base_url`--必填,指定 SUT 的通用架构和主机部分，例如`https://postman-echo.com`. 如果`base_url`指定，`teststep`中的`url`只需要在设置相对路径部分即可。如果您想在不同的 SUT 环境之间切换，这将特别有用。

![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1685200626702-6e5e572d-0543-4188-8d9c-71bfd5dc41a0.png#averageHue=%2331302a&clientId=u14b5bdf7-438b-4&from=paste&height=347&id=u862e5edc&originHeight=834&originWidth=2396&originalType=binary&ratio=1&rotation=0&showTitle=false&size=144341&status=done&style=none&taskId=uf9ce7119-087e-42b9-936a-19c1d0fb7cc&title=&width=998)

   - `variablels`--可选，

<a name="AKWeV"></a>
## 变量
<a name="Xyz2N"></a>
### 说明
HttpRunner是基于变量机制实现参数的生命周期管理，在 HttpRunner 测试用例中，有 4 个地方可以对变量进行声明。

- 声明全局变量`config variables`
- 声明数据驱动`parameters`
- 声明局部变量`teststep variables`
- 提取参数变量`session variavles`
- 环境变量`gloabl vairabls`
<a name="dwNTW"></a>
### 变量的引用

- 一般情况下，约定通过` ${foo} `或 `$foo` 的形式来引用变量
   - 如果在某些字段中存在部分引用变量的情况,例如`ABC123df`中的`C12`需要引入变量，那么只能使用`${C12}`，避免使用`$`会被误解析成`$C123df`
- 另一种需要说明的情况，如果在测试用例中本身就存在`$` 符号，那么可以通过`$$`进行**转义**，测试用例中某个字段的原始内容为` $m`，那么为了避免将其解析为变量，则需要将其写为` $$m`
<a name="AaUQH"></a>
### 变量优先级
针对以上4种变量类型，如果声明的变量名称出现重复，则会按照一定的优先级策略进行处理。<br />优先级从高到低依次为：`step variables > session variables > parameter variables > config variables`
<a name="F96Vy"></a>
### 全局环境变量
全局环境变量是在当前脚手架下所有的测试用例都可以引用到变量。全局变量在脚手架目录下的.env文件中进行配置，

- `.env`文件存放在脚手架根目录中

![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1685023594041-06ed428d-1786-4a28-8728-58a791e15dc6.png#averageHue=%23c3bb07&clientId=u448c3850-e43a-4&from=paste&height=257&id=u1e5a37db&originHeight=548&originWidth=1508&originalType=binary&ratio=2&rotation=0&showTitle=false&size=94002&status=done&style=none&taskId=ua7313e43-5159-4baf-82af-3e3a0dbb301&title=&width=708)

- 调用：可以在任意一个yaml或者json用例文件中，使用**${ENV(环境变量名)}直接调用**例如设置BASE_URL为：[http://127.0.0.1:8000](http://127.0.0.1:8000)
```yaml
# .env文件中
BASE_URL=http://127.0.0.1:8000

# YML测试用例中
url: "${ENV(BASE_URL)}/user/login/"
```
<a name="NUZb1"></a>
### 声明全局变量
作用：在` config `下声明的 `variables` 为测试用例全局变量，作用域为当前整个测试用例，在测试用例的所有地方都可以引用。<br />示例：

- 设置了`base_url`、`test`、`expect_body_code`三个全局变量，分别在`url、params、validate`中进行使用
```yaml
config:
    name: "GET请求测试用例"
    variables:
      base_url: http://www.fairytest.com
      test: test
      expect_body_code: 412

teststeps:
-
  name: GET请求测试用例

  request:
    url: ${base_url}/api/demand/getPageLink
    headers:
        Content-Type: application/json;charset=UTF-8
    method: GET
    params:
        test: ${test}

  validate:
    - eq: ["status_code", 200]
    - eq: ["body.code", $expect_body_code]
```

- **踩坑点：在**`**validate**`**中引用变量只能使用**`**$foo**`**不能使用**`**${foo}**`**,不然会给出YML格式错误**

![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1685024311012-d682ae97-b225-40f6-a8f7-9233b6ece1e4.png#averageHue=%232c2b2b&clientId=u448c3850-e43a-4&from=paste&height=133&id=avt6y&originHeight=256&originWidth=1824&originalType=binary&ratio=2&rotation=0&showTitle=false&size=57948&status=done&style=none&taskId=ub3a49919-2a25-4d37-afac-a4c94af60d8&title=&width=949)
<a name="KMjUD"></a>
### 声明数据驱动
作用：在 `config` 下声明的 `parameters `为测试用例的驱动参数；它的作用域也是覆盖整个测试用例，在测试用例的所有地方都可以引用。<br />说明：在`HttpRunner`中支持使用Pytest原生测试用例，YML格式，以及JSON测试用例，Pytest原生测试用例参数化可以直接使用`pytest.mark.parameterize`，这里我们将针对YML格式的测试用例作讲解

- `YML`用例在测试用例头部`config`中使用关键字`parameters`定义，同时需要指定`parameters_setting`
- 支持使用三种输入格式
   - 参数列表，形如：`user_agent: [ "iOS/10.1", "iOS/10.2" ]`
```shell
config:
  name: post请求测试demo
  author: xiaoqi
  parameters:
    mobile_phone-pwd: [['13300000097','Aa123456'],['13300000098','Aa123456']]

teststeps:
-
  name: 登录接口
  request:
    headers:
      X-Lemonban-Media-Type: lemonban.v2
    method: POST
    url: http://api.lemonban.com/futureloan/member/login
    body: {"mobile_phone": $mobile_phone,"pwd":$pwd}

  validate:
    - eq: ["status_code", 200]
```

   - csv文件，形如：`username-password: ${P(相对路径)} `，csv 示例：`account.csv`
      - `username-password`参数名称采用短横线`（-）`作为分隔符，表示从 csv 中读取` username` 与` password` 这两个参数。如果直接采用列表方式导入参数，username-password需对应一个二维列表，自定义函数方式同理
      - 踩坑点：
```shell
config:
  name: post请求测试demo
  author: xiaoqi
  parameters:
    mobile_phone-pwd: ${P(csv_data/mobile_phone-pwd.csv)}
#    mobile_phone-pwd: ${parameterize(D:\Python\Httprunner_Demo\demo\case_file\Lemon_mobile.csv)}
  #  mobile_phone-pwd: ${parameterize($file)}

  variables:
    file: case_file/Lemon_mobile.csv
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1685087471851-68450355-3e00-4051-bc05-34ec746a3c00.png#averageHue=%23b9ad26&clientId=u661fec2c-a2ea-4&from=paste&height=491&id=u385465c1&originHeight=945&originWidth=1916&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=228901&status=done&style=none&taskId=u8e9356b0-51dd-4844-80f5-ee7d359e478&title=&width=995)

   - 自定义函数，形如：`user_id: ${get_user_id(10)}`，函数返回值为列表

![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1685090203092-0b383954-5682-4e52-844d-4f4dbd60db02.png#averageHue=%23bbb372&clientId=u661fec2c-a2ea-4&from=paste&height=540&id=ufd2c2383&originHeight=1042&originWidth=1920&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=298570&status=done&style=none&taskId=uac2742c2-ae6e-4794-a158-2a265dbdc91&title=&width=994.4000244140625)

      - 自定义函数源自于脚手架目录下的`debugtalk.py`文件，自定义函数目前支持两种语言编写形式，`go、python`此文只针对python进行讲解
      - 使用 python 语言编写方式，仅需在项目根目录 debugtalk.py 中编写自定义函数即可，无需进行额外编译，在YML测试用例中，只需要使用`$函数名`即可进行调用，同时，使用 hrp run/boom 也兼容 v4.0 版本之前的写法
- [ ] `**parameters_setting**`**整体分为一下内容--TODO，此坑暂时未填**
   - `pick_order`整体策略，如果未单独指定参数选取策略，则默认使用整体策略
   - `strategies`单独配置每个参数的策略
   - `strategies` 可以为每一个参数配置参数名称与具体选取策略。参数名称仅用于标识，可选填。如果未设置参数选取策略，则默认使用 sequential 策略。
   - `limit`迭代次数
      - 迭代次数默认为所有顺序选取执行参数的笛卡尔积，我们也可以通过设置 limit 来指定迭代次数，有效的迭代次数为 limit > 0，如果 limit = 0 表示默认，如果 limit < 0，则表示无限制迭代次数。
```yaml
笛卡尔积(Cartesian product)是一个数学术语，指的是两个或多个集合的所有可能的组合方式。在计算机科学中，笛卡尔积通常用于表示两个或多个数据结构之间的所有可能的连接方式。
import itertools
list1 = [1, 2]
list2 = ['a', 'b']
list3 = ['x', 'y']
cartesian_product = list(itertools.product(list1, list2, list3))
print(cartesian_product)

>>> [(1, 'a', 'x'), (1, 'a', 'y'), (1, 'b', 'x'), (1, 'b', 'y'), (2, 'a', 'x'), (2, 'a','y'), (2, 'b', 'x'), (2, 'b', 'y')]
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1685168908102-f6d22202-677e-4e66-87b4-6e8837bc86d2.png#averageHue=%232c2b2a&clientId=u14b5bdf7-438b-4&from=paste&height=144&id=ue760a341&originHeight=312&originWidth=1368&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36922&status=done&style=none&taskId=u8c74e945-7e1d-4e5d-a625-00ec82d74b0&title=&width=631)<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1685168936317-b3a738ff-15ce-41f9-ae48-8067831f75d3.png#averageHue=%233a3b39&clientId=u14b5bdf7-438b-4&from=paste&height=266&id=u4f155aa7&originHeight=554&originWidth=1906&originalType=binary&ratio=1&rotation=0&showTitle=false&size=278817&status=done&style=none&taskId=u39d90b2b-18f1-4887-af93-da410ba0ad6&title=&width=915)

      - 通过笛卡尔积的这种数据组合方式，可以实现数据的覆盖，大大减少了我们编写的测试用例的数量，提高工作效率
<a name="OBQr6"></a>
### 声明局部变量
在实际业务场景中，很多时候存在参数关联的情况，即当前接口请求参数来自于之前接口的响应结果。

- 例如，通过手机号登录的场景中，登录接口请求参数需要带上服务端预先返回的短信验证码；如果缺少这个参数关联操作，接口调用将会失败。

目前，HttpRunner 支持 2 种响应结果字段提取方式。<br />提取的参数变量类似于 session 参数，作用域为当前步骤及之后的步骤，引用方式与普通的变量一致。

- jmespath表达式
   - 若响应结果为 JSON 结构，支持采用 [jmespath](https://jmespath.org/) 表达式进行参数提取。
      - [jmespath](https://jmespath.org/) 是一种 JSON 查询语言，可以使用非常灵活且强大的表达式查询 JSON 数据结构中的字段，并返回符合条件的数据。
```json
{
  "locations": [
    {"name": "Seattle", "state": "WA"},
    {"name": "New York", "state": "NY"},
    {"name": "Bellevue", "state": "WA"},
    {"name": "Olympia", "state": "WA"}
  ]
}

查询所有城市名称：locations[*].name
查询第二个城市名称：locations[1].name => “New York”
查询最后一个州名：locations[-1].state => “WA”
```

      - extract 的对象仅有 5 种类型：
         - status_code：提取响应状态码，例如 200、404
         - proto：提取协议类型，例如 “HTTP/2.0”、“HTTP/1.1”
         - headers：从响应 headers 中提取字段，例如 headers.name
         - cookies：从响应 cookies 中提取字段，例如 cookies.Token
         - body：从响应 body 中提取字段，例如 body.args.foo1
      - 如果表达式中存在 - 的情况，那么需要加引号处理
```json
"teststeps": [
	{
		"name": "",
		"variables": {
			"name": "demo"
		},
		"request": {
			"method": "POST",
			"url": "https://www.httpbin.org",
			"params": {},
			"headers": {
				"name": "$name",
				"Content-Type": "text/plain"
			},
			"body": ""
		},
		"validate": [],
		"extract": {
			"name": "body.headers.Name"
		}
	}
]
```

      - 如果想要提取上述`Content-Type`中的参数，就要特殊处理`headers."Content-Type"`
- 正则表达式
   - 若响应结果为 text/html 格式，支持采用正则表达式的方式提取目标参数。
   - 例如响应的 body 为：
```json
<html>
<title>参数提取（extract） | HttpRunner</title>
</html>
```

   - 如果我们想提取页面的 title 字段，就可以这样做：`<title>(.*)</title>`即在提取表达式中指定目标参数的左右边界，然后将目标参数替换为 (.*)；这样我们就能将正则匹配到的值赋值给参数变量了。
```json
"teststeps": [
	{
		"name": "",
		"variables": {
			"name": "demo"
		},
		"request": {
			"method": "GET",
			"url": "https://www.httpbin.org",
			"params": {},
			"headers": {
				"name": "$name",
				"Content-Type": "text/plain"
			}
		},
		"validate": [],
		"extract": {
			"title": "<title>(.*)</title>"
		}
	}
]
```

- 在实际的YML测试用例中，示例如下：
   - 在第一个步骤中，将变量进行提取，在下一个步骤中可以直接引用
```json
teststeps:
-
  name: 注册接口
  request:
    headers:
      X-Lemonban-Media-Type: lemonban.v2
    method: POST
    url: $base_url/futureloan/member/register
    body: {"mobile_phone": $mobile_phone,"pwd":$pwd}
  validate:
    - eq: ["status_code", 200]
  extract:
    code: body.code

-
  name: 登录接口
  request:
    headers:
      X-Lemonban-Media-Type: lemonban.v2
    method: POST
    url: http://api.lemonban.com/futureloan/member/login
    body: {"mobile_phone": $mobile_phone,"pwd":$pwd,"code":$code}
  validate:
    - eq: ["status_code", 200]
```
<a name="r3BWd"></a>
### 导出会话变量

- 作用：指定测试用例导出的会话变量。意味着把每个测试用例看成一个黑盒子，在`config`中`variables`是当前测试用例的输入部分，`config`中`export`是输出部分，需要先在具体的`teststep`中将数据提取出来，然后在config中导出变量。
- 应用场景：当一个测试用例在另一个测试用例的步骤中被引用时，将提取一些会话变量用于后续测试步骤，那么提取的会话变量应该在配置部分进行配置export。
- 示例：当前接口关联测试用例，需要进行先注册，再登录操作，
   - 关联接口的写法详见下方接口的关联
```shell
config:
  name: 关联测试用例
  parameters:
    mobile_phone-pwd: ${P(csv_data/mobile_phone-pwd.csv)}

teststeps:
-
  name: 注册接口
  testcase: testcases/接口关联demo/register_demo.yml
-
  name: 登录接口
  testcase: testcases/接口关联demo/login_demo.yml
```

- 注册接口，在`teststeps`中先将需要的参数使用`extract`进行提取，在头部`config`中使用关键字`export`导出当前会话变量
```shell
config:
  name: 注册接口
  export:
    - code

teststeps:
-
  name: 注册接口
  request:
    headers:
      X-Lemonban-Media-Type: lemonban.v2
    method: POST
    url: http://api.lemonban.com/futureloan/member/register
    body: {"mobile_phone": $mobile_phone,"pwd":$pwd}
  extract:
    code: body.code
  validate:
    - eq: ["status_code", 200]
```

- 登录接口，获取到变量`code`的值，进行引用
```shell
config:
  name: 登陆接口

teststeps:
-
  name: 登录接口
  request:
    headers:
      X-Lemonban-Media-Type: lemonban.v2
    method: POST
    url: http://api.lemonban.com/futureloan/member/login
    body: {"mobile_phone": $mobile_phone,"pwd":$pwd,"code":$code}
  validate:
    - eq: ["status_code", 200]
```

- 结果验证

![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1685196412198-d86dca8a-f56b-49fe-a5d9-0ce6c9771c6e.png#averageHue=%2371715c&clientId=u14b5bdf7-438b-4&from=paste&height=981&id=u19f5db16&originHeight=981&originWidth=1920&originalType=binary&ratio=1&rotation=0&showTitle=false&size=450412&status=done&style=none&taskId=u834d7765-e226-44eb-b39e-6f97f937f36&title=&width=1920)
<a name="Jh9Je"></a>
## 接口的关联
在常见的业务场景中，常常存在一个接口依赖上游接口的出参，比如：查询项目详情的列表，需要在请求头部添加一个`Token`，而这个`Token`只有用户登录以后才可以获取，所以这整个完整的业务场景应该是：`用户登录 -> 查询项目详情 `，对于这种依赖的接口，可以使用公共封装好的单个测试用例，组合成一个新的YML测试用例<br />注意点：

- 在`teststeps`中使用`testcase`关键字进行引用，参数为当前测试脚手架目录后的相对路径，**---踩坑点**
- 存在数据依赖的情况下，在被依赖的YML文件中使用`export`导出会话变量，这个作用域是针对当前测试用例来说是全局变量，后续的接口依赖的话直接使用`${}`或者`$`直接调用即可
```shell
config:
  name: 关联测试用例
# 使用CSV文件进行参数化，定义变量mobile_phone和pwd
  parameters:
    mobile_phone-pwd: ${P(csv_data/mobile_phone-pwd.csv)}

teststeps:
-
  name: 注册接口
  testcase: testcases/接口关联demo/register_demo.yml
-
  name: 登录接口
  testcase: testcases/接口关联demo/login_demo.yml
```

- 注册接口，在`teststeps`中先将需要的参数使用`extract`进行提取，在头部`config`中使用关键字`export`导出当前会话变量
```shell
config:
  name: 注册接口

  export:
    - code

teststeps:
-
  name: 注册接口
  request:
    headers:
      X-Lemonban-Media-Type: lemonban.v2
    method: POST
    url: http://api.lemonban.com/futureloan/member/register
    body: {"mobile_phone": $mobile_phone,"pwd":$pwd}
  extract:
    code: body.code
  validate:
    - eq: ["status_code", 200]
```

- 登录接口，获取到变量`code`的值，进行引用
```shell
config:
  name: 登陆接口

teststeps:
-
  name: 登录接口
  request:
    headers:
      X-Lemonban-Media-Type: lemonban.v2
    method: POST
    url: http://api.lemonban.com/futureloan/member/login
    body: {"mobile_phone": $mobile_phone,"pwd":$pwd,"code":$code}
  validate:
    - eq: ["status_code", 200]
```

- 实际验证

![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1685196412198-d86dca8a-f56b-49fe-a5d9-0ce6c9771c6e.png#averageHue=%2371715c&clientId=u14b5bdf7-438b-4&from=paste&height=981&id=TfuTS&originHeight=981&originWidth=1920&originalType=binary&ratio=1&rotation=0&showTitle=false&size=450412&status=done&style=none&taskId=u834d7765-e226-44eb-b39e-6f97f937f36&title=&width=1920)

<a name="PkM00"></a>
## YML测试用例
<a name="p0Ouj"></a>
### YML书写格式

- yaml是数据格式，不是数据类型（结构），yaml配置文件的后缀为.yml或者.yaml
- 使用`#`作为注释，注释只能在某一行的前后，不能与`key\value`在同一行
- yaml中有两种结构
   - 一种是`key: value`，value与冒号之间必须有空格
   - 另一种是 `- key: value`，“-”为列表结构
- 嵌套的同一级条目前缩进必须一致（一般缩进2个空格）重点注意相同层级左侧对齐，否则很容易导致测试用例的加载错误
- 如果value使用引号（单引号或者双引号），那么该value为字符串类型
- 如果value中只要有字母，哪怕没有添加引号，一般也会识别为字符串类型（false、true、on、off、null除外）
- value为false、true、on、off，是布尔类型，null为空
- value中为纯数字或者小数，会被识别为int或float类型
<a name="LzWX0"></a>
### GET请求--YML Demo

- `GET`
```bash
config:
    name: "GET请求测试用例"
  	
    variables:
      base_url: http://www.fairytest.com
      test: test

teststeps:
-
  name: GET请求测试用例

  request:
    url: $base_url/api/demand/getPageLink
    headers:
        Content-Type: application/json;charset=UTF-8
    method: GET
    params:
        test: $test

  validate:
    - eq: ["status_code", 200]
    - eq: ["body.code", 412]
#    - eq: ["$..code", [412]]    # 断言参数提取 JsonPath方式提取参数，后续讲解
```
<a name="eqnnY"></a>
### POST请求--YML Demo

- `POST`
```bash
config:
    name: 登录接口

teststeps:
-
  name: 登录接口
  request:
      url: ${ENV(base_url)}/api/leapp/login/login-sms
      headers:
          Content-Type: application/json;charset=UTF-8
          god: 'true'
      method: POST
      body: {"loginName": "","mobile": "16000005576","password": "","smsCode": "123456"}

  variables:
    test: 'test'

  validate:
    - eq: ["status_code", 200]
    - eq: ["body.desc", 成功]
#    - eq: ["$..code", [412]]    # 断言参数提取 JsonPath方式提取参数，后续讲解
```

<a name="aBs2v"></a>
# 测试用例官方文档
**HttpRunner 初始化测试用例的几种方式**

- [录制生成 HAR 文件](https://httprunner.com/docs/user-guide/gen-tests/record/)
   - 基于 HAR 生成测试用例
- [转换生成测试用例](https://httprunner.com/docs/user-guide/gen-tests/convert/)
   - 使用主流 API 工具转换生成测试用例
- [手工编写](https://httprunner.com/docs/user-guide/gen-tests/write-cases/)
   - 手工编写 YAML/JSON/pytest/gotest 测试用例，本次重点讲解的方式
<a name="GmIkv"></a>
## yaml文件格式

<a name="igEZk"></a>
## 测试用例的框架组成
<a name="OVea5"></a>
### 通用概念介绍
在介绍如何手工编写测试用例之前，首先介绍 HttpRunner 中的一些通用概念，理解这些概念对于手工编写测试用例至关重要，因为无论是哪种形态的测试用例，都是按照一定的规则来设计的。这些通用概念具体包含以下的内容：
<a name="zTAp5"></a>
### 测试步骤（teststep）
测试步骤是测试用例的最小执行单元，测试用例是测试步骤的有序集合，对于接口测试来说，每一个测试步骤应该就对应一个具体的用户操作。HttpRunner 支持的测试步骤如下：<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1678626027919-55ada981-273f-4a9c-9568-3c7fe6240300.png#averageHue=%23ebebea&clientId=u6b5d84c6-16c8-4&from=paste&height=349&id=uc417fe82&originHeight=392&originWidth=415&originalType=binary&ratio=2&rotation=0&showTitle=false&size=71142&status=done&style=none&taskId=uf4e35c99-c95a-4dd9-95cd-cbea3e79d71&title=&width=369.5)<br />除了基本的测试步骤之外，部分测试步骤还可以进行增强，从而拓展更多功能，这一部分内容将在[增强测试用例](https://httprunner.com/docs/user-guide/enhance-tests/)章节中进行详细介绍。<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1678626052348-067b5097-827b-43c2-83a8-95519e16f6a5.png#averageHue=%23eeeeee&clientId=u6b5d84c6-16c8-4&from=paste&height=289&id=uf3f121cc&originHeight=339&originWidth=437&originalType=binary&ratio=2&rotation=0&showTitle=false&size=43656&status=done&style=none&taskId=uea2f9e8a-04ea-48e9-9fc2-bff10a6505e&title=&width=372.5)
<a name="Fotg0"></a>
### 测试用例
概括下来，一条测试用例（testcase）应该是为了测试某个特定的功能逻辑而精心设计的，并且至少包含如下几点：

- 明确的测试目的（achieve a particular software testing objective）
- 明确的输入数据（inputs）
- 明确的运行环境（execution conditions）
- 明确的测试步骤描述（testing procedure）
- 明确的预期结果（expected results）

按照上述的测试用例定义，HttpRunner 的测试用例应该保证是完整并且可以独立运行的。<br />从测试用例的组成结构来看，一个测试用例可以分为「测试脚本」和「测试数据」两部分：

- 测试脚本：重点是描述测试的业务功能逻辑，包括预置条件、测试步骤、预期结果等，并且可以结合辅助函数（debugtalk.go/debugtalk.py）实现复杂的运算逻辑
- 测试数据：重点是对应测试的业务数据逻辑，例如数据驱动文件中的定义的 UUID、用户名等等，以及环境配置文件中定义的 base_url 环境变量等等

测试脚本与测试数据分离后，就可以比较方便地实现数据驱动测试，通过对测试脚本传入一组测试数据，实现同一业务功能在输入不同业务数据情况下的测试验证。那么测试数据是如何传入测试脚本中的呢？这就需要用到测试数据与测试脚本之间的桥梁——用例配置（config），测试脚本除了包含多个有序的测试步骤之外，还包含针对当前测试用例的用例配置项，HttpRunner 支持的用例配置项如下：<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1678626176243-8741b59f-b47c-4738-a645-39ab2ebdea8f.png#averageHue=%23efefef&clientId=u6b5d84c6-16c8-4&from=paste&height=481&id=u8a006771&originHeight=635&originWidth=624&originalType=binary&ratio=2&rotation=0&showTitle=false&size=104100&status=done&style=none&taskId=uaefc2023-f3c9-4ea2-9297-052a499ef19&title=&width=473)
<a name="gfF52"></a>
### 测试用例集（testsuite）
从上面定义中可以看出，测试用例集是测试用例的无序集合，通俗来将，测试用例集就是「一堆」测试用例。对应地，HttpRunner 除了支持指定单个文件来运行某一测试用例，也支持指定多个文件或指定文件夹来运行一整个测试用例集。
<a name="THme0"></a>
### 项目根目录：
项目根目录是整个测试用例集的目录，测试用例中的相对路径（例如在测试步骤中引用 API 或测试用例的路径，或者在使用参数驱动功能时引用 CSV 文件的路径）都是基于项目根目录来进行引用的。在 HttpRunner v4.0 中，项目根目录以 proj.json 为锚，并且按照使用习惯，环境配置文件 .env，以及辅助函数的定义文件 debugtalk.py/debugtalk.go 通常也是放在项目根目录下的。
<a name="iKzZ6"></a>
## 创建测试用例步骤
<a name="A9AXH"></a>
## 设置变量
<a name="eVmPF"></a>
### 局部变量
局部变量在yaml文件头部的config中进行配置，例如设置base_url为：[http://127.0.0.1:8000](http://127.0.0.1:8000)

- 需要在variables变量中注册，注册后可以在变量定义的下方，使用$变量进行调用
- 作用域为当前yaml文件，变量定义的下方，不能跨yaml文件进行调用
```yaml
config:
  name: "这是测试报告"
  verify: False
	base_url: http://127.0.0.1:8000
	variables:
		base_url: $base_url
```
<a name="FClmg"></a>
### 定义接口的配置信息
请求参与名称与requests模块完全兼容

- method指定当前接口的请求方法名称，不区分大小写,推荐最好使用大写
   - 请求方法有：GET、POST、PUT、DELETE、PATCH
- headers指定请求头参数
- get方法传参可以使用params，也可以使用querystring
- post方法传参格式请求头使用data
   - json：application/json
   - form-data：application/x-www-form-urlencoded
```yaml
request:
		# 指定当前接口的url地址
		url: "${ENV(BASE_URL)}/user/login/"
    method: post
    headers:
      Content-Type: "application/x-www-form-urlencoded"
    body:
      username: 'LittleSeven'
      password: 'zm123456'
```
<a name="t4FNK"></a>
## 断言
validate指定断言，可以对测试用例在运行过程中是否得到了预期结果进行校验，校验内容包含了 4 个字段，分别是字段提取表达式、断言函数、预期结果以及提示信息

- 断言类型：支持 jmespath 表达式和正则表达式（regex）两种提取方式
- 断言函数：lt、le、gt、ge、ne等等，具体可以在httprunner.utils_test.TestUtils.test_validators中查询到
- 预期结果：方括号中，第一个参数为实际值，第二个参数为期望值
   - 实际值：status_code（响应状态码）, cookies, headers（响应头）,content（响应体数据）, text（响应体数据）, json（响应体数据）
   - 实际值提取方式：
      - 使用实际值加上“.”运算加上key，就能获取到相应值
      - 使用content.key如果提取的结果为列表，可以使用列表中的数字索引来进行提取
```yaml
validate:
  - eq: ["status_code", 200]
  - check: status_code
    assert: eq
    expect: 200
```
<a name="J2Qq1"></a>
## 控制台输出测试报告

- hrun yaml用例（json用例）文件的绝对路径或者相对路径（推荐） 其他参数
- 使用 hrp run 执行接口测试时，我们可以通过添加启动参数 --gen-html-report 在当前项目根目录的 reports 中生成一份 HTML 格式的测试报告。测试报告的输出名称为：report-unix时间戳。

![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1678628329881-2dcd19db-30df-423f-9a4f-ef67abef073d.png#averageHue=%23a9f72e&clientId=u6b5d84c6-16c8-4&from=paste&height=286&id=u9b2391c8&originHeight=571&originWidth=1088&originalType=binary&ratio=2&rotation=0&showTitle=false&size=75344&status=done&style=none&taskId=ubf6a40f0-fad2-4b01-b267-5ba521280c7&title=&width=544)
```yaml
-g, --gen-html-report       generate html report 获取测试报告，会指定在

hrp run /Users/z.m/pythonProject/Demo_one/demo/testcases/get_project_list.yaml --gen-html-report 
```
<a name="dsdbG"></a>
# 实现接口的关联
场景：要先登录才能狗查询项目详情，对于这种前一个接口的出参时候一个接口的入参数据，做接口测试时，需要使用接口的数据关联
<a name="BP10F"></a>
## yml测试用例的关联

- 使用extract关键字对响应数据进行提取，必须是在当前api的测试用例内进行提取
   - 若响应结果为json结构，支持jmepath表达式
   - 若响应结果为text/html格式，也支持使用正则表达式提取目标参数
- 被依赖的接口使用export导出目标参数，可以在当前用例内config全局变量配置，或者依赖步骤内进行添加
- 依赖接口使用前需使用variables对变量进行接收
**测试用例**```yaml
config:
  name: "获取登录token"
  verify: False
  variables:
    base_url: "${ENV(BASE_URL)}"
#  export:
#    - token

teststeps:
  - name: '获取登录token'
    request:
      method: POST
      headers:
#        Content-Type: "application/x-www-form-urlencoded"
        Accept: "application/json"
      url: "${ENV(BASE_URL)}/user/login/"
      body:
        username: "LittleSeven"
        password: "zm123456"
    validate:
      - eq: ["status_code", 200]
    extract:
      token: body.access
      status_code: status_code
```
```yaml
config:
  name: "获取项目信息"
  verify: False
  variables:
    base_url: "${ENV(BASE_URL)}"


teststeps:
  - name: '获取项目信息'
    request:
      method: GET
      headers:
#        Content-Type: "application/x-www-form-urlencoded"
        Accept: "application/json"
        Authorization: "Bearer $token"
      url: "${ENV(BASE_URL)}/projects/"
      params:
        size: 3
        page: 2
    validate:
      - eq: ["status_code", 200]
      - check: status_code
        assert: eq
        expect: 200

```
```yaml
# 指定用例的全局配置信息
config:
  name: "demo testcase"

teststeps:
  -
    name: '先获取登录token'
    testcase:  "api/login_demo.yml_testcase"
    extract:
      token: body.access
    export:
      - token
    validate:
      - eq: [ "status_code", 200 ]

  -
    name: '获取项目详情数据'
#    variables:
#      token: $token
    testcase: "api/projects_list_api.yml_testcase"

```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1679145687537-c1408888-5163-4ea3-8ef0-1cb1b996fb2d.png#averageHue=%23a99d20&clientId=u8412b3d4-d707-4&from=paste&height=528&id=ucc646f80&originHeight=1055&originWidth=1920&originalType=binary&ratio=2&rotation=0&showTitle=false&size=341494&status=done&style=none&taskId=u310b7787-b602-4e01-be6b-f3be3a4fc31&title=&width=960)<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1679145770931-858b9f6c-c0fd-406f-9cae-9854f8fe4bb2.png#averageHue=%23373733&clientId=u8412b3d4-d707-4&from=paste&height=528&id=ub7891711&originHeight=1055&originWidth=1920&originalType=binary&ratio=2&rotation=0&showTitle=false&size=187612&status=done&style=none&taskId=u9a6a2d39-c0ab-4767-8995-02fd1fb2d34&title=&width=960)

<a name="Ozo2b"></a>
# 柠檬班pytest-testreport
<a name="BBnGF"></a>
## 安装方式

- unittestreport是基于python3.6开发的，安装前请确认你的python版本>3.6
```yaml
pip install pytest-testreport
```
<a name="Y516t"></a>
## HTML测试报告生成
通过主函数中参数，来自定义输出测试报告内容，

- **suites: 测试套件（必传）**
- **filename: 指定报告文件名**
- **report_dir:指定存放报告路径**
- **title:指定测试报告的标题**
- **templates: 可以指定1，2，3三个风格的模板**
- **tester:测试人员名称**

![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1679147501865-ab20d3e4-a4d1-4b58-b5b5-da0c2d6de19b.png#averageHue=%23fefdfc&clientId=u8412b3d4-d707-4&from=paste&height=218&id=ucd95077e&originHeight=899&originWidth=1847&originalType=binary&ratio=2&rotation=0&showTitle=false&size=122923&status=done&style=none&taskId=u21feb0de-46a7-44ac-b18f-c99b79c6bf3&title=&width=448.5)![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1679147515275-8909e14c-db05-4f99-8a46-3ce69fee2ccf.png#averageHue=%230c165a&clientId=u8412b3d4-d707-4&from=paste&height=223&id=ucb1d5e39&originHeight=845&originWidth=1891&originalType=binary&ratio=2&rotation=0&showTitle=false&size=684481&status=done&style=none&taskId=u97b0a1b9-ab95-4d8a-aaf8-b4d637cbc72&title=&width=499.5)
```yaml
import pytest

pytest.main(['--report=musen.html',
             '--title=测试报告标题',
             '--tester=木森',
             '--desc=报告描述信息',
             '--template=2'])
```
<a name="MIhD5"></a>
# 测试用例运行调试
两者的区别再报告播件选择时配置不同分 别使用不同的测试报告。
<a name="XS6el"></a>
## 命令行运行
main debug.py文件通过命令行的方式入参调用HR4框架内部api完成测试用例加载和执行操作
```yaml
# 命令行运行方法
python main-debug.py hrp run demo\testcases\demo_get.yml --html=reports/repost.html --self-contained-html
```
```yaml
#!/usr/bin/env python
# -*- coding=utf-8 -*-
 
import sys
from httprunner.cli import main
 
cmd = sys.argv.pop(1)
if cmd in ["hrp", "httprunner", "ate"]:
    main()
```
<a name="r5PRm"></a>
## 主函数运行
run_test.py 提前定义数据后再调 用HR4框架内部的apl完成便用例的加载和执行操作，
```yaml
#!/usr/bin/env python
# -*- coding=utf-8 -*-
 
from httprunner.cli import main_run
if __name__ == '__main__':
    # 可直接运行，如果想定位问题，可直接debug模式运行
    main_run(["demo/testcases/demo_get.yml",  # case路径
              '-v',
              # '-s',
              '--report=testReport.html',
              '--title=自动化报告标题',
              '--tester=测试部分',
              '--desc=报告描述信息',
              '--template=2'])
```
<a name="DoijU"></a>
# HttpRunner 4 源码解析
```yaml
│  xx_test.py   # 单元测试用例，用于测试源码功能
│  cli.py       # 命令集封装
│  client.py    # request封装，网络请求client
│  compat.py    # 用例适配，处理testcase格式v2和v3之间的兼容性问题。
│  config.py    # 数据库、Thrift 配置文件
│  exceptions.py  # 自定义异常，主要继承了Excepetion类，可以根据自己需求重写
│  loader.py    # 加载用例设计文件JSON/YAML、环境变量、参数化，生成model定义的测试数据
│  make.py      # 依据测试数据生产pytest测试文件，并格式化生成的python代码
│  models.py    # pydantic 数据模型定义
│  parser.py    # 参数解析器，解析用例当中引用变量、自定义方法等
│  response.py  # 响应内容处理：断言、变量提取
│  runner.py    # 执行/启动器
│  step.py      # 测试步骤方法定义
│  step_request.py      # hook 测试用例参数和响应
│  step_sql_request.py  # sql 测试用例
│  step_testcase.py     # 测试用例对象封装
│  step_thrift_request.py    # thrift 测试用例，不支持Windows
│  utils.py     # 工具类
│  __init__.py  # 初始化文件，指定httprunner库包含的模块
│  __main__.py  # httprunner命令入库，调用cli.py的main函数
│
├─app     # 网络服务模块
│  │  main.py
│  │  __init__.py
│  │
│  └─routers
│     │  debug.py
│     │  debugtalk.py
│     │  deps.py
│     └─__init__.py
│
├─builtin  # 内置方法、校验比较器，供YAML/JSON用例设计文件中testcases使用
│  │  comparators.py
│  │  functions.py
│  └─__init__.py
│
└─ext  # 扩展功能
   │  __init__.py
   │
   ├─har2case     # har 文件 转 httprunner测试用例文件
   │  │  core.py
   │  │  utils.py
   │  └─__init__.py
   │
   ├─locust      # 性能测试相关
   │  │  locustfile.py
   │  └─__init__.py
   │
   └─uploader  # 文件上传
      │
      └─__init__.py
```
<a name="Jummr"></a>
# 框架运行流程图
![image.png](https://cdn.nlark.com/yuque/0/2023/png/32625797/1679152083715-b0161d16-3278-414e-b6c6-f8a6086db566.png#averageHue=%23f8f8f8&clientId=u8412b3d4-d707-4&from=paste&height=581&id=ucbe1a44d&originHeight=787&originWidth=752&originalType=binary&ratio=2&rotation=0&showTitle=false&size=37809&status=done&style=none&taskId=u2dde63a5-ba67-42a2-a844-ca1dcc71f17&title=&width=555)
