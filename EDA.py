# 타겟컬럼(대출등급)의 비율 시각화
train.loc[:, '대출등급'].value_counts().reset_index().rename(columns={'index':"대출등급", "대출등급":"카운트"}).assign(
    percent=lambda df_: (df_['카운트'] / df_['카운트'].sum()).round(2) * 100
)

y_var = train.loc[:, '대출등급'].value_counts().reset_index().rename(columns={'index':"대출등급", "대출등급":"카운트"}).assign(
    percent=lambda df_: (df_['카운트'] / df_['카운트'].sum()).round(2) * 100)

plt.pie(
    x=y_var['percent'],
    autopct='%.0f%%',
    shadow=True,
    textprops={'fontsize':10, 'color':'#000000'},
)

plt.title("대출등급 데이터 비율", fontsize=14)
plt.legend(y_var['대출등급'], loc='best', fontsize=8)
plt.show()


# 특정 열들의 분포 확인 (대출기간, 근로기간, 주택소유상태, 대출목적)
def counts_plot(rating, col='w', ax=None):
    rating_counts = (
        train.loc[:, rating].value_counts().reset_index()
        .rename(columns={'index':rating, rating:"counts"})
        .assign(percent=lambda df_: (df_['counts'] / df_['counts'].sum()) * 100)
    )
    sns.set_context("paper")
    ax0 = sns.barplot(
        data=rating_counts,
        x='percent',
        y=rating,
        color=col,
        ax=ax,
        order=rating_counts[rating]
    )
    values1 = ax0.containers[0].datavalues
    labels = ["{:g}%".format(val) for val in values1]
    ax0.bar_label(ax0.containers[0], labels=labels, fontsize=9, color='#740405')
    ax0.set_ylabel("")
    ax0.set_xlabel("Percent", fontsize=10)
    ax0.set_title(str.title(rating) + " | proportions ", fontsize=10)
    return


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(11, 6))

counts_plot("대출기간", ax=ax1, col='#009688')
counts_plot("근로기간", ax=ax2, col='#35a79c')
counts_plot("주택소유상태", ax=ax3, col='#59b2a9')
counts_plot("대출목적", ax=ax4, col='#83d0c9')

fig.tight_layout()
plt.show()



# 상관관계
corr_df = train.copy()
corr_matrix=corr_df.corr()

mask = np.zeros_like(corr_matrix)
mask[np.triu_indices_from(mask)] = True

f, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(corr_matrix, mask=mask, annot=True, annot_kws={"size": 8})
plt.suptitle("상관관계")
plt.show()



# 대출등급별 대출기간
unique_values = sorted(train['대출등급'].unique().tolist())

hue_order = sorted(train['대출등급'].unique().tolist())
ax = sns.countplot(x='대출등급', hue='대출기간', data=train, order=hue_order)

for p in ax.patches:
    height = p.get_height()
    ax.annotate(f'{int(height)}', (p.get_x() + p.get_width() / 2, height), ha='center', va='bottom', color='grey', fontsize=8)

plt.title('대출등급별 대출기간', fontweight='bold')
plt.xlabel('대출등급')
plt.ylabel('명수')
plt.legend(title='대출기간')
plt.show()



# 대출등급에 따른 대출목적 분포
grouped = ori_train.groupby('대출등급')['대출목적'].value_counts()
grouped.unstack().plot(kind='bar', stacked=True)
plt.xlabel('대출등급')
plt.ylabel('빈도수')
plt.title('대출등급에 따른 대출목적 분포')
plt.show()
