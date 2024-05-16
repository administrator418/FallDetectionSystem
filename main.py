import os

path = "./UI/main.py"
os.system(f"python {path}")

"""
代码统计：
Total : 79 files,  8734 codes, 1177 comments, 931 blanks, all 10842 lines

Languages
+--------------------+------------+------------+------------+------------+------------+
| language           | files      | code       | comment    | blank      | total      |
+--------------------+------------+------------+------------+------------+------------+
| Python             |         64 |      4,713 |      1,157 |        901 |      6,771 |
| JSON               |         10 |      3,903 |          0 |          7 |      3,910 |
| YAML               |          4 |         79 |         16 |         19 |        114 |
| JSON with Comments |          1 |         39 |          4 |          4 |         47 |
+--------------------+------------+------------+------------+------------+------------+

Directories
+---------------------------------------------------------------------------------------------------------------+------------+------------+------------+------------+------------+
| path                                                                                                          | files      | code       | comment    | blank      | total      |
+---------------------------------------------------------------------------------------------------------------+------------+------------+------------+------------+------------+
| .                                                                                                             |         79 |      8,734 |      1,177 |        931 |     10,842 |
| . (Files)                                                                                                     |          1 |          3 |          0 |          2 |          5 |
| FaceDetection                                                                                                 |          5 |      3,403 |          7 |         12 |      3,422 |
| FaceIdentify                                                                                                  |         13 |      1,313 |        318 |        232 |      1,863 |
| FaceIdentify (Files)                                                                                          |          6 |        494 |        197 |         75 |        766 |
| FaceIdentify/nets                                                                                             |          2 |        180 |         48 |         34 |        262 |
| FaceIdentify/utils                                                                                            |          5 |        639 |         73 |        123 |        835 |
| MedicalInformation                                                                                            |          1 |         34 |          0 |          3 |         37 |
| ModelPredict                                                                                                  |          3 |        355 |         77 |         93 |        525 |
| PostureDetection                                                                                              |          5 |        418 |          9 |         13 |        440 |
| Settings                                                                                                      |          2 |         61 |         19 |         11 |         91 |
| UI                                                                                                            |         49 |      3,147 |        747 |        565 |      4,459 |
| UI (Files)                                                                                                    |          1 |        178 |         80 |         54 |        312 |
| UI/gui                                                                                                        |         48 |      2,969 |        667 |        511 |      4,147 |
| UI/gui/core                                                                                                   |          2 |         42 |         24 |         10 |         76 |
| UI/gui/themes                                                                                                 |          3 |         84 |          0 |          0 |         84 |
| UI/gui/uis                                                                                                    |          7 |        688 |        183 |        161 |      1,032 |
| UI/gui/uis/columns                                                                                            |          2 |         96 |         20 |         28 |        144 |
| UI/gui/uis/pages                                                                                              |          1 |        134 |         10 |         36 |        180 |
| UI/gui/uis/windows                                                                                            |          4 |        458 |        153 |         97 |        708 |
| UI/gui/uis/windows/main_window                                                                                |          4 |        458 |        153 |         97 |        708 |
| UI/gui/widgets                                                                                                |         36 |      2,155 |        460 |        340 |      2,955 |
| UI/gui/widgets (Files)                                                                                        |          1 |         13 |          0 |          0 |         13 |
| UI/gui/widgets/py_circular_progress                                                                           |          2 |         72 |         16 |         13 |        101 |
| UI/gui/widgets/py_credits_bar                                                                                 |          2 |         55 |         14 |         13 |         82 |
| UI/gui/widgets/py_grips                                                                                       |          2 |        156 |         38 |         40 |        234 |
| UI/gui/widgets/py_icon_button                                                                                 |          2 |        173 |         50 |         26 |        249 |
| UI/gui/widgets/py_image_label                                                                                 |          2 |          3 |          0 |          0 |          3 |
| UI/gui/widgets/py_left_column                                                                                 |          3 |        301 |         76 |         47 |        424 |
| UI/gui/widgets/py_left_menu                                                                                   |          4 |        429 |        109 |         85 |        623 |
| UI/gui/widgets/py_line_edit                                                                                   |          2 |         71 |          9 |          6 |         86 |
| UI/gui/widgets/py_push_button                                                                                 |          2 |         45 |          6 |          6 |         57 |
| UI/gui/widgets/py_slider                                                                                      |          2 |         74 |          4 |          5 |         83 |
| UI/gui/widgets/py_table_widget                                                                                |          3 |        192 |          7 |          7 |        206 |
| UI/gui/widgets/py_title_bar                                                                                   |          4 |        422 |        102 |         65 |        589 |
| UI/gui/widgets/py_toggle                                                                                      |          2 |         58 |          4 |         12 |         74 |
| UI/gui/widgets/py_window                                                                                      |          3 |         91 |         25 |         15 |        131 |
+---------------------------------------------------------------------------------------------------------------+------------+------------+------------+------------+------------+

Files
+---------------------------------------------------------------------------------------------------------------+--------------------+------------+------------+------------+------------+
| filename                                                                                                      | language           | code       | comment    | blank      | total      |
+---------------------------------------------------------------------------------------------------------------+--------------------+------------+------------+------------+------------+
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/FaceDetection/datapre.ipynb                                 | JSON               |      3,258 |          0 |          1 |      3,259 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/FaceDetection/eval_data.ipynb                               | JSON               |        105 |          0 |          1 |        106 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/FaceDetection/face.yaml                                     | YAML               |          7 |          0 |          1 |          8 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/FaceDetection/train-val.ipynb                               | JSON               |          1 |          0 |          1 |          2 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/FaceDetection/yolov8n_face.yaml                             | YAML               |         32 |          7 |          8 |         47 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/FaceIdentify/eval_LFW.py                                    | Python             |         27 |         20 |          9 |         56 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/FaceIdentify/eval_data.ipynb                                | JSON               |         77 |          0 |          1 |         78 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/FaceIdentify/nets/facenet.py                                | Python             |        108 |         41 |         21 |        170 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/FaceIdentify/nets/mobelnet.py                               | Python             |         72 |          7 |         13 |         92 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/FaceIdentify/path.py                                        | Python             |          2 |          0 |          0 |          2 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/FaceIdentify/predict.py                                     | Python             |         17 |         11 |         13 |         41 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/FaceIdentify/train.py                                       | Python             |        350 |        160 |         48 |        558 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/FaceIdentify/txt_annotation.py                              | Python             |         21 |          6 |          4 |         31 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/FaceIdentify/utils/callback.py                              | Python             |         98 |          0 |         11 |        109 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/FaceIdentify/utils/dataloader.py                            | Python             |        171 |         35 |         36 |        242 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/FaceIdentify/utils/utils.py                                 | Python             |         59 |         16 |         19 |         94 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/FaceIdentify/utils/utils_fit.py                             | Python             |        175 |          3 |         25 |        203 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/FaceIdentify/utils/utils_metrics.py                         | Python             |        136 |         19 |         32 |        187 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/MedicalInformation/MedicalInformation.py                    | Python             |         34 |          0 |          3 |         37 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/ModelPredict/notify_sms.py                                  | Python             |         15 |         12 |          7 |         34 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/ModelPredict/notify_voice.py                                | Python             |         30 |         10 |         10 |         50 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/ModelPredict/predict.py                                     | Python             |        310 |         55 |         76 |        441 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/PostureDetection/datapre.ipynb                              | JSON               |        158 |          0 |          1 |        159 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/PostureDetection/eval_data.ipynb                            | JSON               |        219 |          0 |          1 |        220 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/PostureDetection/fall.yaml                                  | YAML               |          8 |          2 |          2 |         12 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/PostureDetection/train-val.ipynb                            | JSON               |          1 |          0 |          1 |          2 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/PostureDetection/yolov8n_fall.yaml                          | YAML               |         32 |          7 |          8 |         47 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/Settings/json_settings.py                                   | Python             |         22 |         15 |          7 |         44 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/Settings/settings.json                                      | JSON with Comments |         39 |          4 |          4 |         47 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/core/functions.py                                    | Python             |         20 |          8 |          3 |         31 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/core/json_themes.py                                  | Python             |         22 |         16 |          7 |         45 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/themes/bright_theme.json                             | JSON               |         28 |          0 |          0 |         28 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/themes/default.json                                  | JSON               |         28 |          0 |          0 |         28 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/themes/dracula.json                                  | JSON               |         28 |          0 |          0 |         28 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/uis/columns/left_column_ui.py                        | Python             |         40 |         10 |         12 |         62 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/uis/columns/right_column_ui.py                       | Python             |         56 |         10 |         16 |         82 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/uis/pages/main_pages_ui.py                           | Python             |        134 |         10 |         36 |        180 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/uis/windows/main_window/__init__.py                  | Python             |          2 |          0 |          0 |          2 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/uis/windows/main_window/functions_main_window.py     | Python             |         79 |         27 |         20 |        126 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/uis/windows/main_window/setup_main_window.py         | Python             |        205 |         70 |         42 |        317 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/uis/windows/main_window/ui_main.py                   | Python             |        172 |         56 |         35 |        263 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/__init__.py                                  | Python             |         13 |          0 |          0 |         13 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_circular_progress/__init__.py             | Python             |          1 |          0 |          0 |          1 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_circular_progress/py_circular_progress.py | Python             |         71 |         16 |         13 |        100 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_credits_bar/__init__.py                   | Python             |          1 |          0 |          0 |          1 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_credits_bar/py_credits.py                 | Python             |         54 |         14 |         13 |         81 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_grips/__init__.py                         | Python             |          1 |          0 |          0 |          1 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_grips/py_grips.py                         | Python             |        155 |         38 |         40 |        233 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_icon_button/__init__.py                   | Python             |          1 |          0 |          0 |          1 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_icon_button/py_icon_button.py             | Python             |        172 |         50 |         26 |        248 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_image_label/__init__.py                   | Python             |          1 |          0 |          0 |          1 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_image_label/py_image_label.py             | Python             |          2 |          0 |          0 |          2 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_left_column/__init__.py                   | Python             |          3 |          0 |          0 |          3 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_left_column/py_left_button.py             | Python             |        175 |         49 |         26 |        250 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_left_column/py_left_column.py             | Python             |        123 |         27 |         21 |        171 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_left_menu/__init__.py                     | Python             |          1 |          0 |          0 |          1 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_left_menu/py_div.py                       | Python             |         15 |          2 |          3 |         20 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_left_menu/py_left_menu.py                 | Python             |        170 |         41 |         34 |        245 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_left_menu/py_left_menu_button.py          | Python             |        243 |         66 |         48 |        357 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_line_edit/__init__.py                     | Python             |          1 |          0 |          0 |          1 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_line_edit/py_line_edit.py                 | Python             |         70 |          9 |          6 |         85 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_push_button/__init__.py                   | Python             |          1 |          0 |          0 |          1 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_push_button/py_push_button.py             | Python             |         44 |          6 |          6 |         56 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_slider/__init__.py                        | Python             |          1 |          0 |          0 |          1 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_slider/py_slider.py                       | Python             |         73 |          4 |          5 |         82 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_table_widget/__init__.py                  | Python             |          1 |          0 |          0 |          1 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_table_widget/py_table_widget.py           | Python             |         62 |          5 |          3 |         70 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_table_widget/style.py                     | Python             |        129 |          2 |          4 |        135 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_title_bar/__init__.py                     | Python             |          1 |          0 |          0 |          1 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_title_bar/py_div.py                       | Python             |         16 |          2 |          3 |         21 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_title_bar/py_title_bar.py                 | Python             |        230 |         51 |         36 |        317 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_title_bar/py_title_button.py              | Python             |        175 |         49 |         26 |        250 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_toggle/__init__.py                        | Python             |          1 |          0 |          0 |          1 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_toggle/py_toggle.py                       | Python             |         57 |          4 |         12 |         73 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_window/__init__.py                        | Python             |          1 |          0 |          0 |          1 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_window/py_window.py                       | Python             |         79 |         24 |         15 |        118 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/gui/widgets/py_window/styles.py                          | Python             |         11 |          1 |          0 |         12 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/UI/main.py                                                  | Python             |        178 |         80 |         54 |        312 |
| /Users/jayden/Documents/FallDetectionSystem-统计代码行/main.py                                                     | Python             |          3 |          0 |          2 |          5 |
| Total                                                                                                         |                    |      8,734 |      1,177 |        931 |     10,842 |
+---------------------------------------------------------------------------------------------------------------+--------------------+------------+------------+------------+------------+
"""