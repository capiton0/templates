

<h1 align="center">Templates</h1>

> 基于nuclei的自动化渗透模板。

1.根据构建的指纹库，对目标进行指纹识别。

2.根据workflow + tags 进行 指纹识别后的漏洞扫描，降低扫描过程中的请求量。

3.根据API进行资产搜集——包括端口提取、子域名获取。（需要api秘钥）

4.更新nuclei 国内组件漏洞库模板


🏠[模板使用文档](https://www.yuque.com/yuxin_0/nuclei/)  ⬇️[nuclei下载地址](https://github.com/projectdiscovery/nuclei/releases)


> 注意：仓库内主要为基于nuclei模板语法构建的自动化渗透模板 + nuclei官方社区的模板，每次nuclei官方社区发布最新版本后，将自动打包至此仓库。

nuclei官方模板版本：
<a href="https://github.com/projectdiscovery/nuclei-templates/releases"><img src="https://img.shields.io/github/release/projectdiscovery/nuclei-templates"></a>
## 🚀 快速使用
### 一、安装
    git clone https://github.com/capiton0/nuclei
下载仓库模板，替换nuclei-templates目录

或

移动 `0.local/` `1.other/`文件夹 至 nuclei-templates 目录

---
### 二、运行
1. 基于指纹识别的漏洞扫描
    
    ```bash
    nuclei -w ~/nuclei-templates/0.local/scan/finger-scan.yaml -u http://example.com 
    ```

2. 快速进行指纹识别
    
    ```bash
    nuclei -id finger-index -u http://example.com 
    ```
    或
    ```bash
    nuclei -t ~/nuclei-templates/0.local/finger/finger-index.yaml -u http://example.com 
    ```

其他用法请阅读文档： https://www.yuque.com/yuxin_0/templates/
