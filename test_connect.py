from mongoengine import connect


try:
        connect(host='mongodb+srv://annka:PPBVqTIHCRrtHgMy@cluster0.7dlllzi.mongodb.net/?retryWrites=true&w=majority')
        print("ok connection")
except:
        print('no connection')