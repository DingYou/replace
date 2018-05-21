# -*- coding: utf-8 -*-

import os
import sys

path = sys.path[0]
conf = open('%s%s%s' % (path, '/', 'replace.conf'))
confFile = conf.read()
confRows = confFile.split("\n")

sourcePath = ('%s%s%s' % (path, '/', 'source'))
targetPath = ('%s%s%s' % (path, '/', 'target'))
sourceFileList = os.listdir(sourcePath)

for file in sourceFileList:
    sourceFilePath = '%s%s%s' % (sourcePath, '/', file)
    print('读取文件: %s' % sourceFilePath)
    sourceFile = open(sourceFilePath).read()
    for confRow in confRows:
        if confRow.startswith('#'):
            continue
        old = confRow.split("=")[0]
        new = confRow.split("=")[1]
        print('替换 %s => %s' % (old, new))
        sourceFile = sourceFile.replace(old, new)
    targetName = '%s%s.%s' % (file.split(".")[0], '_target', file.split(".")[1])
    print('生成新文件: %s%s%s' % (targetPath, '/', targetName))
    with open('%s%s%s' % (targetPath, '/', targetName), 'w') as targetFile:
        targetFile.write(sourceFile)
print('替换结束...')
input("Press <enter> to exit...")
