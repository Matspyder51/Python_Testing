from locust import HttpUser, task

class User(HttpUser):
    
    @task
    def index(self):
        self.client.get("/")

    def on_start(self):
        self.client.post("/showSummary", {"email": "john@simplylift.co"})

    @task
    def board(self):
        self.client.get("/board")

    @task
    def purchaseLift(self):
        self.client.post(
            "/purchasePlaces",
            data = {
                'club': 'Simply Lift',
                'competition': 'Spring Festival',
                'places': '2'
            }
        )

    @task
    def purchaseIron(self):
        self.client.post(
            "/purchasePlaces",
            data = {
                'club': 'Iron Temple',
                'competition': 'Fall Classic',
                'places': '3'
            }
        )

    @task
    def purchaseInFuture(self):
        self.client.post(
            "/purchasePlaces",
            data = {
                'club': 'She Lifts',
                'competition': 'Winter Land',
                'places': '8'
            }
        )