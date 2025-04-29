# with dependency injection

class Database:
    def connect(self):
        return 'connected to database'
    
class Service:
    def __init__(self, db: Database):
        self.db = db # loosely coupled

    def get_data(self):
        return self.db.connect()
    
# usage
db = Database()

service = Service(db)
print(service.get_data())