### **Documentation of ChatBot Built Using ChatterBot Library**

**Method :** ChatBot()<br/>
**Parameters** : The user name for chatbot<br/>
**Returns** : The instance of ChatBot classes for further traning of
data<br/>

**Method :** ListTrainer()<br/>
**Parameters** : The instance of ChatBot<br/>
**Training** : ChatterBot comes with training classes built in, or you
can create your own if needed. To use a training class we call 
*train()* on an instance that has been initialized with chat bot.<br/>
**Returns** : The instance of train class which is further used for
training the questions for chatbot<br/>

**Method** : train()<br/>
**Parameters** : the  list of Questions along with answer<br/>
**Returns** : None<br/>

**Method** : get_response()<br/>
**Parameters** : input question from the user<br/>
**Returns** : the response from the in-built train function of
ListTrainer class for user query<br/>
