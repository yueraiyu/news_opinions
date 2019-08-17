# news opinions

### 2019/08/04
1. 初始化工程

2. 项目模块化，不同领域模型放在不同包中
  
    * `conf` : 存放项目配置文件相关，现在只是通过`flask`加载了，具体还未设置
    * `app/db`:存放数据库相关操作，可能涉及`CRUD`的简单操作，也可能涉及查询结果集到`model`的绑定
    * `app/models`:存放实体，比如`User`、`News`、`Opinions`等
    * `app/services`:具体业务逻辑操作
    * `app/routes`:用户请求到`server`后，请求转发及结果返回，不涉及业务逻辑操作
    * `utils`:常用工具集，比如日期转换、异常捕捉等
    
3. 添加测试模块`test`，编写程序过程中涉及大量本地调试，如果用main()函数测试容易导致程序混乱，添加`unittest`辅助测试

4. 前端资源文件

    * static:前端静态资源文件
      * img:图片、ico等
      * css:页面样式
      * js:页面动作
    * templates
      * Error:统一存放错误展示页面

5. 项目缺少部分

    * DB为配置
    * 日志未配置
    * 前端考虑要不要用flask的模版语言来处理，似乎可以解释，Vue是否要引入？

    

### 计划

1. 任务安排分配
   * 用github的wiki，添加新功能和设计
   * 用github的issues，添加功能bug
2. 项目统一提交到develop分支，每个人在自己本地环境创建分支订阅develop，正式且无任何bug代码才合并到master分支

### 2019/08/17

项目重构，针对`python` `flask` `Jinja2` 模版语言需要服务器渲染，页面展示效果不好，而且之前项目结构不太灵活，将项目改为前后端分离，引入`Vue`。

1. 项目结构说明
   * `backend`:后端代码
     * `app`
       * `api`:路由请求
       * `database`:数据库模型
       * `models`:算法模型
       * `utils:部分工具`
   * `frontend`:前端代码
2. 项目启动说明
   * `backend`
     * `step1`:进入后端代码，执行命令`cd backend`
     * `step2`:创建虚拟环境，执行命令`python -m venv venv `
     * `step3`:进入虚拟环境，执行命令`source venv/bin/activate `
     * `step4`:安装相关依赖，执行命令`pip install -r requirements.txt `
     * `step5`:运行后端服务，执行命令`flask run`
   * `frontend`:确保安装了`node` 
     * `step1`:`cd frontend`
     * `step2`:`npm instal`
     * `step3`:`npm run dev` or `npm run build`