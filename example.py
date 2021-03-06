# example predictions
from model_utilities import load_model


#extended examples
def examples_extended(my_model):
    print(my_model.evaluate("current weather in djakarta"))
    print(my_model.evaluate("I will be here until 6"))
    print(my_model.evaluate("I want to travel from miami to lagos"))
    print(my_model.evaluate("I want to leave accra for lagos on tuesday"))
    print(my_model.evaluate("I want to go to accra from lagos on tuesday"))
    print(my_model.evaluate("I want to travel to accra from lagos on tuesday"))
    print(my_model.evaluate("London weather"))
    print(my_model.evaluate("London expected weather"))
    print(my_model.evaluate("what time will the rain start in London"))
    print(my_model.evaluate("Will it rain today in london"))
    print(my_model.evaluate("I would like to know when is the next flight from Miami to Los Angeles"))
    print(my_model.evaluate("I am in Toronto but I want to fly to Bangkok"))
    print(my_model.evaluate("I wanna fly from New York to Toronto"))
    print(my_model.evaluate("Book a flight to Winnipeg from Halifax"))
    print(my_model.evaluate("Book a flight from Halifax to Winnipeg"))
    print(my_model.evaluate("what’s the weather in Paris"))
    print(my_model.evaluate("temperature in San Francisco"))
    print(my_model.evaluate("My friend wants to travel from Westeros to King's Landing"))
    print(my_model.evaluate("Seattle forecast for wednesday"))
    print(my_model.evaluate("What is Seattle forecast for wednesday"))
    print(my_model.evaluate("Current temperature in Westeros"))
    print(my_model.evaluate("Book a flight to Winnipeg from Gotham"))
    print(my_model.evaluate("Give me flights from New York City to Winnipeg"))

#examples from the project documentation
def examples(my_model):
    print(my_model.evaluate("What's the weather like in London?"))
    print(my_model.evaluate("London weather"))
    print(my_model.evaluate("what’s the weather in Paris"))
    print(my_model.evaluate("temperature in San Francisco"))
    print(my_model.evaluate("I wanna fly from New York to Toronto"))



# There are many trained models that were saved on disk, but this is the model with the best performance
gru_nopooling_moredata2 = load_model('gru_nopooling_moredata2')  # best so far

#look at prediction of different models on example queries
best_model = gru_nopooling_moredata2
examples(best_model)
examples_extended(best_model)

#look at summary of best_model
best_model.summary
#look at metrics of best model
best_model.accuracy
best_model.precision
best_model.recall
best_model.f1

#look at parameters of best_model
best_model.name
best_model.rnn_units
best_model.dropout_parameter

#to make a single prediction you just call
best_model.evaluate("it is so hot today")
best_model.evaluate("it is so hot today in singapore")

