# -*- coding: utf-8 -*-

"""
Create a new table to display in GUI
"""

from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex, QPersistentModelIndex
import pandas as pd


class TableModel(QAbstractTableModel):
    """
        Create the model to display result table
    """
    def __init__(self, data: pd.DataFrame):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int = Qt.DisplayRole) -> str | None:
        """
        Override data method of QAbstractTableModel
        """
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)
        return None

    def rowCount(self, parent: QModelIndex | QPersistentModelIndex = QModelIndex()) -> int:
        """
        Override rowCount method of QAbstractTableModel
        """
        return self._data.shape[0]

    def columnCount(self, parent: QModelIndex | QPersistentModelIndex = QModelIndex()) -> int:
        """
        Override columnCount method of QAbstractTableModel
        """
        return self._data.shape[1]

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.DisplayRole) -> str | None:
        """
        Override headerData method of QAbstractTableModel
        """
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            if orientation == Qt.Vertical:
                return str(self._data.index[section])
        return None
