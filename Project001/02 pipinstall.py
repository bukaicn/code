#pipinstall.py
import os
libs=[
      '''
      自定义注释参数：0:已安装，推荐程度1，2，3……。

      爬虫与信息提取：
      "PyQt6",#1，Qt开发框架的Python接口
      "Requests",#0，最友好的网络爬虫功能库
      
      数据分析处理：
      "Numpy",#1，表达N维数组的最基础库
      "Pandas",#Python数据分析高层次应用库
      "SciPy",#数学、科学和工程计算功能库

      数据可视化:
      "Matplotlib",#高质量的二维数据可视化功能库
      "Seaborn",#统计类数据可视化功能库-调用时略为简单
      "Mayavi",#三维科学数据可视化功能库
    
      文本处理:
      "PyPDF2",#处理pdf文件的工具集
      "NLTK",#自然语言文本处理
      "python-docx",#创建或更新Microsoft Word文件
      
      机器学习
      "Scikit-learn",#机器学习方法工具集
      "TensorFlow",#AlphaGo背后的机器学习计算框架
      "MXNet",#基于神经网络的深度学习计算框架

      "pyinstaller",#2，打包成exe
      "wordcloud",#1，词云展示
      "os",#0,操作系统小功能
      "flake8",#0,提升代码质量，确保代码风格的一致性和正确性
      "yapf",#0,提升代码质量，确保代码风格的一致性和正确性
      '''
      "jieba",#0，中文分词
        ]
try:
    for lib in libs:
        os.system("pip install --upgrade "+lib)
    print("Successful")
except:
    print("Failed Somehow")