**如果您还没有选这门课,快跑!**
# 2024.7.17 update2
- 一定程度上修复了guess词汇功能的表现,应该会更像自己猜的一点
- 圣诞颂歌之前生成的不太好,我重新整了一份完整的(毕竟这本书就一次小测,考全部)
- [bug]发现词汇生成随机性都不强,容易撞车,人多的话慎用
# 2024.7.17 update
- 增添了extra credits两本小说的quiz资料
- [bug]发现词汇生成的guess词汇功能容易被老师识别出是字典查的,正在重新训练,请勿使用

# 关于课程
- 本课程没有期末考试,得分由quiz,reading response,class participation决定,比例442,详见syllabus
- 2024暑假是第一次开课,任务量极大我每天除了上课还要花6个小时,大家写邮件反映后减了一本书(此时如果按照他的设定仍然要花4-5个小时),这个仓库会帮你把这个时间节约到1小时以内
  - 课外任务量就是读原著然后写reading response
  - 都比较冷门,没有很多书评和讨论参考
- **class participation(20)** : 本鼠鼠的弱项,乏善可陈
- **quiz(40)** : 总共十几次quiz,每次十几个题目,都是问情节,如果你答在点子上一个词就能拿分
  - 我的方法就是由大模型给我生成quiz的复习资料(文段大意+英文对照),然后过一遍(我没有花时间看英文原文)
- **reading response(40)** : 每节课一次,一般都能拿满
  - 生成/猜词直接生成(不要写太多,最后留10个就够了)
  - idea/question : 看完复习资料其实就知道小说内容了, 这里自己想就可以, 多写点废话以免太短(这一步千万不要用大模型的)
  - 大概把模版A4填满,就能拿满每次的25分
- **下面请看仓库↓↓↓**,脚本都调试好了,如有问题or需要帮助or希望补充一些资料请联系本人wx:15705694836
- 除了本仓库的功能外,其他可能有帮助的工具:
  - [txyz.ai](txyz.ai),支持pdf上传和手动提问的论文阅读网站
# 仓库简介
## /books 
书本epub,pdf版本(可能不全,懒得下载了,其实到处都是)
## /get-words
使用deepseek大模型API的读书脚本,主要功能包括
- 找生词并给出英英释义
- 找guess词汇并给出简短猜测
- 拆分文段并给出大意
- 自定义问问题(比如:用中文帮我理一下这本小说的人物和人际关系)
## /quiz prepare
- 本人自用的quiz准备(实际上我就是把大模型总结的小说大意过一遍)
- 2024-7-11 : 都生成完了
## /Reading Response
- 我自己写的reading response
## /syllabus
- 收录发邮件反馈前后的课程syllabus
# get-words脚本使用方法
- 首先把你当天的阅读内容从pdf中直接选中,拷到a.txt中,然后只需要在脚本中操作就行了
- ```get_words.py```只包含两种取词,功能不全,请你用```get_words.ipynb```
## 配置
- 如果您不会python
  - 如果您仅仅是辅助阅读,quiz prepare文件夹里我都生成好了
  - 如果您需要用脚本,请善用搜索进行vscode配置,python配置,其他python库的配置尤其是jupyter(当然可以用vscode的插件),虽然过程不复杂但是强烈建议直接抓个cs人帮您,也可以直接找我
- 如果您会python
  - 命令行运行
```
pip install openai
```
  - 对于```client = OpenA(api_key="???", base_url="https://api.deepseek.com")```
    - api_key是你的key,在https://platform.deepseek.com/usage 注册,氪个一块够了
## 使用
- 对于```main('a.txt', n, 'sample.json' , prompt1)```
  - a.txt是文本
  - sample.json是参考的回答样本(给大模型学习用的)
  - prompt是提示,修改要求的话改这里文字和sample.json里相应位置的文字就行
  - n是分割的段数,整数(我选择直接将文本分割,因为不管是取词还是总结大意都可以直接这样割)
  - 还有一个main2(),这个是不输入json样例直接对文本问问题的版本
- 写这一段是帮助你看懂和调整切片数,实际上逐次运行四个cell即可
  - 取词程序运行时长1min左右
  - quiz准备资料生成的时长取决于文本切片数n,每个不超过90s
## 各功能效果说明
- 找生词并给出英英释义: 这个很精准,直接将程序输出复制即可
- 找guess词汇并给出简短猜测: 有的时候猜的太准了,稍微改一下
- 填idea和question: 一眼ai,千万别用
- 总结小说大意: 给自己看的,无所谓 
