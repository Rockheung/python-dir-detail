from __future__ import print_function
import os

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



def ddir( obj =object, kwd ='', exc =[ '__doc__'] ):
  isobjDefault ='__main__' not in dir() and obj is object

  if isobjDefault :
    import __main__
    obj =__main__

  print( repr( obj) )

  try :
    isClass =issubclass( obj, object)
  except TypeError :
    isClass =False

  moduleList =dir( obj)
  maxLen =max( map( len, moduleList ) )

  try :
    moduleName =obj.__name__

  except AttributeError:
    try :
      moduleName =repr( obj).split("'")[1]

    except IndexError:
      print( 'Failed to get module name. Check it out.')
      return

  isDunbar =obj.__name__ is not repr( obj).split("'")[1]
  moduleName =obj.__name__ if not isDunbar and not isClass else repr( obj).split("'")[1]

  for mI in moduleList:
    try :
      mExplain =repr( eval( moduleName +'.' +mI ) )

    except AttributeError:
      print( '{:^{w}}'.format( mI, w =maxLen ) )
      break

    if type( mExplain) is dict:
      print( mI)
      d(mExplain)

    else :
      print( '{:^{w}}| {}'.format( mI, mExplain, w =maxLen ) )

  if isobjDefault :
    del __main__

