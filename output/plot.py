# -*- coding: utf-8 -*-

"""
Display a plot in GUI
"""

from PySide6.QtWidgets import QFileDialog, QVBoxLayout, QWidget
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas  # type: ignore
from matplotlib.figure import Figure  # type: ignore
import pandas as pd
import numpy as np
import numpy.typing as npt
from typing import Callable
import platform
import math

from HT.mesh import Mesh
from functions import deleteItemsOfLayout, reconnect
from const_ui import Ui_Form


class MplCanvas(FigureCanvas):
    """
        Create Canvas model for result plotting
    """

    def __init__(self):
        fig = Figure(figsize=(7, 5), facecolor=(0, 0, 0, 0), tight_layout=True)
        self.axes = fig.add_subplot(111, facecolor='#AAA')  # Create figure

        super(MplCanvas, self).__init__(fig)

    def plot(self, widget: QWidget, xdata: pd.Series, ydata: pd.Series, xlabel: str, ylabel: str, loc: str,
             title=None) -> None:
        """
        Create matplotlib plot and add it to GUI

        Parameters
        ----------
        widget:
            Qt widget to display plot
        xdata:
            x-axis data
        ydata:
            y-axis data
        ylabel:
            y-axis label
        loc:
            legend location
        xlabel:
            x-axis label
        """

        if widget.layout() is None:
            layout = QVBoxLayout(widget)
        else:
            layout = widget.layout()
            deleteItemsOfLayout(layout)
            self.axes.clear()
            layout.addWidget(self)

        layout.addWidget(self)
        # Add figure to GUI
        self.axes.plot(xdata, ydata, linewidth=0.8, color="#3372d6", label="Model")
        self.axes.legend(loc=loc, fontsize=13)
        self.axes.set_title(title, fontdict={"color": "#EEE"})
        self.axes.set_xlabel(xlabel, fontsize=16)
        self.axes.set_ylabel(ylabel, fontsize=16)
        self.axes.xaxis.label.set_color('#EEE')
        self.axes.yaxis.label.set_color('#EEE')
        self.axes.tick_params(axis='x', colors="#EEE")
        self.axes.tick_params(axis='y', colors="#EEE")
        self.axes.spines['left'].set_color('#000')
        self.axes.spines['right'].set_color('#000')
        self.axes.spines['top'].set_color('#000')
        self.axes.spines['bottom'].set_color('#000')
        self.axes.grid(color='#EEE')
        self.show()

    def small_plot(self, widget: QWidget, xdata: pd.Series, ydata: pd.Series, xlabel: str, ylabel: str, loc: str):
        if widget.layout() is None:
            layout = QVBoxLayout(widget)
        else:
            layout = widget.layout()
            deleteItemsOfLayout(layout)
        layout.addWidget(self)  # Add figure to GUI

        self.axes.plot(xdata, ydata, linewidth=0.8, color="#3372d6", label="Model")
        self.axes.set_xlabel(xlabel, fontsize=10)
        self.axes.set_ylabel(ylabel, fontsize=10)
        self.axes.xaxis.label.set_color('#EEE')
        self.axes.yaxis.label.set_color('#EEE')
        self.axes.tick_params(axis='x', colors="#EEE", labelsize=8)
        self.axes.tick_params(axis='y', colors="#EEE", labelsize=8)
        self.axes.spines['left'].set_color('#000')
        self.axes.spines['right'].set_color('#000')
        self.axes.spines['top'].set_color('#000')
        self.axes.spines['bottom'].set_color('#000')
        self.axes.set_aspect(aspect='auto')
        self.show()

    def scatter(self, widget: QWidget, xdata: pd.Series, ydata: pd.Series, xlabel: str, ylabel: str, loc: str,
                title=None):
        """
        Create matplotlib plot and add it to GUI

        Parameters
        ----------
        widget:
            Qt widget to display plot
        xdata:
            x-axis data
        ydata:
            y-axis data
        ylabel:
            y-axis label
        loc:
            legend location
        xlabel:
            x-axis label
        """
        if widget.layout() is None:
            layout = QVBoxLayout(widget)
        else:
            layout = widget.layout()
            deleteItemsOfLayout(layout)

        layout.addWidget(self)  # Add figure to GUI
        self.axes.scatter(xdata, ydata, linewidth=0.8, color="#3372d6", label="Model")
        self.axes.legend(loc=loc, fontsize=13)
        self.axes.set_title(title, fontdict={"color": "#EEE"})
        self.axes.set_xlabel(xlabel, fontsize=16)
        self.axes.set_ylabel(ylabel, fontsize=16)
        self.axes.xaxis.label.set_color('#EEE')
        self.axes.yaxis.label.set_color('#EEE')
        self.axes.tick_params(axis='x', colors="#EEE")
        self.axes.tick_params(axis='y', colors="#EEE")
        self.axes.spines['left'].set_color('#000')
        self.axes.spines['right'].set_color('#000')
        self.axes.spines['top'].set_color('#000')
        self.axes.spines['bottom'].set_color('#000')
        self.axes.grid(color='#EEE')
        self.show()

    def savefig(self) -> None:
        """
        Save figure
        """
        dirname = QFileDialog.getSaveFileUrl()[0].toString()
        print(dirname)
        print(platform.system())
        if (platform.system() == "Darwin"):
            self.axes.figure.savefig(dirname.split('//')[1] + '.png')
        else:
            self.axes.figure.savefig(dirname.split('///')[1] + '.png')


class Output:
    """
    Creates Output plots
    """

    def __init__(self, ui: QWidget, data: pd.DataFrame, mesh: Mesh, xlabel: str, ylabel: str, loc: str, plot_type: str):
        # ----- Date initialisation ----- #
        self.__date_min = round(data.index.min())
        self.__date_max = math.ceil(data.index.max())

        # ----- Space initialization ----- #
        self.__space = "0"

        # ----- Properties initialization ---- #
        self._data = data
        self._ui = ui
        self._mesh = mesh
        self._xlabel = xlabel
        self._ylabel = ylabel
        self._loc = loc
        self._type = plot_type

    @property
    def date_min(self):
        return self.__date_min

    def setDateMin(self, value):
        self.__date_min = int(value)
        self.plot()

    @property
    def date_max(self):
        return self.__date_max

    def setDateMax(self, value):
        self.__date_max = int(value)
        self.plot()

    @property
    def space(self):
        return self.__space

    def setSpace(self, value):
        self.__space = value
        self.plot()

    def plot(self):
        """
        Create plot canvas
        """
        canvas = MplCanvas()  # Create canvas
        data = self._data.loc[self.__date_min:self.__date_max]  # select row according to the data range
        x = pd.Series(data.index)
        y_index = self.get_index()
        y = data.iloc[:, y_index]  # Gat column corresponding to selected position
        title = f"{self._type} at {self.__space}cm"
        canvas.plot(self._ui.plot, x, y, self._xlabel, self._ylabel, self._loc, title)  # Plot graph
        reconnect(self._ui.savePlot.clicked, lambda: canvas.savefig())  # Create save button

    def get_index(self):
        """
        Return space position of given nodes point
        """
        dx = self._mesh[4].flatten()
        space = float(self.__space.replace(",", "."))
        difference = np.absolute(dx - space)
        index = difference.argmin()
        return index


class Input:
    """
    Creates Output plots
    """

    def __init__(self, form: Ui_Form(), delta_p: Callable, delta_l: Callable, w: Callable, T: npt.NDArray[np.float64],
                 RH: npt.NDArray[np.float64]):
        # ----- T and RH properties ----- #
        self._T = T
        self._RH = RH

        # ----- Potential modified values init ----- #
        self.__mu = None
        self.__RH_table = delta_l(self._RH)[1]
        self.__delta_l = delta_l(self._RH)[2]
        self.__w = w(self._RH)[2]

        # ----- Ui ----- #
        self._form = form

        # ----- Material methods ----- #
        self._delta_p = delta_p
        self._delta_l = delta_l
        self._w = w

        # ----- Initial plot ---- #
        self.plot_dl()
        self.plot_dp()
        self.plot_w()

        # ----- Signal connection with setters ----- #
        form.mu.textChanged.connect(lambda value: self.setMu(value))
        form.dl_1.textChanged.connect(lambda value: self.setDelta_l(value, 0))
        form.dl_2.textChanged.connect(lambda value: self.setDelta_l(value, 1))
        form.dl_3.textChanged.connect(lambda value: self.setDelta_l(value, 2))
        form.rh_1.textChanged.connect(lambda value: self.setRH_table(value, 0))
        form.rh_2.textChanged.connect(lambda value: self.setRH_table(value, 1))
        form.rh_3.textChanged.connect(lambda value: self.setRH_table(value, 2))
        form.w10.textChanged.connect(lambda value: self.setW(value, 1))
        form.w20.textChanged.connect(lambda value: self.setW(value, 2))
        form.w30.textChanged.connect(lambda value: self.setW(value, 3))
        form.w40.textChanged.connect(lambda value: self.setW(value, 4))
        form.w50.textChanged.connect(lambda value: self.setW(value, 5))
        form.w60.textChanged.connect(lambda value: self.setW(value, 6))
        form.w70.textChanged.connect(lambda value: self.setW(value, 7))
        form.w80.textChanged.connect(lambda value: self.setW(value, 8))
        form.w90.textChanged.connect(lambda value: self.setW(value, 9))
        form.w100.textChanged.connect(lambda value: self.setW(value, 10))

    @property
    def mu(self):
        return self.__mu

    def setMu(self, value):
        self.__mu = value
        self.plot_dp()

    @property
    def delta_l(self):
        return self.__delta_l

    def setDelta_l(self, value, index):
        self.__delta_l[index] = value
        self.plot_dl()

    @property
    def RH_table(self):
        return self.__RH_table

    def setRH_table(self, value, index):
        self.__RH_table[index] = value
        self.plot_dl()

    @property
    def w(self):
        return self.__w

    def setW(self, value, index):
        self.__w[index] = value
        self.plot_w()

    def plot_dp(self):
        """
        Delta p graph
        """
        y = self._delta_p(self._T, self.__mu).flatten()  # Material delta_p function with modified mu
        min_y = '{:.2e}'.format(float(y[0]))  # formatting
        self._form.dp.setText(f"Min: {min_y}")  # Change display value with minimum value
        T = self._T - 273.15
        widget_dp = self._form.graph_dp  # Get the place to plot the graph
        canvas_dp = MplCanvas()  # Create the canavs
        canvas_dp.small_plot(widget_dp, T, y, "T", r"$\delta_{p}$", "upper right")  # create the plot

    def plot_dl(self):
        """
        Delta p graph
        """
        y = \
        self._delta_l(np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]), self.__RH_table, self.__delta_l)[
            0].flatten()
        RH = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]) * 100
        widget_dl = self._form.graph_dl
        canvas_dl = MplCanvas()
        canvas_dl.small_plot(widget_dl, RH, y, "RH", r"$\delta_{l}$", "upper right")

    def plot_w(self):
        """
        Delta p graph
        """
        y = self._w(self._RH, self.__w)[0].flatten()
        RH = self._RH * 100
        widget_w = self._form.graph_w
        canvas_w = MplCanvas()
        canvas_w.small_plot(widget_w, pd.Series(np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]) * 100),
                            self.__w, "RH", "w", "upper right")
