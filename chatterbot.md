### **Documentation of ChatBot Built Using ChatterBot Library**

**Method :** ChatBot()
**Parameters** : The user name for chatbot
**Returns** : The instance of ChatBot classes for further traning of
data

**Method :** ListTrainer()
**Parameters** : The instance of ChatBot
**Training** : ChatterBot comes with training classes built in, or you
can create your own if needed. To use a training class we call 
*train()* on an instance that has been initialized with chat bot.
**Returns** : The instance of train class which is further used for
training the questions for chatbot

**Method** : train()
**Parameters** : the  list of Questions along with answer
**Returns** : None

**Method** : get_response()
**Parameters** : input question from the user
**Returns** : the response from the in-built train function of
ListTrainer class for user query
