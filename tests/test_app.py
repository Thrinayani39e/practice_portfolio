# tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app, TimelinePost

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def tearDown(self):
        # Keep tests isolated: clear posts so each starts with an empty table.
        TimelinePost.delete().execute()

    def test_home(self):
        response = self.client.get("/", follow_redirects=True)
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "Thrinayani" in html
        # more tests relating to the home page
        # navbar should link out to the other pages in the app
        for link in ("/experience", "/hobbies", "/timeline", "/projects"):
            assert link in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
        # more tests relating to the /api/timeline_post GET and POST apis
        ada = self.client.post("/api/timeline_post", data={
            "name": "Ada Lovelace",
            "email": "ada@example.com",
            "content": "First programmer.",
        }).get_json()
        assert ada["content"] == "First programmer."

        self.client.post("/api/timeline_post", data={
            "name": "Alan Turing",
            "email": "alan@example.com",
            "content": "Can machines think?",
        })

        posts = self.client.get("/api/timeline_post").get_json()["timeline_posts"]
        assert len(posts) == 2
        names = {p["name"] for p in posts}
        assert names == {"Ada Lovelace", "Alan Turing"}

        delete = self.client.delete(f"/api/timeline_post/{ada['id']}")
        assert delete.status_code == 200
        remaining = self.client.get("/api/timeline_post").get_json()["timeline_posts"]
        assert len(remaining) == 1
        assert remaining[0]["name"] == "Alan Turing"

        # more tests relating to the timeline page
        # timeline page should render the post form (name/email/content)
        page = self.client.get("/timeline")
        assert page.status_code == 200
        page_html = page.get_data(as_text=True)
        assert '<form' in page_html
        for field in ('name="name"', 'name="email"', 'name="content"'):
            assert field in page_html

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html


if __name__ == '__main__':
    unittest.main()
