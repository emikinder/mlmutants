from flask import Flask, Response, request
from flask_restful import Resource, Api
from database import getStats, postDna
from service import isMutant, isDna
import json

app = Flask(__name__)
api = Api(app)

class Mutant(Resource):
    def post(self):
        # Valida si es JSON
        if not request.is_json:
            return Response(status=400)

        dnaJson = request.get_json()
        dna = dnaJson['dna']
        if not isDna(dna):
            return Response(status=400) #Bad request.

        if isMutant(dna):
            print('Result: Mutant dna.')
            postDna(dna, 1)
            return Response(status=200) #Ok.
        else:
            print('Result: Human dna.')
            postDna(dna, 0)
            return Response(status=403) #Forbidden.

class Stats(Resource):
    def get(self):
        data = getStats()
        return Response(data, status=200)

api.add_resource(Mutant, '/mutant/')
api.add_resource(Stats, '/stats')

if __name__ == '__main__':
     app.run(port='5000')