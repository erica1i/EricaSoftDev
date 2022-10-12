## Flask() is a module.
- "__name__" is a special Python variable with the value of "__main__". 
- Flask is more intended for dynamic content

## WEB SERVERS VS. WEB BROWERS 
- Web Browswers is software that allow the users to broswe the web
    (ie Firefox, Safari, Google)
- Web Servers returns a response. 

In app.py, the code created a web server that serves/opens a page that
says "No hablo queso!" It is a static server at the moment which is why refreshing
the page does not change anything about the actual server itself. 

## Flask Serving Staticly 
- In order for Flask to even serve the html files staticly, app.py must first be run
- static/foo.html serves up text on a new page
- static/foo serves up a download
