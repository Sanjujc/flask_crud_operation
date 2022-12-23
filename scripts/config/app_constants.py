class Status:
    executed = 'Successfully Executed'
    error_occurred = 'Error Occurred'


class CollectionName:
    user_management = "user_management"


class MongoQuery:
    def update_query(self, key, values):
        ud_query = {
            f'{key}': f'{values}'
        }
        return ud_query
