# core
from casatasks import importfits, imsmooth, imhead, exportfits
import shutil
commonPath = '/data/RF'

def Align_cubes(pathIN, kernel, tarBeam, fitsOUT, f0) : # 因為又統一解析度又改寫標頭，所以叫命名為對齊
    importfits(fitsimage=pathIN, imagename='casaIN.image', overwrite=True) 
    print('tataima!')
    imsmooth(imagename='casaIN.image', outfile='casaOUT.image', kernel=kernel, beam=tarBeam, targetres=True, overwrite=True)
    imhead(imagename='casaOUT.image', mode='put', hdkey='restfreq', hdvalue=str(f0)) # 資料型態竟然要是字串，不客氣，幫轉了
    print(f"Header keyWord 'RESTFREQ' now is {f0} Hz") 
    exportfits(imagename='casaOUT.image', fitsimage=fitsOUT, overwrite=True)
    shutil.rmtree('casaIN.image')
    shutil.rmtree('casaOUT.image')
    print('Metafiles cleaned')

# CO 
path = f'{commonPath}Cloverleaf.spw27_CO.fits'
out = 'CO-3-2_cube_smoothed-1515.fits'
tarBeam = {'major': '1.5arcsec', 'minor': '1.5arcsec', 'pa': '0deg'}
Align_cubes(path, 'g', tarBeam, out, 1.15271E+11)


# CN
path = f'{commonPath}Cloverleaf.spw25_CN.fits'
out = 'CN-3-2_cube_smoothed-1515.fits'
tarBeam = {'major': '1.5arcsec', 'minor': '1.5arcsec', 'pa': '0deg'}
Align_cubes(path, 'g', tarBeam, out, 1.15271E+11)
