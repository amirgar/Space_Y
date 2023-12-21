# -*- coding: utf-8 -*-

"""
Для установки PyQt5:
>> pip install PyQt5
Для установки Wikipedia:
>> pip install wikipedia
Для установки Skyfield.api:
>> pip install skyfield
"""

import sqlite3  # подключён для работы с базой данных
import wikipedia  # подключен для вывода пользователю краткой информации
from PyQt5 import (
    QtCore,
    QtGui,
    QtWidgets,
)  # подключён для создания приложения, его графического интерфейса
from skyfield.api import (
    load,
    Topos,
)  # подключен для вывода пользователю точной информации  о местоположении кос. объекта

# data base
db = sqlite3.connect("star_grp.db")  # создание файла базы данных
cursor = db.cursor()  # создание инструмента для работы с базой данных
cursor.execute(
    """CREATE TABLE IF NOT EXISTS star_group( 
    title text
    )"""
)  # создание таблицы
db.commit()

# создание элементов
cursor.execute("INSERT INTO star_group VALUES ('Андормеда')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Близнецы')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Большая медведица')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Весы')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Большой пес')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Водолей')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Возничий')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Волк')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Волопас')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Волосы Вероники')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Ворон')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Геркулес')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Гидра')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Голубь')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Гончие псы')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Дева')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Дельфин')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Дракон')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Единорог')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Жертвенник')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Живописец')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Жираф')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Заяц')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Ворон')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Змееносец')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Змея')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Золотая рыба')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Индеец')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Кассиопея')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Кентавр')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Киль')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Кит')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Козерог')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Компас')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Корма')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Лебедь')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Лев')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Летучая рыба')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Лира')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Лисичка')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Малая медведица')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Малый конь')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Малый лев')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Малый пес')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Микроскоп')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Муха')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Насос')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Наугольник')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Овен')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Октант')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Орел')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Орион')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Павлин')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Паруса')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Пегас')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Персей')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Печь')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Райская птица')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Рак')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Резец')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Рыбы')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Рысь')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Северная корона')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Секстант')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Сетка')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Скорпион')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Скульптор')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Столовая гора')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Стрела')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Стрелец')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Телескоп')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Телец')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Треугольник')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Тукан')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Феникс')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Хамелеон')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Цефей')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Циркуль')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Часы')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Чаша')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Щит')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Эридан')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Южная гидра')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Южная Корона')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Южная рыба')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Южный крест')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Южный треугольник')")
db.commit()

cursor.execute("INSERT INTO star_group VALUES ('Ящерица')")
db.commit()

# Нужно для вывода бд
# cursor.execute("SELECT * FROM star_group")
# all_results = cursor.fetchall()
# print(all_results)

db.close()  # конец работы с базой данных


class Ui_MainWindow(object):
    # функция для поиска спутника
    def sputnik_search(self):
        text4 = " "
        text5 = " "
        az = 0
        db = "https://celestrak.com/NORAD/elements/active.txt"  # база данных модуля skyfield

        sputnik = self.sputnik_input.text()  # получение названия спутника

        satellites = load.tle(db)  # поиск названия спутника в бд
        t = load.timescale().now()  # получение времени
        # местоположение
        location = Topos("52.173141 N", "44.108612 E")
        # вычесление азимута, широты и высоты
        for sat in satellites.values():
            difference = sat - location
            topocentric = difference.at(t)
            alt, az, distance = topocentric.altaz()
            break

        # подготовка всех полученных данных для вычислений

        text2 = str(alt)
        s = 0
        for i in text2:
            s += 1
            if i == "d":
                break
            else:
                pass
        text2 = text2[0 : s - 1]
        az = str(az)
        az1 = az[0:4]
        if "d" and "e" in az1:
            az1 = az[0:2]
        if "d" in az1:
            az1 = az[0:3]

        # Вычисление местоположения спутника

        c = int(az1)
        if 25 > c >= 0:
            text4 = "Спутник на севере"
        if 25 <= c < 90:
            text4 = "Спутник на северо-востоке"
        if 115 > c >= 90:
            text4 = "Спутник на востоке"
        if 1515 < c <= 180:
            text4 = "Спутник на юго-востоке"
        if 205 > c > 180:
            text4 = "Спутник на юге"
        if 205 < c <= 270:
            text4 = "Спутник на юго-западе"
        if 295 > c >= 270:
            text4 = "Спутник на севере"
        if 295 < c <= 360:
            text4 = "Спутник на севере"

        # Вычисления возможности видимости спутника на данный момент

        alt = str(alt)
        a1t = alt[0:3]
        if "d" in az1:
            a1t = alt[0:2]
        if alt[0] == "-":
            text5 = "На данный момент спутник не виден."
        c = int(az1)
        if 0 <= c <= 10:
            text5 = "Вы можете посмотреть спутник ровно на горизонте."
        elif 10 < c <= 80:
            text5 = "Вы можете разглядеть на небе спутник в данный момент."
        elif 80 < c <= 90:
            text5 = "Спутник находится прямо над вами!"

        # Вывод результата

        text_i = "Высота: {}, {}, азимут:{},{}".format(text2, text4, az1, text5)
        self.sputnik_res.setText(text_i)

    # Поиск информации в разделе Энциклопедия

    def get_information(self):
        """ВНИМАНИЕ! Данный раздел работает только при подключении к интернету,
        потому что Wikipedia может работать только с подключением к интернету."""
        # Получение названия объекта
        text = self.enc_input.text()
        # Выбор языка
        wikipedia.set_lang("ru")
        # Поиск информации в бд Википедии
        text0 = wikipedia.summary(text, sentences=2)
        # форматирования результатов
        text0 = (
            text0[:80]
            + "\n"
            + text0[80:160]
            + "\n"
            + text0[160:240]
            + "\n"
            + text0[240:320]
            + "\n"
            + text0[400:480]
            + "\n"
            + text0[480:560]
            + "\n"
            + text0[560:]
        )
        # вывод
        self.enc_res.setText(text0)

    # Поиск звёзд
    def star_search1(self):
        """В будущих обнавлениях список звёзд будет пополняться"""
        # звёзды в северном полушарии
        self.sev_star = ["Солнце", "Сириус", "Канопус", "Ригель", "Ахернар"]
        # звёзды в южном полушарии
        self.ug_star = ["Арктур", "Бетельгейзе", "Вега", "Капелла", "Процион"]
        # ввод информации
        text = self.star_input.text()
        # проверка, вывод информации
        if text in self.sev_star:
            self.sta_res.setText("Звезда находится в северном полушарии")
        elif text in self.ug_star:
            self.sta_res.setText("Звезда находится в южном полушарии")
        else:
            self.sta_res.setText(
                "Звезда либо не существует, либо недоступна на данный момент"
            )

    def galaxy_search(self):
        user_input = self.galaxy_input.text()
        # Получение названия объекта
        # Выбор языка
        wikipedia.set_lang("ru")
        # Поиск информации в бд Википедии
        text0 = wikipedia.summary(user_input + " созвездие", sentences=5)
        # форматирования результатов
        text0 = (
            text0[:80]
            + "\n"
            + text0[80:160]
            + "\n"
            + text0[160:240]
            + "\n"
            + text0[240:320]
            + "\n"
            + text0[400:480]
            + "\n"
            + text0[480:560]
            + "\n"
            + text0[560:640]
            + text0[640:720]
            + text0[720:800]
            + text0[800:]
        )
        db = sqlite3.connect("star_grp.db")  # создание файла базы данных
        cursor = db.cursor()
        info = cursor.execute("SELECT * FROM star_group WHERE title=?",
                              (user_input,))
        if info.fetchone() is None:
            self.galaxy_res.setText(
                "Данного созвездия не существует! Проверьте правильность "
                "ввода!"
            )
        else:
            self.galaxy_res.setText("Созвездие: {} \n {}".format(user_input,
                                                                 text0))

    # создание приложения
    def setupUi(self, MainWindow):
        # создание окна
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 470)
        MainWindow.setMouseTracking(False)
        # создание иконки приложения
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap('unnamed.jpg'), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        # центрирование объектов
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # создание меню приложения
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 791, 471))
        self.tabWidget.setObjectName("tabWidget")
        # создание раздела стартовая страница
        self.Start_Page = QtWidgets.QWidget()
        self.Start_Page.setObjectName("Start_Page")
        self.Calendar = QtWidgets.QCalendarWidget(self.Start_Page)
        self.Calendar.setGeometry(QtCore.QRect(411, 10, 361, 221))
        self.Calendar.setObjectName("Calendar")
        self.Space__STARTPAGE = QtWidgets.QLabel(self.Start_Page)
        self.Space__STARTPAGE.setGeometry(QtCore.QRect(100, 270, 601, 121))
        self.Space__STARTPAGE.setText("")
        self.Space__STARTPAGE.setPixmap(QtGui.QPixmap("unnamed.jpg"))
        self.Space__STARTPAGE.setObjectName("Space__STARTPAGE")
        self.Space_y_new_era = QtWidgets.QLabel(self.Start_Page)
        self.Space_y_new_era.setGeometry(QtCore.QRect(40, 30, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(12)
        self.Space_y_new_era.setFont(font)
        self.Space_y_new_era.setStyleSheet("color: rgb(87, 118, 255);")
        self.Space_y_new_era.setObjectName("Space_y_new_era")
        self.what_new = QtWidgets.QLabel(self.Start_Page)
        self.what_new.setGeometry(QtCore.QRect(40, 80, 351, 131))
        self.what_new.setObjectName("what_new")
        self.tabWidget.addTab(self.Start_Page, "")
        # создание раздела Энциклопедия
        self.Encyclopedia = QtWidgets.QWidget()
        self.Encyclopedia.setObjectName("Encyclopedia")
        self.space_y_enc = QtWidgets.QLabel(self.Encyclopedia)
        self.space_y_enc.setGeometry(QtCore.QRect(110, 10, 591, 131))
        self.space_y_enc.setText("")
        self.space_y_enc.setPixmap(QtGui.QPixmap("../unnamed.jpg"))
        self.space_y_enc.setObjectName("space_y_enc")
        self.search_information = QtWidgets.QPushButton(self.Encyclopedia)
        self.search_information.setGeometry(QtCore.QRect(500, 170, 201, 61))
        self.search_information.setObjectName("search_information")
        self.search_information.clicked.connect(self.get_information)
        self.enc_res = QtWidgets.QLabel(self.Encyclopedia)
        self.enc_res.setGeometry(QtCore.QRect(90, 252, 621, 121))
        self.enc_res.setText("")
        self.enc_res.setObjectName("enc_res")
        self.enc_input = QtWidgets.QLineEdit(self.Encyclopedia)
        self.enc_input.setGeometry(QtCore.QRect(110, 170, 371, 61))
        self.enc_input.setObjectName("enc_input")
        self.tabWidget.addTab(self.Encyclopedia, "")
        # создание раздела Поиск спутника
        self.Sputnik_search = QtWidgets.QWidget()
        self.Sputnik_search.setObjectName("Sputnik_search")
        self.sputnik_space_y = QtWidgets.QLabel(self.Sputnik_search)
        self.sputnik_space_y.setGeometry(QtCore.QRect(110, 10, 591, 131))
        self.sputnik_space_y.setText("")
        self.sputnik_space_y.setPixmap(QtGui.QPixmap("unnamed.jpg"))
        self.sputnik_space_y.setObjectName("sputnik_space_y")
        self.Sputnik_Searc = QtWidgets.QPushButton(self.Sputnik_search)
        self.Sputnik_Searc.setGeometry(QtCore.QRect(500, 160, 201, 61))
        self.Sputnik_Searc.setObjectName("Sputnik_Searc")
        self.sputnik_res = QtWidgets.QLabel(self.Sputnik_search)
        self.sputnik_res.setGeometry(QtCore.QRect(100, 250, 611, 141))
        self.sputnik_res.setText("")
        self.sputnik_res.setObjectName("sputnik_res")
        self.sputnik_input = QtWidgets.QLineEdit(self.Sputnik_search)
        self.sputnik_input.setGeometry(QtCore.QRect(110, 160, 381, 61))
        self.sputnik_input.setObjectName("sputnik_input")
        self.Sputnik_Searc.clicked.connect(self.sputnik_search)
        self.tabWidget.addTab(self.Sputnik_search, "")
        # создание раздела Поиск звезды
        self.Star_search = QtWidgets.QWidget()
        self.Star_search.setObjectName("Star_search")
        self.star_space_y = QtWidgets.QLabel(self.Star_search)
        self.star_space_y.setGeometry(QtCore.QRect(90, 10, 591, 131))
        self.star_space_y.setText("")
        self.star_space_y.setPixmap(QtGui.QPixmap("unnamed.jpg"))
        self.star_space_y.setObjectName("star_space_y")
        self.star_search = QtWidgets.QPushButton(self.Star_search)
        self.star_search.setGeometry(QtCore.QRect(480, 160, 201, 61))
        self.star_search.setObjectName("star_search")
        self.star_search.clicked.connect(self.star_search1)
        self.star_input = QtWidgets.QLineEdit(self.Star_search)
        self.star_input.setGeometry(QtCore.QRect(90, 160, 381, 61))
        self.star_input.setObjectName("star_input")
        self.sta_res = QtWidgets.QLabel(self.Star_search)
        self.sta_res.setGeometry(QtCore.QRect(80, 240, 601, 111))
        self.sta_res.setText("")
        self.sta_res.setObjectName("sta_res")
        self.tabWidget.addTab(self.Star_search, "")
        # создание раздела Инструкции
        self.Instruction = QtWidgets.QWidget()
        self.Instruction.setObjectName("Instruction")
        self.ins_space_y = QtWidgets.QLabel(self.Instruction)
        self.ins_space_y.setGeometry(QtCore.QRect(110, 10, 591, 131))
        self.ins_space_y.setText("")
        self.ins_space_y.setPixmap(QtGui.QPixmap("unnamed.jpg"))
        self.ins_space_y.setObjectName("ins_space_y")
        self.instr = QtWidgets.QLabel(self.Instruction)
        self.instr.setGeometry(QtCore.QRect(90, 160, 661, 231))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.instr.setFont(font)
        self.instr.setObjectName("instr")
        self.tabWidget.addTab(self.Instruction, "")
        # Создание раздела о нас
        self.About_Us = QtWidgets.QWidget()
        self.About_Us.setObjectName("About_Us")
        self.abt_space_y = QtWidgets.QLabel(self.About_Us)
        self.abt_space_y.setGeometry(QtCore.QRect(120, 10, 571, 101))
        self.abt_space_y.setText("")
        self.abt_space_y.setPixmap(QtGui.QPixmap("unnamed.jpg"))
        self.abt_space_y.setObjectName("abt_space_y")
        self.abt_1 = QtWidgets.QLabel(self.About_Us)
        self.abt_1.setGeometry(QtCore.QRect(80, 150, 641, 91))
        self.abt_1.setObjectName("abt_1")
        self.abt_2 = QtWidgets.QLabel(self.About_Us)
        self.abt_2.setGeometry(QtCore.QRect(130, 240, 551, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.abt_2.setFont(font)
        self.abt_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.abt_2.setObjectName("abt_2")
        self.tabWidget.addTab(self.About_Us, " ")
        # создание раздела Созвездия
        self.Galaxy = QtWidgets.QWidget()
        self.Galaxy.setObjectName("Galaxy")
        self.tabWidget.addTab(self.Galaxy, "Galaxy")
        self.space_y_galaxy = QtWidgets.QLabel(self.Galaxy)
        self.space_y_galaxy.setGeometry(QtCore.QRect(110, 10, 591, 131))
        self.space_y_galaxy.setText("")
        self.space_y_galaxy.setPixmap(QtGui.QPixmap("unnamed.jpg"))
        self.space_y_galaxy.setObjectName("space_y_galaxy")
        self.search_galaxy = QtWidgets.QPushButton(self.Galaxy)
        self.search_galaxy.setGeometry(QtCore.QRect(500, 170, 201, 61))
        self.search_galaxy.setObjectName("search_galaxy")
        self.galaxy_input = QtWidgets.QLineEdit(self.Galaxy)
        self.galaxy_input.setGeometry(QtCore.QRect(110, 170, 371, 61))
        self.galaxy_input.setObjectName("galaxy_input")
        self.galaxy_res = QtWidgets.QLabel(self.Galaxy)
        self.galaxy_res.setGeometry(QtCore.QRect(80, 240, 601, 111))
        self.galaxy_res.setText("")
        self.galaxy_res.setObjectName("sta_res")
        self.search_galaxy.clicked.connect(self.galaxy_search)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # добавление текста в выше перечисленные разделы
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Space Y"))
        self.Space_y_new_era.setText(
            _translate("MainWindow", "Space Y - это новая"
                                     " эра любительской "
                                     "астрономии.")
        )
        self.what_new.setText(
            _translate(
                "MainWindow",
                "                                      В Space Y вы "
                "можете:\n"
                "   💫Узнать местоположение звёзд \n"
                "💫Узнать краткую информацию о планетах \n"
                " 💫Узнать местоположение звезды \n"
                " 💫Узнать местоположение спутника\n"
                "💫Узнать краткую информацию о космическом объекте \n"
                "                                      Последнее обновление:\n"
                " (04.04.22) v.2.5 Добавление раздела Galaxy, исправление "
                "багов\n"
                " (29.03.22) v.2.4 Улучшение интерфейса приложения, "
                "оптимизация",
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.Start_Page),
            _translate("MainWindow", "Start Page"),
        )
        self.search_information.setText(_translate("MainWindow",
                                                   "SEARCH INFORMATION!"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.Encyclopedia),
            _translate("MainWindow", "Encyclopedia"),
        )
        self.Sputnik_Searc.setText(_translate("MainWindow",
                                              "SPUTNIK SEARCH!"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.Sputnik_search),
            _translate("MainWindow", "Sputnik Search"),
        )
        self.star_search.setText(_translate("MainWindow",
                                            "STAR SEARCH!"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.Star_search),
            _translate("MainWindow", "Star Search!"),
        )
        self.instr.setText(
            _translate(
                "MainWindow",
                "                                                             "
                "                                         "
                "Инструкция\n"
                "                                                           "
                "                                    Для чайников в Space Y\n"
                " Start Page. Стартовая страница запускается при открытии "
                "приложения. Сверху появится меню.\n"
                " Sputnik Search! Вы вводите название спутника, немного "
                "подождав, вам выведится вся информация.\n"
                " Encyclopedia. Вводите название объекта, немного подождав, "
                "выводиться результат.\n"
                " Planet Search!. Вводите название планеты, неного подождав "
                "будет выведен результат.\n"
                " Galaxy. Вводите название созвездия, немного подождав будет "
                "выведен результат.",
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.Instruction),
            _translate("MainWindow", "Instruction"),
        )
        self.abt_1.setText(
            _translate(
                "MainWindow",
                "Разработчиком данного приложения является ученик 9 "
                "класса Лицея №78 г. Набережные Челны (Татарстан). Цель "
                "данного\n"
                "проекта - Создать приложение - помощник для астрономов - "
                "любителей, в котором пользователь сможет узнать краткую\n"
                " информацию о космическом объекте. "
                "Проект является победителем"
                " многих конференций республиканского и \n"
                "всероссийского уровня.\n"
                'В будущем планируется создать раздел "Планеты", в котором '
                'будет удобнее работать с данными о планетах.',
            )
        )
        self.abt_2.setText(
            _translate(
                "MainWindow",
                "ВСЕ ВАШИ ПОЖЕЛАНИЯ МОЖНО ОСТАВИТЬ ЗДЕСЬ: "
                "gareev05@internet.ru",
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.About_Us), _translate(
                "MainWindow", "About us")
        )
        self.search_galaxy.setText(_translate("MainWindow",
                                              "GALAXY SEARCH!"))


if __name__ == "__main__":
    # получение информации об операционной системы пользователя, запуск приложения
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
