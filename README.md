## 本套UI(接口)自动化测试框架特点纪要：
* 使用环境建议为Windows系统；
* 支持多线程、单线程运行测试用例；
* 运行runner.py会自动生成HTML和excel形式的测试报告，其中HTML支持在线预览或者远程预览，并且会发送邮件；
* 程序在运行时会自动产生对应的log日志，可在log文件中查看对应日志；
* 支持定时任务执行整个测试用例，无需搭建Jenkins、数据库；
* 浏览器启动为setUpClass，浏览器关闭为tearDownClass；
* 每条用例测试结果记录在tearDown中，非跳过用例，如在tearDown之前出现errors那在测试报告中不会体现，但会在控制台中体现出来；
* 支持接口依赖调用并在测试报告中体现；
* 为更好的使用本套测试框架建议使用python3.7+；
* 在线预览HTML测试报告时，需启动HTMLReport;
* 支持上一条用例因失败、错误、预期失败、跳过时跳过该用例方法；
* 注意：此框架不适用于入门级！不然你会弄的一脸懵逼。

## 需安装第三方依赖包如下：
* 接口辅助测试包：requests；
* 上传附件测试包：pykeyboard；
* 图像处理包：pillow；
* 配置文件处理包：ConfigParameter；
* 浏览器驱动程序：selenium；
* 测试报告处理包：bottle、xlsxwriter；
* 处理yaml数据包：yaml；
* 读取当前运行用例计算配置信息包：wmi；
* 日志处理包：logging；
* 发送邮件处理包：smtplib；
* 定时任务处理包：schedule；
* 断言判断包：operator

## HTML测试报告效果图：
![image-text](https://github.com/houc/UI/blob/dev/img/TestReportHtml.jpeg)

## EXCEL测试报告效果图：
![image-text](https://github.com/houc/UI/blob/dev/img/ExcelTestRport.jpeg)

## 发送邮件效果图：
![image-text](https://github.com/houc/UI/blob/dev/img/Email.jpeg)

## 如有疑问可咨询(也可技术分享)：
![image-text](https://github.com/houc/UI/blob/dev/img/Welcome.jpeg)

## 开源不易感谢支持,不定期更新与优化：
![image-text](https://github.com/houc/UI/blob/dev/img/Cash.jpeg)
