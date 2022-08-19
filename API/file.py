from flask import Flask
from flask_restful import Api, Resource, reqparse
from resource import ai_quotes
import random

app = Flask(__name__)




class Quote(Resource):
# The GET method returns a random quote if id contains a
#  default value (that is, id was not specified when the 
# method was called).
    
    
    def get(self, id=0):
        if id ==0:
            return random.choice(ai_quotes),200

        for quote in ai_quotes:
            if(quote["id"] == id):
                return quote, 200
        return "Quote not found", 404



# POST method to add a new quote to the repository.
    def post(self, id):
      parser = reqparse.RequestParser()
      parser.add_argument("author")
      parser.add_argument("quote")
      params = parser.parse_args()

      for quote in ai_quotes:
          if(id == quote["id"]):
              return f"Quote with id {id} already exists", 400

      quote = {
          "id": int(id),
          "author": params["author"],
          "quote": params["quote"]
      }

      ai_quotes.append(quote)
      return quote, 201




#  PUT method to modify the contents of an existing quote 
# in the repository:
    def put(self, id):
      parser = reqparse.RequestParser()
      parser.add_argument("author")
      parser.add_argument("quote")
      params = parser.parse_args()

      for quote in ai_quotes:
          if(id == quote["id"]):
              quote["author"] = params["author"]
              quote["quote"] = params["quote"]
              return quote, 200
      
      quote = {
          "id": id,
          "author": params["author"],
          "quote": params["quote"]
      }
      
      ai_quotes.append(quote)
      return quote, 201



# a DELETE method to remove a quote that no longer 
#  seems inspirational to us:
    def delete(self, id):
      global ai_quotes
      ai_quotes = [qoute for qoute in ai_quotes if qoute["id"] != id]
      return f"Quote with id {id} is deleted.", 200






api.add_resource(Quote, "/ai-quotes", "/ai-quotes/", "/ai-quotes/<int:id>")

if __name__ == '__main__':
    app.run(debug=True)


