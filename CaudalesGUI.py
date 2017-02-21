# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GestorCaudales.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pandas as pd
import atexit
import stat
import os
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1798, 955)
        self.rutaBD=''
        self.archivolocacion=''
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ventana = QtGui.QTabWidget(self.centralwidget)
        self.ventana.setObjectName(_fromUtf8("ventana"))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.gridLayout_25 = QtGui.QGridLayout(self.tab_6)
        self.gridLayout_25.setObjectName(_fromUtf8("gridLayout_25"))
        self.frame = QtGui.QFrame(self.tab_6)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_24 = QtGui.QGridLayout(self.frame)
        self.gridLayout_24.setObjectName(_fromUtf8("gridLayout_24"))
        self.frame_18 = QtGui.QFrame(self.frame)
        self.frame_18.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_18.setObjectName(_fromUtf8("frame_18"))
        self.gridLayout_23 = QtGui.QGridLayout(self.frame_18)
        self.gridLayout_23.setObjectName(_fromUtf8("gridLayout_23"))
        self.label_24 = QtGui.QLabel(self.frame_18)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_23.addWidget(self.label_24, 0, 0, 1, 1)
        self.label_30 = QtGui.QLabel(self.frame_18)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout_23.addWidget(self.label_30, 1, 0, 1, 1)
        self.label_31 = QtGui.QLabel(self.frame_18)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.gridLayout_23.addWidget(self.label_31, 2, 0, 1, 1)
        self.label_35 = QtGui.QLabel(self.frame_18)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.gridLayout_23.addWidget(self.label_35, 3, 0, 1, 1)
        self.label_36 = QtGui.QLabel(self.frame_18)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.gridLayout_23.addWidget(self.label_36, 4, 0, 1, 1)
        self.label_37 = QtGui.QLabel(self.frame_18)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.gridLayout_23.addWidget(self.label_37, 5, 0, 1, 1)
        self.label_38 = QtGui.QLabel(self.frame_18)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.gridLayout_23.addWidget(self.label_38, 6, 0, 1, 1)
        self.label_39 = QtGui.QLabel(self.frame_18)
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.gridLayout_23.addWidget(self.label_39, 7, 0, 1, 1)
        self.label_40 = QtGui.QLabel(self.frame_18)
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.gridLayout_23.addWidget(self.label_40, 8, 0, 1, 1)
        self.label_41 = QtGui.QLabel(self.frame_18)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.gridLayout_23.addWidget(self.label_41, 9, 0, 1, 1)
        self.label_42 = QtGui.QLabel(self.frame_18)
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.gridLayout_23.addWidget(self.label_42, 10, 0, 1, 1)
        self.label_43 = QtGui.QLabel(self.frame_18)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.gridLayout_23.addWidget(self.label_43, 11, 0, 1, 1)
        self.label_44 = QtGui.QLabel(self.frame_18)
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.gridLayout_23.addWidget(self.label_44, 12, 0, 1, 1)
        self.label_45 = QtGui.QLabel(self.frame_18)
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.gridLayout_23.addWidget(self.label_45, 13, 0, 1, 1)
        self.gridLayout_24.addWidget(self.frame_18, 0, 0, 1, 1)
        self.frame_17 = QtGui.QFrame(self.frame)
        self.frame_17.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_17.setObjectName(_fromUtf8("frame_17"))
        self.gridLayout_22 = QtGui.QGridLayout(self.frame_17)
        self.gridLayout_22.setObjectName(_fromUtf8("gridLayout_22"))
        self.codigoEstacion = QtGui.QLineEdit(self.frame_17)
        self.codigoEstacion.setObjectName(_fromUtf8("codigoEstacion"))
        self.gridLayout_22.addWidget(self.codigoEstacion, 0, 0, 1, 1)
        self.nombreEstacion = QtGui.QLineEdit(self.frame_17)
        self.nombreEstacion.setObjectName(_fromUtf8("nombreEstacion"))
        self.gridLayout_22.addWidget(self.nombreEstacion, 1, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.frame_17)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_22.addWidget(self.lineEdit, 2, 0, 1, 1)
        self.lineEdit_29 = QtGui.QLineEdit(self.frame_17)
        self.lineEdit_29.setObjectName(_fromUtf8("lineEdit_29"))
        self.gridLayout_22.addWidget(self.lineEdit_29, 3, 0, 1, 1)
        self.lineEdit_30 = QtGui.QLineEdit(self.frame_17)
        self.lineEdit_30.setObjectName(_fromUtf8("lineEdit_30"))
        self.gridLayout_22.addWidget(self.lineEdit_30, 4, 0, 1, 1)
        self.lineEdit_31 = QtGui.QLineEdit(self.frame_17)
        self.lineEdit_31.setObjectName(_fromUtf8("lineEdit_31"))
        self.gridLayout_22.addWidget(self.lineEdit_31, 5, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.frame_17)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_22.addWidget(self.lineEdit_2, 6, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.frame_17)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_22.addWidget(self.lineEdit_3, 7, 0, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.frame_17)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout_22.addWidget(self.lineEdit_4, 8, 0, 1, 1)
        self.lineEdit_5 = QtGui.QLineEdit(self.frame_17)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout_22.addWidget(self.lineEdit_5, 9, 0, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.frame_17)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout_22.addWidget(self.lineEdit_6, 10, 0, 1, 1)
        self.lineEdit_7 = QtGui.QLineEdit(self.frame_17)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.gridLayout_22.addWidget(self.lineEdit_7, 11, 0, 1, 1)
        self.lineEdit_8 = QtGui.QLineEdit(self.frame_17)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.gridLayout_22.addWidget(self.lineEdit_8, 12, 0, 1, 1)
        self.gridLayout_24.addWidget(self.frame_17, 0, 2, 1, 1)

        self.crearTabla = QtGui.QPushButton(self.frame)
        self.crearTabla.setObjectName(_fromUtf8("crearTabla"))
        self.crearTabla.clicked.connect(self.tablaCreacion)
        self.gridLayout_24.addWidget(self.crearTabla, 1, 0, 1, 3)

        self.line_2 = QtGui.QFrame(self.frame)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_24.addWidget(self.line_2, 2, 0, 1, 3)
        self.label_29 = QtGui.QLabel(self.frame)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_24.addWidget(self.label_29, 3, 0, 1, 1)
        self.codigoEstacion2 = QtGui.QLineEdit(self.frame)
        self.codigoEstacion2.setObjectName(_fromUtf8("codigoEstacion2"))
        self.gridLayout_24.addWidget(self.codigoEstacion2, 3, 1, 1, 2)
        self.tablaBorrar = QtGui.QPushButton(self.frame)
        self.tablaBorrar.setObjectName(_fromUtf8("tablaBorrar"))
        self.gridLayout_24.addWidget(self.tablaBorrar, 4, 0, 1, 3)
        self.gridLayout_25.addWidget(self.frame, 0, 0, 2, 2)
        self.line_4 = QtGui.QFrame(self.tab_6)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout_25.addWidget(self.line_4, 1, 1, 1, 1)
        self.frame_16 = QtGui.QFrame(self.tab_6)
        self.frame_16.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_16.setObjectName(_fromUtf8("frame_16"))
        self.gridLayout_21 = QtGui.QGridLayout(self.frame_16)
        self.gridLayout_21.setObjectName(_fromUtf8("gridLayout_21"))
        self.tabla5 = QtGui.QTableWidget(self.frame_16)
        self.tabla5.setObjectName(_fromUtf8("tabla5"))
        self.tabla5.setColumnCount(0)
        self.tabla5.setRowCount(0)
        self.gridLayout_21.addWidget(self.tabla5, 0, 0, 1, 1)
        self.gridLayout_25.addWidget(self.frame_16, 1, 2, 1, 1)
        self.ventana.addTab(self.tab_6, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_16 = QtGui.QGridLayout(self.tab)
        self.gridLayout_16.setObjectName(_fromUtf8("gridLayout_16"))
        self.frame_5 = QtGui.QFrame(self.tab)
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.gridLayout_9 = QtGui.QGridLayout(self.frame_5)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))

        self.label_5 = QtGui.QLabel(self.frame_5)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_9.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_6 = QtGui.QLabel(self.frame_5)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_9.addWidget(self.label_6, 1, 0, 1, 1)

        self.menuEstaciones = QtGui.QComboBox(self.frame_5)
        self.menuEstaciones.setObjectName(_fromUtf8("menuEstaciones"))
        self.menuEstaciones.activated.connect(self.Actualizar_Manual)#actualiza ni bien uno escoje el combo
        self.gridLayout_9.addWidget(self.menuEstaciones, 1, 2, 1, 2)

        self.label_25 = QtGui.QLabel(self.frame_5)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_9.addWidget(self.label_25, 3, 0, 1, 1)

        self.fecha1 = QtGui.QLineEdit(self.frame_5)
        self.fecha1.setObjectName(_fromUtf8("fecha1"))
        self.gridLayout_9.addWidget(self.fecha1, 3, 3, 1, 1)

        self.csvconvencional = QtGui.QPushButton(self.frame_5)
        self.csvconvencional.setObjectName(_fromUtf8("csvconvencional"))
        self.csvconvencional.clicked.connect(self.csvFileConvencional)
        self.gridLayout_9.addWidget(self.csvconvencional, 1, 4, 1, 1)

        self.exportcsvM = QtGui.QPushButton(self.frame_5)
        self.exportcsvM.setObjectName(_fromUtf8("exportcsvM"))
        self.exportcsvM.clicked.connect(self.exportCSV1)
        self.gridLayout_9.addWidget(self.exportcsvM, 1, 5, 1, 1)

        self.gridLayout_16.addWidget(self.frame_5, 0, 0, 1, 1)
        self.line = QtGui.QFrame(self.tab)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_16.addWidget(self.line, 0, 1, 1, 1)
        self.frame_6 = QtGui.QFrame(self.tab)
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.gridLayout_10 = QtGui.QGridLayout(self.frame_6)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.label_7 = QtGui.QLabel(self.frame_6)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_10.addWidget(self.label_7, 0, 0, 1, 1)

        self.actualizar1 = QtGui.QPushButton(self.frame_6)
        self.actualizar1.setObjectName(_fromUtf8("actualizar1"))
        self.actualizar1.clicked.connect(self.filtrarConvencionales)
        self.gridLayout_10.addWidget(self.actualizar1, 1, 0, 1, 1)

        self.guardar1 = QtGui.QPushButton(self.frame_6)
        self.guardar1.setObjectName(_fromUtf8("guardar1"))
        self.guardar1.clicked.connect(self.Guardar_click)
        self.gridLayout_10.addWidget(self.guardar1, 1, 1, 1, 1)

        self.borrar1 = QtGui.QPushButton(self.frame_6)
        self.borrar1.setObjectName(_fromUtf8("borrar1"))
        self.borrar1.clicked.connect(self.borrarL)
        self.gridLayout_10.addWidget(self.borrar1, 1, 2, 1, 1)

        self.gridLayout_16.addWidget(self.frame_6, 0, 2, 1, 1)
        self.frame_4 = QtGui.QFrame(self.tab)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.N1 = QtGui.QLineEdit(self.frame_4)
        self.N1.setObjectName(_fromUtf8("N1"))
        self.gridLayout_2.addWidget(self.N1, 0, 0, 1, 1)
        self.N2 = QtGui.QLineEdit(self.frame_4)
        self.N2.setObjectName(_fromUtf8("N2"))
        self.gridLayout_2.addWidget(self.N2, 0, 1, 1, 1)
        self.N3 = QtGui.QLineEdit(self.frame_4)
        self.N3.setObjectName(_fromUtf8("N3"))
        self.gridLayout_2.addWidget(self.N3, 0, 2, 1, 1)
        self.N4 = QtGui.QLineEdit(self.frame_4)
        self.N4.setObjectName(_fromUtf8("N4"))
        self.gridLayout_2.addWidget(self.N4, 0, 3, 1, 1)
        self.N5 = QtGui.QLineEdit(self.frame_4)
        self.N5.setObjectName(_fromUtf8("N5"))
        self.gridLayout_2.addWidget(self.N5, 0, 4, 1, 1)
        self.N6 = QtGui.QLineEdit(self.frame_4)
        self.N6.setObjectName(_fromUtf8("N6"))
        self.gridLayout_2.addWidget(self.N6, 0, 5, 1, 1)
        self.N7 = QtGui.QLineEdit(self.frame_4)
        self.N7.setObjectName(_fromUtf8("N7"))
        self.gridLayout_2.addWidget(self.N7, 0, 6, 1, 1)
        self.N8 = QtGui.QLineEdit(self.frame_4)
        self.N8.setObjectName(_fromUtf8("N8"))
        self.gridLayout_2.addWidget(self.N8, 0, 7, 1, 1)
        self.N9 = QtGui.QLineEdit(self.frame_4)
        self.N9.setObjectName(_fromUtf8("N9"))
        self.gridLayout_2.addWidget(self.N9, 0, 8, 1, 1)
        self.N10 = QtGui.QLineEdit(self.frame_4)
        self.N10.setObjectName(_fromUtf8("N10"))
        self.gridLayout_2.addWidget(self.N10, 0, 9, 1, 1)
        self.N11 = QtGui.QLineEdit(self.frame_4)
        self.N11.setObjectName(_fromUtf8("N11"))
        self.gridLayout_2.addWidget(self.N11, 0, 10, 1, 1)
        self.N12 = QtGui.QLineEdit(self.frame_4)
        self.N12.setObjectName(_fromUtf8("N12"))
        self.gridLayout_2.addWidget(self.N12, 0, 11, 1, 1)
        self.N13 = QtGui.QLineEdit(self.frame_4)
        self.N13.setObjectName(_fromUtf8("N13"))
        self.gridLayout_2.addWidget(self.N13, 0, 12, 1, 1)
        self.N14 = QtGui.QLineEdit(self.frame_4)
        self.N14.setObjectName(_fromUtf8("N14"))
        self.gridLayout_2.addWidget(self.N14, 0, 13, 1, 1)
        self.N15 = QtGui.QLineEdit(self.frame_4)
        self.N15.setObjectName(_fromUtf8("N15"))
        self.gridLayout_2.addWidget(self.N15, 0, 14, 1, 1)
        self.N16 = QtGui.QLineEdit(self.frame_4)
        self.N16.setObjectName(_fromUtf8("N16"))
        self.gridLayout_2.addWidget(self.N16, 0, 15, 1, 1)
        self.N17 = QtGui.QLineEdit(self.frame_4)
        self.N17.setObjectName(_fromUtf8("N17"))
        self.gridLayout_2.addWidget(self.N17, 0, 16, 1, 1)
        self.N18 = QtGui.QLineEdit(self.frame_4)
        self.N18.setObjectName(_fromUtf8("N18"))
        self.gridLayout_2.addWidget(self.N18, 0, 17, 1, 1)
        self.N19 = QtGui.QLineEdit(self.frame_4)
        self.N19.setObjectName(_fromUtf8("N19"))
        self.gridLayout_2.addWidget(self.N19, 0, 18, 1, 1)
        self.N20 = QtGui.QLineEdit(self.frame_4)
        self.N20.setObjectName(_fromUtf8("N20"))
        self.gridLayout_2.addWidget(self.N20, 0, 19, 1, 1)
        self.N21 = QtGui.QLineEdit(self.frame_4)
        self.N21.setObjectName(_fromUtf8("N21"))
        self.gridLayout_2.addWidget(self.N21, 0, 20, 1, 1)
        self.N22 = QtGui.QLineEdit(self.frame_4)
        self.N22.setObjectName(_fromUtf8("N22"))
        self.gridLayout_2.addWidget(self.N22, 0, 21, 1, 1)
        self.N23 = QtGui.QLineEdit(self.frame_4)
        self.N23.setObjectName(_fromUtf8("N23"))
        self.gridLayout_2.addWidget(self.N23, 0, 22, 1, 1)
        self.N24 = QtGui.QLineEdit(self.frame_4)
        self.N24.setObjectName(_fromUtf8("N24"))
        self.gridLayout_2.addWidget(self.N24, 0, 23, 1, 1)
        self.gridLayout_16.addWidget(self.frame_4, 1, 0, 1, 3)
        self.tabla1 = QtGui.QTableWidget(self.tab)
        self.tabla1.setObjectName(_fromUtf8("tabla1"))
        self.tabla1.setColumnCount(0)
        self.tabla1.setRowCount(0)
        self.gridLayout_16.addWidget(self.tabla1, 2, 0, 1, 3)
        self.frame_11 = QtGui.QFrame(self.tab)
        self.frame_11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_11.setObjectName(_fromUtf8("frame_11"))
        self.gridLayout_11 = QtGui.QGridLayout(self.frame_11)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.label = QtGui.QLabel(self.frame_11)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_11.addWidget(self.label, 1, 0, 1, 1)
        self.busqueda1 = QtGui.QLineEdit(self.frame_11)
        self.busqueda1.setObjectName(_fromUtf8("busqueda1"))
        self.gridLayout_11.addWidget(self.busqueda1, 1, 2, 1, 1)
        self.busqueda11 = QtGui.QLineEdit(self.frame_11)
        self.busqueda11.setObjectName(_fromUtf8("busqueda11"))
        self.gridLayout_11.addWidget(self.busqueda11, 1, 1, 1, 1)
        self.gridLayout_16.addWidget(self.frame_11, 3, 0, 1, 1)
        self.ventana.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_17 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_17.setObjectName(_fromUtf8("gridLayout_17"))
        self.tabal2 = QtGui.QTableWidget(self.tab_2)
        self.tabal2.setObjectName(_fromUtf8("tabal2"))
        self.tabal2.setColumnCount(0)
        self.tabal2.setRowCount(0)
        self.gridLayout_17.addWidget(self.tabal2, 2, 0, 1, 1)
        self.frame_12 = QtGui.QFrame(self.tab_2)
        self.frame_12.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_12.setObjectName(_fromUtf8("frame_12"))
        self.gridLayout_13 = QtGui.QGridLayout(self.frame_12)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.busqueda22 = QtGui.QLineEdit(self.frame_12)
        self.busqueda22.setObjectName(_fromUtf8("busqueda22"))
        self.gridLayout_13.addWidget(self.busqueda22, 1, 1, 1, 1)
        self.busqueda2 = QtGui.QLineEdit(self.frame_12)
        self.busqueda2.setObjectName(_fromUtf8("busqueda2"))
        self.gridLayout_13.addWidget(self.busqueda2, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame_12)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_13.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_17.addWidget(self.frame_12, 3, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(self.tab_2)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.N2_2 = QtGui.QLineEdit(self.frame_2)
        self.N2_2.setObjectName(_fromUtf8("N2_2"))
        self.gridLayout_4.addWidget(self.N2_2, 0, 1, 1, 1)
        self.N1_2 = QtGui.QLineEdit(self.frame_2)
        self.N1_2.setObjectName(_fromUtf8("N1_2"))
        self.gridLayout_4.addWidget(self.N1_2, 0, 0, 1, 1)
        self.N3_2 = QtGui.QLineEdit(self.frame_2)
        self.N3_2.setObjectName(_fromUtf8("N3_2"))
        self.gridLayout_4.addWidget(self.N3_2, 0, 2, 1, 1)
        self.N7_2 = QtGui.QLineEdit(self.frame_2)
        self.N7_2.setObjectName(_fromUtf8("N7_2"))
        self.gridLayout_4.addWidget(self.N7_2, 0, 6, 1, 1)
        self.N5_2 = QtGui.QLineEdit(self.frame_2)
        self.N5_2.setObjectName(_fromUtf8("N5_2"))
        self.gridLayout_4.addWidget(self.N5_2, 0, 4, 1, 1)
        self.N4_2 = QtGui.QLineEdit(self.frame_2)
        self.N4_2.setObjectName(_fromUtf8("N4_2"))
        self.gridLayout_4.addWidget(self.N4_2, 0, 3, 1, 1)
        self.N6_2 = QtGui.QLineEdit(self.frame_2)
        self.N6_2.setObjectName(_fromUtf8("N6_2"))
        self.gridLayout_4.addWidget(self.N6_2, 0, 5, 1, 1)
        self.N9_2 = QtGui.QLineEdit(self.frame_2)
        self.N9_2.setObjectName(_fromUtf8("N9_2"))
        self.gridLayout_4.addWidget(self.N9_2, 0, 8, 1, 1)
        self.N11_2 = QtGui.QLineEdit(self.frame_2)
        self.N11_2.setObjectName(_fromUtf8("N11_2"))
        self.gridLayout_4.addWidget(self.N11_2, 0, 10, 1, 1)
        self.N13_2 = QtGui.QLineEdit(self.frame_2)
        self.N13_2.setObjectName(_fromUtf8("N13_2"))
        self.gridLayout_4.addWidget(self.N13_2, 0, 12, 1, 1)
        self.N8_2 = QtGui.QLineEdit(self.frame_2)
        self.N8_2.setObjectName(_fromUtf8("N8_2"))
        self.gridLayout_4.addWidget(self.N8_2, 0, 7, 1, 1)
        self.N12_2 = QtGui.QLineEdit(self.frame_2)
        self.N12_2.setObjectName(_fromUtf8("N12_2"))
        self.gridLayout_4.addWidget(self.N12_2, 0, 11, 1, 1)
        self.N16_2 = QtGui.QLineEdit(self.frame_2)
        self.N16_2.setObjectName(_fromUtf8("N16_2"))
        self.gridLayout_4.addWidget(self.N16_2, 0, 15, 1, 1)
        self.N18_2 = QtGui.QLineEdit(self.frame_2)
        self.N18_2.setObjectName(_fromUtf8("N18_2"))
        self.gridLayout_4.addWidget(self.N18_2, 0, 17, 1, 1)
        self.N23_2 = QtGui.QLineEdit(self.frame_2)
        self.N23_2.setObjectName(_fromUtf8("N23_2"))
        self.gridLayout_4.addWidget(self.N23_2, 0, 22, 1, 1)
        self.N24_2 = QtGui.QLineEdit(self.frame_2)
        self.N24_2.setObjectName(_fromUtf8("N24_2"))
        self.gridLayout_4.addWidget(self.N24_2, 0, 23, 1, 1)
        self.N21_2 = QtGui.QLineEdit(self.frame_2)
        self.N21_2.setObjectName(_fromUtf8("N21_2"))
        self.gridLayout_4.addWidget(self.N21_2, 0, 20, 1, 1)
        self.N17_2 = QtGui.QLineEdit(self.frame_2)
        self.N17_2.setObjectName(_fromUtf8("N17_2"))
        self.gridLayout_4.addWidget(self.N17_2, 0, 16, 1, 1)
        self.N19_2 = QtGui.QLineEdit(self.frame_2)
        self.N19_2.setObjectName(_fromUtf8("N19_2"))
        self.gridLayout_4.addWidget(self.N19_2, 0, 18, 1, 1)
        self.N22_2 = QtGui.QLineEdit(self.frame_2)
        self.N22_2.setObjectName(_fromUtf8("N22_2"))
        self.gridLayout_4.addWidget(self.N22_2, 0, 21, 1, 1)
        self.N20_2 = QtGui.QLineEdit(self.frame_2)
        self.N20_2.setObjectName(_fromUtf8("N20_2"))
        self.gridLayout_4.addWidget(self.N20_2, 0, 19, 1, 1)
        self.N15_2 = QtGui.QLineEdit(self.frame_2)
        self.N15_2.setObjectName(_fromUtf8("N15_2"))
        self.gridLayout_4.addWidget(self.N15_2, 0, 14, 1, 1)
        self.N14_2 = QtGui.QLineEdit(self.frame_2)
        self.N14_2.setObjectName(_fromUtf8("N14_2"))
        self.gridLayout_4.addWidget(self.N14_2, 0, 13, 1, 1)
        self.N10_2 = QtGui.QLineEdit(self.frame_2)
        self.N10_2.setObjectName(_fromUtf8("N10_2"))
        self.gridLayout_4.addWidget(self.N10_2, 0, 9, 1, 1)
        self.gridLayout_17.addWidget(self.frame_2, 1, 0, 1, 1)
        self.frame_3 = QtGui.QFrame(self.tab_2)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.gridLayout_27 = QtGui.QGridLayout(self.frame_3)
        self.gridLayout_27.setObjectName(_fromUtf8("gridLayout_27"))
        self.frame_19 = QtGui.QFrame(self.frame_3)
        self.frame_19.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_19.setObjectName(_fromUtf8("frame_19"))
        self.gridLayout_12 = QtGui.QGridLayout(self.frame_19)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))

        self.label_8 = QtGui.QLabel(self.frame_19)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_12.addWidget(self.label_8, 0, 0, 1, 1)

        self.comboBox = QtGui.QComboBox(self.frame_19)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.activated.connect(self.Actualizar_Auto)
        self.gridLayout_12.addWidget(self.comboBox, 0, 1, 1, 1)

        self.label_26 = QtGui.QLabel(self.frame_19)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_12.addWidget(self.label_26, 1, 0, 1, 1)

        self.fecha2 = QtGui.QLineEdit(self.frame_19)
        self.fecha2.setObjectName(_fromUtf8("fecha2"))
        self.gridLayout_12.addWidget(self.fecha2, 1, 1, 1, 1)

        self.gridLayout_27.addWidget(self.frame_19, 0, 0, 1, 1)
        self.frame_20 = QtGui.QFrame(self.frame_3)
        self.frame_20.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_20.setObjectName(_fromUtf8("frame_20"))
        self.gridLayout_26 = QtGui.QGridLayout(self.frame_20)
        self.gridLayout_26.setObjectName(_fromUtf8("gridLayout_26"))

        self.actualizar2 = QtGui.QPushButton(self.frame_20)
        self.actualizar2.setObjectName(_fromUtf8("actualizar2"))
        self.actualizar2.clicked.connect(self.filtrarAutomaticas)
        self.gridLayout_26.addWidget(self.actualizar2, 0, 0, 1, 1)

        self.guardar2 = QtGui.QPushButton(self.frame_20)
        self.guardar2.setObjectName(_fromUtf8("guardar2"))
        self.guardar2.clicked.connect(self.Guardar_click2)
        self.gridLayout_26.addWidget(self.guardar2, 0, 1, 1, 1)

        self.borrar2 = QtGui.QPushButton(self.frame_20)
        self.borrar2.setObjectName(_fromUtf8("borrar2"))
        self.borrar2.clicked.connect(self.borrarAuto)
        self.gridLayout_26.addWidget(self.borrar2, 0, 2, 1, 1)

        self.importcsv = QtGui.QPushButton(self.frame_20)
        self.importcsv.setObjectName(_fromUtf8("importcsv"))
        self.importcsv.clicked.connect(self.csvFile)
        self.gridLayout_26.addWidget(self.importcsv, 0, 3, 1, 1)

        self.exportcsvA = QtGui.QPushButton(self.frame_20)
        self.exportcsvA.setObjectName(_fromUtf8("exportcsvA"))
        self.exportcsvA.clicked.connect(self.exportCSV2)#exportar a un csv
        self.gridLayout_26.addWidget(self.exportcsvA, 0, 4, 1, 1)

        self.gridLayout_27.addWidget(self.frame_20, 0, 1, 1, 1)
        self.gridLayout_17.addWidget(self.frame_3, 0, 0, 1, 1)
        self.ventana.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_8 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.busqueda33 = QtGui.QLineEdit(self.tab_3)
        self.busqueda33.setObjectName(_fromUtf8("busqueda33"))
        self.gridLayout_8.addWidget(self.busqueda33, 4, 1, 1, 1)
        self.frame_8 = QtGui.QFrame(self.tab_3)
        self.frame_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_8.setObjectName(_fromUtf8("frame_8"))
        self.gridLayout_7 = QtGui.QGridLayout(self.frame_8)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.label_17 = QtGui.QLabel(self.frame_8)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_7.addWidget(self.label_17, 0, 0, 1, 1)

        self.comboBox_2 = QtGui.QComboBox(self.frame_8)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.activated.connect(self.Actualizar_Aforo)
        self.gridLayout_7.addWidget(self.comboBox_2, 0, 1, 1, 1)

        self.label_27 = QtGui.QLabel(self.frame_8)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_7.addWidget(self.label_27, 0, 2, 1, 1)
        self.fecha3 = QtGui.QLineEdit(self.frame_8)
        self.fecha3.setObjectName(_fromUtf8("fecha3"))
        self.gridLayout_7.addWidget(self.fecha3, 0, 3, 1, 2)

        self.actualizar3 = QtGui.QPushButton(self.frame_8)
        self.actualizar3.setObjectName(_fromUtf8("actualizar3"))
        self.actualizar3.clicked.connect(self.filtrarAforos)
        self.gridLayout_7.addWidget(self.actualizar3, 1, 0, 1, 1)

        self.guardar3 = QtGui.QPushButton(self.frame_8)
        self.guardar3.setObjectName(_fromUtf8("guardar3"))
        self.guardar3.clicked.connect(self.Guardar_click3)
        self.gridLayout_7.addWidget(self.guardar3, 1, 1, 1, 1)

        self.borrar3 = QtGui.QPushButton(self.frame_8)
        self.borrar3.setObjectName(_fromUtf8("borrar3"))
        self.borrar3.clicked.connect(self.borrarAforo)
        self.gridLayout_7.addWidget(self.borrar3, 1, 2, 1, 1)

        self.csvaforo = QtGui.QPushButton(self.frame_8)
        self.csvaforo.setObjectName(_fromUtf8("csvaforo"))
        self.csvaforo.clicked.connect(self.csvFileAforo)
        self.gridLayout_7.addWidget(self.csvaforo, 1, 3, 1, 1)

        self.exportcsvAf = QtGui.QPushButton(self.frame_8)
        self.exportcsvAf.setObjectName(_fromUtf8("exportcsvAf"))
        self.exportcsvAf.clicked.connect(self.exportCSV3)
        self.gridLayout_7.addWidget(self.exportcsvAf, 1, 4, 1, 1)

        self.gridLayout_8.addWidget(self.frame_8, 0, 0, 1, 1)
        self.frame_7 = QtGui.QFrame(self.tab_3)
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame_7)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_9 = QtGui.QLabel(self.frame_7)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.frame_7)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_3.addWidget(self.label_10, 0, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.frame_7)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_3.addWidget(self.label_11, 0, 2, 1, 1)
        self.label_12 = QtGui.QLabel(self.frame_7)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_3.addWidget(self.label_12, 0, 3, 1, 1)
        self.label_13 = QtGui.QLabel(self.frame_7)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_3.addWidget(self.label_13, 0, 4, 1, 1)
        self.label_14 = QtGui.QLabel(self.frame_7)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_3.addWidget(self.label_14, 0, 5, 1, 1)
        self.label_15 = QtGui.QLabel(self.frame_7)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_3.addWidget(self.label_15, 0, 6, 1, 1)
        self.label_16 = QtGui.QLabel(self.frame_7)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_3.addWidget(self.label_16, 0, 7, 1, 1)
        self.label_19 = QtGui.QLabel(self.frame_7)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_3.addWidget(self.label_19, 0, 8, 1, 1)
        self.label_20 = QtGui.QLabel(self.frame_7)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_3.addWidget(self.label_20, 0, 9, 1, 1)
        self.nivel = QtGui.QLineEdit(self.frame_7)
        self.nivel.setObjectName(_fromUtf8("nivel"))
        self.gridLayout_3.addWidget(self.nivel, 1, 0, 1, 1)
        self.caudal = QtGui.QLineEdit(self.frame_7)
        self.caudal.setObjectName(_fromUtf8("caudal"))
        self.gridLayout_3.addWidget(self.caudal, 1, 1, 1, 1)
        self.area = QtGui.QLineEdit(self.frame_7)
        self.area.setObjectName(_fromUtf8("area"))
        self.gridLayout_3.addWidget(self.area, 1, 2, 1, 1)
        self.velocidad = QtGui.QLineEdit(self.frame_7)
        self.velocidad.setObjectName(_fromUtf8("velocidad"))
        self.gridLayout_3.addWidget(self.velocidad, 1, 3, 1, 1)
        self.ti = QtGui.QLineEdit(self.frame_7)
        self.ti.setObjectName(_fromUtf8("ti"))
        self.gridLayout_3.addWidget(self.ti, 1, 4, 1, 1)
        self.tc = QtGui.QLineEdit(self.frame_7)
        self.tc.setObjectName(_fromUtf8("tc"))
        self.gridLayout_3.addWidget(self.tc, 1, 5, 1, 1)
        self.td = QtGui.QLineEdit(self.frame_7)
        self.td.setObjectName(_fromUtf8("td"))
        self.gridLayout_3.addWidget(self.td, 1, 6, 1, 1)
        self.dist_2 = QtGui.QLineEdit(self.frame_7)
        self.dist_2.setObjectName(_fromUtf8("dist_2"))
        self.gridLayout_3.addWidget(self.dist_2, 1, 7, 1, 1)
        self.ancho = QtGui.QLineEdit(self.frame_7)
        self.ancho.setObjectName(_fromUtf8("ancho"))
        self.gridLayout_3.addWidget(self.ancho, 1, 8, 1, 1)
        self.factork = QtGui.QLineEdit(self.frame_7)
        self.factork.setObjectName(_fromUtf8("factork"))
        self.gridLayout_3.addWidget(self.factork, 1, 9, 1, 1)
        self.gridLayout_8.addWidget(self.frame_7, 1, 0, 1, 2)
        self.tabla3 = QtGui.QTableWidget(self.tab_3)
        self.tabla3.setObjectName(_fromUtf8("tabla3"))
        self.tabla3.setColumnCount(0)
        self.tabla3.setRowCount(0)
        self.gridLayout_8.addWidget(self.tabla3, 2, 0, 1, 2)
        self.busqueda3 = QtGui.QLineEdit(self.tab_3)
        self.busqueda3.setObjectName(_fromUtf8("busqueda3"))
        self.gridLayout_8.addWidget(self.busqueda3, 4, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.tab_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_8.addWidget(self.label_3, 3, 0, 1, 1)
        self.ventana.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridLayout_15 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_15.setObjectName(_fromUtf8("gridLayout_15"))
        self.frame_9 = QtGui.QFrame(self.tab_4)
        self.frame_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_9.setObjectName(_fromUtf8("frame_9"))
        self.gridLayout_5 = QtGui.QGridLayout(self.frame_9)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_21 = QtGui.QLabel(self.frame_9)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_5.addWidget(self.label_21, 0, 0, 1, 1)
        self.label_22 = QtGui.QLabel(self.frame_9)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_5.addWidget(self.label_22, 0, 1, 1, 1)
        self.label_23 = QtGui.QLabel(self.frame_9)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_5.addWidget(self.label_23, 0, 2, 1, 1)
        self.amarilla = QtGui.QLineEdit(self.frame_9)
        self.amarilla.setObjectName(_fromUtf8("amarilla"))
        self.gridLayout_5.addWidget(self.amarilla, 1, 0, 1, 1)
        self.naranja = QtGui.QLineEdit(self.frame_9)
        self.naranja.setObjectName(_fromUtf8("naranja"))
        self.gridLayout_5.addWidget(self.naranja, 1, 1, 1, 1)
        self.roja = QtGui.QLineEdit(self.frame_9)
        self.roja.setObjectName(_fromUtf8("roja"))
        self.gridLayout_5.addWidget(self.roja, 1, 2, 1, 1)
        self.gridLayout_15.addWidget(self.frame_9, 1, 0, 1, 2)
        self.tabla4 = QtGui.QTableWidget(self.tab_4)
        self.tabla4.setObjectName(_fromUtf8("tabla4"))
        self.tabla4.setColumnCount(0)
        self.tabla4.setRowCount(0)
        self.gridLayout_15.addWidget(self.tabla4, 2, 0, 1, 2)
        self.frame_10 = QtGui.QFrame(self.tab_4)
        self.frame_10.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_10.setObjectName(_fromUtf8("frame_10"))
        self.gridLayout_14 = QtGui.QGridLayout(self.frame_10)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.label_18 = QtGui.QLabel(self.frame_10)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_14.addWidget(self.label_18, 0, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.frame_10)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_14.addWidget(self.line_3, 0, 1, 2, 1)
        self.label_28 = QtGui.QLabel(self.frame_10)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_14.addWidget(self.label_28, 0, 2, 1, 1)
        self.fecha4 = QtGui.QLineEdit(self.frame_10)
        self.fecha4.setObjectName(_fromUtf8("fecha4"))
        self.gridLayout_14.addWidget(self.fecha4, 0, 3, 1, 1)

        self.comboBox_3 = QtGui.QComboBox(self.frame_10)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItems(filter(lambda k: '_Alertas' in k, self.lista())) 
        self.comboBox_3.activated.connect(self.Actualizar_Alerta)
        self.gridLayout_14.addWidget(self.comboBox_3, 1, 0, 1, 1)

        self.actualizar4 = QtGui.QPushButton(self.frame_10)
        self.actualizar4.setObjectName(_fromUtf8("actualizar4"))
        self.actualizar4.clicked.connect(self.filtrarAlertas)
        self.gridLayout_14.addWidget(self.actualizar4, 1, 2, 1, 1)

        self.guardar4 = QtGui.QPushButton(self.frame_10)
        self.guardar4.setObjectName(_fromUtf8("guardar4"))
        self.guardar4.clicked.connect(self.Guardar_click4)
        self.gridLayout_14.addWidget(self.guardar4, 1, 3, 1, 1)

        self.borrar4 = QtGui.QPushButton(self.frame_10)
        self.borrar4.setObjectName(_fromUtf8("borrar4"))
        self.borrar4.clicked.connect(self.borrarAlerta)
        self.gridLayout_14.addWidget(self.borrar4, 1, 4, 1, 1)

        self.csvalertas = QtGui.QPushButton(self.frame_10)
        self.csvalertas.setObjectName(_fromUtf8("csvalertas"))
        self.csvalertas.clicked.connect(self.csvFileAlertas)
        self.gridLayout_14.addWidget(self.csvalertas, 1, 5, 1, 1)

        self.exportcsvAl = QtGui.QPushButton(self.frame_10)
        self.exportcsvAl.setObjectName(_fromUtf8("exportcsvAl"))
        self.exportcsvAl.clicked.connect(self.exportCSV4)
        self.gridLayout_14.addWidget(self.exportcsvAl, 1, 6, 1, 1)

        self.gridLayout_15.addWidget(self.frame_10, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.tab_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_15.addWidget(self.label_4, 3, 0, 1, 1)
        self.busqueda4 = QtGui.QLineEdit(self.tab_4)
        self.busqueda4.setObjectName(_fromUtf8("busqueda4"))
        self.gridLayout_15.addWidget(self.busqueda4, 5, 0, 1, 1)
        self.busqueda44 = QtGui.QLineEdit(self.tab_4)
        self.busqueda44.setObjectName(_fromUtf8("busqueda44"))
        self.gridLayout_15.addWidget(self.busqueda44, 5, 1, 1, 1)
        self.ventana.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.gridLayout_20 = QtGui.QGridLayout(self.tab_5)
        self.gridLayout_20.setObjectName(_fromUtf8("gridLayout_20"))
        self.frame_13 = QtGui.QFrame(self.tab_5)
        self.frame_13.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_13.setObjectName(_fromUtf8("frame_13"))
        self.gridLayout_6 = QtGui.QGridLayout(self.frame_13)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_32 = QtGui.QLabel(self.frame_13)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.gridLayout_6.addWidget(self.label_32, 0, 0, 1, 1)

        self.comboBox_4 = QtGui.QComboBox(self.frame_13)
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.activated.connect(self.Actualizar_Caudal)
        self.gridLayout_6.addWidget(self.comboBox_4, 0, 1, 1, 1)

        self.label_34 = QtGui.QLabel(self.frame_13)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.gridLayout_6.addWidget(self.label_34, 1, 0, 1, 1)
        self.fecha5 = QtGui.QLineEdit(self.frame_13)
        self.fecha5.setObjectName(_fromUtf8("fecha5"))
        self.gridLayout_6.addWidget(self.fecha5, 1, 1, 1, 1)

        self.importCSVQ = QtGui.QPushButton(self.frame_13)
        self.importCSVQ.setObjectName(_fromUtf8("importCSVQ"))
        self.importCSVQ.clicked.connect(self.csvFileQ)
        self.gridLayout_6.addWidget(self.importCSVQ, 1, 2, 1, 1)

        self.exportCSVQ = QtGui.QPushButton(self.frame_13)
        self.exportCSVQ.setObjectName(_fromUtf8("exportCSVQ"))
        self.exportCSVQ.clicked.connect(self.exportCSV5)
        self.gridLayout_6.addWidget(self.exportCSVQ, 1, 3, 1, 1)

        self.Filtrar5 = QtGui.QPushButton(self.frame_13)
        self.Filtrar5.setObjectName(_fromUtf8("Filtrar5"))
        self.Filtrar5.clicked.connect(self.filtrarCaudales)
        self.gridLayout_6.addWidget(self.Filtrar5, 1, 4, 1, 1)

        self.guardar5 = QtGui.QPushButton(self.frame_13)
        self.guardar5.setObjectName(_fromUtf8("guardar5"))
        self.guardar5.clicked.connect(self.Guardar_click5)
        self.gridLayout_6.addWidget(self.guardar5, 1, 5, 1, 1)

        self.borrar5 = QtGui.QPushButton(self.frame_13)
        self.borrar5.setObjectName(_fromUtf8("borrar5"))
        self.borrar5.clicked.connect(self.borrarCaudal)
        self.gridLayout_6.addWidget(self.borrar5, 1, 6, 1, 1)

        self.gridLayout_20.addWidget(self.frame_13, 0, 0, 1, 1)
        self.frame_14 = QtGui.QFrame(self.tab_5)
        self.frame_14.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_14.setObjectName(_fromUtf8("frame_14"))
        self.gridLayout_18 = QtGui.QGridLayout(self.frame_14)
        self.gridLayout_18.setObjectName(_fromUtf8("gridLayout_18"))
        self.q1 = QtGui.QLineEdit(self.frame_14)
        self.q1.setObjectName(_fromUtf8("q1"))
        self.gridLayout_18.addWidget(self.q1, 0, 0, 1, 1)
        self.q2 = QtGui.QLineEdit(self.frame_14)
        self.q2.setObjectName(_fromUtf8("q2"))
        self.gridLayout_18.addWidget(self.q2, 0, 1, 1, 1)
        self.q3 = QtGui.QLineEdit(self.frame_14)
        self.q3.setObjectName(_fromUtf8("q3"))
        self.gridLayout_18.addWidget(self.q3, 0, 2, 1, 1)
        self.q4 = QtGui.QLineEdit(self.frame_14)
        self.q4.setObjectName(_fromUtf8("q4"))
        self.gridLayout_18.addWidget(self.q4, 0, 3, 1, 1)
        self.q5 = QtGui.QLineEdit(self.frame_14)
        self.q5.setObjectName(_fromUtf8("q5"))
        self.gridLayout_18.addWidget(self.q5, 0, 4, 1, 1)
        self.q6 = QtGui.QLineEdit(self.frame_14)
        self.q6.setObjectName(_fromUtf8("q6"))
        self.gridLayout_18.addWidget(self.q6, 0, 5, 1, 1)
        self.q7 = QtGui.QLineEdit(self.frame_14)
        self.q7.setObjectName(_fromUtf8("q7"))
        self.gridLayout_18.addWidget(self.q7, 0, 6, 1, 1)
        self.q8 = QtGui.QLineEdit(self.frame_14)
        self.q8.setObjectName(_fromUtf8("q8"))
        self.gridLayout_18.addWidget(self.q8, 0, 7, 1, 1)
        self.q9 = QtGui.QLineEdit(self.frame_14)
        self.q9.setObjectName(_fromUtf8("q9"))
        self.gridLayout_18.addWidget(self.q9, 0, 8, 1, 1)
        self.q10 = QtGui.QLineEdit(self.frame_14)
        self.q10.setObjectName(_fromUtf8("q10"))
        self.gridLayout_18.addWidget(self.q10, 0, 9, 1, 1)
        self.q11 = QtGui.QLineEdit(self.frame_14)
        self.q11.setObjectName(_fromUtf8("q11"))
        self.gridLayout_18.addWidget(self.q11, 0, 10, 1, 1)
        self.q12 = QtGui.QLineEdit(self.frame_14)
        self.q12.setObjectName(_fromUtf8("q12"))
        self.gridLayout_18.addWidget(self.q12, 0, 11, 1, 1)
        self.q13 = QtGui.QLineEdit(self.frame_14)
        self.q13.setObjectName(_fromUtf8("q13"))
        self.gridLayout_18.addWidget(self.q13, 0, 12, 1, 1)
        self.q14 = QtGui.QLineEdit(self.frame_14)
        self.q14.setObjectName(_fromUtf8("q14"))
        self.gridLayout_18.addWidget(self.q14, 0, 13, 1, 1)
        self.q15 = QtGui.QLineEdit(self.frame_14)
        self.q15.setObjectName(_fromUtf8("q15"))
        self.gridLayout_18.addWidget(self.q15, 0, 14, 1, 1)
        self.q16 = QtGui.QLineEdit(self.frame_14)
        self.q16.setObjectName(_fromUtf8("q16"))
        self.gridLayout_18.addWidget(self.q16, 0, 15, 1, 1)
        self.q17 = QtGui.QLineEdit(self.frame_14)
        self.q17.setObjectName(_fromUtf8("q17"))
        self.gridLayout_18.addWidget(self.q17, 0, 16, 1, 1)
        self.q18 = QtGui.QLineEdit(self.frame_14)
        self.q18.setObjectName(_fromUtf8("q18"))
        self.gridLayout_18.addWidget(self.q18, 0, 17, 1, 1)
        self.q19 = QtGui.QLineEdit(self.frame_14)
        self.q19.setObjectName(_fromUtf8("q19"))
        self.gridLayout_18.addWidget(self.q19, 0, 18, 1, 1)
        self.q20 = QtGui.QLineEdit(self.frame_14)
        self.q20.setObjectName(_fromUtf8("q20"))
        self.gridLayout_18.addWidget(self.q20, 0, 19, 1, 1)
        self.q21 = QtGui.QLineEdit(self.frame_14)
        self.q21.setObjectName(_fromUtf8("q21"))
        self.gridLayout_18.addWidget(self.q21, 0, 20, 1, 1)
        self.q22 = QtGui.QLineEdit(self.frame_14)
        self.q22.setObjectName(_fromUtf8("q22"))
        self.gridLayout_18.addWidget(self.q22, 0, 21, 1, 1)
        self.q23 = QtGui.QLineEdit(self.frame_14)
        self.q23.setObjectName(_fromUtf8("q23"))
        self.gridLayout_18.addWidget(self.q23, 0, 22, 1, 1)
        self.q24 = QtGui.QLineEdit(self.frame_14)
        self.q24.setObjectName(_fromUtf8("q24"))
        self.gridLayout_18.addWidget(self.q24, 0, 23, 1, 1)
        self.gridLayout_20.addWidget(self.frame_14, 1, 0, 1, 1)
        self.tabla6 = QtGui.QTableWidget(self.tab_5)
        self.tabla6.setObjectName(_fromUtf8("tabla6"))
        self.tabla6.setColumnCount(0)
        self.tabla6.setRowCount(0)
        self.gridLayout_20.addWidget(self.tabla6, 2, 0, 1, 1)
        self.frame_15 = QtGui.QFrame(self.tab_5)
        self.frame_15.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_15.setObjectName(_fromUtf8("frame_15"))
        self.gridLayout_19 = QtGui.QGridLayout(self.frame_15)
        self.gridLayout_19.setObjectName(_fromUtf8("gridLayout_19"))
        self.label_33 = QtGui.QLabel(self.frame_15)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.gridLayout_19.addWidget(self.label_33, 0, 0, 1, 1)
        self.busqueda5 = QtGui.QLineEdit(self.frame_15)
        self.busqueda5.setObjectName(_fromUtf8("busqueda5"))
        self.gridLayout_19.addWidget(self.busqueda5, 0, 1, 1, 1)
        self.busqueda55 = QtGui.QLineEdit(self.frame_15)
        self.busqueda55.setObjectName(_fromUtf8("busqueda55"))
        self.gridLayout_19.addWidget(self.busqueda55, 0, 2, 1, 1)
        self.gridLayout_20.addWidget(self.frame_15, 3, 0, 1, 1)
        self.ventana.addTab(self.tab_5, _fromUtf8(""))
        self.gridLayout.addWidget(self.ventana, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1798, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuEquipo = QtGui.QMenu(self.menubar)
        self.menuEquipo.setObjectName(_fromUtf8("menuEquipo"))
        self.menuArchivo = QtGui.QMenu(self.menubar)
        self.menuArchivo.setObjectName(_fromUtf8("menuArchivo"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.actionDesarrolladores = QtGui.QAction(MainWindow)
        self.actionDesarrolladores.setObjectName(_fromUtf8("actionDesarrolladores"))
        self.actionDesarrolladores.triggered.connect(self.ayuda)
        self.actionAbrir_Base = QtGui.QAction(MainWindow)
        self.actionAbrir_Base.setObjectName(_fromUtf8("actionAbrir_Base"))
        self.actionAbrir_Base.triggered.connect(self.openDB)
        self.menuEquipo.addAction(self.actionDesarrolladores)

        self.menuArchivo.addAction(self.actionAbrir_Base)
        self.menubar.addAction(self.menuEquipo.menuAction())
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        self.ventana.setCurrentIndex(0)#ventana displayada inicialmente
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Base de Datos Q-H", None))
        self.label_24.setText(_translate("MainWindow", "Codigo de Estacion", None))
        self.label_30.setText(_translate("MainWindow", "Nombre de Estacion", None))
        self.label_31.setText(_translate("MainWindow", "DRE", None))
        self.label_35.setText(_translate("MainWindow", "SIS HIDRO", None))
        self.label_36.setText(_translate("MainWindow", "CUENCA", None))
        self.label_37.setText(_translate("MainWindow", "RIO", None))
        self.label_38.setText(_translate("MainWindow", "DPTO", None))
        self.label_39.setText(_translate("MainWindow", "PROV", None))
        self.label_40.setText(_translate("MainWindow", "LONG", None))
        self.label_41.setText(_translate("MainWindow", "LAT", None))
        self.label_42.setText(_translate("MainWindow", "ALT", None))
        self.label_43.setText(_translate("MainWindow", "INICIO", None))
        self.label_44.setText(_translate("MainWindow", "ENTt", None))
        self.label_45.setText(_translate("MainWindow", "Q", None))
        self.crearTabla.setText(_translate("MainWindow", "Crear Tabla", None))
        self.label_29.setText(_translate("MainWindow", "Nombre de Estacion", None))
        self.tablaBorrar.setText(_translate("MainWindow", "Borrar Tabla", None))
        self.ventana.setTabText(self.ventana.indexOf(self.tab_6), _translate("MainWindow", "Crear Tabla Nueva", None))
        self.label_5.setText(_translate("MainWindow", "Informacion de la Cuenca", None))
        self.label_6.setText(_translate("MainWindow", "Escoger Tabla", None))
        self.label_25.setText(_translate("MainWindow", "fecha", None))
        self.csvconvencional.setText(_translate("MainWindow", "Importar csv", None))
        self.exportcsvM.setText(_translate("MainWindow", "Exportar csv", None))
        self.label_7.setText(_translate("MainWindow", "Edicion de Tablas", None))
        self.actualizar1.setText(_translate("MainWindow", "Filtrar", None))
        self.guardar1.setText(_translate("MainWindow", "Guardar", None))
        self.borrar1.setText(_translate("MainWindow", "Borrar", None))
        self.label.setText(_translate("MainWindow", "Busqueda", None))
        self.ventana.setTabText(self.ventana.indexOf(self.tab), _translate("MainWindow", "Niveles Manuales", None))
        self.label_2.setText(_translate("MainWindow", "Busqueda", None))
        self.label_8.setText(_translate("MainWindow", "Escoger tabla", None))
        self.label_26.setText(_translate("MainWindow", "Fecha", None))
        self.actualizar2.setText(_translate("MainWindow", "Filtrar", None))
        self.guardar2.setText(_translate("MainWindow", "Guardar", None))
        self.borrar2.setText(_translate("MainWindow", "Borrar", None))
        self.importcsv.setText(_translate("MainWindow", "Importar csv", None))
        self.exportcsvA.setText(_translate("MainWindow", "Exportar csv", None))
        self.ventana.setTabText(self.ventana.indexOf(self.tab_2), _translate("MainWindow", "Niveles Automaticos", None))
        self.label_17.setText(_translate("MainWindow", "Edicion de Tablas", None))
        self.label_27.setText(_translate("MainWindow", "Fecha", None))
        self.actualizar3.setText(_translate("MainWindow", "Filtrar", None))
        self.guardar3.setText(_translate("MainWindow", "Guardar", None))
        self.borrar3.setText(_translate("MainWindow", "Borrar", None))
        self.csvaforo.setText(_translate("MainWindow", "Importar csv", None))
        self.exportcsvAf.setText(_translate("MainWindow", "Export csv", None))
        self.label_9.setText(_translate("MainWindow", "Nivel", None))
        self.label_10.setText(_translate("MainWindow", "Caudal", None))
        self.label_11.setText(_translate("MainWindow", "Area", None))
        self.label_12.setText(_translate("MainWindow", "Velocidad", None))
        self.label_13.setText(_translate("MainWindow", "tiempo margen izquierdo", None))
        self.label_14.setText(_translate("MainWindow", "tiempo en el centro", None))
        self.label_15.setText(_translate("MainWindow", "tiempo margen derecha", None))
        self.label_16.setText(_translate("MainWindow", "distancia", None))
        self.label_19.setText(_translate("MainWindow", "ancho del rio", None))
        self.label_20.setText(_translate("MainWindow", "factor K", None))
        self.label_3.setText(_translate("MainWindow", "Busqueda", None))
        self.ventana.setTabText(self.ventana.indexOf(self.tab_3), _translate("MainWindow", "Aforos", None))
        self.label_21.setText(_translate("MainWindow", "Alerta Amarilla", None))
        self.label_22.setText(_translate("MainWindow", "Alerta Naranja", None))
        self.label_23.setText(_translate("MainWindow", "Alerta Roja", None))
        self.label_18.setText(_translate("MainWindow", "Edicion de Tablas", None))
        self.label_28.setText(_translate("MainWindow", "fecha", None))
        self.actualizar4.setText(_translate("MainWindow", "Filtrar", None))
        self.guardar4.setText(_translate("MainWindow", "Guardar", None))
        self.borrar4.setText(_translate("MainWindow", "Borrar", None))
        self.csvalertas.setText(_translate("MainWindow", "Import csv", None))
        self.exportcsvAl.setText(_translate("MainWindow", "Exportar csv", None))
        self.label_4.setText(_translate("MainWindow", "Busqueda", None))
        self.ventana.setTabText(self.ventana.indexOf(self.tab_4), _translate("MainWindow", "Alertas", None))
        self.label_32.setText(_translate("MainWindow", "Escoger Tabla", None))
        self.label_34.setText(_translate("MainWindow", "fecha", None))
        self.importCSVQ.setText(_translate("MainWindow", "import csv", None))
        self.exportCSVQ.setText(_translate("MainWindow", "export csv", None))
        self.Filtrar5.setText(_translate("MainWindow", "filtrar", None))
        self.guardar5.setText(_translate("MainWindow", "guardar", None))
        self.borrar5.setText(_translate("MainWindow", "borrar", None))
        self.label_33.setText(_translate("MainWindow", "Busqueda", None))
        self.ventana.setTabText(self.ventana.indexOf(self.tab_5), _translate("MainWindow", "Curva Q-H", None))
        self.menuEquipo.setTitle(_translate("MainWindow", "Equipo", None))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo", None))
        self.actionDesarrolladores.setText(_translate("MainWindow", "Desarrolladores", None))
        self.actionAbrir_Base.setText(_translate("MainWindow", "Abrir Base", None))


        
        self.N6.setStyleSheet("border: 2px solid blue;")
        self.N10.setStyleSheet("border: 2px solid blue;")
        self.N14.setStyleSheet("border: 2px solid blue;")
        self.N18.setStyleSheet("border: 2px solid blue;")

        self.fecha1.setText(time.strftime("%Y-%m-%d"))
        self.fecha2.setText(time.strftime("%Y-%m-%d"))
        self.fecha3.setText(time.strftime("%Y-%m-%d"))
        self.fecha4.setText(time.strftime("%Y-%m-%d"))
        self.fecha5.setText(time.strftime("%Y-%m-%d"))

        self.tabla1.itemChanged.connect(self.Actualizarcelda1)
        self.tabal2.itemChanged.connect(self.Actualizarcelda2)
        self.tabla3.itemChanged.connect(self.Actualizarcelda3)
        self.tabla4.itemChanged.connect(self.Actualizarcelda4)
        self.tabla6.itemChanged.connect(self.Actualizarcelda5)
##################33
    def Actualizar_Manual(self):
        conn = sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()
        
        #str(combobox1.currentText())
        cursor.execute('SELECT * FROM ' +str(self.menuEstaciones.currentText()))        
     
        #nombre y tamaño de la celda
        self.tabla1.clear()
        self.tabla1.setRowCount(0);
        self.tabla1.setColumnCount(26)

        self.tabla1.setHorizontalHeaderLabels(['fecha']+['N'+str(x) for x in range(1,25)]+['codigo'])

        numRows = cursor.execute( "SELECT COUNT(*) FROM "+str(self.menuEstaciones.currentText())).fetchall()[0][0]
        if numRows<=60:
            cursor.execute('SELECT * FROM ' +str(self.menuEstaciones.currentText()))    
            for row,form in enumerate(cursor):
                self.tabla1.insertRow(row)
                for column,item in enumerate(form):
                    self.tabla1.setItem(row,column,QtGui.QTableWidgetItem(str(item)))  

        else:
            cursor.execute('SELECT * FROM ' +str(self.menuEstaciones.currentText())+' limit '+str(numRows-31)+','+str(numRows))    
            for row,form in enumerate(cursor):
                self.tabla1.insertRow(row)
                for column,item in enumerate(form):
                    self.tabla1.setItem(row,column,QtGui.QTableWidgetItem(str(item)))  


    def Actualizar_Auto(self):
        conn = sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()
        
        #str(combobox1.currentText())
        cursor.execute('SELECT * FROM ' +str(self.comboBox.currentText()))        
     
        #nombre y tamaño de la celda
        self.tabal2.clear()
        self.tabal2.setRowCount(0);
        self.tabal2.setColumnCount(26)

        self.tabal2.setHorizontalHeaderLabels(['fecha']+['N'+str(x) for x in range(1,25)]+['codigo'])

        numRows = cursor.execute( "SELECT COUNT(*) FROM "+str(self.comboBox.currentText())).fetchall()[0][0]
        if numRows<=60:
            cursor.execute('SELECT * FROM ' +str(self.comboBox.currentText()))    
            for row,form in enumerate(cursor):
                self.tabal2.insertRow(row)
                for column,item in enumerate(form):
                    self.tabal2.setItem(row,column,QtGui.QTableWidgetItem(str(item)))  

        else:
            cursor.execute('SELECT * FROM ' +str(self.comboBox.currentText())+' limit '+str(numRows-31)+','+str(numRows))    
            for row,form in enumerate(cursor):
                self.tabal2.insertRow(row)
                for column,item in enumerate(form):
                    self.tabal2.setItem(row,column,QtGui.QTableWidgetItem(str(item)))  


    def Actualizar_Aforo(self):
        conn = sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()
        
        #str(combobox1.currentText())
        cursor.execute('SELECT * FROM ' +str(self.comboBox_2.currentText()))        
     
        #nombre y tamaño de la celda
        self.tabla3.clear()
        self.tabla3.setRowCount(0);
        self.tabla3.setColumnCount(12)

        self.tabla3.setHorizontalHeaderLabels(['fecha']+['N'+str(x) for x in range(1,11)]+['codigo'])

        numRows = cursor.execute( "SELECT COUNT(*) FROM "+str(self.comboBox_2.currentText())).fetchall()[0][0]
        if numRows<=60:
            cursor.execute('SELECT * FROM ' +str(self.comboBox_2.currentText()))    
            for row,form in enumerate(cursor):
                self.tabla3.insertRow(row)
                for column,item in enumerate(form):
                    self.tabla3.setItem(row,column,QtGui.QTableWidgetItem(str(item)))  

        else:
            cursor.execute('SELECT * FROM ' +str(self.comboBox_2.currentText())+' limit '+str(numRows-31)+','+str(numRows))  #selecciona el ultimo año previo al valor observado al final  
            for row,form in enumerate(cursor):
                self.tabla3.insertRow(row)
                for column,item in enumerate(form):
                    self.tabla3.setItem(row,column,QtGui.QTableWidgetItem(str(item)))  

    def Actualizar_Alerta(self):
        conn = sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()
        
        #str(combobox1.currentText())
        cursor.execute('SELECT * FROM ' +str(self.comboBox_3.currentText()))        
     
        #nombre y tamaño de la celda
        self.tabla4.clear()
        self.tabla4.setRowCount(0);
        self.tabla4.setColumnCount(5)

        self.tabla4.setHorizontalHeaderLabels(['fecha']+['A'+str(x) for x in range(1,4)]+['codigo'])

        numRows = cursor.execute( "SELECT COUNT(*) FROM "+str(self.comboBox_3.currentText())).fetchall()[0][0]
        if numRows<=60:
            cursor.execute('SELECT * FROM ' +str(self.comboBox_3.currentText()))    
            for row,form in enumerate(cursor):
                self.tabla4.insertRow(row)
                for column,item in enumerate(form):
                    self.tabla4.setItem(row,column,QtGui.QTableWidgetItem(str(item)))  

        else:
            cursor.execute('SELECT * FROM ' +str(self.comboBox_3.currentText())+' limit '+str(numRows-31)+','+str(numRows))    
            for row,form in enumerate(cursor):
                self.tabla4.insertRow(row)
                for column,item in enumerate(form):
                    self.tabla4.setItem(row,column,QtGui.QTableWidgetItem(str(item)))  


    def Actualizar_Caudal(self):
        conn = sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()
        
        #str(combobox1.currentText())
        cursor.execute('SELECT * FROM ' +str(self.comboBox_4.currentText()))        
     
        #nombre y tamaño de la celda
        self.tabla6.clear()
        self.tabla6.setRowCount(0);
        self.tabla6.setColumnCount(26)

        self.tabla6.setHorizontalHeaderLabels(['fecha']+['N'+str(x) for x in range(1,25)]+['codigo'])

        numRows = cursor.execute( "SELECT COUNT(*) FROM "+str(self.comboBox_4.currentText())).fetchall()[0][0]
        if numRows<=60:
            cursor.execute('SELECT * FROM ' +str(self.comboBox_4.currentText()))    
            for row,form in enumerate(cursor):
                self.tabla6.insertRow(row)
                for column,item in enumerate(form):
                    self.tabla6.setItem(row,column,QtGui.QTableWidgetItem(str(item)))  

        else:
            cursor.execute('SELECT * FROM ' +str(self.comboBox_4.currentText())+' limit '+str(numRows-31+','+str(numRows))    
            for row,form in enumerate(cursor):
                self.tabla6.insertRow(row)
                for column,item in enumerate(form):
                    self.tabla6.setItem(row,column,QtGui.QTableWidgetItem(str(item)))  

    def Actualizar_Maestro(self):
        conn = sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()
        
        #str(combobox1.currentText())
        cursor.execute('SELECT * FROM Maestro')        
     
        #nombre y tamaño de la celda
        self.tabla5.clear()
        self.tabla5.setRowCount(0);
        self.tabla5.setColumnCount(15)
        self.tabla5.setHorizontalHeaderLabels(['Codigo','Nombre','DRE','Sishidro',
              'Cuenca','rio','DPTO','PROV','DISTRITO','LONG','LAT','ALT', 'Inicio','ENT','Q'])
        for row,form in enumerate(cursor):
            self.tabla5.insertRow(row)
            for column,item in enumerate(form):
                self.tabla5.setItem(row,column,QtGui.QTableWidgetItem(str(item)))  

        
    def Guardar_click(self):
        conn = sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()
        self.fecha= str(self.fecha1.text())
        self.nivel1 = str(self.N1.text())
        self.nivel2 = str(self.N2.text())
        self.nivel3 = str(self.N3.text())
        self.nivel4 = str(self.N4.text())
        self.nivel5 = str(self.N5.text())
        self.nivel6 = str(self.N6.text())
        self.nivel7 = str(self.N7.text())
        self.nivel8 = str(self.N8.text())
        self.nivel9 = str(self.N9.text())
        self.nivel10 = str(self.N10.text())
        self.nivel11 = str(self.N11.text())
        self.nivel12 = str(self.N12.text())
        self.nivel13 = str(self.N13.text())
        self.nivel14 = str(self.N14.text())
        self.nivel15 = str(self.N15.text())
        self.nivel16 = str(self.N16.text())
        self.nivel17 = str(self.N17.text())
        self.nivel18 = str(self.N18.text())
        self.nivel19 = str(self.N19.text())
        self.nivel20 = str(self.N20.text())
        self.nivel21 = str(self.N21.text())
        self.nivel22 = str(self.N22.text())
        self.nivel23 = str(self.N23.text())
        self.nivel24 = str(self.N24.text())


        self.registro = (self.fecha,self.nivel1,self.nivel2,self.nivel3,self.nivel4,self.nivel5,self.nivel6,self.nivel7,self.nivel8,self.nivel9
            ,self.nivel10,self.nivel11,self.nivel12,self.nivel13,self.nivel14,self.nivel15,self.nivel16,self.nivel17,self.nivel18
            ,self.nivel19,self.nivel20,self.nivel21,self.nivel22,self.nivel23,self.nivel24)

        cursor.execute("""INSERT INTO """+ str(self.menuEstaciones.currentText())+ """ (fecha,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,n21,n22,n23,n24) 
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """, self.registro)
       
        conn.commit()
        #self.fecha1.setText(time.strftime("%Y-%m-%d"))
        self.N1.setText("")
        self.N2.setText("")
        self.N3.setText("")
        self.N4.setText("")
        self.N5.setText("")
        self.N6.setText("")
        self.N7.setText("")
        self.N8.setText("")
        self.N9.setText("")
        self.N10.setText("")
        self.N11.setText("")
        self.N12.setText("")
        self.N13.setText("")
        self.N14.setText("")
        self.N15.setText("")
        self.N16.setText("")
        self.N17.setText("")
        self.N18.setText("")
        self.N19.setText("")
        self.N20.setText("")
        self.N21.setText("")
        self.N22.setText("")
        self.N23.setText("")
        self.N24.setText("")
        conn.commit()
        #QMessageBox.information(self,"Registro guardado", "Aviso")
        self.Actualizar_Manual()

    def Guardar_click2(self):
        conn = sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()
        self.fecha= str(self.fecha2.text())
        self.nivel1 = str(self.N1_2.text())
        self.nivel2 = str(self.N2_2.text())
        self.nivel3 = str(self.N3_2.text())
        self.nivel4 = str(self.N4_2.text())
        self.nivel5 = str(self.N5_2.text())
        self.nivel6 = str(self.N6_2.text())
        self.nivel7 = str(self.N7_2.text())
        self.nivel8 = str(self.N8_2.text())
        self.nivel9 = str(self.N9_2.text())
        self.nivel10 = str(self.N10_2.text())
        self.nivel11 = str(self.N11_2.text())
        self.nivel12 = str(self.N12_2.text())
        self.nivel13 = str(self.N13_2.text())
        self.nivel14 = str(self.N14_2.text())
        self.nivel15 = str(self.N15_2.text())
        self.nivel16 = str(self.N16_2.text())
        self.nivel17 = str(self.N17_2.text())
        self.nivel18 = str(self.N18_2.text())
        self.nivel19 = str(self.N19_2.text())
        self.nivel20 = str(self.N20_2.text())
        self.nivel21 = str(self.N21_2.text())
        self.nivel22 = str(self.N22_2.text())
        self.nivel23 = str(self.N23_2.text())
        self.nivel24 = str(self.N24_2.text())


        self.registro = (self.fecha,self.nivel1,self.nivel2,self.nivel3,self.nivel4,self.nivel5,self.nivel6,self.nivel7,self.nivel8,self.nivel9
            ,self.nivel10,self.nivel11,self.nivel12,self.nivel13,self.nivel14,self.nivel15,self.nivel16,self.nivel17,self.nivel18
            ,self.nivel19,self.nivel20,self.nivel21,self.nivel22,self.nivel23,self.nivel24)

        cursor.execute("""INSERT INTO """+ str(self.comboBox.currentText())+ """ (fecha,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,n21,n22,n23,n24) 
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """, self.registro)
       
        conn.commit()
        #self.fecha2.setText(time.strftime("%Y-%m-%d"))
        self.N1_2.setText("")
        self.N2_2.setText("")
        self.N3_2.setText("")
        self.N4_2.setText("")
        self.N5_2.setText("")
        self.N6_2.setText("")
        self.N7_2.setText("")
        self.N8_2.setText("")
        self.N9_2.setText("")
        self.N10_2.setText("")
        self.N11_2.setText("")
        self.N12_2.setText("")
        self.N13_2.setText("")
        self.N14_2.setText("")
        self.N15_2.setText("")
        self.N16_2.setText("")
        self.N17_2.setText("")
        self.N18_2.setText("")
        self.N19_2.setText("")
        self.N20_2.setText("")
        self.N21_2.setText("")
        self.N22_2.setText("")
        self.N23_2.setText("")
        self.N24_2.setText("")
        conn.commit()
        #QMessageBox.information(self,"Registro guardado", "Aviso")
        self.Actualizar_Auto()

    def Guardar_click3(self):
        "Guarda los nuevos registros del Aforo"
        conn = sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()
        self.registro=(str(self.fecha3.text()),str(self.nivel.text()),str(self.caudal.text()),str(self.area.text()),str(self.velocidad.text()),str(self.ti.text()),str(self.tc.text()),str(self.td.text()),str(self.dist_2.text()),str(self.ancho.text()),str(self.factork.text()))
        cursor.execute("""INSERT INTO """+str(self.comboBox_2.currentText())+ """(fecha,N,q,area,V,ti,tc,td,L,b,K)
            VALUES (?,?,?,?,?,?,?,?,?,?,?)""",self.registro)
        conn.commit()
        self.Actualizar_Aforo()

    def Guardar_click4(self):
        "Guarda los nuevos registros de Alertas"
        conn = sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()
        self.fechas=str(self.fecha4.text())
        self.a=str(self.amarilla.text())
        self.n=str(self.naranja.text())
        self.r=str(self.roja.text())

        self.registro=(self.fechas,self.a,self.n,self.r)
        cursor.execute("""INSERT INTO """+ str(self.comboBox_3.currentText())+ """ (fecha,h_ama,h_nar,h_roj) 
            VALUES (?,?,?,?)
            """, self.registro)
        conn.commit()

        self.Actualizar_Alerta()

    def Guardar_click5(self):
        conn = sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()

        self.fecha= str(self.fecha5.text())
        self.nivel1 = str(self.q1.text())
        self.nivel2 = str(self.q2.text())
        self.nivel3 = str(self.q3.text())
        self.nivel4 = str(self.q4.text())
        self.nivel5 = str(self.q5.text())
        self.nivel6 = str(self.q6.text())
        self.nivel7 = str(self.q7.text())
        self.nivel8 = str(self.q8.text())
        self.nivel9 = str(self.q9.text())
        self.nivel10 = str(self.q10.text())
        self.nivel11 = str(self.q11.text())
        self.nivel12 = str(self.q12.text())
        self.nivel13 = str(self.q13.text())
        self.nivel14 = str(self.q14.text())
        self.nivel15 = str(self.q15.text())
        self.nivel16 = str(self.q16.text())
        self.nivel17 = str(self.q17.text())
        self.nivel18 = str(self.q18.text())
        self.nivel19 = str(self.q19.text())
        self.nivel20 = str(self.q20.text())
        self.nivel21 = str(self.q21.text())
        self.nivel22 = str(self.q22.text())
        self.nivel23 = str(self.q23.text())
        self.nivel24 = str(self.q24.text())


        self.registro = (self.fecha,self.nivel1,self.nivel2,self.nivel3,self.nivel4,self.nivel5,self.nivel6,self.nivel7,self.nivel8,self.nivel9
            ,self.nivel10,self.nivel11,self.nivel12,self.nivel13,self.nivel14,self.nivel15,self.nivel16,self.nivel17,self.nivel18
            ,self.nivel19,self.nivel20,self.nivel21,self.nivel22,self.nivel23,self.nivel24)

        cursor.execute("""INSERT INTO """+ str(self.comboBox_4.currentText())+ """ (fecha,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,n21,n22,n23,n24) 
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """, self.registro)
       
        conn.commit()
        #self.fecha2.setText(time.strftime("%Y-%m-%d"))
        self.N1_2.setText("")
        self.N2_2.setText("")
        self.N3_2.setText("")
        self.N4_2.setText("")
        self.N5_2.setText("")
        self.N6_2.setText("")
        self.N7_2.setText("")
        self.N8_2.setText("")
        self.N9_2.setText("")
        self.N10_2.setText("")
        self.N11_2.setText("")
        self.N12_2.setText("")
        self.N13_2.setText("")
        self.N14_2.setText("")
        self.N15_2.setText("")
        self.N16_2.setText("")
        self.N17_2.setText("")
        self.N18_2.setText("")
        self.N19_2.setText("")
        self.N20_2.setText("")
        self.N21_2.setText("")
        self.N22_2.setText("")
        self.N23_2.setText("")
        self.N24_2.setText("")
        conn.commit()
        #QMessageBox.information(self,"Registro guardado", "Aviso")
        self.Actualizar_Caudal()

    def tablaCreacion(self):
        conn=sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()

        nombre=self.nombreEstacion.text()
        codigo=self.codigoEstacion.text()
        dre=self.lineEdit.text()
        sishi=self.lineEdit_29.text()
        cuen=self.lineEdit_30.text()
        rio=self.lineEdit_31.text()
        dpto=self.lineEdit_2.text()
        prov=self.lineEdit_3.text()
        lon=self.lineEdit_4.text()
        lat=self.lineEdit_5.text()
        alt=self.lineEdit_6.text()
        ent=self.lineEdit_7.text()
        q=self.lineEdit_8.text()


        registro=(codigo,nombre,dre,sishi,cuen,rio,dpto,prov,lon,lat,alt,ent,q)
        cursor.execute("""INSERT INTO """+ "Maestro"+ """ (Codigo,Nombre,DRE,Sishidro,
              Cuenca,rio,DPTO,PROV,DISTRITO,LONG,LAT,ALT, Inicio,ENT,Q) 
             VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
             """,registro)

        cursor.execute ("""CREATE TABLE IF NOT EXISTS """+str(nombre)+"""_Niveles_Convencionales (fecha DATE,n1 REAL,
                    n2 REAL,n3 REAL,n4 REAL,n5 REAL,n6 REAL,n7 REAL,n8 REAL,n9 REAL,n10 REAL,n11 REAL,n12 REAL,
                    n13 REAL,n14 REAL,n15 REAL,n16 REAL,n17 REAL,n18 REAL,n19 REAL,n20 REAL,n21 REAL,n22 REAL,n23 REAL,
                    n24 REAL ,codigo REAL, FOREIGN KEY(codigo) REFERENCES Maestro(Codigo))""")
                    
        cursor.execute ("""CREATE TABLE IF NOT EXISTS """+str(nombre)+"""_Niveles_Automaticos (fecha DATE,n1 REAL,
                    n2 REAL,n3 REAL,n4 REAL,n5 REAL,n6 REAL,n7 REAL,n8 REAL,n9 REAL,n10 REAL,n11 REAL,n12 REAL,
                    n13 REAL,n14 REAL,n15 REAL,n16 REAL,n17 REAL,n18 REAL,n19 REAL,n20 REAL,n21 REAL,n22 REAL,n23 REAL,
                    n24 REAL,codigo REAL,FOREIGN KEY(codigo) REFERENCES Maestro(Codigo))""")
                    
            
            
        cursor.execute ("""CREATE TABLE IF NOT EXISTS """+str(nombre)+"""_Aforos (fecha DATE,N REAL,q REAL,area REAL,V REAL,
                ti REAL,tc REAL,td REAL,L REAL,b REAL,K REAL,codigo REAL,FOREIGN KEY(codigo) REFERENCES Maestro(Codigo))""")
                
            
        cursor.execute ("""CREATE TABLE IF NOT EXISTS """+str(nombre)+"""_Alertas (fecha DATE,
                 h_ama REAL,h_nar REAL,h_roj REAL,codigo REAL,FOREIGN KEY(codigo) REFERENCES Maestro(Codigo))""")

        cursor.execute ("""CREATE TABLE IF NOT EXISTS """+str(nombre)+"""_Caudales (fecha DATE,n1 REAL,
                    n2 REAL,n3 REAL,n4 REAL,n5 REAL,n6 REAL,n7 REAL,n8 REAL,n9 REAL,n10 REAL,n11 REAL,n12 REAL,
                    n13 REAL,n14 REAL,n15 REAL,n16 REAL,n17 REAL,n18 REAL,n19 REAL,n20 REAL,n21 REAL,n22 REAL,n23 REAL,
                    n24 REAL ,codigo REAL, FOREIGN KEY(codigo) REFERENCES Maestro(Codigo))""")
                 
        return True
            



    def csvFile(self):
        "funcion para cargar datos csv a los datos automaticos sqlite"
        self.archivolocacion = QtGui.QFileDialog.getOpenFileName()
        print "La locacion de su archivo es : "+ self.archivolocacion
        conn=sqlite3.connect(self.rutaBD)
        df = pd.read_csv(str(self.archivolocacion))
        df.to_sql(str(self.comboBox.currentText()), conn, if_exists='append', index=False)
        self.Actualizar_Auto()

    def csvFileConvencional(self):
        "funcion para cargar datos csv a los datos automaticos sqlite"
        self.archivolocacion = QtGui.QFileDialog.getOpenFileName()
        print "La locacion de su archivo es : "+ self.archivolocacion
        conn=sqlite3.connect(self.rutaBD)
        df = pd.read_csv(str(self.archivolocacion))
        df.to_sql(str(self.menuEstaciones.currentText()), conn, if_exists='append', index=False)
        self.Actualizar_Manual()

    def csvFileAforo(self):
        "funcion para cargar datos csv a los datos automaticos sqlite"
        self.archivolocacion = QtGui.QFileDialog.getOpenFileName()
        print "La locacion de su archivo es : "+ self.archivolocacion
        conn=sqlite3.connect(self.rutaBD)
        df = pd.read_csv(str(self.archivolocacion))
        df.to_sql(str(self.comboBox_2.currentText()), conn, if_exists='append', index=False)
        self.Actualizar_Aforo()

    def csvFileAlertas(self):
        "funcion para cargar datos csv a los datos automaticos sqlite"
        self.archivolocacion = QtGui.QFileDialog.getOpenFileName()
        print "La locacion de su archivo es : "+ self.archivolocacion
        conn=sqlite3.connect(self.rutaBD)
        df = pd.read_csv(str(self.archivolocacion))
        df.to_sql(str(self.comboBox_3.currentText()), conn, if_exists='append', index=False)
        self.Actualizar_Alerta()

    def csvFileQ(self):
        "funcion para cargar datos csv a los datos automaticos sqlite"
        self.archivolocacion = QtGui.QFileDialog.getOpenFileName()
        print "La locacion de su archivo es : "+ self.archivolocacion
        conn=sqlite3.connect(self.rutaBD)
        df = pd.read_csv(str(self.archivolocacion))
        df.to_sql(str(self.comboBox_4.currentText()), conn, if_exists='append', index=False)
        self.Actualizar_Caudal()


    def borrarL(self):
        conn=sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()

        data3 = str(self.tabla1.currentItem().text())
        aa=cursor.execute("DELETE FROM "+ str(self.menuEstaciones.currentText()) +" WHERE fecha=?", (data3,))
        #cursor.execute("DELETE FROM Zoznam WHERE Name=?", (data3,))  
        conn.commit()
        cursor.close()
        self.Actualizar_Manual()

    def borrarAuto(self):
        conn=sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()

        data3 = str(self.tabal2.currentItem().text())
        aa=cursor.execute("DELETE FROM "+ str(self.comboBox.currentText()) +" WHERE fecha=?", (data3,))
        #cursor.execute("DELETE FROM Zoznam WHERE Name=?", (data3,))  
        conn.commit()
        cursor.close()
        self.Actualizar_Auto()

    def borrarAforo(self):
        conn=sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()

        data3 = str(self.tabla3.currentItem().text())
        aa=cursor.execute("DELETE FROM "+ str(self.comboBox_2.currentText()) +" WHERE fecha=?", (data3,))
        #cursor.execute("DELETE FROM Zoznam WHERE Name=?", (data3,))  
        conn.commit()
        cursor.close()
        self.Actualizar_Aforo()

    def borrarAlerta(self):
        conn=sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()

        data3 = str(self.tabla4.currentItem().text())
        aa=cursor.execute("DELETE FROM "+ str(self.comboBox_3.currentText()) +" WHERE fecha=?", (data3,))
        #cursor.execute("DELETE FROM Zoznam WHERE Name=?", (data3,))  
        conn.commit()
        cursor.close()
        self.Actualizar_Alerta()

    def borrarCaudal(self):
        conn=sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()

        data3 = str(self.tabla6.currentItem().text())
        aa=cursor.execute("DELETE FROM "+ str(self.comboBox_4.currentText()) +" WHERE fecha=?", (data3,))
        #cursor.execute("DELETE FROM Zoznam WHERE Name=?", (data3,))  
        conn.commit()
        cursor.close()
        self.Actualizar_Caudal()

    def Actualizarcelda1(self):
        "modificar las celdas de la estaciones Convencionales"
        conn=sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()
        column=self.tabla1.currentColumn()
        row=self.tabla1.currentRow()
        try:
            ids=str(self.tabla1.item(row,0).text())
            columns=['fecha']+['n'+str(x) for x in range(1,25)]
            value=str(self.tabla1.currentItem().text())
            cursor.execute("UPDATE "+str(self.menuEstaciones.currentText()) +" SET "+columns[column]+'='+ value+' WHERE fecha=?',(ids,))
            conn.commit()
            cursor.close()
            #self.Actualizar_Manual()
        except:
            print("")

    def Actualizarcelda2(self):
        "modificar las celdas de la estaciones Convencionales"
        conn=sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()
        column=self.tabal2.currentColumn()
        row=self.tabal2.currentRow()
        try:
            ids=str(self.tabal2.item(row,0).text())
            columns=['fecha']+['n'+str(x) for x in range(1,25)]
            value=str(self.tabal2.currentItem().text())
            cursor.execute("UPDATE "+str(self.comboBox.currentText()) +" SET "+columns[column]+'='+ value+' WHERE fecha=?',(ids,))
            conn.commit()
            cursor.close()
            #self.Actualizar_Auto()
        except:
            print("")

    def Actualizarcelda3(self):
        "modificar las celdas de la estaciones Convencionales"
        conn=sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()
        column=self.tabla3.currentColumn()
        row=self.tabla3.currentRow()
        try:
            ids=str(self.tabla3.item(row,0).text())
            columns=['fecha']+['n'+str(x) for x in range(1,25)]
            value=str(self.tabla3.currentItem().text())
            cursor.execute("UPDATE "+str(self.comboBox_2.currentText()) +" SET "+columns[column]+'='+ value+' WHERE fecha=?',(ids,))
            conn.commit()
            cursor.close()
            #self.Actualizar_Aforo()
        except:
            print("")

    def Actualizarcelda4(self):
        "modificar las celdas de la estaciones Convencionales"
        conn=sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()
        column=self.tabla4.currentColumn()
        row=self.tabla4.currentRow()
        try:
            ids=str(self.tabla4.item(row,0).text())
            columns=['fecha']+['n'+str(x) for x in range(1,25)]
            value=str(self.tabla4.currentItem().text())
            cursor.execute("UPDATE "+str(self.comboBox_3.currentText()) +" SET "+columns[column]+'='+ value+' WHERE fecha=?',(ids,))
            conn.commit()
            cursor.close()
            #self.Actualizar_Alerta()
        except:
            print("")

    def Actualizarcelda5(self):
        "modificar las celdas Caudales"
        conn=sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()
        column=self.tabla6.currentColumn()
        row=self.tabla1.currentRow()
        try:
            ids=str(self.tabla6.item(row,0).text())
            columns=['fecha']+['n'+str(x) for x in range(1,25)]
            value=str(self.tabla6.currentItem().text())
            cursor.execute("UPDATE "+str(self.comboBox_4.currentText()) +" SET "+columns[column]+'='+ value+' WHERE fecha=?',(ids,))
            conn.commit()
            cursor.close()
            #self.Actualizar_Caudal()# actualizar caudales
        except:
            print("")

    #modificar la ruta de guardado de datos
    def exportCSV1(self):
        name = QtGui.QFileDialog.getSaveFileName()
        ora_conn =sqlite3.connect(self.rutaBD)
        df_ora = pd.read_sql('select * from '+str(self.menuEstaciones.currentText()), con=ora_conn)  
        df_ora.to_csv(name,index_label=False,index=False)

    def exportCSV2(self):
        name = QtGui.QFileDialog.getSaveFileName()
        ora_conn =sqlite3.connect(self.rutaBD)
        df_ora = pd.read_sql('select * from '+str(self.comboBox.currentText()), con=ora_conn)  
        df_ora.to_csv(name,index_label=False,index=False)

    def exportCSV3(self):
        name = QtGui.QFileDialog.getSaveFileName()
        ora_conn =sqlite3.connect(self.rutaBD)
        df_ora = pd.read_sql('select * from '+str(self.comboBox_2.currentText()), con=ora_conn)  
        df_ora.to_csv(name,index_label=False,index=False)

    def exportCSV4(self):
        "exportar datos de la tabla a un csv"
        name = QtGui.QFileDialog.getSaveFileName()
        ora_conn =sqlite3.connect(self.rutaBD)
        df_ora = pd.read_sql('select * from '+str(self.comboBox_3.currentText()), con=ora_conn)  
        df_ora.to_csv(name,index_label=False,index=False)

    def exportCSV5(self):
        "exportar datos de la tabla a un csv"
        name = QtGui.QFileDialog.getSaveFileName()
        ora_conn =sqlite3.connect(self.rutaBD)
        df_ora = pd.read_sql('select * from '+str(self.comboBox_4.currentText()), con=ora_conn)  
        df_ora.to_csv(name,index_label=False,index=False)

    def filtrarConvencionales(self):
        conn = sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()
        date1="'"+str(self.busqueda11.text())+"'"
        date2="'"+str(self.busqueda1.text())+"'"
        cursor.execute('SELECT * FROM ' +str(self.menuEstaciones.currentText())+' WHERE fecha >=  '+date1+" AND fecha<="+date2)  
        self.tabla1.clear()
        self.tabla1.setRowCount(0);
        self.tabla1.setColumnCount(26)
        self.tabla1.setHorizontalHeaderLabels(['fecha']+['N'+str(x) for x in range(1,25)]+['codigo'])
        for row,form in enumerate(cursor):
            self.tabla1.insertRow(row)
            for column,item in enumerate(form):
                self.tabla1.setItem(row,column,QtGui.QTableWidgetItem(str(item)))  

    def filtrarAutomaticas(self):
        conn = sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()
        date1="'"+str(self.busqueda2.text())+"'"
        date2="'"+str(self.busqueda22.text())+"'"
        cursor.execute('SELECT * FROM ' +str(self.comboBox.currentText())+' WHERE fecha >=  '+date1+" AND fecha<="+date2)  
        self.tabal2.clear()
        self.tabal2.setRowCount(0);
        self.tabal2.setColumnCount(26)
        self.tabal2.setHorizontalHeaderLabels(['fecha']+['N'+str(x) for x in range(1,25)]+['codigo'])
        for row,form in enumerate(cursor):
            self.tabal2.insertRow(row)
            for column,item in enumerate(form):
                self.tabal2.setItem(row,column,QtGui.QTableWidgetItem(str(item))) 

    def filtrarCaudales(self):
        conn = sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()
        date1="'"+str(self.busqueda5.text())+"'"
        date2="'"+str(self.busqueda55.text())+"'"
        cursor.execute('SELECT * FROM ' +str(self.comboBox_4.currentText())+' WHERE fecha >=  '+date1+" AND fecha<="+date2)  
        self.tabla6.clear()
        self.tabla6.setRowCount(0);
        self.tabla6.setColumnCount(26)
        self.tabla6.setHorizontalHeaderLabels(['fecha']+['N'+str(x) for x in range(1,25)]+['codigo'])
        for row,form in enumerate(cursor):
            self.tabla6.insertRow(row)
            for column,item in enumerate(form):
                self.tabla6.setItem(row,column,QtGui.QTableWidgetItem(str(item))) 

    def filtrarAforos(self):
        conn = sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()
        date1="'"+str(self.busqueda3.text())+"'"
        date2="'"+str(self.busqueda33.text())+"'"
        cursor.execute('SELECT * FROM ' +str(self.comboBox_2.currentText())+' WHERE fecha >=  '+date1+" AND fecha<="+date2)  
        self.tabla3.clear()
        self.tabla3.setRowCount(0);
        self.tabla3.setColumnCount(12)
        self.tabla3.setHorizontalHeaderLabels(['fecha']+['N'+str(x) for x in range(1,11)]+['codigo'])
        for row,form in enumerate(cursor):
            self.tabla3.insertRow(row)
            for column,item in enumerate(form):
                self.tabla3.setItem(row,column,QtGui.QTableWidgetItem(str(item))) 

    def filtrarAlertas(self):
        conn = sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()
        date1="'"+str(self.busqueda4.text())+"'"
        date2="'"+str(self.busqueda44.text())+"'"
        cursor.execute('SELECT * FROM ' +str(self.comboBox_3.currentText())+' WHERE fecha >=  '+date1+" AND fecha<="+date2)  
        self.tabla4.clear()
        self.tabla4.setRowCount(0);
        self.tabla4.setColumnCount(5)
        self.tabla4.setHorizontalHeaderLabels(['fecha']+['A'+str(x) for x in range(1,4)]+['codigo'])
        for row,form in enumerate(cursor):
            self.tabla4.insertRow(row)
            for column,item in enumerate(form):
                self.tabla4.setItem(row,column,QtGui.QTableWidgetItem(str(item))) 

    def tablaMaestro(self):
        conn=sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()
        cursor.execute ("""CREATE TABLE IF NOT EXISTS Maestro (Codigo string,
        Nombre string,DRE string,SisHidro string,
                 Cuenca string,rio string,DPTO string,PROV string,
                 DISTRITO string,LONG string,
                 LAT string,ALT string, Inicio string,ENT string,Q string)""")

    def ayuda(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setText("""
        Este Programa a sido realizado por:
        Programador:Jose Augusto Zevallos Ruiz 
        Visualizacion y Testeo: Carloz Martinez
        Director de Hidrologia: Oscar Felipe Obando
        Director de Operativa: Ing. Arboleda
        contacto : ingjosezr@gmail.com

        """)
        ret = msgBox.exec_()

    def lista(self):
        "lista todas las tablas contenidas en la base de datos"
        conn=sqlite3.connect(self.rutaBD)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        resul=cursor.fetchall()
        re=[resul[i][0] for i in range(len(resul))]

        return re
    def openDB(self):
        "localizar la base de datos correspodiente"
        self.rutaBD=str(QtGui.QFileDialog.getOpenFileName())
        lista=self.lista()
        self.menuEstaciones.addItems(filter(lambda k: '_Niveles_Convencionales' in k,lista))
        self.comboBox.addItems(filter(lambda k: '_Niveles_Automaticos' in k, lista))  
        self.comboBox_2.addItems(filter(lambda k: '_Aforos' in k, lista)) 
        self.comboBox_3.addItems(filter(lambda k: '_Alertas' in k, lista)) 
        self.comboBox_4.addItems(filter(lambda k: '_Caudales' in k, lista))
        self.Actualizar_Maestro()

    def borrarTabla(self):
        pass

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())