train = train.drop(['ID'], axis=1)
train['대출기간'] = train['대출기간'].str.replace(" months", "")
train['대출기간'] = train['대출기간'].astype(int)
train['근로기간'] = train['근로기간'].str.replace(' years', '').str.replace(' years', '')
train['근로기간'] = train['근로기간'].str.replace(' year', '').str.replace('years', '')
train['근로기간'] = train['근로기간'].str.replace('10+', '10')
train['근로기간'] = train['근로기간'].str.replace('10\+', '10')
train['근로기간'] = train['근로기간'].str.replace('<1', '0').str.replace("< 1", '1')
train['근로기간'] = train['근로기간'].str.replace("Unknown", '0')

train['근로기간'] = train['근로기간'].astype(int)

cols_to_cate = ['대출기간', '근로기간', '주택소유상태', '대출목적']
train[cols_to_cate] = train[cols_to_cate].astype("category")

grade_mapping = {'ANY': 5, 'RENT': 10, 'MORTGAGE': 20, 'OWN': 30}
train['주택소유상태'] = train['주택소유상태'].map(grade_mapping)
