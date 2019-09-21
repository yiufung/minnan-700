# Expand 700iongji.csv to generate csv for Anki import.
# ***Need to rename all mp3s to minnan700-***.mp3 first.***

import pandas as pd

iongji = pd.read_csv('/media/nas_documents/闽南语/700iongji.csv')

anki_iongji = iongji.copy()
anki_iongji = pd.concat([anki_iongji, anki_iongji['用例'].str.split('、', expand = True)], axis=1)

# 用字讀音
anki_iongji['用字讀音'] = '[sound:minnan700-' + anki_iongji["編號"].map(str) + '-' + anki_iongji['建議用字'] + '.mp3]'
# 用例讀音：total 5 columns
anki_iongji['用例讀音一'] = '[sound:minnan700-' + anki_iongji["編號"].map(str) + '-' + anki_iongji[0] + '.mp3]'
anki_iongji['用例讀音二'] = '[sound:minnan700-' + anki_iongji["編號"].map(str) + '-' + anki_iongji[1] + '.mp3]'
anki_iongji['用例讀音三'] = '[sound:minnan700-' + anki_iongji["編號"].map(str) + '-' + anki_iongji[2] + '.mp3]'
anki_iongji['用例讀音四'] = '[sound:minnan700-' + anki_iongji["編號"].map(str) + '-' + anki_iongji[3] + '.mp3]'
anki_iongji['用例讀音五'] = '[sound:minnan700-' + anki_iongji["編號"].map(str) + '-' + anki_iongji[4] + '.mp3]'
# tag column required by anki.
anki_iongji['tag'] = '閩南語'

# Anki deck 里所有columns
all_columns = ['編號', '建議用字', '音讀', '又音', '對應華語', '用例', '異用字', '用字讀音', '用例讀音一', '用例讀音二', '用例讀音三', '用例讀音四', '用例讀音五', 'tag']

anki_iongji.fillna("", inplace=True)
anki_iongji = anki_iongji[all_columns]

anki_iongji.to_csv("/media/nas_documents/闽南语/anki_csv.csv", index=None, header=None)
anki_iongji
