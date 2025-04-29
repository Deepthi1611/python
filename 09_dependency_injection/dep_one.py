# without dependency injection

class Database:
    def connect(self):
        return 'connected to database'
    
class Service:
    def __init__(self):
        self.db = Database() # tightly coupled

    def get_data(self):
        return self.db.connect()
    
# usage
service = Service()
print(service.get_data())