from __future__ import print_function
import os
ttyR, ttyC =map( int, os.popen( 'stty size', 'r').read().split() )


def d( dictStyle =eval( 'globals()'), kwd ='', exc =[ '__doc__'] ):

  dictKeys = dictStyle.keys()
  maxLen =max( map( len, dictKeys ) )

  try :
    dictKeys =sorted( dictKeys)
  except TypeError:
    pass

  for i in dictKeys:
    if i not in exc:
      try :
        print('|- {:^{w}}| {}'.format( i, dictStyle[i], w =maxLen ) )
      except TypeError:
        print('|- {}| {}'.format( i, dictStyle[i] ) )



def ddir( obj =None, kwd ='', exc =[ '__doc__'] ):
  objDefault ='__main__' not in dir() and obj is None

  if objDefault :
    import __main__
    obj =__main__

  mList =dir( obj)
  maxLen =max( map( len, mList ) )
  for mI in mList:
    try:
      mExplain =eval( obj.__name__ +'.' +mI )
      if type( mExplain) is dict:
        print( mI)
        d(mExplain)
      else :
        print( '{:^{w}}| {}'.format( mI, mExplain, w =maxLen ) )

    except AttributeError:
      print( '{:^{w}}'.format( mI, w =maxLen ) )

    except NameError:
      print( '{}'.format( mI) )

  if objDefault :
    del __main__

