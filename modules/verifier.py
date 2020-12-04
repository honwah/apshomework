"""
aps排程文档校验，校验时如发现不符合要求的文档会抛出异常
"""

import pandas as pd
import numpy as np

column_crca = ["ARBPL", "KAPAZ"]  # 工作产能中心表头
column_mara = ["MATNR", "MATKL"]  # 物料主数据表头
column_plaf = ["PLNUM", "MATNR", "PLWRK", "GSMNG", "PEDTR"]  # 计划订单清单表头
column_plpo = ["MATNR", "ARBPL", "TIME"]  # 物料工艺路线表头
docpath = "../documents/"
dfcrca = pd.read_csv(docpath + "CRCA.csv")
dfmara = pd.read_csv(docpath + "MARA.csv")
dfplaf = pd.read_csv(docpath + "PLAF.csv")
dfplpo = pd.read_csv(docpath + "PLPO.csv")


# 校验工作产能中心文件格式
def verify_crca(df):
    right = False
    actualcol = df.columns.values
    if np.array_equal(actualcol, column_crca):
        right = True
    return right


# 校验物料主数据格式
def verify_mara(df):
    right = False
    actualcol = df.columns.values
    if np.array_equal(actualcol, column_mara):
        right = True
    return right

# 校验计划订单清单格式
def verify_plaf(df):
    right = False
    actualcol = df.columns.values
    if np.array_equal(actualcol, column_plaf):
        right = True
    return right

# 校验物料工艺路线格式
def verify_plpo(df):
    right = False
    actualcol = df.columns.values
    if np.array_equal(actualcol, column_plpo):
        right = True
    return right

if (__name__ == "__main__"):
    print(verify_crca(dfcrca))
    print(verify_mara(dfmara))
    print(verify_plaf(dfplaf))
    print(verify_plpo(dfplpo))
