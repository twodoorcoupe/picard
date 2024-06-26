# Form implementation generated from reading ui file 'ui/multi_locale_selector.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# Automatically generated - do not edit.
# Use `python setup.py build_ui` to update it.

from PyQt6 import (
    QtCore,
    QtGui,
    QtWidgets,
)

from picard.i18n import gettext as _


class Ui_MultiLocaleSelector(object):
    def setupUi(self, MultiLocaleSelector):
        MultiLocaleSelector.setObjectName("MultiLocaleSelector")
        MultiLocaleSelector.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        MultiLocaleSelector.resize(507, 284)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MultiLocaleSelector.sizePolicy().hasHeightForWidth())
        MultiLocaleSelector.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(MultiLocaleSelector)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=MultiLocaleSelector)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.selected_locales = QtWidgets.QListWidget(parent=MultiLocaleSelector)
        self.selected_locales.setObjectName("selected_locales")
        self.verticalLayout_2.addWidget(self.selected_locales)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.move_up = QtWidgets.QToolButton(parent=MultiLocaleSelector)
        self.move_up.setText("")
        icon = QtGui.QIcon.fromTheme(":/images/16x16/go-up.png")
        self.move_up.setIcon(icon)
        self.move_up.setObjectName("move_up")
        self.verticalLayout_3.addWidget(self.move_up)
        self.add_locale = QtWidgets.QToolButton(parent=MultiLocaleSelector)
        self.add_locale.setText("")
        icon = QtGui.QIcon.fromTheme(":/images/16x16/go-previous.png")
        self.add_locale.setIcon(icon)
        self.add_locale.setObjectName("add_locale")
        self.verticalLayout_3.addWidget(self.add_locale)
        self.remove_locale = QtWidgets.QToolButton(parent=MultiLocaleSelector)
        self.remove_locale.setText("")
        icon = QtGui.QIcon.fromTheme(":/images/16x16/go-next.png")
        self.remove_locale.setIcon(icon)
        self.remove_locale.setObjectName("remove_locale")
        self.verticalLayout_3.addWidget(self.remove_locale)
        self.move_down = QtWidgets.QToolButton(parent=MultiLocaleSelector)
        self.move_down.setText("")
        icon = QtGui.QIcon.fromTheme(":/images/16x16/go-down.png")
        self.move_down.setIcon(icon)
        self.move_down.setObjectName("move_down")
        self.verticalLayout_3.addWidget(self.move_down)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(parent=MultiLocaleSelector)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.available_locales = QtWidgets.QListWidget(parent=MultiLocaleSelector)
        self.available_locales.setObjectName("available_locales")
        self.verticalLayout_4.addWidget(self.available_locales)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.button_box = QtWidgets.QDialogButtonBox(parent=MultiLocaleSelector)
        self.button_box.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Save)
        self.button_box.setObjectName("button_box")
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(MultiLocaleSelector)
        QtCore.QMetaObject.connectSlotsByName(MultiLocaleSelector)

    def retranslateUi(self, MultiLocaleSelector):
        MultiLocaleSelector.setWindowTitle(_("Locale Selector"))
        self.label.setText(_("Selected Locales"))
        self.move_up.setToolTip(_("Move selected locale up"))
        self.add_locale.setToolTip(_("Add to selected locales"))
        self.remove_locale.setToolTip(_("Remove selected locale"))
        self.move_down.setToolTip(_("Move selected locale down"))
        self.label_2.setText(_("Available Locales"))
