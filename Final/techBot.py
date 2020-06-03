'''import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random
import json
import pickle

with open("F:\\upload\\uploads\\intent.json") as file:
    data = json.load(file)

try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []
    out_empty = [0 for _ in range(len(labels))]
    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)


    training = numpy.array(training)
    output = numpy.array(output)

    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

tensorflow.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
    model.load('model.tflearn')
except:
    tensorflow.reset_default_graph()

    net = tflearn.input_data(shape=[None, len(training[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(output[0]), activation='softmax')
    net = tflearn.regression(net)

    model = tflearn.DNN(net)

    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")

def bag_of_words(s, words):
        bag = [0 for _ in range(len(words))]

        s_words = nltk.word_tokenize(s)
        s_words = [stemmer.stem(word.lower()) for word in s_words]

        for se in s_words:
            for i, w in enumerate(words):
                if w == se:
                    bag[i] = 1
            
        return numpy.array(bag)

def techChat(inp):
    print("Start talking with the bot (type quit to stop)!")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break''''''
    results = model.predict([bag_of_words(inp, words)])
    results_index = numpy.argmax(results)
    tag = labels[results_index]

    for tg in data["intents"]:
        if tg['tag'] == tag:
             responses = tg['responses']

    return random.choice(responses)

#chat()'''

from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
     [
        r"what is your name ?",
        ["My name is Chatty and I'm a chatbot ?",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    
     [
        r"Clearpass is extended to IT systems using which API?",
        ["REST based API",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"name the authentication/authorization sources used by clearpass",
        ["AD, LDAP, and SQL dB.",]
        
    ],
    [
        r"Which are the authentication protocols used for employee access ?",
        ["PEAP, EAP-FAST, EAP-TLS, EAP-TTLS, and EAP-PEAP-Public",]
        
    ],
    [
        r"(.*) created ?",
        ["HP created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Bangalore, Karnataka',]
    ],
    [
        r"Which  virtualization platforms  is supported by Clearpass?",
        ["VMware vSphere Hypervisor (ESXi), Microsoft Hyper V, and Amazon AWS (EC2)",]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it.",]
    ],
[
        r"Which browsers are supported for ClearPass?",
        ["Mozilla Firefox,Google Chrome,Apple safari,Microsoft Internet Explorer ",]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"Virtual Appliances are supported on which platforms?",
        ["VMware ESX ,ESXi and Microsoft Hyper-V"]
    ],
    [
        r"what are the active Profiling Methods?",
        ["Nmap, WMI, SSH, SNMP"]
     ],
    [
        r"what are the passive Profiling Methods?",
        ["MAC OUI, DHCP, TCP, Netflow v5/v10, IPFIX, sFLOW, ‘SPAN’ Port, HTTP User-Agent, IF-MAP",]
    ],
    [
        r"what are the Integrated and Third-Party Profiling Methods?",
        ["Onboard, OnGuard, ArubaOS, EMM/MDM, Rapid7, Cisco device sensor",]
    ],
    [
        r"Name the ClearPass Hardware Appliance Ports",
        ["Data port,iLO port,Management port,Serial port,USB ports"]
    ],
    [
        r"which versons is supported by VMware vSphere Hypervisor?",
        ["5.5,6.0,6.5 U1"]
     ],
    [
        r"What are the multiple device registration portals?",
        ["Guest, Aruba AirGroup, BYOD (bring your own device)"]
    ],
    [
        r"how does Admin/Operator access security?",
        ["via CAC (Common Access Card) and TLS (Transport Layer Security) certificates",]
    ],
    [
        r"Name the identity stores supported by Clearpass?",
        ["Built-in SQL store,Built-in SQL store, static hosts list"]
    ],
    [
        r"What is the expansion of OCSP?",
        ["Online Certificate Status Protocol",]
   ],
    [
        r"does Clearpass use ipv6 or ipv4 addressing?",
        ["Ipv6"]
    ],
    [
        r"what is ClearPass C1000 Hardware Appliance?",
        ["It is a RADIUS/ TACACS+ server that provides advanced policy control for up to 500 simultaneous sessions."]
    ],
    [
        r"how many sessioons can  be pro5000 simultaneous sessions vided by ClearPass C2000 Hardware Appliance?",
        ["5000 simultaneous sessions"]
    ],
    [
        r"which color indicates Risk Score Colors?",
        ["Blue-Very Low Risk,brown - Low Risk,yellow-Medium Risk,Red-High Risk"]
   ],
    [
        r"Which standard the clearpass Guest is built on?",
        ["AAA framework which consisting on authentication,authorization, and accounting components."]
   ],
    [
        r"which protocol is used by the  NAS  to authenticate the user ?",
        ["RADIUS protocol"]
    ],
    [
        r"Which network connectivity is provisioned for Clearpass Guest?",
        ["VLAN selection, IP address, and hostname"]
    ],
    [
        r"What is the use of airgroup?",
        ["AirGroup allows users to register their personal mobile devices on the local network and define a group of friends or associates who are allowed to share them."]
    ],
    [
        r"What are cookies?",
        ["Cookies are small text files that are placed on a user’s computer by Web sites the user visits."]
    ],
    [
        r"What is NAS?",
        ["Network Access Server used to authenticate and  provide access to the network"]
    ],
    [
        r"What are cookies used for?",
        ["Cookies are used  to make Web sites work, or work more efficiently, as well as to provide information to the owners"]
    ],
     [
        r"What are the possible states of a session?",
        ["Active,stale,closed"]
    ],
     [
        r"what does dynamic authorisation mean?",
        ["Dynamic Authorization describes the ability to make changes to a guest account’s session while it is in progress."]
    ],
     [
        r"what are the built-in AAA services used in aruba",
        ["RADIUS, TACACS+, and Kerberos"]
    ],
     [
        r"what are mobile device posture checks used in aruba",
        ["Network Access Control (NAC), Network Access Protection (NAP) posture and health checks, and Mobile Device Management(MDM)"]
    ],
     [
        r"how is Device and User certificate enrollment done in aruba",
        ["Simple Certificate Enrollment Protocol (SCEP), Enrollment over Secure Transport (EST) and REST API-based workflows"]
    ],
     [
        r"what are the APIs used in aruba",
        ["HTTP/RESTful APIs"]
   ],
     [
        r"what are Framework and Protocol used in aruba",
        ["EAP-FAST,PEAP,EAP-TTLS,EAP-TLS"]
    ],
     [
        r"what are Supported Identity Stores in aruba",
        ["Microsoft Active Directory,Kerberos,Microsoft SQL, PostgreSQL, MariaDB, and Oracle 11g ODBC-compliant SQL server"]
    ],
     [
        r"what are supported browser for aruba",
        ["Apple Safari 9.x,Mobile Safari 5.x,Microsoft Edge"]
    ],
    [
        r"what are the special character that are supported in passwords of aruba",
        ["Plus sign,Comma,Hyphen,Period,Semicolon,Equal sign,Question mark,Underscore"]
    ], 
    [
        r"how is Initial Login and Activation of the ClearPass Platform License done in aruba",
        ["Specifying the ClearPass Platform License Key Upon Initial Login,Logging in to the ClearPass Server,Customizing the Landing Page Layout,"]
    ], 
    [
        r"what is the default password",
        ["eTIPS123"]
     ], 
    [
        r"what are graph that displays all requests",
        [" RADIUS,TACACS+, and WebAuth requests"]
     ],
     [
        r"what are the services that are provided by aruba",
        ["Services Flow and Creation Methods ,Modifying and Managing Services,Using Templates to Create ClearPass Services,Configuring Other Policy Manager Services"]
     ],
     [
        r"what are the options provided by  Posture",
        ["Posture Architecture and Flow,Creating a New Posture Policy,Configuring Audit Servers"]
     ],
     [
        r"what are the elements that can be modified in  Profile and Network Scan page",
        ["Subnet scans,Network scans,SNMP Configuration,SSH Configuration,WMI Configuration"]
     ],
    [
        r"what are the List of Provided Service Templates",
        ["802.1X Wired, 802.1X Wireless, and Aruba 802.1X Wireless Service Template,"]
     ],
    [
        r"how is aruba 802.1X Wired service template designed",
        ["The Aruba 802.1X Wireless template is designed for wireless end-hosts connecting through an Aruba 802.11 wireless access device or controller using IEEE 802.1X authentication"]
     ],
    [
        r"what are the parameter that are used for Authentication Source",
        ["Server,Port,Identity,Password,NetBIOS,Base DN"]
     ],
    [
        r"what are the  attributes defined in the Authentication Source",
        ["Account Expires,Department,Email,Name,Phone, UserDN,Company,member of"]
     ],
    [
        r"how is Wired Network Settings done in aruba",
        ["Select Switch,Device Name,IP Address,Vendor Name,RADIUS Shared Secret"]
     ],
    [
        r"what is Pagination?",
        [" pagination controls to navigate through pages of your results. The count of results displayed and total shows below the page links"]
     ],
    [
        r"what are the type of the filters that are used",
        ["user,host,IP"]
     ],[
        r"what are the Column that are used in database?",
        ["Entity,Department,Risk Score,Change"]
     ],[
        r"what are the actions that are available in Entity360 Data",
        ["Time Range Picker,Search Bar,Filter Options"]
     ],
    [
        r"what are the column that are used in  Contributing Alerts?",
        ["Type,Contribution,Date,Severity,Confidence,Stage"]
     ],
    [
        r"what are the buttons in Entity360 Card",
        ["actions,summary,NAC Timeline,activity,group by,devices,apps & ports,auth. history,conv. graph,web history,comments"]
     ],
    [
        r"what are the Login Details?",
        ["Time,Domain,Host Name,IP Address,MAC Address,Logon Type,Status"]
     ],
    [
        r"what are the attributes in Profile Overviews",
        ["top internal server,bottom internal server,top internal apps,top internet sites,top internal hosts"]
     ],
    [
        r"Is Windows Server 2008 Server Core appropriate for a SQL Server instance?",
        ["The Windows Server 2008 Core edition can:Run the file server role.Run the Hyper-V virtualization server role.Run the Directory Services role.Run the DHCP server role."]
     ],
    [
        r"Is there any list of the network devices supported by clearpass for 802.1x auth",
        [" Clearpass is vendor Neutral, any network device that has 802.1x feature, it should work with clearpass"]
     ],
    [
        r"How can I Block my users from installing new virtual machines",
        ["This depending upon the user level access that you create on the ESX (Assuming you are using VM Ware virutal machines).  you could assign the roles, access for the VM users on the ESX itself and you can authenticate and return the respective roles from Clearpass"]
     ],
    [
        r"what are Good branching and merging tutorials for TortoiseSVN?",
        ["A very good resource for source control in general. Not really TortoiseSVN specific, though"]
     ],
    [
        r"Is there any list of medical devices compatible with clearpass ?",
        ["if the device supports authentication, it would work with clearpass."]
     ],
    [
        r"how to Add scripting functionality to .NET applications",
        ["You could use any of the DLR languages, which provide a way to really easily host your own scripting platform. However, you don't have to use a scripting language for this. You could use C# and compile it with the C# code provider. As long as you load it in its own AppDomain, you can load and unload it to your heart's content."]
     ],
    [
        r"Setting up Continuous Integration with SVN",
        ["CC is quite good in that you can have one CC server monitor another CC server so you could set up stuff like - when a build completes on your build server, your test server would wake up, boot up a virtual machine and deploy your application"]
     ],
    [
        r"Does CruiseControl.NET run on IIS 7.0?",
        ["just use the http://confluence.public.thoughtworks.org/display/CCNET/Welcome+to+CruiseControl.NET rel=nofollow title=Human Interface Guidelines>CruiseControl.NET wiki"]
     ],
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"what are the  three hardware appliance platforms that aruba provides",
        ["ClearPass Policy Manager, C1000 ClearPass Policy Manager C2000, ClearPass Policy Manager C3000"]
    ],
    [
        r"how to Powering Off the ClearPass Hardware Appliance",
        ["Connect to the CLI from the serial console using the serial port.And then Enter the following commands: login: poweroff, password: poweroff"]
    ],
    [
        r"what are the Supported Hypervisors for clearpass",
        ["VMware vSphere Hypervisor (ESXi),Microsoft Hyper-V"]
    ],
    [
        r"what are the Login Details?",
        ["Time,Domain,Host Name,IP Address,MAC Address,Logon Type,Status"]
    ],
    [
        r"what is Viewing Conversations Graph?",
        ["The graph shows only the 1000 most recent conversations, which covers only a small amount of time. For best performance, use search criteria to refine the results. You may also want to keep the date range set to past hour or today, unless you use extensive search criteria."]
    ],
    [
        r"what are Conversations Graph Options",
        ["General Settings,Nodes Tab,Links Tab,Timebar Tab, Properties Tab"]
    ],
    [
        r"what are Classification for  Alert ",
        ["Attack Stage,Alert Category,Alert Type,Alert Name"]
    ],
    [
        r"what is alert360",
        ["Use Alert360 to view, investigate, and take action on an alert.The panels on this page are explained in this section.Different panels appear for discrete versus GUEBA alerts and different alert conditions."]
    ],
    
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    
    
]
def chatty(userText):
    print("Hi, I'm Chatty and I chat alot ;). Type quit to leave ") #default message at the start
    chat = Chat(pairs, reflections)
    userText=userText.lower()
    return chat.respond(userText)
    #chat.converse()

