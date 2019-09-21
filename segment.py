# Adjust spacings in Audacity and use labels from csv sheet to generate
# timestamps. The final labels used to split audio is 'computed_labels.txt'.

import pandas as pd

labels = pd.read_csv('/media/nas_documents/闽南语/labels/all_labels.txt', sep='\t', header=None)
iongji = pd.read_csv('/media/nas_documents/闽南语/700iongji.csv')

print(labels.shape)
print(iongji.shape)
print(labels.head(5))
print(iongji.head(5))

all_segments = []
for index, row in iongji[['編號', '建議用字', '用例']].iterrows():
    if index not in [41]: # Case 42 無主編號
        all_segments.append('-'.join([str(row['編號']), row['建議用字']]))
    all_segments.extend([str(row['編號']) + '-' +  s for s in row['用例'].split('、')])
    if index in [62]: # Special case for case 63
        all_segments.extend([str(row['編號']) + '-2-' +  s for s in row['用例'].split('、')])

# 所有用例加起來的數字應該和labels一樣
print("Total segments: {}".format(len(all_segments)))
# assert(len(all_segments) == labels.shape[0])

labels.columns = ['start', 'end', 'label']

# assign computed labels and see if they match in audacity
labels['label'] = pd.Series(all_segments)

labels.to_csv('/media/nas_documents/闽南语/labels/computed_labels.txt', header=None, sep='\t', index=None)
