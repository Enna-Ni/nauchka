import pandas as pd
import matplotlib.pyplot as plt
def star_magn(data):
    df = pd.read_csv(data, sep=r'\s+')
    mjd = df['#'].values
    mag = df['MJD'].values
    plt.scatter(mjd, mag, s=15, alpha=0.7, linewidths=0.3)
    plt.gca().invert_yaxis()
    plt.xlabel('Мод. юлианская дата, дни', fontsize=20)
    plt.ylabel('Видимая зв. величина', fontsize=20)
    plt.title(f'Кривая блеска звезды {data}', fontsize=25)
    plt.xticks(size = 15)
    plt.yticks(size = 15)   
    plt.show()
star_magn("k.txt")