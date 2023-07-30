import requests
import json
from streamlit.connections import ExperimentalBaseConnection

class SpoonacularConnectionProvider(ExperimentalBaseConnection[requests.Session]):
    """
    A connection class to fetch food data from the  API.

    Attributes:
        connection_name (str): The name of the connection (optional).
    """
    def __init__(self, *args, connection_name=None, **kwargs):
        """
        Initializes the recipeProvidrConnection.

        Args:
            *args: Variable-length argument list.
            connection_name (str, optional): The name of the connection (default is None).
            **kwargs: Keyword arguments.
        """
        super().__init__(*args, connection_name=connection_name, **kwargs)
        self._resource = self._connect()

    def _connect(self) -> requests.Session:
        """
        Creates a new requests session as the underlying resource.

        Returns:
            requests.Session: A new requests session.
        """
        return requests.Session()

    def cursor(self):
        """
        Returns the underlying requests session as the cursor.

        Returns:
            requests.Session: The requests session object.
        """
        return self._resource
    
    def query(self, recipes, ttl: int = 3600):
        """
       Fetches recipes for the specified search query from the Spoonacular API.

        Args:
            query (string): A search query for which recipes are to be fetched.
            

        Returns:
            dict: A dictionary containing recipe data for each query.
                  The structure of the returned dictionary:
                  {
    "results": [
        {
            "id": 654959,
            "title": "Pasta With Tuna",
            "image": "https://spoonacular.com/recipeImages/654959-312x231.jpg",
            "imageType": "jpg"
        },
        ......
        {
            "id": 511728,
            "title": "Pasta Margherita",
            "image": "https://spoonacular.com/recipeImages/511728-312x231.jpg",
            "imageType": "jpg"
        },
       
    ],
    "offset": 0,
    "number": 20,
    "totalResults": 261
}
        """
        def get_recipes_data(query):
            """
            Fetches recipe data for the specified query from the Spoonacular API.
            
            """
            recipes = {}
          
            url = 'https://api.spoonacular.com/recipes/complexSearch'
            params = {
                    'query': query,
                    'apiKey': '154d948da7aa4ecaab36c89c5cdd7522',
                    'number':10,
                    
                    
                    # 'units': 'metric'
                }

            response = self._resource.get(url, params=params)

            if response.status_code == 200:
                    data = response.json()
                    
                    for result in data['results']:
                         recipes[result['title']] = {
                                 "id": result['id'],
                                 "title": result['title'],
                                 "image": result['image'],
                                 "imageType": result['imageType'],
      
            }
            else:
                raise Exception(f"Failed to fetch recipe data for {query}.")

            return recipes
        
        
        
       
        
        
        

        return get_recipes_data(recipes)

        
       