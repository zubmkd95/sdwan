def create_team(team_name):
    """Create a new Webex team."""
    url = f"{BASE_URL}/teams"
    payload = {
        "name": team_name
    }
    
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code == 200:
        return response.json()["id"]
    else:
        print(f"Error creating team: {response.text}")
        return None

 def create_space(team_id, space_name):
    """Create a new space in the team."""
    url = f"{BASE_URL}/rooms"
    payload = {
        "title": space_name,
        "teamId": team_id
    }
    
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code == 200:
        return response.json()["id"]
    else:
        print(f"Error creating space: {response.text}")
        return None


 def add_member_to_space(space_id, email):
    """Add a member to the space."""
    url = f"{BASE_URL}/memberships"
    payload = {
        "roomId": space_id,
        "personEmail": email,
        "isModerator": False
    }
    
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code == 200:
        print(f"Successfully added {email} to the space")
    else:
        print(f"Error adding member: {response.text}")

def add_member_to_team(team_id, email):
    """Add a member to the team."""
    url = f"{BASE_URL}/team/memberships"
    payload = {
        "teamId": team_id,
        "personEmail": email,
        "isModerator": False
    }
    
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code == 200:
        print(f"Successfully added {email} to the team")
    else:
        print(f"Error adding member to team: {response.text}")


  def post_message(space_id, message):
    """Post a message to the space."""
    url = f"{BASE_URL}/messages"
    payload = {
        "roomId": space_id,
        "text": message
    }
    
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code == 200:
        print("Message posted successfully")
    else:
        print(f"Error posting message: {response.text}")            