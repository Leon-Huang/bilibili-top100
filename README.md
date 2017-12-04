# bilibili-top100 视频地址爬取

Bilibili Top100 示例页面：https://www.bilibili.com/ranking?spm_id_from=333.334.ranking_douga.8#!/all/0/1/3/

## 依赖包：
1. beautifulsoap
```
pip install bs4
```
2. selenium
```
pip install selenium
```
3. 浏览器对应的Driver，参见http://selenium-python.readthedocs.io/installation.html

下载 Driver 后，把可执行文件丢到系统路径中，如`/usr/local/bin`保证能正常调用该驱动

在命令行下直接输入`chromedriver`(以chrome 浏览器访问 bilibili.com 为例，如果使用其他浏览器请自行更换文件名）

正确响应如下：

```
a123@MBP:~$ chromedriver
Starting ChromeDriver 2.33.506106 (8a06c39c4582fbfbab6966dbb1c38a9173bfb1a2) on port 9515
Only local connections are allowed.

# OK，CTRL+C to quit
```

4. 代码中只抓取了：『鬼畜』『游戏』『音乐』『舞蹈』这四个栏目

5. 运行
```
python3 bilibili.py
```

