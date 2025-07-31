"""
Wikipedia API & Python Library
A program that uses the Wikipedia API to search and display page information
"""

import wikipedia


def search_wikipedia():
    """Search Wikipedia pages based on user input"""
    print("Wikipedia Search Tool")
    print("Enter a page title or search phrase (or blank to quit)")
    print("-" * 50)
    
    while True:
        # Get user input
        search_term = input("\nEnter page title: ").strip()
        
        # Check if user wants to quit
        if not search_term:
            print("Thank you.")
            break
