import os

def d( kwd ='', obj =globals(), root ='/', esc =[ '__doc__']):

  # Get terminal's pixel width from os
  ttyh, ttyw =tuple( list( map( int, os.popen( 'stty size', 'r').read().split() ) ) )

  # Print table from dict type data including string type kwd variable
  while True:

    # Sort keys by alphabetical order.
    # If Non-string type key exist, exclude it.
    try :
      objKeys =list( filter( lambda x: kwd in x, obj.keys() ) )
      objKeys =sorted( objKeys)

    except TypeError:
      objEtcs =list( filter( lambda x: type( x) is str, obj.keys() ) )
      objKeys =list( filter( lambda x: x not in objEtcs, obj.keys() ) )
      objKeys =list( filter( lambda x: kwd in x, objKeys ) )
      objKeys =sorted( objKeys)

    # Get key's max string length.
    maxLen =max( map( len, objKeys ) )

    largerTen = 2 if len( objKeys) >=100 else 1 if len( objKeys) >=10 else 0

    try :
      assert largerTen <=2
    except AssertionError :
      print( 'Too big dictionary')
      break

    for i, key in enumerate(objKeys, start =1) :
      explain =str(obj[key]) if '\n' not in str(obj[key]) else str(obj[key]).split('\n')[0] +' ...More'
      print('{:{n}d}.{:^{w}}| {:.{p}}'.format( i,
                                               key,
                                               explain,
                                               n =1 +largerTen,
                                               w =maxLen,
                                               p =ttyw -maxLen -4 -largerTen )
           )

    kwd =input('{} '.format( root) )
    objKeys =list( filter( lambda x: kwd[:-1] if kwd[-1] =='/' else kwd in x, objKeys ) )

    if kwd =='..' :
      return

    elif kwd =='' :
      break

    elif kwd =='.' :
      kwd =''
      continue

    elif len( objKeys ) ==1 :

      new_obj =dict()
      subroot ='{}{}'.format( '.'.join( root.split('/')[1:] ),
                                objKeys[0] )

      for i in dir( eval( subroot ) ):
        try :
          new_obj[i] =eval( subroot +'.' +i )
        except AttributeError :
          new_obj[i] =None

      d( obj =new_obj, root =root +objKeys[0] +'/' )
      kwd =''

    elif kwd[-1] =='/' and kwd[:-1] in objKeys :

      new_obj =dict()
      subroot = '{}{}'.format( '.'.join( root.split('/')[1:] ),
                                 kwd[:-1] )

      print(subroot, '\n')
      for i in dir( eval( subroot ) ):
        try :
          new_obj[i] =eval( subroot +'.' +i )
        except AttributeError :
          new_obj[i] =None

      d( obj =new_obj, root =root +kwd )
      kwd =''

    else :
      pass
