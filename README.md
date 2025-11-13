## 데이터베이스 기반 인사정보 조회 프로그램 구현 (Python, Oracle)
-  Oracle과 python 연동 (oracledb)
-  부서 선택, 부서 위치 표시, 사원 정보 표시, 조회 버튼, 종료 버튼 GUI 구현 (PyQt5.QtWidgets)
-  QPushButton(Query)에 SQL JOIN 쿼리(emp e, emp m, dept d) 실행 함수 연결 (PyQt5.QtWidgets, PyQt5.QtCore)
-  프로그램 실행 시 dept 테이블 조회, QComboBox(부서)의 아이템 동적 생성
-  QComboBox(부서) 선택에 따라 QPushButton(Query) 클릭 시 QTextEdit(부서 위치) 및 QTableWidget(사원 정보)에 동적 결과 표시
