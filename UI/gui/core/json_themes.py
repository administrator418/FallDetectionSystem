import json
import os
from Settings.json_settings import Settings

# 应用程序主题
# ///////////////////////////////////////////////////////////////
class Themes(object):
    # 导入设置
    # ///////////////////////////////////////////////////////////////
    setup_settings = Settings()
    _settings = setup_settings.items

    # app path
    # ///////////////////////////////////////////////////////////////
    json_file = f"UI/gui/themes/{_settings['theme_name']}.json"
    app_path = os.path.abspath(os.getcwd())
    settings_path = os.path.normpath(os.path.join(app_path, json_file))
    if not os.path.isfile(settings_path):
        print(f"WARNING: \"UI/gui/themes/{_settings['theme_name']}.json\" not found! check in the folder {settings_path}")

    # 初始化设置
    # ///////////////////////////////////////////////////////////////
    def __init__(self):
        super(Themes, self).__init__()

        # 只是为了有对象引用
        self.items = {}

        # 反序列化
        self.deserialize()

    # 序列化(将Python数据结构序列化为JSON格式的字符串)
    # ///////////////////////////////////////////////////////////////
    def serialize(self):
        # 写JSON文件
        with open(self.settings_path, "w", encoding='utf-8') as write:
            json.dump(self.items, write, indent=4)

    # 反序列化(将JSON格式的字符串转换成Python的数据结构)
    # ///////////////////////////////////////////////////////////////
    def deserialize(self):
        # 读JSON文件
        with open(self.settings_path, "r", encoding='utf-8') as reader:
            settings = json.loads(reader.read())
            self.items = settings