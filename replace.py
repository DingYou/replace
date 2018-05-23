# -*- coding:utf-8 -*-
"""
Copyright 2018 DingYou

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import os
import sys
import platform
from typing import Dict

currentSys = platform.system()
print('当前系统%s' % currentSys)
separate = ('\\' if ('Windows' in currentSys) else '/')

path = sys.path[0]
__conf_dict: Dict[str, str] = {}


def read_config(conf_file_path):
    print('读取配置文件:%s' % conf_file_path)
    conf = open(conf_file_path, encoding='utf-8')
    conf_file = conf.read()
    conf_rows = conf_file.split("\n")
    for confRow in conf_rows:
        if confRow is None or confRow == '' or confRow.startswith('#'):
            continue
        conf_arr = confRow.split('=')
        flag = True
        old = ''
        new = ''
        for i in range(0, len(conf_arr)):
            temp = conf_arr[i]
            strip_str = temp.rstrip('\\')
            if temp != strip_str:
                if flag:
                    old = '%s%s%s' % (old, strip_str, '=')
                else:
                    new = '%s%s%s' % (new, strip_str, '=')
            else:
                if flag:
                    old = '%s%s' % (old, strip_str)
                    flag = False
                else:
                    new = '%s%s' % (new, strip_str)
        __conf_dict[old] = new


read_config('%s%s%s' % (path, separate, 'replace.conf'))

sourcePath = ('%s%s%s' % (path, separate, 'source'))
targetPath = ('%s%s%s' % (path, separate, 'result'))
sourceFileList = os.listdir(sourcePath)

for file in sourceFileList:
    sourceFilePath = '%s%s%s' % (sourcePath, separate, file)
    print('读取文件: %s' % sourceFilePath)
    sourceFile = open(sourceFilePath, encoding='utf-8').read()
    for k, v in __conf_dict.items():
        print('替换 %s => %s' % (k, v))
        sourceFile = sourceFile.replace(k, v)
    targetName = '%s%s.%s' % (file.split('.')[0], '_result', file.split('.')[1])
    print('生成新文件: %s%s%s' % (targetPath, separate, targetName))
    with open('%s%s%s' % (targetPath, separate, targetName), 'w', encoding='utf-8') as targetFile:
        targetFile.write(sourceFile)
print('替换完成...')
input('Press <enter> to exit...')
