import json
import os
import re

# 应用程序设置
# ///////////////////////////////////////////////////////////////
class Settings(object):
    # 应用程序路径
    # ///////////////////////////////////////////////////////////////
    json_file = "Settings/settings.json"
    app_path = os.path.abspath(os.getcwd())
    settings_path = os.path.normpath(os.path.join(app_path, json_file))
    if not os.path.isfile(settings_path):
        print(f"WARNING: \"UI/settings.json\" not found! check in the folder {settings_path}")
    
    # 初始化设置
    # ///////////////////////////////////////////////////////////////
    def __init__(self):
        super(Settings, self).__init__()

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
            content = reader.read()
            # 删除注释
            content_no_comments = re.sub(r'\/\/.*', '', content)
            settings = json.loads(content_no_comments)
            self.items = settings
