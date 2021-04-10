import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as ss
import cooler
from cooltools import eigdecomp
from chromosight.utils.preprocessing import detrend

CHROM = 'chr18'

clr = cooler.Cooler('SRR6675327_hic_hsap_GM12878_100kb.cool')


def viz_eig(chrom):
    mat = clr.matrix(sparse=False, balance=True).fetch(chrom)
    values, eig_df = eigdecomp.cis_eig(mat)
    eig_df = pd.DataFrame({'E0': eig_df[0, :], 'E1': eig_df[1, :], 'E2': eig_df[2, :]})
    eig_df = pd.concat([clr.bins().fetch(chrom).reset_index(drop=True), eig_df], axis=1)
    gc = pd.read_csv('hg19_gc.tsv', sep='\t')
    gc = gc.loc[gc.chrom == chrom, :]
    gc = gc.reset_index(drop=True)
    df = eig_df.merge(gc[['end', 'GC']], on='end', how='inner')
    fig, ax = plt.subplots(1, 3)
    df_valid = df.dropna()
    for i, eig in enumerate(['E0', 'E1', 'E2']):
        sns.regplot(data=df, x='GC', y=eig, ax=ax[i])
        coeff = ss.pearsonr(df_valid.GC, df_valid[eig])[0]
        ax[i].set_title(f'{eig}: {coeff:.2f}')
    return df

df = viz_eig(CHROM)
df.to_csv(f'hg19_100kb_eig_vs_gc_{CHROM}.tsv', sep='\t', index=False)
plt.show()

mat = clr.matrix(sparse=True, balance=True).fetch(CHROM)
bad = np.isnan(clr.bins().fetch(CHROM).weight).values
mat = mat.tocsr()
mat = mat[~bad, :][:, ~bad]
mat = mat.tocoo()
df = df.loc[~bad[:-1], :].reset_index(drop=True)
plt.figure(dpi=300)
plt.imshow(np.log10(mat.toarray()), cmap='afmhot_r')
plt.show()
plt.figure(dpi=300)
plt.imshow(detrend(mat).toarray(), cmap='afmhot_r', vmax=2.5)
plt.show()

fig, ax = plt.subplots(2, 3, gridspec_kw={'height_ratios': [20, 1]})
for i, eig in enumerate(['E0', 'E1', 'E2']):
    eigv = np.nan_to_num(np.array(df[eig]))
    ax[0, i].imshow(eigv[:, None] @ eigv[None, :], cmap='bwr', vmin=-.0001, vmax=.0001)
    a = eigv.copy()
    b = eigv.copy()
    a[a<=0] = 0
    b[b>0] = 0
    ax[1, i].fill_between(df.index, 0, a, color="g")
    ax[1, i].fill_between(df.index, 0, b, color="r")
    ax[1, i].axhline(0, c="black")

plt.show()
