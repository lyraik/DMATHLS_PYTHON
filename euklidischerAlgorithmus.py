import numpy as np
import pandas as pd

def erweiterter_euklidischer_algo(a0, a1):
    """
    Berechnet ein DataFrame df mit den Spalten 'a', 'x', 'y'.
    Die ersten beiden Zeilen sind
    a   x  y
    --------
    a0  1  0
    a1  0  1
    für jede weitere Spalte gilt
    ndf.iloc[i+2] ==  df.iloc[i] - q * df.iloc[i+1]  
    wobei q = df.iloc[i, 0] // df.iloc[i+1, 0].
    Die letze Zeile ist (ai, x, y), wobei
    ai = ggT(a0, a1) = x * a0 + y * a1
    
    :param a0: Erstes Argument für ggT
    :param a1: Zweites Argument für ggT
    :returns: Ein Dataframe, das die Berchnung des ggT
        mit dem erweiterten Euklidischen Algo zeigt.
    """
    arr =  np.array(
        [[a0, 1, 0], [a1, 0, 1]])
    while True:
        q = arr[-2, 0] // arr[-1, 0]
        neue_zeile = arr[-2] - q * arr[-1]
        if neue_zeile[0] == 0:
            break
        arr = np.vstack((arr, neue_zeile))
    return pd.DataFrame(arr, columns = ['a', 'x', 'y'])

print(erweiterter_euklidischer_algo(93, 42))
"""
im output ist a der ggT, x und y sind die Koeffizienten
also a*x + b*y = ggT(a,b)"""
