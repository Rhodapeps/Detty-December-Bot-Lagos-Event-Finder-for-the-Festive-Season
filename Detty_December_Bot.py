# Detty December Bot: A guide to discovering events in Lagos during the festive season.
# This bot helps users find concerts, beach parties, kid-friendly activities, and more
# based on their preferences for event type and location.

class DettyDecemberBot:
    def __init__(self):
        self.messages = []  # Initialize the message list
        self.events = []  # Initialize the events list

    def greet_user(self):
        """Returns a greeting message for the user."""
        return ("Welcome to the Detty December Lagos guide! 🎉"
                " I can help you explore the hottest events, parties, concerts, cinema experiences, and family-friendly activities for kids and teens lined up in Lagos."
                " Just let me know what you're looking for!")

    def collect_preferences(self, input_text):
        """Analyzes user preferences from the input text."""
        preferences = {
            "event_type": [],  # e.g., concerts, beach parties, cinema, kid-friendly
            "location": [],    # e.g., Lekki, Victoria Island
        }

        # Match event types based on user input
        if "concert" in input_text.lower() or "afrobeats" in input_text.lower():
            preferences["event_type"].append("concert")
        if "beach" in input_text.lower() or "party" in input_text.lower():
            preferences["event_type"].append("beach party")
        if "kids" in input_text.lower() or "children" in input_text.lower():
            preferences["event_type"].append("kid-friendly")
        if "teens" in input_text.lower():
            preferences["event_type"].append("teen-friendly")
        if "cinema" in input_text.lower():
            preferences["event_type"].append("cinema")
        if "church" in input_text.lower() or "carol" in input_text.lower():
            preferences["event_type"].append("church concert")
        
        # Match locations based on user input
        if "lekki" in input_text.lower():
            preferences["location"].append("Lekki")
        if "victoria island" in input_text.lower() or "vi" in input_text.lower():
            preferences["location"].append("Victoria Island")
        if "oniru" in input_text.lower():
            preferences["location"].append("Oniru")
        if "alausa" in input_text.lower():
            preferences["location"].append("Alausa")
        if "ikeja gra" in input_text.lower() or "ikeja" in input_text.lower():
            preferences["location"].append("Ikeja GRA")
        if "sangotedo" in input_text.lower():
            preferences["location"].append("Sangotedo")
        
        return preferences

    def load_events(self):
        """Loads a predefined list of events that users can choose from."""
        # Sample events with details such as name, type, location, price, and date
        self.events = [
            {"name": "Afrobeats Night with Burna Boy", "type": "concert", "location": "Victoria Island", "price": "20,000 NGN", "date": "Dec 24th"},
            {"name": "Lekki Beach Party", "type": "beach party", "location": "Lekki", "price": "10,000 NGN", "date": "Dec 25th"},
            {"name": "Christmas Wonderland at Landmark Beach", "type": "kid-friendly", "location": "Oniru", "price": "5,000 NGN", "date": "Dec 20th - Dec 26th"},
            {"name": "Teens Hangout at JJT Park", "type": "teen-friendly", "location": "Alausa", "price": "Free", "date": "Dec 22nd"},
            {"name": "Church Christmas Carol", "type": "church concert", "location": "Lekki", "price": "Free", "date": "Dec 24th"},
            {"name": "Kids Funfair at Fun Factory", "type": "kid-friendly", "location": "Lekki", "price": "3,000 NGN", "date": "Dec 18th - Dec 28th"},
            {"name": "Teens Christmas Bash", "type": "teen-friendly", "location": "Victoria Island", "price": "2,000 NGN", "date": "Dec 23rd"},
            {"name": "Family Day Out at Upbeat", "type": "kid-friendly", "location": "Lekki", "price": "7,000 NGN", "date": "Dec 25th"},
            {"name": "Canopy Walk at LCC", "type": "teen-friendly", "location": "Lekki", "price": "2,000 NGN", "date": "Throughout December"},
            {"name": "Bowling at Rufus and Bee", "type": "teen-friendly", "location": "Lekki", "price": "5,000 NGN", "date": "Throughout December"},
            {"name": "Sip and Paint at Just Paint NG", "type": "teen-friendly", "location": "Lekki", "price": "10,000 NGN", "date": "Throughout December"},
            {"name": "Visit Giwa Water Park", "type": "teen-friendly", "location": "Sangotedo", "price": "3,000 NGN", "date": "Throughout December"},
            {"name": "Skating at Skate City", "type": "teen-friendly", "location": "Maryland", "price": "3,000 NGN", "date": "Throughout December"},
            {"name": "Gaming & Arcade at Rufus and Bee", "type": "teen-friendly", "location": "Lekki", "price": "5,000 NGN", "date": "Throughout December"},
            {"name": "Pottery Making at Ceraceni ArtHub", "type": "teen-friendly", "location": "Lekki", "price": "15,000 NGN", "date": "Throughout December"},
            {"name": "Omu Resort (Games, Rides, Swimming, Zoo)", "type": "kid-friendly", "location": "Bogije", "price": "3,000 NGN", "date": "Throughout December"},
            {"name": "Indoor Play Center at Nars Supermarket", "type": "kid-friendly", "location": "VI", "price": "2,500 NGN", "date": "Throughout December"},
            {"name": "Doodles Play Center", "type": "kid-friendly", "location": "Lekki", "price": "3,000 NGN", "date": "Throughout December"},
            {"name": "Fun Factory", "type": "kid-friendly", "location": "Lekki", "price": "3,000 NGN", "date": "Throughout December"},
            {"name": "Hi Impact Planet", "type": "kid-friendly", "location": "Mowe/Ibafo", "price": "10,000 NGN", "date": "Throughout December"},
            {"name": "Cinema Experience: Mufasa: The Lion King", "type": "cinema", "location": "Genesis Cinemas, VI", "price": "5,000 NGN", "date": "Dec 20th - Jan 5th"},
            {"name": "Cinema Experience: Alakada: Bad and Boujee", "type": "cinema", "location": "Filmhouse Cinemas, Lekki", "price": "5,000 NGN", "date": "Dec 20th - Jan 5th"},
            {"name": "Cinema Experience: The Waiter", "type": "cinema", "location": "Silverbird Galleria, VI", "price": "5,000 NGN", "date": "Dec 20th - Jan 5th"},
            {"name": "Cinema Experience: Everybody Loves Jenifa", "type": "cinema", "location": "Genesis Cinemas, VI", "price": "5,000 NGN", "date": "Dec 20th - Jan 5th"},
            {"name": "Cinema Experience: Thin Line", "type": "cinema", "location": "Filmhouse Cinemas, Lekki", "price": "5,000 NGN", "date": "Dec 20th - Jan 5th"}
        ]

    def suggest_events(self, preferences):
        """Suggests events based on user preferences."""
       # Filter events that match the user’s event types and locations
        suggestions = [
            event for event in self.events  # Iterate through the events list
            if (not preferences["event_type"] or event["type"] in preferences["event_type"])
            and (not preferences["location"] or event["location"] in preferences["location"])
        ]
        
        # Return message if no events match the preferences
        if not suggestions:
            return "I couldn't find events matching your preferences. Try being more flexible with your options!"

        # Format and return a list of matching event details
        suggestions_text = "Here are some recommendations for you:\n"
        for event in suggestions:
            suggestions_text += (f"- {event['name']}\n"
                                 f"  Type: {event['type']}\n"
                                 f"  Location: {event['location']}\n"
                                 f"  Price: {event['price']}\n"
                                 f"  Date: {event['date']}\n\n")

        return suggestions_text
    
    def chat(self, user_input):
        """Handles user input and returns a response."""
        preferences = self.collect_preferences(user_input)  # Extract preferences from the user input
        return self.suggest_events(preferences) # Return the suggested events

# Example usage
bot = DettyDecemberBot()
bot.load_events()   # Load the events data for the bot to work with

# Example input to simulate user chat
user_input = "I'm interested in kid-friendly activities in Lekki."

# Get event suggestions based on the user input
print(bot.chat(user_input))
