# Web Proxy Server

Note that this extracredit assignment is an addition to the TCP Client-Server project. This part of the assignment is optional. Students who implement this option will need to modify the main manu of their TCP Client-Server project. The new menu should look like the following one: 

```
****** TCP Client-Server Network ******
-----------------------
Options Available:
1. Get user list
2. Sent a message
3. Get my messages
4. Create a new chat room
5. Join an existing chat room
6. Turn web proxy server on
7. Disconnect from server
```

## Getting Started with the proxy server option (option 6 in the menu)

When users select this option, the server will turn on the web server proxy services and will show the following additional menu to the user. 

```
*** Proxy Server Settings *** 
1. Turn web caching On
2. Turn authentication On
3. Turn private browsing Off
4. Send a request (GET, HEAD OR POST): 
5. Turn web proxy server off

```

### Option 1: Turn web caching On. 
  
Once this option is selected, the user should be informed that the web caching option is on. Note how the next time the 
menu is loaded when this option is active, the option has changed to "turn web caching Off". 
  
```
Your option <enter a number>: 1
Web caching is on

*** Proxy Server Settings *** 
1. Turn web caching Off
2. Turn authentication On
3. Turn private browsing Off
4. Send a request (GET, HEAD OR POST): 
5. Turn web proxy server off
```
Once the web caching system is active in the proxy server, all the GET requests done in option 4, need to be cached. Every time we send a request to a original server (i.e google), the proxy should check, first, if that resource already exist in the cache folder. Otherwise, the resource needs to be cached. The cache files contain the response from the original server (headers and body). The name of the files should be a hashed identifier with extension .pickle The following are examples of files cached by the proxy server. 

```
53d9b3a0-4c87-11ea-9d7f-784f4387efce.pickle
d54442c6-4c86-11ea-9d7f-784f4387efce.pickle
```
You should keep track in memory of the identifier of each file, last_modified_date, and the domain (server site). The next time the proxy server requests a resource that already exist in the cache. It should hand to the user the version cached. 

### Option 2: Turn authentication On.

Similar to option 1, when option 2 is turned on, the next time the proxy server menu is loaded, it should look like the following menu:

```
Your option <enter a number>: 2
Web authentication is on

*** Proxy Server Settings *** 
1. Turn web caching Off
2. Turn authentication Off
3. Turn private browsing Off
4. Send a request (GET, HEAD OR POST): 
5. Turn web proxy server off
```

Note how option 2 now says "Turn authentication Off"

When activated, this option should implement authentication services. There are sites that ask you to provide your credentials (if already registered in the site) in order to access some of their resources or to simply login into the site. After making a request, this option should ask first for username and password. See option 4 of this document to see examples about authentifications using requests.

### Option 3: Turn private browsing Off.

By default, this option needs to be turned On automatically when the proxy server is activated for the first time. This option allow clients to mask the IP address of the machine performing the request to the original server. For instance, let's assume that a client has IP address 180.4.4.23, and the proxy server running in a different machine has IP address 167.7.9.87. So, if private browsing is active, and the client make a request to www.google.com, from the eyes of google the request is comming from IP address 167.7.9.87. However, the request is really comming from 180.4.4.23. Thus, the proxy server is hidding your IP address from the original server. This is usefull when browsing in private mode is required, or your IP has been blocked to access certain resources in a site. 

### Option 4: Send a request (GET, HEAD OR POST): 

This option allows a client to create GET, HEAD and POST requests. 

* GET requests 

GET requests are done by a client in order to get complete responses from original servers that are filtered by a proxy server. Additional data requested is appended to the URL part of the header. For instance, a request to www.example.com attaching name="Jose" and lastname="Ortiz" will be send in the request header as www.example.com?name=Jose&lastname=Ortiz 

* HEAD requests

HEAD requests are different from GET requests. When a HEAD request is performed, the original server will send only the headers of the response (not the actual data such as HTML of a file). This is usefull when you need to check if the last-modified-date header of your resource cached is outdated and the original server has a newer version of the file you have in cache from that server. 

* POST requests

POST requests are done to add some sense of security to the data sent in the request. Normally, POST requests are done when you need to submit forms or any other resource that needs to be transmitted to the server in the body of the requests. 

Examples for option 4 

GET request with authentification off.

```
*** Proxy Server Settings *** 
1. Turn web caching On
2. Turn authentication On
3. Turn private browsing Off
4. Send a request (GET, HEAD OR POST): 
5. Turn web proxy server off


Your option <enter a number>: 4
request> GET https://api.github.com/user
Source IP address: 127.0.0.1
401 Unauthorized. Activate authentication in your proxy server and try again.
```

GET request with authentification on.

```
Your option <enter a number>: 2
Web authentication is on

*** Proxy Server Settings *** 
1. Turn web caching On
2. Turn authentication Off
3. Turn private browsing Off
4. Send a request (GET, HEAD OR POST): 
5. Turn web proxy server off


Your option <enter a number>: 4
request> GET https://api.github.com/user
Source IP address: 127.0.0.1
Username: joseortizcostadev@gmail.com
Password: 
Success 200 OK
{"login":"joseortizcostadev","id":11967132,"node_id":"MDQ6VXNlcjExOTY3MTMy","avatar_url":"https://avatars0.githubusercontent.com/u/11967132?v=4","gravatar_id":"","url":"https://api.github.com/users/joseortizcostadev","html_url":"https://github.com/joseortizcostadev","followers_url":"https://api.github.com/users/joseortizcostadev/followers","following_url":"https://api.github.com/users/joseortizcostadev/following{/other_user}","gists_url":"https://api.github.com/users/joseortizcostadev/gists{/gist_id}","starred_url":"https://api.github.com/users/joseortizcostadev/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/joseortizcostadev/subscriptions","organizations_url":"https://api.github.com/users/joseortizcostadev/orgs","repos_url":"https://api.github.com/users/joseortizcostadev/repos","events_url":"https://api.github.com/users/joseortizcostadev/events{/privacy}","received_events_url":"https://api.github.com/users/joseortizcostadev/received_events","type":"User","site_admin":false,"name":"Jose Ortiz Costa","company":null,"blog":"http://joseortizcosta.me","location":"San Francisco","email":"jose@jortizsd.com","hireable":true,"bio":"Software Engineer and Computer Science Instructor at SFSU\r\n","public_repos":12,"public_gists":8,"followers":4,"following":3,"created_at":"2015-04-15T19:05:38Z","updated_at":"2020-02-19T22:39:12Z","private_gists":10,"total_private_repos":0,"owned_private_repos":0,"disk_usage":36322,"collaborators":0,"two_factor_authentication":false,"plan":{"name":"pro","space":976562499,"collaborators":0,"private_repos":9999}}
```





HEAD requests will create a request similar to the  in the GET re







  
