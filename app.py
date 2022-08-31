# -*- coding: utf-8 -*-

"""
Application GUI management and main function
"""

import multiprocessing
import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QHBoxLayout, QWidget, QMessageBox
import pandas as pd
import numpy as np

from main_ui import Ui_MainWindow
from HT.algorithm import init
from output.plot import MplCanvas, Output, Input
from const_ui import Ui_Form
from plot_ui import Ui_Form as Plot_UI
from functions import create_const, create_input_layers, material_factory, deleteItemsOfLayout, resource_path, reconnect
from worker_manager import WorkerManager


basedir = os.path.dirname(__file__)


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        # Create UI from file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(1034, 806)
        self.setWindowTitle("HTM-OLIMP")
        self.ui.stackedWidget.setCurrentWidget(self.ui.filePage)

        # ----- Initialize Meteo Data and Rad selection UI ----- #
        self.ui.useDefault.setChecked(True)
        self.ui.importButton.setDisabled(True)
        self.ui.useDefault_ray.setChecked(True)
        self.ui.importButton_ray.setDisabled(True)
        self.ui.useCustom.clicked.connect(lambda: self.ui.importButton.setEnabled(True))
        self.ui.useDefault.clicked.connect(lambda: self.ui.importButton.setEnabled(False))
        self.ui.useCustom_ray.clicked.connect(lambda: self.ui.importButton_ray.setEnabled(True))
        self.ui.useDefault_ray.clicked.connect(lambda: self.ui.importButton_ray.setEnabled(False))
        self.ui.downloadDefault.clicked.connect(lambda: os.system('open ./data/data_air.xlsx'))  # Open default meteo file
        self.ui.downloadDefault_ray.clicked.connect(lambda: os.system('open ./data/data_radiation.xlsx')) # Open default ray file

        # ----- Button signal connection ----- #
        self.ui.importButton.clicked.connect(self.load_excel_meteo_data)  # Import climate data
        self.ui.importButton_ray.clicked.connect(self.load_excel_rad_data)  # Import rad data
        self.ui.validLayer.clicked.connect(self.settings_layer)  # Set number of layers
        self.ui.nextButton.clicked.connect(self.settings)  # Go to Material page
        self.ui.returnButton.clicked.connect(self.new)  # Go back to Settings page
        self.ui.run.clicked.connect(self.create_worker)  # Launch worker
        self.ui.stopButton.clicked.connect(self.stop)  # Stop worker
        self.ui.goResult.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.resultPage))  # Go to page result
        self.ui.newButton.clicked.connect(self.new)  # Go back to Settings page once simulation's over

        # ----- Hide UI ----- #
        self.ui.returnButton_stop.setVisible(False)
        self.ui.timeText.setVisible(False)
        self.ui.goResult.setVisible(False)

        # ----- Initialize values ----- #
        self.consts = {}
        self.worker = WorkerManager()
        self.climate_data = None
        self.rad_data = None

    def load_excel_meteo_data(self) -> None:
        """
            Load excel input
        """
        file = QFileDialog.getOpenFileUrl(self.ui.centralwidget, filter='*.xlsx')[0].toString()  # Open select file box
        df = pd.read_excel(file)
        self.ui.selectedFile.setText(file.split('/')[-1])
        # If file not corresponding to template, create error message box and exit
        if not np.array_equal(df.columns.tolist(),
                              ['Time (s)', 'T_out (°C)', 'T_ins (°C)', 'RH_out (%)', 'RH_int (%)']):
            QMessageBox.critical(self, "Not good format!",
                                 "Please import a file following the template of the default file",
                                 buttons=QMessageBox.Ok)
            return
        self.climate_data = df.values

    def load_excel_rad_data(self) -> None:
        """
            Load excel input
        """
        file = QFileDialog.getOpenFileUrl(self.ui.centralwidget, filter='*.xlsx')[0].toString()  # Open select file box
        df = pd.read_excel(file)
        self.ui.selectedFile_ray.setText(file.split('/')[-1])
        # If file not corresponding to template, create error message box and exit
        if not np.array_equal(df.columns.tolist(),
                              ['Time (s)', 'h (°)', 'Az (°)', 'DirH (W/m2)', 'DifH (W/m2)']):
            QMessageBox.critical(self, "Not good format!",
                                 "Please import a file following the template of the default file",
                                 buttons=QMessageBox.Ok)
            return
        self.rad_data = df.values

    def settings(self) -> None:
        """
            Build boundary condition for the model, from meteo and radiation data
        """
        # If use default is checked, load data_air file
        if self.ui.useDefault.isChecked():
            df = pd.read_excel(resource_path('data/data_air.xlsx'))
            self.climate_data = df.values
        # Else check if a file is loaded correctly
        else:
            if self.climate_data is None:
                QMessageBox.critical(self, "Select a file",
                                     "Please select a valid file for meteo input, or use the default one",
                                     buttons=QMessageBox.Ok)
                return

        # Load default rad data file
        if self.ui.useDefault_ray.isChecked():
            df_rad = pd.read_excel(resource_path('data/data_radiation.xlsx'))
            self.rad_data = df_rad.values
        else:
            if self.rad_data is None:
                QMessageBox.critical(self, "Select a file",
                                     "Please select a valid file for rad input, or use the default one",
                                     buttons=QMessageBox.Ok)
                return

        self.create_mesh()
        self.worker.build_boundary(self.climate_data, self.rad_data)
        self.create_tab_material()
        self.get_const()
        self.ui.stackedWidget.setCurrentWidget(self.ui.constPage)

    def create_tab_material(self):
        """
        Create a tab for each layer in Material page
        """

        mat = list(dict.fromkeys(self.worker.materials))  # Get list of unique material
        tab_widget = self.ui.tabConst

        nb_mat = len(mat)
        for i in range(nb_mat):  # For each material, create a tab
            form = Ui_Form()
            widget = QWidget()
            form.setupUi(widget)
            self.consts[mat[i]] = form
            tab_widget.insertTab(i, widget, mat[i])

    def get_const(self) -> None:
        """
            Build constant which can be modified by user
        """
        const_settings = {
            "rho": "",
            "k": "",
            "cp": "",
            "dp": "",
            "dl": "",
            "mu": ""
        }
        (T, RH, cp) = init(self.worker.bo, self.worker.mesh)  # Initialize T and RH
        # Fill the UI with default values for given material
        for mat, ui in self.consts.items():
            material = material_factory(mat)
            dl = material.delta_l(RH)
            w = material.w(RH)
            const_settings["rho"] = material.rho()
            const_settings["cp"] = material.Cp(RH)
            const_settings["k"] = material.k()
            const_settings["dp"] = material.delta_p(T)
            const_settings["mu"] = material.mu()

            const_settings = create_const(const_settings)
            ui.rho.setText(str(const_settings["rho"]))
            ui.cp.setText(str(const_settings["cp"]))
            ui.k_2.setText(str(const_settings["k"]))
            ui.mu.setText(str(const_settings["mu"]))
            ui.dl_1.setText(str(dl[2][0]))
            ui.dl_2.setText(str(dl[2][1]))
            ui.dl_3.setText(str(dl[2][2]))
            ui.rh_1.setText(str(dl[1][0]))
            ui.rh_2.setText(str(dl[1][1]))
            ui.rh_3.setText(str(dl[1][2]))

            ui.w10.setText(str(w[2][1]))
            ui.w20.setText(str(w[2][2]))
            ui.w30.setText(str(w[2][3]))
            ui.w40.setText(str(w[2][4]))
            ui.w50.setText(str(w[2][5]))
            ui.w60.setText(str(w[2][6]))
            ui.w70.setText(str(w[2][7]))
            ui.w80.setText(str(w[2][8]))
            ui.w90.setText(str(w[2][9]))
            ui.w100.setText(str(w[2][10]))

            Input(ui, material.delta_p, material.delta_l, material.w, T, RH)

    def create_mesh(self) -> None:
        """
        Create mesh and save material properties
        """
        nb_custom = 1
        nb_layer = int(self.ui.nb_layers.text())  # Get the number of layers
        if len(self.ui.layersSettings.children()) == 0:
            QMessageBox.critical(self, "Select at least one layer",
                                 "Please select at least one layer",
                                 buttons=QMessageBox.Ok)
            raise ValueError  # If no layer, launch error

        for i, child in enumerate(self.ui.layersSettings.children()):
            c = child.findChildren(QHBoxLayout)

            s = c[0].itemAt(1)
            try:
                self.worker.sizes.append(float(s.widget().text()))  # save sizes of each layers
            except ValueError:  # If not a valid number, raise error
                QMessageBox.critical(self, "Enter a valid number",
                                     "Please enter a valid number for the layers sizes",
                                     buttons=QMessageBox.Ok)
                raise ValueError

            m = c[1].itemAt(1)

            text = str(m.widget().currentText())
            if text == "Custom":
                text = f"Custom {nb_custom}"
                nb_custom += 1
            self.worker.materials.append(text)  # Save material in a list

        self.worker.build_mesh(nb_layer)  # Build mesh

    def create_worker(self) -> None:
        """
        Create a worker instance
        """
        self.worker.run_ht(self.consts, self.progress_bar, self.create_table, self.finished)
        self.ui.stackedWidget.setCurrentWidget(self.ui.runningPage)

    def create_table(self, data: dict) -> None:
        """
        Create the result table

        Parameters
        ----------
        data:
            Output simulation data
        """
        with open(resource_path('data/temp.csv'), 'w+') as writer:
            data["T"].to_csv(writer)  # Write result in temp.csv
        with open(resource_path('data/RH.csv'), 'w+') as writer:
            data["RH"].to_csv(writer)  # Write result in temp.csv
        with open(resource_path('data/pv.csv'), 'w+') as writer:
            data["pv"].to_csv(writer)  # Write result in temp.csv
        self.ui.download_T.clicked.connect(lambda: os.system('open ./data/temp.csv'))
        self.ui.download_RH.clicked.connect(lambda: os.system('open ./data/RH.csv'))
        self.ui.download_pv.clicked.connect(lambda: os.system('open ./data/pv.csv'))
        self.plot(data["scatter"], data["T"], data["RH"], data["pv"])  # Plot result

    def plot(self, scatter: list, T: pd.DataFrame, RH: pd.DataFrame, pv: pd.DataFrame) -> None:
        """
        Create the result graphs

        Parameters
        ----------
        scatter:
            Data for Space/Time scatter plot
        T:
            Temperature dataframe
        RH:
            RH dataframe
        pv:
            pv dataframe
        """
        mesh = self.worker.mesh
        # ----- Plot T ----- #
        plot_T = Plot_UI()  # Get UI file
        widget = QWidget()  # Create a new widget
        plot_T.setupUi(widget)  # Add widget to file
        self.ui.resulTabWidget.addTab(widget, "T")  # Create a new tab
        output_T = Output(plot_T, T, mesh, "Day", "$T$ [°C]", "upper right", "T")  # create instance
        plot_T.date_min.setValue(output_T.date_min)  # Init date min
        plot_T.date_min.setMinimum(output_T.date_min)  # Init minimum value of date min
        plot_T.date_min.setMaximum(output_T.date_max)  # Init maximum value of date min
        plot_T.date_max.setValue(output_T.date_max)  # Init date max
        plot_T.date_max.setMinimum(output_T.date_min)  # Init minimum value of date max
        plot_T.date_max.setMaximum(output_T.date_max)  # Init maximum value of date max
        plot_T.space.setMaximum(np.sum(self.worker.sizes))  # Init max value of space
        plot_T.date_min.textChanged.connect(lambda value: output_T.setDateMin(value))  # Signal to update graph when date min change
        plot_T.date_max.textChanged.connect(lambda value: output_T.setDateMax(value))  # Signal to update graph when date max change
        plot_T.space.textChanged.connect(lambda value: output_T.setSpace(value))  # Signal to update graph when space change

        output_T.plot() # Plot graph

        # ----- Plot RH ----- #
        plot_RH = Plot_UI()
        widget = QWidget()
        plot_RH.setupUi(widget)
        output_RH = Output(plot_RH, RH, mesh, "Day", "$RH$ [%]", "upper right", "RH")
        self.ui.resulTabWidget.addTab(widget, "RH")
        plot_RH.date_min.setValue(output_RH.date_min)
        plot_RH.date_min.setMinimum(output_RH.date_min)
        plot_RH.date_min.setMaximum(output_RH.date_min)
        plot_RH.date_max.setValue(output_RH.date_max)
        plot_RH.date_max.setMinimum(output_RH.date_min)
        plot_RH.date_max.setMaximum(output_RH.date_max)
        plot_RH.space.setMaximum(np.sum(self.worker.sizes))
        plot_RH.date_min.textChanged.connect(lambda value: output_RH.setDateMin(value))
        plot_RH.date_max.textChanged.connect(lambda value: output_RH.setDateMax(value))
        plot_RH.space.textChanged.connect(lambda value: output_RH.setSpace(value))
        output_RH.plot()

        # ----- Plot vapour pressure ----- #
        plot_pv = Plot_UI()
        widget = QWidget()
        plot_pv.setupUi(widget)
        self.ui.resulTabWidget.addTab(widget, "pv")
        output_pv = Output(plot_pv, pv, mesh, "Day", "$pv$ [Pa]", "upper right", "pv")
        plot_pv.date_min.setValue(output_pv.date_min)
        plot_pv.date_min.setMinimum(output_pv.date_min)
        plot_pv.date_min.setMaximum(output_pv.date_min)
        plot_pv.date_max.setValue(output_pv.date_max)
        plot_pv.date_max.setMinimum(output_pv.date_min)
        plot_pv.date_max.setMaximum(output_pv.date_max)
        plot_pv.space.setMaximum(np.sum(self.worker.sizes))
        plot_pv.date_min.textChanged.connect(lambda value: output_pv.setDateMin(value))
        plot_pv.date_max.textChanged.connect(lambda value: output_pv.setDateMax(value))
        plot_pv.space.textChanged.connect(lambda value: output_pv.setSpace(value))
        output_pv.plot()

        # ----- Temps/Espace ----- #
        plot_T_E = Plot_UI()
        widget = QWidget()
        plot_T_E.setupUi(widget)
        self.ui.resulTabWidget.addTab(widget, "Space/Time")
        plot_T_E.space.setVisible(False)  # Hide space selection
        plot_T_E.lineEdit_4.setVisible(False)  # Hide space selection
        plot_T_E.date_min.setVisible(False)  # Hide date selection
        plot_T_E.date_max.setVisible(False)  # Hide space selection
        plot_T_E.lineEdit_3.setVisible(False)  # Hide space selection
        canvasT_E = MplCanvas()  # Create canvas
        canvasT_E.scatter(plot_T_E.plot, scatter[0], scatter[1], "Day", "Dist(cm)", "upper right", "Condensation zones")  # Plot
        reconnect(plot_T_E.savePlot.clicked, lambda: canvasT_E.savefig())  # Save figure

    def progress_bar(self, progress: float) -> None:
        """
        Update progress bar

        Parameters
        ----------
        progress:
            Actual progression in simulation
        """
        self.ui.progressBar.setValue(progress * 100)

    def settings_layer(self) -> None:
        """
        Create UI to fill layers properties
        """
        nb_layers = self.ui.nb_layers.value()  # Get number of layers
        layout = self.ui.layersSettings



        # Clear already existing layer setting if some
        deleteItemsOfLayout(layout)

        for i in range(0, nb_layers):
            layout.addLayout(create_input_layers(i))  # Add layer line for

    def finished(self, time: float) -> None:
        """
        Launch when worker is finished

        Parameters
        ----------
        time:
            Total time simulation took
        """
        self.ui.goResult.setVisible(True)
        self.ui.timeText.setVisible(True)
        self.ui.timeText.setText("Time [min]: " + str(round(time, 2)))

    def stop(self) -> None:
        """
        Stop the worker
        """
        self.worker.stop()
        self.ui.returnButton_stop.setVisible(True)
        self.ui.returnButton_stop.clicked.connect(self.new)

    def new(self) -> None:
        """
        Go back to Settings page and clean properties to launch new simulation
        """
        self.ui.stackedWidget.setCurrentWidget(self.ui.filePage)  # Go back to settings page

        self.consts = {}
        self.worker.sizes = []
        self.worker.materials = []
        self.ui.goResult.setVisible(False)
        self.ui.timeText.setVisible(False)
        self.ui.returnButton_stop.setVisible(False)

        # remove tab widget
        tab_widget = self.ui.tabConst
        while tab_widget.count() > 0:
            tab_widget.removeTab(0)

        # remove result tab
        result_tab_widget = self.ui.resulTabWidget
        while result_tab_widget.count() > 0:
            result_tab_widget.removeTab(0)


if __name__ == "__main__":
    multiprocessing.freeze_support()
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
