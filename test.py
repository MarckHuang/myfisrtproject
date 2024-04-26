def info(name, **kw):
    print('name is', name)
    for k,v in kw.items():
        print(k,v)
info('Mike', age=21, country='Taiwan')
print(info)