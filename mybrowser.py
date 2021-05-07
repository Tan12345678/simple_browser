import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class Mainwin(QMainWindow):
    def __init__(self):
        super(Mainwin,self).__init__()
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl('http://www.google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navbar
        navbar=QToolBar()
        self.addToolBar(navbar)

        back_btn=QAction('Back',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn=QAction('Forward',self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        refresh_btn=QAction('Refresh',self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)

        wiki=QAction('WIKI',self)
        wiki.triggered.connect(self.wiki_open)
        navbar.addAction(wiki)

        home=QAction('Home',self)
        home.triggered.connect(self.navigate_home)
        navbar.addAction(home)

        bing= QAction('BING', self)
        bing.triggered.connect(self.navigate_BING)
        navbar.addAction(bing)




        self.url_bar=QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)



    def navigate_home(self):
        self.browser.setUrl(QUrl('http://www.google.com'))

    def wiki_open(self):
        self.browser.setUrl(QUrl('http://www.wikipedia.com'))

    def navigate_BING(self):
        self.browser.setUrl(QUrl('http://www.bing.com'))


    def navigate_to_url(self):
        url=self.url_bar.text()
        self.browser.setUrl(QUrl(url))
    def update_url(self,q):
        self.url_bar.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName("Tan browser")
window=Mainwin()
app.exec_()

