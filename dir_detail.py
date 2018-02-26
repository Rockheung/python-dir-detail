import os

def d( kwd ='', obj =globals(), exc =[ '__doc__'], lines =1 ):
  ttyw =int( os.popen( 'stty size', 'r').read().split()[1] )

  objKeys =obj.keys()
  maxLen =max( map( len, objKeys ) )

  try :
    objKeys =list( filter( lambda x: kwd in x, objKeys ) )
    objKeys =sorted( objKeys)

  except TypeError:
    objEtcs =list( filter( lambda x: type( x) is str, objKeys ) )
    objKeys =list( filter( lambda x: x not in objEtcs, objKeys ) )
    objKeys =list( filter( lambda x: kwd in x, objKeys ) )
    objKeys =sorted( objKeys)


  while True:

    for i in objKeys:
      if i not in exc:
        print('{:^{w}}| {:.{p}}'.format( i, str(obj[i]), w =maxLen, p =ttyw -maxLen -2 ) )

    kwd =input('\\ ')

    if kwd == '' or len(objKeys) ==0 :
      break
    elif len(objKeys) ==1 :
      objKey = objKeys

      objKeys =dir( eval( objKey) )

    objKeys =list( filter( lambda x: kwd in x, objKeys ) )

  



# def ddir( obj =object, kwd ='', exc =[ '__doc__'] ):
#   isobjDefault ='__main__' not in dir() and obj is object
# 
#   if isobjDefault :
#     import __main__
#     obj =__main__
# 
#   print( repr( obj) )
# 
#   try :
#     isClass =issubclass( obj, object)
#   except TypeError :
#     isClass =False
# 
#   moduleList =dir( obj)
#   maxLen =max( map( len, moduleList ) )
# 
#   try :
#     moduleName =obj.__name__
# 
#   except AttributeError:
#     try :
#       moduleName =repr( obj).split("'")[1]
# 
#     except IndexError:
#       print( 'Failed to get module name. Check it out.')
#       return
# 
#   isDunbar =obj.__name__ is not repr( obj).split("'")[1]
#   moduleName =obj.__name__ if not isDunbar and not isClass else repr( obj).split("'")[1]
# 
#   for mI in moduleList:
#     try :
#       mExplain =repr( eval( moduleName +'.' +mI ) )
# 
#     except AttributeError:
#       print( '{:^{w}}'.format( mI, w =maxLen ) )
#       break
# 
#     if type( mExplain) is obj:
#       print( mI)
#       d(mExplain)
# 
#     else :
#       print( '{:^{w}}| {}'.format( mI, mExplain, w =maxLen ) )
# 
#   if isobjDefault :
#     del __main__
# 
