#!/bin/bash

# 1. Post a new random entry
echo "Adding a new timeline post..."
POST_RESPONSE=$(curl -X POST http://localhost:5000/api/timeline_post -d 'name=TestUser&email=test@example.com&content=This is a random test post.')
echo "POST Response: $POST_RESPONSE"

# 2. Extract the ID of the new post from the JSON response
# This assumes your API returns {"id": 1, ...}
POST_ID=$(echo $POST_RESPONSE | grep -o '"id":[0-9]*' | cut -d: -f2)
echo "Added post with ID: $POST_ID"

# 3. Fetch all entries to verify the post was added
echo -e "\nFetching all timeline posts to verify:"
curl http://localhost:5000/api/timeline_post

# 4. Delete the entry
if [ ! -z "$POST_ID" ]; then
    echo -e "\n\nDeleting test post with ID: $POST_ID..."
    curl -X DELETE http://localhost:5000/api/timeline_post/$POST_ID
fi
