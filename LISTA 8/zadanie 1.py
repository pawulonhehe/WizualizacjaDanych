import numpy as np
import pandas as pd
import xlrd
import openpyxl

xlsx=pd.ExcelFile('imiona.xlsx')
df=pd.read_excel(xlsx, 'Arkusz1')
print(df)