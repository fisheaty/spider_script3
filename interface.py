# -*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtWebKit import *


app = QApplication([])
webview = QWebView()
loop = QEventLoop()
webview.loadFinished.connect(loop.quit)
webview.load(QUrl('http://example.webscraping.com/search'))
loop.exec_()
webview.show()
frame = webview.page().mainFrame()
frame.findFirstElement('#search_term').setAttribute('value', '.')
frame.findFirstElement('#page_size option[selected=""]').setPlainText('1000')
frame.findFirstElement('#search').evaluateJavaScript('this.click()')

elements = None
while not elements:
	app.processEvents()
	elements = frame.findAllElements('#results a')
countries = [e.toPlainText().strip() for e in elements]
print countries