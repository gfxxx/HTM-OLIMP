# -*- coding: utf-8 -*-

"""
Miscellaneous functions used in the program
"""

import sys
import os
from PySide6.QtWidgets import QLineEdit, QComboBox, QHBoxLayout
from PySide6.QtCore import Qt, Signal
from typing import Callable, Type
import numpy as np
import numpy.typing as npt

from HT.materials_library import MaterialTemplate, Rammed_Earth, Hempcrete


def create_input_layers(i: int) -> QHBoxLayout:
    """
    Create layers input in settings page

    Parameters
    ----------
    i:
        Actual number of the layer

    Returns
    -------
    Layout with all input field for each layers
    """
    layout = QHBoxLayout()
    layout.setAlignment(Qt.AlignTop)

    # Style Sheets
    text_ss = "background: transparent; border: none; color:white;"
    input_ss = "background-color: rgba(255, 255, 255, 0.2); border:none; color:white;"
    dropdown_ss = """
    QComboBox{
        background-color: rgba(255, 255, 255, 0.2);
        border:none;
        color:white;
    }
    QComboBox::item{
        color: white;
    }
    QComboBox::item:selected{
        background-color: gray;
    }
    QComboBox QAbstractItemView{
	    background-color: "#343434";
        color: white;
    }
    QComboBox QAbstractItemView::item:selected{
	    background-color: gray;
    }
    """
    # ----- Layer text ----- #
    layer_text = QLineEdit()
    layer_text.setText(f"Layer {i}: ")
    layer_text.setReadOnly(True)
    layer_text.setStyleSheet(text_ss)
    layer_text.setMaximumWidth(60)
    layout.addWidget(layer_text)

    size_layout = QHBoxLayout()
    size_layout.setAlignment(Qt.AlignLeft)

    # ----- Size text ----- #
    size_text = QLineEdit()
    size_text.setText("size [m]: ")
    size_text.setReadOnly(True)
    size_text.setStyleSheet(text_ss)
    size_text.setMaximumWidth(60)
    size_layout.addWidget(size_text)

    # ----- Size input ----- #
    size_input = QLineEdit()
    size_input.setText("0.5")
    size_input.setObjectName(f"size_{i}")
    size_input.setStyleSheet(input_ss)
    size_input.setMaximumWidth(50)
    size_layout.addWidget(size_input)

    material_layout = QHBoxLayout()
    material_layout.setAlignment(Qt.AlignLeft)

    # ----- Material text ----- #
    material_text = QLineEdit()
    material_text.setText("Material: ")
    material_text.setReadOnly(True)
    material_text.setStyleSheet(text_ss)
    material_text.setMaximumWidth(60)
    material_layout.addWidget(material_text)

    # ----- Material input ----- #
    material_input = QComboBox()
    material_input.addItem("Rammed Earth")
    material_input.addItem("Hempcrete")
    material_input.addItem("Custom")
    material_input.setObjectName(f"material_{i}")
    material_input.setStyleSheet(dropdown_ss)
    material_input.setMaximumWidth(200)
    material_layout.addWidget(material_input)

    layout.addLayout(size_layout, stretch=1)
    layout.addLayout(material_layout, stretch=2)

    return layout


def deleteItemsOfLayout(layout: QHBoxLayout) -> None:
    """
    Delete all items in a layout

    Parameters
    ----------
    layout:
        Layout on which items will be deleted
    """
    if layout is not None:
        while (item := layout.takeAt(0)) != None:
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
            else:
                deleteItemsOfLayout(item.layout())


def create_const(d: dict) -> dict:
    """
    Take all material parameters, if field is an array, take first value and format it

    Parameters
    ----------
    d:
        Dictionary of materials parameters
    """
    for key, value in d.items():
        if isinstance(value, np.ndarray):
            d[key] = '{:.2e}'.format(float(value[0][0]))
    return d


def material_factory(material: str) -> Type[MaterialTemplate]:
    """
    Choose between all material in database

    Parameters
    ----------
    material:
        Choosen material

    Returns
    -------
    Corresponding Material in the library
    """
    match material:
        case "Rammed Earth":
            return Rammed_Earth
        case "Hempcrete":
            return Hempcrete
        case _:
            return MaterialTemplate


def check_modified(ui: QLineEdit, material: Callable, array: list) -> None:
    """
    Check if a material parameters input field has been changed, and add value to array

    Parameters
    ----------
    ui:
        Input field
    material:
        Material method
    array:
        Parameter array where value is saved
    """
    if not ui.isModified():
        array.append(material)
    else:
        array.append(ui.text())


def check_callable(func: Callable | float, args: list = []) -> Callable | float:
    """
    Check if function or constant

    Parameters
    ----------
    func:
        Element to check
    args:
        Potential arguments of func

    Returns
    -------
    Return value of const or result of func if callable
    """
    if callable(func):
        f = func(*args)
        if len(f) == 3:
            return f[0]
        else:
            return f
    return func


def create_array_material(n_nodes: npt.NDArray[np.int64], tot: int, const: Callable | float, args: list = [], other = []) -> \
npt.NDArray[np.float64]:
    """
    Create an array for ``const``

    Parameters
    ----------
    n_nodes:
        Number of nodes for each layer
    tot:
        Number of node total
    const:
        Material parameter
    args:
        Potential arguments of Material parameter

    Returns
    -------
    Array for ``const``
    """
    array = np.zeros([tot, 1])
    n_tot = 0  # keep track of where we are
    for i, node in enumerate(n_nodes):
        n = int(node[0])
        if i == 0:
            args_n = [arg[:n] for arg in args]
            if len(other) > 0:
                args_n.extend([o[i] for o in other])
            array[:n] = check_callable(const[i], args_n)
        else:
            args_n = [arg[n_tot: n_tot + n] for arg in args]
            array[n_tot: n_tot + n] = check_callable(const[i], args_n)

        n_tot += n
    return array


def reconnect(signal: Callable[[], Signal], new_handler: Callable | None = None):
    """Check if ``signal``is connected.
    If so, disconnect the signal and reconnect with ``new_handler``

    Parameters
    ----------
    signal:
        The signal to check
    new_handler:
        The new connection to create
    """
    try:
        signal.disconnect()
    except RuntimeError:
        pass
    if new_handler is not None:
        signal.connect(new_handler)

def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller
    See stackoverflow answer: https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile
    """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

