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

### Examples for option 4. Note that in all the following examples, private web browsing was turned on automatically, so the source IP you see is not the client IP address (127.0.0.1), it is the proxy IP address running in a different machine. 

GET request with authentification off trying to create a request to a resource that needs authorization.

```
*** Proxy Server Settings *** 
1. Turn web caching On
2. Turn authentication On
3. Turn private browsing Off
4. Send a request (GET, HEAD OR POST): 
5. Turn web proxy server off


Your option <enter a number>: 4
request> GET https://api.github.com/user
Source IP address: 180.8.8.21
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
Source IP address: 180.8.8.21
Username: joseortizcostadev@gmail.com
Password: 
Success 200 OK
{"login":"joseortizcostadev","id":11967132,"node_id":"....","avatar_url":"https://avatars0.githubusercontent.com/u/11967132?....}
```

GET request with authentification turned off, and web cache turned on. Since it is the first time we access to the resource, it will cach the info in the cache but will show the entire response in screen. 

```
Your option <enter a number>: 1
Web caching is on

*** Proxy Server Settings *** 
1. Turn web caching Off
2. Turn authentication On
3. Turn private browsing Off
4. Send a request (GET, HEAD OR POST): 
5. Turn web proxy server off


Your option <enter a number>: 4
request> GET https://example.com
Source IP address: 180.8.8.21
Success 200 OK
<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
        
    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>    
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>

```

GET request to the same resource as the one above. However, the resource this time is cached. In addition, we turned off private browsing and now it shows the real source IP address. (the one from the client)

```
Your option <enter a number>: 3
Private browsing is off

*** Proxy Server Settings *** 
1. Turn web caching Off
2. Turn authentication On
3. Turn private browsing On
4. Send a request (GET, HEAD OR POST): 
5. Turn web proxy server off


Your option <enter a number>: 4
request> GET https://example.com
Source IP address: 127.0.0.1
Success 200 OK (cache)
```

HEAD request example. Note that web caching only works for GET and POST requests.

```
Your option <enter a number>: 4                       
request> HEAD https://example.com
Source IP address: 127.0.0.1
Success! 200 OK
{'Content-Encoding': 'gzip', 'Accept-Ranges': 'bytes', 'Age': '558039', 'Cache-Control': 'max-age=604800', 'Content-Type': 'text/html; charset=UTF-8', 'Date': 'Wed, 19 Feb 2020 23:07:05 GMT', 'Etag': '"3147526947+gzip"', 'Expires': 'Wed, 26 Feb 2020 23:07:05 GMT', 'Last-Modified': 'Thu, 17 Oct 2019 07:18:26 GMT', 'Server': 'ECS (sjc/4E5D)', 'X-Cache': 'HIT', 'Content-Length': '648'}

```

POST request example with name and lastname. You can see in the response how those values are enblemmed into the body of the response.  

```
Your option <enter a number>: 4
request> POST http://httpbin.org/post
Source IP address: 127.0.0.1
POST keys separated by comma: name,lastname
POST values separated by a comma: Jose,Ortiz
Success 200 OK
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "lastname": "Ortiz", 
    "name": "Jose"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "24", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.22.0", 
    "X-Amzn-Trace-Id": "Root=1-5e4dc024-6acb6e343143004027059d22"
  }, 
  "json": null, 
  "origin": "73.92.230.115", 
  "url": "http://httpbin.org/post"
}

```

You also need to take into consideration failing requests, and inform the user with the appropiate message. For example, a HEAD request to google will fail with code status 301 (Moved permanently)

```
Your option <enter a number>: 4
request> HEAD https://google.com
Source IP address: 127.0.0.1
Note: authentication does not work with HEAD request
Request failed with status code 301
```

However, a basic GET request to google will work

```
Your option <enter a number>: 4
request> GET https://google.com
Source IP address: 127.0.0.1
Success 200 OK
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en"><head><meta content="Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking for." name="description"><meta content="noodp" name="robots"><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="ffHmu/8Tzx0uNQvmezayDg==">(function(){window.google={kEI:'b8FNXr2FGMHk-gS4xZjQCg',kEXPI:'0,1353746,5663,731,223,5105,206,2954,250,10,1051,175,364,925,510,4,60,690,52,75,383,876,504,225,7,15,60,219,415288,712177,680,1197113,231,125,44,329074,1294,12383,4855,32691,15248,867,6056,22628,369,8819,8384,4859,1361,4325,4965,3024,4744,3118,7910,1,1812,1976,2044,5766,1,3142,5297,2974,873,38,1179,2975,2785,3645,1142,6290,3254,620,2883,21,318,234,1746,1192,1344,2780,517,401,2276,8,570,2226,814,779,1279,390,652,1170,202,37,291,149,1103,840,517,1466,8,49,819,3438,109,151,52,1135,1,3,2669,1839,184,1920,377,686,1261,244,503,283,1,145,44,1009,93,328,1284,16,84,417,2426,1425,821,474,1339,29,719,1039,15,3212,2845,7,438,379,503,951,3328,780,1184,70,6513,1831,832,169,899,2023,2458,1226,1462,280,420,3235,1274,108,1246,1680,481,908,2,433,1040,322,1760,2397,1953,3111,355,225,402,594,830,1,839,185,2,293,548,877,98,258,723,186,814,58,125,278,110,40,165,89,1,1668,218,242,128,1660,1,707,148,543,1237,418,414,415,474,98,3,91,299,12,1,740,41,329,1,743,18,2,52,59,28,130,1,21,49,72,14,467,127,18,98,134,62,678,353,166,42,1075,274,898,143,1136,297,66,417,443,5845084,1872,1804021,4194968,2801054,549,333,444,1,2,80,1,900,896,1,8,1,2,2551,1,748,141,59,736,563,1,4265,1,1,1,1,137,1,879,9,305,239,402,5,96,3,1,3364996,17378642,3220020,23',kBL:'lyiv'};google.sn='webhp';google.kHL='en';})();(function(){google.lc=[];google.li=0;google.getEI=function(a){for(var b;a&&(!a.getAttribute||!(b=a.getAttribute("eid")));)a=a.parentNode;return b||google.kEI};google.getLEI=function(a){for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute("leid")));)a=a.parentNode;return b};google.ml=function(){return null};google.time=function(){return Date.now()};google.log=function(a,b,e,c,g){if(a=google.logUrl(a,b,e,c,g)){b=new Image;var d=google.lc,f=google.li;d[f]=b;b.onerror=b.onload=b.onabort=function(){delete d[f]};google.vel&&google.vel.lu&&google.vel.lu(a);b.src=a;google.li=f+1}};google.logUrl=function(a,b,e,c,g){var d="",f=google.ls||"";e||-1!=b.search("&ei=")||(d="&ei="+google.getEI(c),-1==b.search("&lei=")&&(c=google.getLEI(c))&&(d+="&lei="+c));c="";!e&&google.cshid&&-1==b.search("&cshid=")&&"slh"!=a&&(c="&cshid="+google.cshid);a=e||"/"+(g||"gen_204")+"?atyp=i&ct="+a+"&cad="+b+d+f+"&zx="+google.time()+c;/^http:/i.test(a)&&"https:"==window.location.protocol&&(google.ml(Error("a"),!1,{src:a,glmm:1}),a="");return a};}).call(this);(function(){google.y={};google.x=function(a,b){if(a)var c=a.id;else{do c=Math.random();while(google.y[c])}google.y[c]=[a,b];return!1};google.lm=[];google.plm=function(a){google.lm.push.apply(google.lm,a)};google.lq=[];google.load=function(a,b,c){google.lq.push([[a],b,c])};google.loadAll=function(a,b){google.lq.push([a,b])};}).call(this);google.f={};(function(){
document.documentElement.addEventListener("submit",function(b){var a;if(a=b.target){var c=a.getAttribute("data-submitfalse");a="1"==c||"q"==c&&!a.elements.q.value?!0:!1}else a=!1;a&&(b.preventDefault(),b.stopPropagation())},!0);document.documentElement.addEventListener("click",function(b){var a;a:{for(a=b.target;a&&a!=document.documentElement;a=a.parentElement)if("A"==a.tagName){a="1"==a.getAttribute("data-nohref");break a}a=!1}a&&b.preventDefault()},!0);}).call(this);
var a=window.location,b=a.href.indexOf("#");if(0<=b){var c=a.href.substring(b+1);/(^|&)q=/.test(c)&&-1==c.indexOf("#")&&a.replace("/search?"+c.replace(/(^|&)fp=[^&]*/g,"")+"&cad=h")};</script><style>#gbar,#guser{font-size:13px;padding-top:1px !important;}#gbar{height:22px}#guser{padding-bottom:7px !important;text-align:right}.gbh,.gbd{border-top:1px solid #c9d7f1;font-size:1px}.gbh{height:0;position:absolute;top:24px;width:100%}@media all{.gb1{height:22px;margin-right:.5em;vertical-align:top}#gbar{float:left}}a.gb1,a.gb4{text-decoration:underline !important}a.gb1,a.gb4{color:#00c !important}.gbi .gb4{color:#dd8e27 !important}.gbf .gb4{color:#900 !important}
</style><style>body,td,a,p,.h{font-family:arial,sans-serif}body{margin:0;overflow-y:scroll}#gog{padding:3px 8px 0}td{line-height:.8em}.gac_m td{line-height:17px}form{margin-bottom:20px}.h{color:#36c}.q{color:#00c}.ts td{padding:0}.ts{border-collapse:collapse}em{font-weight:bold;font-style:normal}.lst{height:25px;width:496px}.gsfi,.lst{font:18px arial,sans-serif}.gsfs{font:17px arial,sans-serif}.ds{display:inline-box;display:inline-block;margin:3px 0 4px;margin-left:4px}input{font-family:inherit}body{background:#fff;color:#000}a{color:#11c;text-decoration:none}a:hover,a:active{text-decoration:underline}.fl a{color:#36c}a:visited{color:#551a8b}.sblc{padding-top:5px}.sblc a{display:block;margin:2px 0;margin-left:13px;font-size:11px}.lsbb{background:#eee;border:solid 1px;border-color:#ccc #999 #999 #ccc;height:30px}.lsbb{display:block}.ftl,#fll a{display:inline-block;margin:0 12px}.lsb{background:url(/images/nav_logo229.png) 0 -261px repeat-x;border:none;color:#000;cursor:pointer;height:30px;margin:0;outline:0;font:15px arial,sans-serif;vertical-align:top}.lsb:active{background:#ccc}.lst:focus{outline:none}</style><script nonce="ffHmu/8Tzx0uNQvmezayDg=="></script></head><body bgcolor="#fff"><script nonce="ffHmu/8Tzx0uNQvmezayDg==">(function(){var src='/images/nav_logo229.png';var iesg=false;document.body.onload = function(){window.n && window.n();if (document.images){new Image().src=src;}
if (!iesg){document.f&&document.f.q.focus();document.gbqf&&document.gbqf.q.focus();}
}
})();</script><div id="mngb"> <div id=gbar><nobr><b class=gb1>Search</b> <a class=gb1 href="https://www.google.com/imghp?hl=en&tab=wi">Images</a> <a class=gb1 href="https://maps.google.com/maps?hl=en&tab=wl">Maps</a> <a class=gb1 href="https://play.google.com/?hl=en&tab=w8">Play</a> <a class=gb1 href="https://www.youtube.com/?gl=US&tab=w1">YouTube</a> <a class=gb1 href="https://news.google.com/nwshp?hl=en&tab=wn">News</a> <a class=gb1 href="https://mail.google.com/mail/?tab=wm">Gmail</a> <a class=gb1 href="https://drive.google.com/?tab=wo">Drive</a> <a class=gb1 style="text-decoration:none" href="https://www.google.com/intl/en/about/products?tab=wh"><u>More</u> &raquo;</a></nobr></div><div id=guser width=100%><nobr><span id=gbn class=gbi></span><span id=gbf class=gbf></span><span id=gbe></span><a href="http://www.google.com/history/optout?hl=en" class=gb4>Web History</a> | <a  href="/preferences?hl=en" class=gb4>Settings</a> | <a target=_top id=gb_70 href="https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/" class=gb4>Sign in</a></nobr></div><div class=gbh style=left:0></div><div class=gbh style=right:0></div> </div><center><br clear="all" id="lgpd"><div id="lga"><img alt="Google" height="92" src="/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png" style="padding:28px 0 14px" width="272" id="hplogo"><br><br></div><form action="/search" name="f"><table cellpadding="0" cellspacing="0"><tr valign="top"><td width="25%">&nbsp;</td><td align="center" nowrap=""><input name="ie" value="ISO-8859-1" type="hidden"><input value="en" name="hl" type="hidden"><input name="source" type="hidden" value="hp"><input name="biw" type="hidden"><input name="bih" type="hidden"><div class="ds" style="height:32px;margin:4px 0"><input class="lst" style="color:#000;margin:0;padding:5px 8px 0 6px;vertical-align:top" autocomplete="off" value="" title="Google Search" maxlength="2048" name="q" size="57"></div><br style="line-height:0"><span class="ds"><span class="lsbb"><input class="lsb" value="Google Search" name="btnG" type="submit"></span></span><span class="ds"><span class="lsbb"><input class="lsb" id="tsuid1" value="I'm Feeling Lucky" name="btnI" type="submit"><script nonce="ffHmu/8Tzx0uNQvmezayDg==">(function(){var id='tsuid1';document.getElementById(id).onclick = function(){if (this.form.q.value){this.checked = 1;if (this.form.iflsig)this.form.iflsig.disabled = false;}
else top.location='/doodles/';};})();</script><input value="AINFCbYAAAAAXk3Pf_KSUy6JTEhsacDOHEoQmaACNS-5" name="iflsig" type="hidden"></span></span></td><td class="fl sblc" align="left" nowrap="" width="25%"><a href="/advanced_search?hl=en&amp;authuser=0">Advanced search</a></td></tr></table><input id="gbv" name="gbv" type="hidden" value="1"><script nonce="ffHmu/8Tzx0uNQvmezayDg==">(function(){var a,b="1";if(document&&document.getElementById)if("undefined"!=typeof XMLHttpRequest)b="2";else if("undefined"!=typeof ActiveXObject){var c,d,e=["MSXML2.XMLHTTP.6.0","MSXML2.XMLHTTP.3.0","MSXML2.XMLHTTP","Microsoft.XMLHTTP"];for(c=0;d=e[c++];)try{new ActiveXObject(d),b="2"}catch(h){}}a=b;if("2"==a&&-1==location.search.indexOf("&gbv=2")){var f=google.gbvu,g=document.getElementById("gbv");g&&(g.value=a);f&&window.setTimeout(function(){location.href=f},0)};}).call(this);</script></form><div id="gac_scont"></div><div style="font-size:83%;min-height:3.5em"><br></div><span id="footer"><div style="font-size:10pt"><div style="margin:19px auto;text-align:center" id="fll"><a href="/intl/en/ads/">Advertising Programs</a><a href="/services/">Business Solutions</a><a href="/intl/en/about.html">About Google</a></div></div><p style="color:#767676;font-size:8pt">&copy; 2020 - <a href="/intl/en/policies/privacy/">Privacy</a> - <a href="/intl/en/policies/terms/">Terms</a></p></span></center><script nonce="ffHmu/8Tzx0uNQvmezayDg==">(function(){window.google.cdo={height:0,width:0};(function(){var a=window.innerWidth,b=window.innerHeight;if(!a||!b){var c=window.document,d="CSS1Compat"==c.compatMode?c.documentElement:c.body;a=d.clientWidth;b=d.clientHeight}a&&b&&(a!=google.cdo.width||b!=google.cdo.height)&&google.log("","","/client_204?&atyp=i&biw="+a+"&bih="+b+"&ei="+google.kEI);}).call(this);})();(function(){var u='/xjs/_/js/k\x3dxjs.hp.en_US.wv6Biy5pB4Y.O/m\x3dsb_he,d/am\x3dgAEBNgI/d\x3d1/rs\x3dACT90oGn6BLi3_K49plSlp17NnHesX7UkQ';
setTimeout(function(){var b=document;var a="SCRIPT";"application/xhtml+xml"===b.contentType&&(a=a.toLowerCase());a=b.createElement(a);a.src=u;google.timers&&google.timers.load&&google.tick&&google.tick("load","xjsls");document.body.appendChild(a)},0);})();(function(){window.google.xjsu='/xjs/_/js/k\x3dxjs.hp.en_US.wv6Biy5pB4Y.O/m\x3dsb_he,d/am\x3dgAEBNgI/d\x3d1/rs\x3dACT90oGn6BLi3_K49plSlp17NnHesX7UkQ';})();function _DumpException(e){throw e;}
function _F_installCss(c){}
(function(){google.spjs=false;google.snet=true;google.em=[];google.emw=false;google.pdt=0;})();(function(){var pmc='{\x22d\x22:{},\x22sb_he\x22:{\x22agen\x22:true,\x22cgen\x22:true,\x22client\x22:\x22heirloom-hp\x22,\x22dh\x22:true,\x22dhqt\x22:true,\x22ds\x22:\x22\x22,\x22ffql\x22:\x22en\x22,\x22fl\x22:true,\x22host\x22:\x22google.com\x22,\x22isbh\x22:28,\x22jsonp\x22:true,\x22msgs\x22:{\x22cibl\x22:\x22Clear Search\x22,\x22dym\x22:\x22Did you mean:\x22,\x22lcky\x22:\x22I\\u0026#39;m Feeling Lucky\x22,\x22lml\x22:\x22Learn more\x22,\x22oskt\x22:\x22Input tools\x22,\x22psrc\x22:\x22This search was removed from your \\u003Ca href\x3d\\\x22/history\\\x22\\u003EWeb History\\u003C/a\\u003E\x22,\x22psrl\x22:\x22Remove\x22,\x22sbit\x22:\x22Search by image\x22,\x22srch\x22:\x22Google Search\x22},\x22ovr\x22:{},\x22pq\x22:\x22\x22,\x22refpd\x22:true,\x22rfs\x22:[],\x22sbpl\x22:16,\x22sbpr\x22:16,\x22scd\x22:10,\x22stok\x22:\x22jdx57DidmDsKEbU17xIzr-SJe_U\x22,\x22uhde\x22:false}}';google.pmc=JSON.parse(pmc);})();</script>        </body></html>

```






  
