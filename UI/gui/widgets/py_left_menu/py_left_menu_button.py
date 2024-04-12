import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *
from gui.core.functions import *

# 自定义左侧菜单
# ///////////////////////////////////////////////////////////////
class PyLeftMenuButton(QPushButton):
    def __init__(
        self,
        app_parent,
        text,
        btn_id = None,
        tooltip_text = "",
        margin = 4,
        dark_one = "#1b1e23",
        dark_three = "#21252d",
        dark_four = "#272c36",
        bg_one = "#2c313c",
        icon_color = "#c3ccdf",
        icon_color_hover = "#dce1ec",
        icon_color_pressed = "#edf0f5",
        icon_color_active = "#f5f6f9",
        context_color = "#568af2",
        text_foreground = "#8a95aa",
        text_active = "#dce1ec",
        icon_path = "icon_add_user.svg",
        icon_active_menu = "active_menu.svg",
        is_active = False,
        is_active_tab = False,
        is_toggle_active = False
    ):
        super().__init__()
        self.setText(text)
        self.setCursor(Qt.PointingHandCursor)
        self.setMaximumHeight(50)
        self.setMinimumHeight(50)
        self.setObjectName(btn_id)

        # app path
        self._icon_path = Functions.set_svg_icon(icon_path)
        self._icon_active_menu = Functions.set_svg_icon(icon_active_menu)

        # 属性
        self._margin = margin
        self._dark_one = dark_one
        self._dark_three = dark_three
        self._dark_four = dark_four
        self._bg_one = bg_one
        self._context_color = context_color
        self._icon_color = icon_color
        self._icon_color_hover = icon_color_hover
        self._icon_color_pressed = icon_color_pressed
        self._icon_color_active = icon_color_active
        self._set_icon_color = self._icon_color # 设置图标颜色
        self._set_bg_color = self._dark_one # 设置背景颜色
        self._set_text_foreground = text_foreground
        self._set_text_active = text_active
        self._parent = app_parent
        self._is_active = is_active
        self._is_active_tab = is_active_tab
        self._is_toggle_active = is_toggle_active

        # 工具提示设置(默认隐藏)
        self._tooltip_text = tooltip_text
        self.tooltip = _ToolTip(
            app_parent,
            tooltip_text,
            dark_one,
            context_color,
            text_foreground
        )
        self.tooltip.hide()

    # 绘制事件
    # ///////////////////////////////////////////////////////////////
    def paintEvent(self, event):
        # 初始化绘制器
        p = QPainter()
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.setPen(Qt.NoPen)
        p.setFont(self.font())

        # 定义矩形区域
        rect = QRect(4, 5, self.width(), self.height() - 10)
        rect_inside = QRect(4, 5, self.width() - 8, self.height() - 10)
        rect_icon = QRect(0, 0, 50, self.height())
        rect_blue = QRect(4, 5, 20, self.height() - 10)
        rect_inside_active = QRect(7, 5, self.width(), self.height() - 10)
        rect_text = QRect(45, 0, self.width() - 50, self.height())

        # 绘制不同状态
        if self._is_active:
            # 绘制蓝色背景
            p.setBrush(QColor(self._context_color))
            p.drawRoundedRect(rect_blue, 8, 8)

            # 绘制内部背景
            p.setBrush(QColor(self._bg_one))
            p.drawRoundedRect(rect_inside_active, 8, 8)

            # 绘制激活
            icon_path = self._icon_active_menu
            app_path = os.path.abspath(os.getcwd())
            icon_path = os.path.normpath(os.path.join(app_path, icon_path))
            self._set_icon_color = self._icon_color_active
            self.icon_active(p, icon_path, self.width())

            # 绘制文本
            p.setPen(QColor(self._set_text_active))
            p.drawText(rect_text, Qt.AlignVCenter, self.text())

            # 绘制图标
            self.icon_paint(p, self._icon_path, rect_icon, self._set_icon_color) 

        elif self._is_active_tab:
            # 绘制蓝色背景
            p.setBrush(QColor(self._dark_four))
            p.drawRoundedRect(rect_blue, 8, 8)

            # 绘制内部背景
            p.setBrush(QColor(self._bg_one))
            p.drawRoundedRect(rect_inside_active, 8, 8)

            # 绘制激活
            icon_path = self._icon_active_menu
            app_path = os.path.abspath(os.getcwd())
            icon_path = os.path.normpath(os.path.join(app_path, icon_path))
            self._set_icon_color = self._icon_color_active
            self.icon_active(p, icon_path, self.width())

            # 绘制文本
            p.setPen(QColor(self._set_text_active))
            p.drawText(rect_text, Qt.AlignVCenter, self.text())

            # 绘制图标
            self.icon_paint(p, self._icon_path, rect_icon, self._set_icon_color)

        # 常规背景
        else:
            if self._is_toggle_active:
                # 绘制暗色背景
                p.setBrush(QColor(self._dark_three))
                p.drawRoundedRect(rect_inside, 8, 8)

                # 绘制文本
                p.setPen(QColor(self._set_text_foreground))
                p.drawText(rect_text, Qt.AlignVCenter, self.text())

                # 绘制图标
                if self._is_toggle_active:
                    self.icon_paint(p, self._icon_path, rect_icon, self._context_color)
                else:
                    self.icon_paint(p, self._icon_path, rect_icon, self._set_icon_color)
            else:
                # 绘制常规背景
                p.setBrush(QColor(self._set_bg_color))
                p.drawRoundedRect(rect_inside, 8, 8)

                # 绘制文本
                p.setPen(QColor(self._set_text_foreground))
                p.drawText(rect_text, Qt.AlignVCenter, self.text())

                # 绘制图标
                self.icon_paint(p, self._icon_path, rect_icon, self._set_icon_color)        

        p.end()

    # 设置激活状态
    # ///////////////////////////////////////////////////////////////
    def set_active(self, is_active):
        self._is_active = is_active
        if not is_active:
            self._set_icon_color = self._icon_color
            self._set_bg_color = self._dark_one

        self.repaint()

    # 设置tab激活状态
    # ///////////////////////////////////////////////////////////////
    def set_active_tab(self, is_active):
        self._is_active_tab = is_active
        if not is_active:
            self._set_icon_color = self._icon_color
            self._set_bg_color = self._dark_one
            
        self.repaint()

    # 返回激活状态
    # ///////////////////////////////////////////////////////////////
    def is_active(self):
        return self._is_active

    # 返回tab激活状态
    # ///////////////////////////////////////////////////////////////
    def is_active_tab(self):
        return self._is_active_tab
    
    # 设置活动切换
    # ///////////////////////////////////////////////////////////////
    def set_active_toggle(self, is_active):
        self._is_toggle_active = is_active

    # 设置图标
    # ///////////////////////////////////////////////////////////////
    def set_icon(self, icon_path):
        self._icon_path = icon_path
        self.repaint()

    # 绘制一个图标并将其颜色调整为指定的颜色
    # ///////////////////////////////////////////////////////////////
    def icon_paint(self, qp, image, rect, color):
        icon = QPixmap(image)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2, 
            (rect.height() - icon.height()) / 2,
            icon
        )        
        painter.end()

    # 绘制经过颜色修改的图标
    # ///////////////////////////////////////////////////////////////
    def icon_active(self, qp, image, width):
        icon = QPixmap(image)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), self._bg_one)
        qp.drawPixmap(width - 5, 0, icon)
        painter.end()

    # 改变样式
    # ///////////////////////////////////////////////////////////////
    def change_style(self, event):
        if event == QEvent.Enter:
            if not self._is_active:
                self._set_icon_color = self._icon_color_hover
                self._set_bg_color = self._dark_three
            self.repaint()          
        elif event == QEvent.Leave:
            if not self._is_active:
                self._set_icon_color = self._icon_color
                self._set_bg_color = self._dark_one
            self.repaint()
        elif event == QEvent.MouseButtonPress:
            if not self._is_active:         
                self._set_icon_color = self._context_color
                self._set_bg_color = self._dark_four
            self.repaint()  
        elif event == QEvent.MouseButtonRelease:
            if not self._is_active:
                self._set_icon_color = self._icon_color_hover
                self._set_bg_color = self._dark_three
            self.repaint()
    
    # 鼠标进入
    # ///////////////////////////////////////////////////////////////
    def enterEvent(self, event):
        self.change_style(QEvent.Enter)
        if self.width() == 50 and self._tooltip_text:
            self.move_tooltip()
            self.tooltip.show()

    # 鼠标离开
    # ///////////////////////////////////////////////////////////////
    def leaveEvent(self, event):
        self.change_style(QEvent.Leave)
        self.tooltip.hide()

    # 鼠标按下
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.change_style(QEvent.MouseButtonPress)
            self.tooltip.hide()
            return self.clicked.emit()

    # 鼠标释放
    # ///////////////////////////////////////////////////////////////
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.change_style(QEvent.MouseButtonRelease)
            return self.released.emit()

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
        pos_x = pos.x() + self.width() + 5
        pos_y = pos.y() + (self.width() - self.tooltip.height()) // 2

        # 移动位置
        self.tooltip.move(pos_x, pos_y) 

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
        border-left: 3px solid {_context_color};
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

    
