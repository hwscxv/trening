
def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

name = input('podaj imie')
times = int(input('ile razy'))

def repeat(times):
    def wrapper(func):
        def i_wrapper(*args, **kwargs):
            response = []
            for _ in range(times):
                response.append(func(*args, **kwargs))

            return response
        
        return i_wrapper
    
    return wrapper




# def repeat(func):

#     def i_wrapper(*args, **kwargs):

#         response = []
#         for i in range(times):
#             response.append(func(*args, **kwargs))

#         return response
    
#     return i_wrapper





@repeat(times)
def hello(name):
    return f'hello {name}'

print(hello(name))

