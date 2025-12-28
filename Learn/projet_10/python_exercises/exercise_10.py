# Exercise 10: Subscriptions
# Practice managing subscriptions and notifications

# TODO: Create a class 'SubscriptionManager'
# - __init__: create empty subscriptions dict
# - subscribe: add callback for uri
# - unsubscribe: remove callback for uri
# - notify: call all callbacks for uri with data

# TODO: Create a function 'handle_subscription_request'
# Parameters: uri (str), callback (function)
# Use SubscriptionManager to handle the request
# Return success message

class SubscriptionManager:
    def __init__(self):
        self.subscriptions = {}

    def subscribe(self, uri: str, callback):
        # TODO: Implement
        pass

    def unsubscribe(self, uri: str, callback):
        # TODO: Implement
        pass

    def notify(self, uri: str, data):
        # TODO: Implement
        pass

def handle_subscription_request(uri: str, callback):
    # TODO: Implement
    pass

def main():
    # Test subscription system
    pass

if __name__ == "__main__":
    main()
