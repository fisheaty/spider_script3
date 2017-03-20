#--coding:utf-8 --*
from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtWebKit import *
import lxml.html

import json
from download import download_agent as D

url = 'http://example.webscraping.com/dynamic'
html = D(url)
tree = lxml.html.fromstring(html)
tree.cssselect('#result')[0].text_content()

app = QApplication([]) 
#初始化QApplication对象

webview = QWebView() 
#Web 文档容器

loop = QEventLoop() 
#创建QEventLoop()对象，该对象用于创建本地事件循环

webview.loadFinished.connect(loop.quit) 
#网页加载完成之后停止事件循环

webview.load(QUrl(url)) 
#将要加载的URL传给QWebView 
#PyQt必须讲URL字符串封装在QUrl对象当中，而PySide则是可选项

loop.exec_() 
#QWebView的加载方法是异步的，这一步是等待网页加载完成

html = webview.page().mainFrame().toHtml() 
#对加载的网页html进行抽取

tree = lxml.html.fromstring(html)
print tree.cssselect('#result')[0].text_content()