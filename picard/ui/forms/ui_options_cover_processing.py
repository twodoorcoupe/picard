# Form implementation generated from reading ui file 'ui/options_cover_processing.ui'
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


class Ui_CoverProcessingOptionsPage(object):
    def setupUi(self, CoverProcessingOptionsPage):
        CoverProcessingOptionsPage.setObjectName("CoverProcessingOptionsPage")
        CoverProcessingOptionsPage.resize(535, 467)
        self.verticalLayout = QtWidgets.QVBoxLayout(CoverProcessingOptionsPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.filtering = QtWidgets.QGroupBox(parent=CoverProcessingOptionsPage)
        self.filtering.setCheckable(True)
        self.filtering.setChecked(False)
        self.filtering.setObjectName("filtering")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.filtering)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.filtering_width_widget = QtWidgets.QWidget(parent=self.filtering)
        self.filtering_width_widget.setObjectName("filtering_width_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.filtering_width_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filtering_width_label = QtWidgets.QLabel(parent=self.filtering_width_widget)
        self.filtering_width_label.setObjectName("filtering_width_label")
        self.horizontalLayout.addWidget(self.filtering_width_label)
        self.filtering_width_value = QtWidgets.QSpinBox(parent=self.filtering_width_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filtering_width_value.sizePolicy().hasHeightForWidth())
        self.filtering_width_value.setSizePolicy(sizePolicy)
        self.filtering_width_value.setMaximum(9999)
        self.filtering_width_value.setProperty("value", 250)
        self.filtering_width_value.setObjectName("filtering_width_value")
        self.horizontalLayout.addWidget(self.filtering_width_value)
        self.px_label1 = QtWidgets.QLabel(parent=self.filtering_width_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.px_label1.sizePolicy().hasHeightForWidth())
        self.px_label1.setSizePolicy(sizePolicy)
        self.px_label1.setObjectName("px_label1")
        self.horizontalLayout.addWidget(self.px_label1)
        self.verticalLayout_2.addWidget(self.filtering_width_widget)
        self.filtering_height_widget = QtWidgets.QWidget(parent=self.filtering)
        self.filtering_height_widget.setObjectName("filtering_height_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.filtering_height_widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.filtering_height_label = QtWidgets.QLabel(parent=self.filtering_height_widget)
        self.filtering_height_label.setObjectName("filtering_height_label")
        self.horizontalLayout_2.addWidget(self.filtering_height_label)
        self.filtering_height_value = QtWidgets.QSpinBox(parent=self.filtering_height_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filtering_height_value.sizePolicy().hasHeightForWidth())
        self.filtering_height_value.setSizePolicy(sizePolicy)
        self.filtering_height_value.setMaximum(9999)
        self.filtering_height_value.setProperty("value", 250)
        self.filtering_height_value.setObjectName("filtering_height_value")
        self.horizontalLayout_2.addWidget(self.filtering_height_value)
        self.px_label2 = QtWidgets.QLabel(parent=self.filtering_height_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.px_label2.sizePolicy().hasHeightForWidth())
        self.px_label2.setSizePolicy(sizePolicy)
        self.px_label2.setObjectName("px_label2")
        self.horizontalLayout_2.addWidget(self.px_label2)
        self.verticalLayout_2.addWidget(self.filtering_height_widget)
        self.verticalLayout.addWidget(self.filtering)
        self.resizing = QtWidgets.QGroupBox(parent=CoverProcessingOptionsPage)
        self.resizing.setCheckable(False)
        self.resizing.setChecked(False)
        self.resizing.setObjectName("resizing")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.resizing)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tags_scale_down = QtWidgets.QGroupBox(parent=self.resizing)
        self.tags_scale_down.setCheckable(True)
        self.tags_scale_down.setChecked(False)
        self.tags_scale_down.setObjectName("tags_scale_down")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tags_scale_down)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tags_resize_mode = QtWidgets.QComboBox(parent=self.tags_scale_down)
        self.tags_resize_mode.setObjectName("tags_resize_mode")
        self.tags_resize_mode.addItem("")
        self.tags_resize_mode.addItem("")
        self.tags_resize_mode.addItem("")
        self.verticalLayout_3.addWidget(self.tags_resize_mode)
        self.tags_resize_width_widget = QtWidgets.QWidget(parent=self.tags_scale_down)
        self.tags_resize_width_widget.setObjectName("tags_resize_width_widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tags_resize_width_widget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tags_resize_width_label = QtWidgets.QCheckBox(parent=self.tags_resize_width_widget)
        self.tags_resize_width_label.setObjectName("tags_resize_width_label")
        self.horizontalLayout_5.addWidget(self.tags_resize_width_label)
        self.tags_resize_width_value = QtWidgets.QSpinBox(parent=self.tags_resize_width_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tags_resize_width_value.sizePolicy().hasHeightForWidth())
        self.tags_resize_width_value.setSizePolicy(sizePolicy)
        self.tags_resize_width_value.setMaximum(9999)
        self.tags_resize_width_value.setProperty("value", 1000)
        self.tags_resize_width_value.setObjectName("tags_resize_width_value")
        self.horizontalLayout_5.addWidget(self.tags_resize_width_value)
        self.px_label5 = QtWidgets.QLabel(parent=self.tags_resize_width_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.px_label5.sizePolicy().hasHeightForWidth())
        self.px_label5.setSizePolicy(sizePolicy)
        self.px_label5.setObjectName("px_label5")
        self.horizontalLayout_5.addWidget(self.px_label5)
        self.verticalLayout_3.addWidget(self.tags_resize_width_widget)
        self.tags_resize_height_widget = QtWidgets.QWidget(parent=self.tags_scale_down)
        self.tags_resize_height_widget.setObjectName("tags_resize_height_widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tags_resize_height_widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tags_resize_height_label = QtWidgets.QCheckBox(parent=self.tags_resize_height_widget)
        self.tags_resize_height_label.setObjectName("tags_resize_height_label")
        self.horizontalLayout_3.addWidget(self.tags_resize_height_label)
        self.tags_resize_height_value = QtWidgets.QSpinBox(parent=self.tags_resize_height_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tags_resize_height_value.sizePolicy().hasHeightForWidth())
        self.tags_resize_height_value.setSizePolicy(sizePolicy)
        self.tags_resize_height_value.setMaximum(9999)
        self.tags_resize_height_value.setProperty("value", 1000)
        self.tags_resize_height_value.setObjectName("tags_resize_height_value")
        self.horizontalLayout_3.addWidget(self.tags_resize_height_value)
        self.px_label6 = QtWidgets.QLabel(parent=self.tags_resize_height_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.px_label6.sizePolicy().hasHeightForWidth())
        self.px_label6.setSizePolicy(sizePolicy)
        self.px_label6.setObjectName("px_label6")
        self.horizontalLayout_3.addWidget(self.px_label6)
        self.verticalLayout_3.addWidget(self.tags_resize_height_widget)
        self.tags_scale_up = QtWidgets.QCheckBox(parent=self.tags_scale_down)
        self.tags_scale_up.setObjectName("tags_scale_up")
        self.verticalLayout_3.addWidget(self.tags_scale_up)
        self.horizontalLayout_7.addWidget(self.tags_scale_down)
        self.file_scale_down = QtWidgets.QGroupBox(parent=self.resizing)
        self.file_scale_down.setCheckable(True)
        self.file_scale_down.setObjectName("file_scale_down")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.file_scale_down)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.file_resize_mode = QtWidgets.QComboBox(parent=self.file_scale_down)
        self.file_resize_mode.setObjectName("file_resize_mode")
        self.file_resize_mode.addItem("")
        self.file_resize_mode.addItem("")
        self.file_resize_mode.addItem("")
        self.verticalLayout_4.addWidget(self.file_resize_mode)
        self.file_scale_widget = QtWidgets.QWidget(parent=self.file_scale_down)
        self.file_scale_widget.setObjectName("file_scale_widget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.file_scale_widget)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_4.addWidget(self.file_scale_widget)
        self.file_resize_width_widget = QtWidgets.QWidget(parent=self.file_scale_down)
        self.file_resize_width_widget.setObjectName("file_resize_width_widget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.file_resize_width_widget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.file_resize_width_label = QtWidgets.QCheckBox(parent=self.file_resize_width_widget)
        self.file_resize_width_label.setObjectName("file_resize_width_label")
        self.horizontalLayout_6.addWidget(self.file_resize_width_label)
        self.file_resize_width_value = QtWidgets.QSpinBox(parent=self.file_resize_width_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_resize_width_value.sizePolicy().hasHeightForWidth())
        self.file_resize_width_value.setSizePolicy(sizePolicy)
        self.file_resize_width_value.setMaximum(9999)
        self.file_resize_width_value.setProperty("value", 1000)
        self.file_resize_width_value.setObjectName("file_resize_width_value")
        self.horizontalLayout_6.addWidget(self.file_resize_width_value)
        self.px_label3 = QtWidgets.QLabel(parent=self.file_resize_width_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.px_label3.sizePolicy().hasHeightForWidth())
        self.px_label3.setSizePolicy(sizePolicy)
        self.px_label3.setObjectName("px_label3")
        self.horizontalLayout_6.addWidget(self.px_label3)
        self.verticalLayout_4.addWidget(self.file_resize_width_widget)
        self.file_resize_height_widget = QtWidgets.QWidget(parent=self.file_scale_down)
        self.file_resize_height_widget.setObjectName("file_resize_height_widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.file_resize_height_widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.file_resize_height_label = QtWidgets.QCheckBox(parent=self.file_resize_height_widget)
        self.file_resize_height_label.setObjectName("file_resize_height_label")
        self.horizontalLayout_4.addWidget(self.file_resize_height_label)
        self.file_resize_height_value = QtWidgets.QSpinBox(parent=self.file_resize_height_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_resize_height_value.sizePolicy().hasHeightForWidth())
        self.file_resize_height_value.setSizePolicy(sizePolicy)
        self.file_resize_height_value.setMaximum(9999)
        self.file_resize_height_value.setProperty("value", 1000)
        self.file_resize_height_value.setObjectName("file_resize_height_value")
        self.horizontalLayout_4.addWidget(self.file_resize_height_value)
        self.px_label4 = QtWidgets.QLabel(parent=self.file_resize_height_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.px_label4.sizePolicy().hasHeightForWidth())
        self.px_label4.setSizePolicy(sizePolicy)
        self.px_label4.setObjectName("px_label4")
        self.horizontalLayout_4.addWidget(self.px_label4)
        self.verticalLayout_4.addWidget(self.file_resize_height_widget)
        self.file_scale_up = QtWidgets.QCheckBox(parent=self.file_scale_down)
        self.file_scale_up.setObjectName("file_scale_up")
        self.verticalLayout_4.addWidget(self.file_scale_up)
        self.horizontalLayout_7.addWidget(self.file_scale_down)
        self.verticalLayout.addWidget(self.resizing)
        self.converting = QtWidgets.QGroupBox(parent=CoverProcessingOptionsPage)
        self.converting.setCheckable(False)
        self.converting.setChecked(False)
        self.converting.setObjectName("converting")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.converting)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.convert_tags = QtWidgets.QGroupBox(parent=self.converting)
        self.convert_tags.setCheckable(True)
        self.convert_tags.setObjectName("convert_tags")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.convert_tags)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.convert_tags_label = QtWidgets.QLabel(parent=self.convert_tags)
        self.convert_tags_label.setObjectName("convert_tags_label")
        self.horizontalLayout_13.addWidget(self.convert_tags_label)
        self.convert_tags_format = QtWidgets.QComboBox(parent=self.convert_tags)
        self.convert_tags_format.setObjectName("convert_tags_format")
        self.convert_tags_format.addItem("")
        self.convert_tags_format.addItem("")
        self.convert_tags_format.addItem("")
        self.convert_tags_format.addItem("")
        self.horizontalLayout_13.addWidget(self.convert_tags_format)
        self.horizontalLayout_12.addWidget(self.convert_tags)
        self.convert_file = QtWidgets.QGroupBox(parent=self.converting)
        self.convert_file.setCheckable(True)
        self.convert_file.setObjectName("convert_file")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.convert_file)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.convert_file_label = QtWidgets.QLabel(parent=self.convert_file)
        self.convert_file_label.setObjectName("convert_file_label")
        self.horizontalLayout_14.addWidget(self.convert_file_label)
        self.convert_file_format = QtWidgets.QComboBox(parent=self.convert_file)
        self.convert_file_format.setObjectName("convert_file_format")
        self.convert_file_format.addItem("")
        self.convert_file_format.addItem("")
        self.convert_file_format.addItem("")
        self.convert_file_format.addItem("")
        self.horizontalLayout_14.addWidget(self.convert_file_format)
        self.horizontalLayout_12.addWidget(self.convert_file)
        self.verticalLayout.addWidget(self.converting)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(CoverProcessingOptionsPage)
        QtCore.QMetaObject.connectSlotsByName(CoverProcessingOptionsPage)

    def retranslateUi(self, CoverProcessingOptionsPage):
        CoverProcessingOptionsPage.setWindowTitle(_("Form"))
        self.filtering.setTitle(_("Discard images if below the given size"))
        self.filtering_width_label.setText(_("Minimum width:"))
        self.px_label1.setText(_("px"))
        self.filtering_height_label.setText(_("Minimum height:"))
        self.px_label2.setText(_("px"))
        self.resizing.setTitle(_("Resize images to the given size"))
        self.tags_scale_down.setTitle(_("Resize images saved to tags "))
        self.tags_resize_mode.setItemText(0, _("Maintain aspect ratio"))
        self.tags_resize_mode.setItemText(1, _("Crop to fit"))
        self.tags_resize_mode.setItemText(2, _("Stretch to fit"))
        self.tags_resize_width_label.setText(_("Width:"))
        self.px_label5.setText(_("px"))
        self.tags_resize_height_label.setText(_("Height:"))
        self.px_label6.setText(_("px"))
        self.tags_scale_up.setText(_("Don\'t enlarge"))
        self.file_scale_down.setTitle(_("Resize images saved to files"))
        self.file_resize_mode.setItemText(0, _("Maintain aspect ratio"))
        self.file_resize_mode.setItemText(1, _("Crop to fit"))
        self.file_resize_mode.setItemText(2, _("Stretch to fit"))
        self.file_resize_width_label.setText(_("Width:"))
        self.px_label3.setText(_("px"))
        self.file_resize_height_label.setText(_("Height:"))
        self.px_label4.setText(_("px"))
        self.file_scale_up.setText(_("Don\'t enlarge"))
        self.converting.setTitle(_("Convert images to the given format"))
        self.convert_tags.setTitle(_("Convert images saved to tags"))
        self.convert_tags_label.setText(_("New format:"))
        self.convert_tags_format.setItemText(0, _("JPEG"))
        self.convert_tags_format.setItemText(1, _("PNG"))
        self.convert_tags_format.setItemText(2, _("WebP"))
        self.convert_tags_format.setItemText(3, _("TIFF"))
        self.convert_file.setTitle(_("Convert images saved to files"))
        self.convert_file_label.setText(_("New format:"))
        self.convert_file_format.setItemText(0, _("JPEG"))
        self.convert_file_format.setItemText(1, _("PNG"))
        self.convert_file_format.setItemText(2, _("WebP"))
        self.convert_file_format.setItemText(3, _("TIFF"))
