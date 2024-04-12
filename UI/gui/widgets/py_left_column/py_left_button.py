from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *

# PY TITLE BUTTON
# ///////////////////////////////////////////////////////////////
class PyLeftButton(QPushButton):
    def __init__(
        self,
        parent,
        app_parent = None,
        tooltip_text = "",
        btn_id = None,
        width = 30,
        height = 30,
        radius = 8,
        bg_color = "#343b48",
        bg_color_hover = "#3c4454",
        bg_color_pressed = "#2c313c",
        icon_color = "#c3ccdf",
        icon_color_hover = "#dce1ec",
        icon_color_pressed = "#edf0f5",
        icon_color_active = "#f5f6f9",
        icon_path = "no_icon.svg",
        dark_one = "#1b1e23",
        context_color = "#568af2",
        text_foreground = "#8a95aa",
        is_active = False
    ):
        super().__init__()
        
        # 设置默认参数
        self.setFixedSize(width, height)
        self.setCursor(Qt.PointingHandCursor)
        self.setObjectName(btn_id)

        # 属性
        self._bg_color = bg_color
        self._bg_color_hover = bg_color_hover
        self._bg_color_pressed = bg_color_pressed        
        self._icon_color = icon_color
        self._icon_color_hover = icon_color_hover
        self._icon_color_pressed = icon_color_pressed
        self._icon_color_active = icon_color_active
        self._context_color = context_color
        self._top_margin = self.height() + 6
        self._is_active = is_active
        # 设置属性
        self._set_bg_color = bg_color
        self._set_icon_path = icon_path
        self._set_icon_color = icon_color
        self._set_border_radius = radius
        # 父级
        self._parent = parent
        self._app_parent = app_parent

        # 工具提示设置(默认隐藏)
        self._tooltip_text = tooltip_text
        self._tooltip = _ToolTip(
            app_parent,
            tooltip_text,
            dark_one,
            context_color,
            text_foreground
        )
        self._tooltip.hide()

    # 设置激活状态
    # ///////////////////////////////////////////////////////////////
    def set_active(self, is_active):
        self._is_active = is_active
        self.repaint()

    # 返回激活状态
    # ///////////////////////////////////////////////////////////////
    def is_active(self):
        return self._is_active

    # 绘制事件
    # 绘制按钮和图标
    # ///////////////////////////////////////////////////////////////
    def paintEvent(self, event):
        # 初始化绘图器
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # 根据激活状态使用不同的填充颜色
        if self._is_active:
            brush = QBrush(QColor(self._bg_color_pressed))
        else:
            brush = QBrush(QColor(self._set_bg_color))

        # 绘制圆角矩形
        rect = QRect(0, 0, self.width(), self.height())
        paint.setPen(Qt.NoPen)
        paint.setBrush(brush)
        paint.drawRoundedRect(
            rect, 
            self._set_border_radius, 
            self._set_border_radius
        )

        # 绘制图标
        self.icon_paint(paint, self._set_icon_path, rect)

        # 结束绘制
        paint.end()

    # 根据不同的鼠标事件改变按钮的背景和图标颜色
    # ///////////////////////////////////////////////////////////////
    def change_style(self, event):
        if event == QEvent.Enter:
            self._set_bg_color = self._bg_color_hover
            self._set_icon_color = self._icon_color_hover
            self.repaint()         
        elif event == QEvent.Leave:
            self._set_bg_color = self._bg_color
            self._set_icon_color = self._icon_color
            self.repaint()
        elif event == QEvent.MouseButtonPress:            
            self._set_bg_color = self._bg_color_pressed
            self._set_icon_color = self._icon_color_pressed
            self.repaint()
        elif event == QEvent.MouseButtonRelease:
            self._set_bg_color = self._bg_color_hover
            self._set_icon_color = self._icon_color_hover
            self.repaint()

    # 鼠标进入
    # ///////////////////////////////////////////////////////////////
    def enterEvent(self, event):
        self.change_style(QEvent.Enter)
        self.move_tooltip()
        self._tooltip.show()

    # 鼠标离开
    # ///////////////////////////////////////////////////////////////
    def leaveEvent(self, event):
        self.change_style(QEvent.Leave)
        self.move_tooltip()
        self._tooltip.hide()

    # 鼠标按下
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.change_style(QEvent.MouseButtonPress)
            # SET FOCUS
            self.setFocus()
            # EMIT SIGNAL
            return self.clicked.emit()

    # 鼠标释放
    # ///////////////////////////////////////////////////////////////
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.change_style(QEvent.MouseButtonRelease)
            # EMIT SIGNAL
            return self.released.emit()

    # 绘制图标
    # ///////////////////////////////////////////////////////////////
    def icon_paint(self, qp, image, rect):
        icon = QPixmap(image)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        if self._is_active:
            painter.fillRect(icon.rect(), self._context_color)
        else:
            painter.fillRect(icon.rect(), self._set_icon_color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2, 
            (rect.height() - icon.height()) / 2,
            icon
        )        
        painter.end()

    # 设置图标
    # ///////////////////////////////////////////////////////////////
    def set_icon(self, icon_path):
        self._set_icon_path = icon_path
        self.repaint()

    # 计算并调整工具提示的位置, 使其基于按钮的位置进行偏移
    # ///////////////////////////////////////////////////////////////
    def move_tooltip(self):
        # 获取主窗口的位置
        gp = self.mapToGlobal(QPoint(0, 0))

        # 设置小部件以获取位置
        # 返回应用程序内部部件的绝对位置
        pos = self._parent.mapFromGlobal(gp)

        # 格式化位置
        # 使用偏移调整工具提示位置
        pos_x = (pos.x() - self._tooltip.width()) + self.width() + 5
        pos_y = pos.y() + self._top_margin

        # 移动位置
        self._tooltip.move(pos_x, pos_y)

# 具有自定义样式和阴影效果的工具提示标签
# ///////////////////////////////////////////////////////////////
class _ToolTip(QLabel):
    # 样式表
    style_tooltip = """ 
    QLabel {{		
        background-color: {_dark_one};	
        color: {_text_foreground};
        padding-left: 10px;
        padding-right: 10px;
        border-radius: 17px;
        border: 0px solid transparent;
        border-right: 3px solid {_context_color};
        font: 800 9pt "Segoe UI";
    }}
    """
    def __init__(
        self,
        parent, 
        tooltip,
        dark_one,
        context_color,
        text_foreground
    ):
        QLabel.__init__(self)

        # 设置标签样式和属性
        style = self.style_tooltip.format(
            _dark_one = dark_one,
            _context_color = context_color,
            _text_foreground = text_foreground
        )
        self.setObjectName(u"label_tooltip")
        self.setStyleSheet(style)
        self.setMinimumHeight(34)
        self.setParent(parent)
        self.setText(tooltip)
        self.adjustSize()

        # 添加阴影效果
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.setGraphicsEffect(self.shadow)
