## Predictions
loginpage() is the main page: 
- will contain a form 
- app will render login.html where the name of the tab will be LOGIN PAGE, heading will be "Welcome, Travelers of the Intertoobz!"
- in the terminal, it will print...

authenticate():
- links the /auth in the front and backend together
- returns Waaaa hooo HAAAh on the page 

## Front-End and Back-End
- Front End: When you submit the form, there will be a form tag of /auth. Back-End: the app.route also have "/auth" This is one of the linkages 

## GET & POST
- Before uncommenting GET & Post: 
127.0.0.1 - - [14/Oct/2022 13:56:38] "GET / HTTP/1.1" 200 -

- After uncommenting GET & POST: 
127.0.0.1 - - [14/Oct/2022 13:57:22] "GET /auth?username=eli30&sub1=Submit HTTP/1.1" 200 

- If you get rid of 'GET' and just leave 'POST' it makes the method not allowed on  
- You can't have methods = []

## Thoughts
- Default method is always GET
- POST cannot work without GET
- POST is possibly arbitrary? 