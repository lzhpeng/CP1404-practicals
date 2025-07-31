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
        
        try:
            # Try to get the page
            page = wikipedia.page(search_term, autosuggest=False)
            
            # Display page information
            print(f"\n{page.title}")
            print(f"{page.summary}")
            print(f"{page.url}")
            
        except wikipedia.exceptions.DisambiguationError as e:
            # Handle disambiguation pages
            print("We need a more specific title. Try one of the following, or a new search:")
            print(f"{e.options[:10]}...")  # Show first 10 options
            
        except wikipedia.exceptions.PageError:
            # Handle pages not found
            print(f'Page id "{search_term}" does not match any pages. Try another id!')
            
        except wikipedia.exceptions.WikipediaException as e:
            # Handle other Wikipedia API errors
            print(f"Wikipedia API error: {e}")
            
        except Exception as e:
            # Handle any other unexpected errors
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    search_wikipedia() 