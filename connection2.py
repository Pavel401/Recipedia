import requests
import json
from streamlit.connections import ExperimentalBaseConnection

class SpoonacularMetadataConnectionProvider(ExperimentalBaseConnection[requests.Session]):
    """
    A connection class to fetch food meta data from the  API.

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
    "vegetarian": false,
    "vegan": false,
    "glutenFree": false,
    "dairyFree": false,
    "veryHealthy": false,
    "cheap": false,
    "veryPopular": false,
    "sustainable": false,
    "lowFodmap": false,
    "weightWatcherSmartPoints": 16,
    "gaps": "no",
    "preparationMinutes": -1,
    "cookingMinutes": -1,
    "aggregateLikes": 209,
    "healthScore": 18,
    "creditsText": "Full Belly Sisters",
    "license": "CC BY-SA 3.0",
    "sourceName": "Full Belly Sisters",
    "pricePerServing": 157.06,
    "extendedIngredients": [
        {
            "id": 1001,
            "aisle": "Milk, Eggs, Other Dairy",
            "image": "butter-sliced.jpg",
            "consistency": "SOLID",
            "name": "butter",
            "nameClean": "butter",
            "original": "1 tbsp butter",
            "originalName": "butter",
            "amount": 1.0,
            "unit": "tbsp",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 1.0,
                    "unitShort": "Tbsp",
                    "unitLong": "Tbsp"
                },
                "metric": {
                    "amount": 1.0,
                    "unitShort": "Tbsp",
                    "unitLong": "Tbsp"
                }
            }
        },
        {
            "id": 10011135,
            "aisle": "Produce",
            "image": "cauliflower.jpg",
            "consistency": "SOLID",
            "name": "cauliflower florets",
            "nameClean": "cauliflower florets",
            "original": "about 2 cups frozen cauliflower florets, thawed, cut into bite-sized pieces",
            "originalName": "about frozen cauliflower florets, thawed, cut into bite-sized pieces",
            "amount": 2.0,
            "unit": "cups",
            "meta": [
                "frozen",
                "thawed",
                "cut into bite-sized pieces"
            ],
            "measures": {
                "us": {
                    "amount": 2.0,
                    "unitShort": "cups",
                    "unitLong": "cups"
                },
                "metric": {
                    "amount": 200.0,
                    "unitShort": "g",
                    "unitLong": "grams"
                }
            }
        },
        {
            "id": 1038,
            "aisle": "Cheese",
            "image": "parmesan.jpg",
            "consistency": "SOLID",
            "name": "cheese",
            "nameClean": "pecorino romano",
            "original": "2 tbsp grated cheese (I used romano)",
            "originalName": "grated cheese (I used romano)",
            "amount": 2.0,
            "unit": "tbsp",
            "meta": [
                "grated",
                "(I used romano)"
            ],
            "measures": {
                "us": {
                    "amount": 2.0,
                    "unitShort": "Tbsps",
                    "unitLong": "Tbsps"
                },
                "metric": {
                    "amount": 2.0,
                    "unitShort": "Tbsps",
                    "unitLong": "Tbsps"
                }
            }
        },
        {
            "id": 1034053,
            "aisle": "Oil, Vinegar, Salad Dressing",
            "image": "olive-oil.jpg",
            "consistency": "LIQUID",
            "name": "extra virgin olive oil",
            "nameClean": "extra virgin olive oil",
            "original": "1-2 tbsp extra virgin olive oil",
            "originalName": "extra virgin olive oil",
            "amount": 1.0,
            "unit": "tbsp",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 1.0,
                    "unitShort": "Tbsp",
                    "unitLong": "Tbsp"
                },
                "metric": {
                    "amount": 1.0,
                    "unitShort": "Tbsp",
                    "unitLong": "Tbsp"
                }
            }
        },
        {
            "id": 11215,
            "aisle": "Produce",
            "image": "garlic.png",
            "consistency": "SOLID",
            "name": "garlic",
            "nameClean": "garlic",
            "original": "5-6 cloves garlic",
            "originalName": "garlic",
            "amount": 5.0,
            "unit": "cloves",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 5.0,
                    "unitShort": "cloves",
                    "unitLong": "cloves"
                },
                "metric": {
                    "amount": 5.0,
                    "unitShort": "cloves",
                    "unitLong": "cloves"
                }
            }
        },
        {
            "id": 10720420,
            "aisle": "Pasta and Rice",
            "image": "spaghetti.jpg",
            "consistency": "SOLID",
            "name": "pasta",
            "nameClean": "linguine",
            "original": "6-8 ounces pasta (I used linguine)",
            "originalName": "pasta (I used linguine)",
            "amount": 6.0,
            "unit": "ounces",
            "meta": [
                "(I used linguine)"
            ],
            "measures": {
                "us": {
                    "amount": 6.0,
                    "unitShort": "oz",
                    "unitLong": "ounces"
                },
                "metric": {
                    "amount": 170.097,
                    "unitShort": "g",
                    "unitLong": "grams"
                }
            }
        },
        {
            "id": 1032009,
            "aisle": "Spices and Seasonings",
            "image": "red-pepper-flakes.jpg",
            "consistency": "SOLID",
            "name": "couple of pepper flakes",
            "nameClean": "red pepper flakes",
            "original": "couple of pinches red pepper flakes, optional",
            "originalName": "couple of red pepper flakes, optional",
            "amount": 2.0,
            "unit": "pinches",
            "meta": [
                "red"
            ],
            "measures": {
                "us": {
                    "amount": 2.0,
                    "unitShort": "pinches",
                    "unitLong": "pinches"
                },
                "metric": {
                    "amount": 2.0,
                    "unitShort": "pinches",
                    "unitLong": "pinches"
                }
            }
        },
        {
            "id": 1102047,
            "aisle": "Spices and Seasonings",
            "image": "salt-and-pepper.jpg",
            "consistency": "SOLID",
            "name": "salt and pepper",
            "nameClean": "salt and pepper",
            "original": "salt and pepper, to taste",
            "originalName": "salt and pepper, to taste",
            "amount": 2.0,
            "unit": "servings",
            "meta": [
                "to taste"
            ],
            "measures": {
                "us": {
                    "amount": 2.0,
                    "unitShort": "servings",
                    "unitLong": "servings"
                },
                "metric": {
                    "amount": 2.0,
                    "unitShort": "servings",
                    "unitLong": "servings"
                }
            }
        },
        {
            "id": 11291,
            "aisle": "Produce",
            "image": "spring-onions.jpg",
            "consistency": "SOLID",
            "name": "scallions",
            "nameClean": "spring onions",
            "original": "3 scallions, chopped, white and green parts separated",
            "originalName": "scallions, chopped, white and green parts separated",
            "amount": 3.0,
            "unit": "",
            "meta": [
                "white",
                "green",
                "separated",
                "chopped"
            ],
            "measures": {
                "us": {
                    "amount": 3.0,
                    "unitShort": "",
                    "unitLong": ""
                },
                "metric": {
                    "amount": 3.0,
                    "unitShort": "",
                    "unitLong": ""
                }
            }
        },
        {
            "id": 14106,
            "aisle": "Alcoholic Beverages",
            "image": "white-wine.jpg",
            "consistency": "LIQUID",
            "name": "white wine",
            "nameClean": "dry white wine",
            "original": "2-3 tbsp white wine",
            "originalName": "white wine",
            "amount": 2.0,
            "unit": "tbsp",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 2.0,
                    "unitShort": "Tbsps",
                    "unitLong": "Tbsps"
                },
                "metric": {
                    "amount": 2.0,
                    "unitShort": "Tbsps",
                    "unitLong": "Tbsps"
                }
            }
        },
        {
            "id": 99025,
            "aisle": "Pasta and Rice",
            "image": "breadcrumbs.jpg",
            "consistency": "SOLID",
            "name": "bread crumbs",
            "nameClean": "whole wheat breadcrumbs",
            "original": "1/4 cup whole wheat bread crumbs (I used panko)",
            "originalName": "whole wheat bread crumbs (I used panko)",
            "amount": 0.25,
            "unit": "cup",
            "meta": [
                "whole wheat",
                "(I used panko)"
            ],
            "measures": {
                "us": {
                    "amount": 0.25,
                    "unitShort": "cups",
                    "unitLong": "cups"
                },
                "metric": {
                    "amount": 27.0,
                    "unitShort": "g",
                    "unitLong": "grams"
                }
            }
        }
    ],
    "id": 716429,
    "title": "Pasta with Garlic, Scallions, Cauliflower & Breadcrumbs",
    "readyInMinutes": 45,
    "servings": 2,
    "sourceUrl": "http://fullbellysisters.blogspot.com/2012/06/pasta-with-garlic-scallions-cauliflower.html",
    "image": "https://spoonacular.com/recipeImages/716429-556x370.jpg",
    "imageType": "jpg",
    "summary": "You can never have too many main course recipes, so give Pasta with Garlic, Scallions, Cauliflower & Breadcrumbs a try. One serving contains <b>543 calories</b>, <b>17g of protein</b>, and <b>16g of fat</b>. For <b>$1.57 per serving</b>, this recipe <b>covers 22%</b> of your daily requirements of vitamins and minerals. This recipe serves 2. A mixture of butter, white wine, pasta, and a handful of other ingredients are all it takes to make this recipe so yummy. 209 people have tried and liked this recipe. It is brought to you by fullbellysisters.blogspot.com. From preparation to the plate, this recipe takes approximately <b>45 minutes</b>. Taking all factors into account, this recipe <b>earns a spoonacular score of 83%</b>, which is tremendous. If you like this recipe, take a look at these similar recipes: <a href=\"https://spoonacular.com/recipes/pasta-with-garlic-scallions-cauliflower-breadcrumbs-1230187\">Pasta with Garlic, Scallions, Cauliflower & Breadcrumbs</a>, <a href=\"https://spoonacular.com/recipes/pasta-with-garlic-scallions-cauliflower-breadcrumbs-1229807\">Pasta with Garlic, Scallions, Cauliflower & Breadcrumbs</a>, and <a href=\"https://spoonacular.com/recipes/pasta-with-garlic-scallions-cauliflower-breadcrumbs-1229669\">Pasta with Garlic, Scallions, Cauliflower & Breadcrumbs</a>.",
    "cuisines": [],
    "dishTypes": [
        "side dish",
        "lunch",
        "main course",
        "main dish",
        "dinner"
    ],
    "diets": [],
    "occasions": [],
    "winePairing": {
        "pairedWines": [],
        "pairingText": "No one wine will suit every pasta dish. Pasta in a tomato-based sauce will usually work well with a medium-bodied red, such as a montepulciano or chianti. Pasta with seafood or pesto will fare better with a light-bodied white, such as a pinot grigio. Cheese-heavy pasta can pair well with red or white - you might try a sangiovese wine for hard cheeses and a chardonnay for soft cheeses. We may be able to make a better recommendation if you ask again with a specific pasta dish.",
        "productMatches": []
    },
    "instructions": "",
    "analyzedInstructions": [],
    "originalId": null,
    "spoonacularSourceUrl": "https://spoonacular.com/pasta-with-garlic-scallions-cauliflower-breadcrumbs-716429"
}
       
    ],
    "offset": 0,
    "number": 20,
    "totalResults": 261
}
        """
        def getMetaData(query):
            """
            Fetches recipe data for the specified query from the Spoonacular API.
            
            """
            recipe_data = {}
          
            url = f'https://api.spoonacular.com/recipes/{query}/information'
            params = {
                     'includeNutrition': False,
        'apiKey': '154d948da7aa4ecaab36c89c5cdd7522',
        'id': query,
                }
            print(f"Fetching recipe data for {query}...")
            print(f"URL is {url}")
            print(f"Params are {params}")
            response = self._resource.get(url, params=params)

            if response.status_code == 200:
                    data = response.json()
                    
                    recipe_data = {
            "title": data['title'],
            "pricePerServing": data['pricePerServing'],
            "healthScore": data['healthScore'],
            "instructions": data['instructions'],
            "image": data['image'],
            "sourceUrl": data['sourceUrl'],
            "readyInMinutes": data['readyInMinutes'],
            "glutenFree":data['glutenFree'],
        }
      
            
            else:
                raise Exception(f"Failed to fetch recipe data for {query}.")

            return recipe_data
        
        
        
       
        
        
        

        return getMetaData(recipes)

        
       