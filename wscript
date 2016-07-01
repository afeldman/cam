top = '.'

def options(opt):
    opt.load('python')

def configure(conf):
    conf.load('python')
    conf.check_python_version((2,7,0))

    try:
        conf.check_python_module('os')
    except:
        print('python module os missing')

    try:
        conf.check_python_module('sys')
    except:
        print('python module sys missing')

    try:
        conf.check_python_module('math')
    except:
        print('python module math missing')
