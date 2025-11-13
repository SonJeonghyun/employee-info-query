import sys
import oracledb
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import Qt

# 데이터베이스 연결 함수
def connectDB():
   dsn = " " # 접속할 db명
   user = " "           # 접속할 db의 user명
   pw = " "             # 접속할 db의 password

   # DB에 접속
   conn = oracledb.connect(user = user, password = pw, dsn=dsn)
   return(conn) 

# 데이터베이스 연결 해제 함수
def disconnectDB(conn): 
    conn.close() 

class MyApp(QWidget):
   def __init__(self):
      super().__init__()
      self.initUI()

   # UI 디자인 함수
   def initUI(self):
      label1 = QLabel('부서명 선택')
      self.dname = QComboBox() 
      self.dname.setFixedWidth(200)
      self.dname.setFixedHeight(30)   
      self.text_loc = QTextEdit()
      self.text_loc.setFixedWidth(100)
      self.text_loc.setFixedHeight(30)
      
      # QComboBox에 부서목록 입력
      sql = "SELECT dname \
      FROM dept " 

      conn = connectDB()
      curs = conn.cursor()
      curs.execute(sql)

      cname = curs.fetchone()
      while(cname):
         self.dname.addItem(cname[0])
         cname = curs.fetchone()

      curs.close()
      disconnectDB(conn)

      btn_1 = QPushButton('Query')
      btn_1.clicked.connect(self.btn_1_clicked)

      btn_2 = QPushButton('Exit', self)
      btn_2.clicked.connect(self.close) 
      btn_2.clicked.connect(QCoreApplication.instance().quit) 

      self.emp_info = QTableWidget()
      self.emp_info.setFixedWidth(350)

      # UI 배치
      gbox = QGridLayout()
      dlBox = QHBoxLayout()
      dlBox.addWidget(self.dname)
      dlBox.addWidget(self.text_loc)

      gbox.addWidget(label1, 0, 0)
      gbox.addLayout(dlBox, 0, 1)
      gbox.addWidget(btn_1, 0, 3)
      gbox.addWidget(btn_2, 1, 3)
      gbox.addWidget(self.emp_info, 1, 1)   
      
      self.setLayout(gbox)
      self.setWindowTitle('Employee Info')
      self.setGeometry(300,300, 550,300)
      self.show()

   # 버튼 클릭 시 처리 함수
   def btn_1_clicked(self):
      self.emp_info.clearContents()            
       
      dept_name = self.dname.currentText()

      # SQL JOIN 쿼리
      sql = "SELECT e.empno, e.ename, e.job, e.sal, m.ename, loc\
      FROM emp e , emp m, dept d \
      WHERE e.mgr = m.empno \
      And e.deptno = d.deptno \
      AND dname = :var1" 

      conn = connectDB()
      curs = conn.cursor()
      curs.execute(sql, var1=dept_name)

      self.emp_info.setColumnCount(5)
      self.emp_info.setHorizontalHeaderItem(0, 
                     QTableWidgetItem("사원번호"))
      self.emp_info.setHorizontalHeaderItem(1, 
                     QTableWidgetItem("사원이름"))
      self.emp_info.setHorizontalHeaderItem(2, 
                     QTableWidgetItem("담당업무"))
      self.emp_info.setHorizontalHeaderItem(3, 
                     QTableWidgetItem("급여"))
      self.emp_info.setHorizontalHeaderItem(4, 
                     QTableWidgetItem("매니저이름"))

      result = curs.fetchone()
      i = 0                       
      while(result):
         rowPosition = self.emp_info.rowCount()
         self.emp_info.insertRow(rowPosition)

         pop = QTableWidgetItem(str(result[0])) 
         pop.setTextAlignment(Qt.AlignRight) 
         self.emp_info.setItem(i, 0, pop)

         self.emp_info.setItem(i, 1, QTableWidgetItem(result[1]))
         
         self.emp_info.setItem(i, 2, QTableWidgetItem(result[2]))

         pop = QTableWidgetItem(str(result[3]))
         pop.setTextAlignment(Qt.AlignRight) 
         self.emp_info.setItem(i, 3, pop)

         self.emp_info.setItem(i, 4, QTableWidgetItem(result[4]))

         self.text_loc.setText(result[5])

       
         result = curs.fetchone()
         i = i+1

      curs.close()
      disconnectDB(conn)

# 프로그램 실행 
if (__name__ == '__main__'):
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())