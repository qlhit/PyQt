from PyQt5 import QtWidgets,QtCore
from PyQt5.QtCore import Qt
from typing import List
import sys

class ExtendedComboBox(QtWidgets.QComboBox):
    def __init__(self, parent=None):
        super(ExtendedComboBox, self).__init__(parent)

        self.setFocusPolicy(Qt.StrongFocus)
        self.setEditable(True)

        # add a filter model to filter matching items
        self.pFilterModel = QtCore.QSortFilterProxyModel(self)
        self.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pFilterModel.setSourceModel(self.model())

        # add a completer, which uses the filter model
        self.completer = QtWidgets.QCompleter(self.pFilterModel, self)
        # always show all (filtered) completions
        self.completer.setCompletionMode(QtWidgets.QCompleter.UnfilteredPopupCompletion)
        self.setCompleter(self.completer)

        # connect signals
        self.lineEdit().textEdited.connect(self.pFilterModel.setFilterFixedString)
        self.completer.activated.connect(self.on_completer_activated)

    # on selection of an item from the completer, select the corresponding item from combobox
    def on_completer_activated(self, text):
        if text:
            index = self.findText(text)
            self.setCurrentIndex(index)
            self.activated[str].emit(self.itemText(index))

    # on model change, update the models of the filter and completer as well
    def setModel(self, model):
        super(ExtendedComboBox, self).setModel(model)
        self.pFilterModel.setSourceModel(model)
        self.completer.setModel(self.pFilterModel)

    # on model column change, update the model column of the filter and completer as well
    def setModelColumn(self, column):
        self.completer.setCompletionColumn(column)
        self.pFilterModel.setFilterKeyColumn(column)
        super(ExtendedComboBox, self).setModelColumn(column)


class MultiChoiceWidget(QtWidgets.QWidget):
    def __init__(self,left_list:List[str]):
        super().__init__()
        self.left_name_list = left_list
        self.init_ui()
        pass
    def init_ui(self):
        self.setWindowTitle("多项选择")
        self.setMinimumWidth(1000)
        self.setMinimumHeight(600)

        check_submit_btn = QtWidgets.QPushButton('确认提交')
        check_submit_btn.clicked.connect(self.check_submit_btn_clicked)

        layout_0 = QtWidgets.QHBoxLayout()
        layout_0.addStretch(1)
        layout_0.addWidget(check_submit_btn)

        self.combox = ExtendedComboBox()
        self.combox.addItems(self.left_name_list)
        self.combox.currentTextChanged.connect(self.combox_currentTextChanged)

        self.left_list_widget = QtWidgets.QListWidget()
        self.left_list_widget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.left_list_widget.addItems(self.left_name_list)

        layout_1 = QtWidgets.QVBoxLayout()
        layout_1.addWidget(self.combox)
        layout_1.addWidget(self.left_list_widget)

        add_btn = QtWidgets.QPushButton('添加>>')
        add_btn.clicked.connect(self.add_btn_clicked)
        del_btn = QtWidgets.QPushButton('<<删除')
        del_btn.clicked.connect(self.del_btn_clicked)
        all_selected_btn = QtWidgets.QPushButton('全选')
        all_selected_btn.clicked.connect(self.all_selected_btn_clicked)
        cancel_seleced_btn = QtWidgets.QPushButton('取消选中')
        cancel_seleced_btn.clicked.connect(self.cancel_seleced_btn_clicked)
        clear_btn = QtWidgets.QPushButton('清空')
        clear_btn.clicked.connect(self.clear_btn_clicked)

        layout_2 = QtWidgets.QVBoxLayout()
        layout_2.addStretch(1)
        layout_2.addWidget(add_btn)
        layout_2.addWidget(del_btn)
        layout_2.addWidget(all_selected_btn)
        layout_2.addWidget(cancel_seleced_btn)
        layout_2.addWidget(clear_btn)
        layout_2.addStretch(1)

        self.right_list_widget = QtWidgets.QListWidget()
        self.right_list_widget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

        layout_3 = QtWidgets.QHBoxLayout()
        layout_3.addLayout(layout_1)
        layout_3.addLayout(layout_2)
        layout_3.addWidget(self.right_list_widget)

        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(layout_0)
        layout.addLayout(layout_3)
        self.setLayout(layout)
        pass
    def combox_currentTextChanged(self,cur_text:str):
        '''下拉框选中'''
        total_count = self.left_list_widget.count()
        for i in range(total_count):
            item = self.left_list_widget.item(i)
            if item.text() == cur_text:
                item.setSelected(True)
                self.left_list_widget.setCurrentRow(i)
                break
        pass
    def check_submit_btn_clicked(self):
        '''确认提交'''
        text_list = self.gain_right_all_list_text()
        if len(text_list)<=0:
            QtWidgets.QMessageBox.information(
                self,
                '提示',
                '您没有选择任何项',
                QtWidgets.QMessageBox.Ok
            )
            return
        print(text_list)
        pass
    def add_btn_clicked(self):
        '''从左侧添加项到右侧'''
        selected_items = self.left_list_widget.selectedItems()
        if len(selected_items)<=0:
            QtWidgets.QMessageBox.information(
                self,
                '提示',
                '请选择要添加的项',
                QtWidgets.QMessageBox.Ok
            )
            return
        text_list = [i.text() for i in selected_items]
        right_text_list = self.gain_right_all_list_text()
        for item in text_list:
            if item in right_text_list:
                continue
            self.right_list_widget.addItem(item)
        self.cancel_left_list_selected()
        pass
    def gain_right_all_list_text(self)->List[str]:
        '''获取右侧列表中所有相的文本'''
        right_total_count = self.right_list_widget.count()
        text_list = []
        for i in range(right_total_count):
            item = self.right_list_widget.item(i)
            text_list.append(item.text())
        return text_list
    def del_btn_clicked(self):
        '''从右侧将项删除'''
        selected_items = self.right_list_widget.selectedItems()
        if len(selected_items)<=0:
            return
        for item in selected_items:
            # 拿出对象（凭借对象得到行数）以后移除
            self.right_list_widget.removeItemWidget(self.right_list_widget.takeItem(self.right_list_widget.row(item)))
        pass
    def all_selected_btn_clicked(self):
        '''将左侧的项全部选中'''
        total_count = self.left_list_widget.count()
        for i in range(total_count):
            item = self.left_list_widget.item(i)
            item.setSelected(True)
        pass
    def cancel_seleced_btn_clicked(self):
        '''取消左右两侧已选中的项'''
        self.cancel_left_list_selected()
        self.cancel_right_list_selected()
        pass
    def cancel_left_list_selected(self):
        selected_items = self.left_list_widget.selectedItems()
        if len(selected_items)<=0:
            return
        for item in selected_items:
            item.setSelected(False)
        pass
    def cancel_right_list_selected(self):
        selected_items = self.right_list_widget.selectedItems()
        if len(selected_items)<=0:
            return
        for item in selected_items:
            item.setSelected(False)
        pass
    def clear_btn_clicked(self):
        '''清空右侧'''
        self.right_list_widget.clear()
        pass
    pass

if __name__ == '__main__':
    temp_list = ["aaaaaa","bbbbbb","cccccc","dddddd","eeeeee","ffffff","gggggg","aabbcc","123aa"]

    app = QtWidgets.QApplication(sys.argv)
    temp_widget = MultiChoiceWidget(temp_list)
    temp_widget.show()
    sys.exit(app.exec_())
