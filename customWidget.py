from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QEvent, QSize, Property
from PySide6.QtGui import QEnterEvent, QColor


class ZoomButton(QPushButton):
    """
        Widget button which is zooming when hovering
    """
    def __init__(self, *args, **kwargs):
        QPushButton.__init__(self, *args, **kwargs)
        self.iconAnim = QPropertyAnimation(self, b'iconSize')
        self.iconAnim.setEasingCurve(QEasingCurve.InQuad)
        self.iconAnim.setDuration(200)

    def enterEvent(self, event: QEnterEvent) -> None:
        self.iconAnim.setDirection(self.iconAnim.Forward)
        if self.iconAnim.state() == self.iconAnim.State.Stopped:
            size = self.iconSize()
            self.iconAnim.setStartValue(size)
            size += QSize(3, 3)
            self.iconAnim.setEndValue(size)

            self.iconAnim.start()
        QPushButton.enterEvent(self, event)

    def leaveEvent(self, event: QEvent) -> None:
        self.iconAnim.setDirection(self.iconAnim.Backward)
        if self.iconAnim.state() == self.iconAnim.State.Stopped:
            self.iconAnim.start()
        QPushButton.leaveEvent(self, event)


class ColorButton(QPushButton):
    """
        Widget button which change is color when hovering
    """
    def __init__(self, color, *args, **kwargs):
        QPushButton.__init__(self, *args, **kwargs)

        self.__color = QColor(255, 255, 255, 0)
        self.colorAnim = QPropertyAnimation(self, b'color')
        self.colorAnim.setDuration(200)
        self.colorAnim.setStartValue(QColor(255, 255, 255, 0))
        self.colorAnim.setEndValue(color)
        self.new_color = color

    @Property(QColor)
    def color(self):
        return self.__color

    @color.setter
    def color(self, val):
        self.__color = val

        policeColor = self.new_color
        if val == self.new_color:
            policeColor = QColor(255, 255, 255)

        self.setStyleSheet(
            f"border: 1px solid rgba({self.new_color.red()},{self.new_color.green()},{self.new_color.blue()},{self.new_color.alpha()});"
            f" background-color: rgba({val.red()},{val.green()},{val.blue()},{val.alpha()});"
            f" color: rgba({policeColor.red()},{policeColor.green()},{policeColor.blue()},{policeColor.alpha()})")

    def enterEvent(self, event: QEnterEvent) -> None:
        self.colorAnim.setDirection(self.colorAnim.Forward)
        if self.colorAnim.state() == self.colorAnim.State.Stopped:
            self.colorAnim.start()
        QPushButton.enterEvent(self, event)

    def leaveEvent(self, event: QEvent) -> None:
        self.colorAnim.setDirection(self.colorAnim.Backward)
        if self.colorAnim.state() == self.colorAnim.State.Stopped:
            self.colorAnim.start()
        QPushButton.leaveEvent(self, event)


class ColorButtonGreen(ColorButton):
    def __init__(self, *args, **kwargs):
        ColorButton.__init__(self, QColor(51, 214, 75), *args, **kwargs)


class ColorButtonRed(ColorButton):
    def __init__(self, *args, **kwargs):
        ColorButton.__init__(self, QColor(214, 51, 56), *args, **kwargs)
