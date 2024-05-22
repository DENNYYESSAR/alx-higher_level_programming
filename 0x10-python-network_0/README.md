Python - Network #0

I covered this
What a URL is
What HTTP is
How to read a URL
The scheme for a HTTP URL
What a domain name is
What a sub-domain is
How to define a port number in a URL
What a query string is
What an HTTP request is
What an HTTP response is
What HTTP headers are
What the HTTP message body is
What an HTTP request method is
What an HTTP response status code is
What an HTTP Cookie is
How to make a request with cURL

Tasks
0. Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

The size must be displayed in bytes
You have to use curl

1. Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response

Display only body of a 200 status code response
You have to use curl

2. Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

You have to use curl

3. Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

4. Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response

A header variable X-School-User-Id must be sent with the value 98

5. Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response

A variable email must be sent with the value test@gmail.com
A variable subject must be sent with the value I will always be here for PLD

6. Write a function that finds a peak in a list of unsorted integers.

Prototype: def find_peak(list_of_integers):
You are not allowed to import any module
Your algorithm must have the lowest complexity (hint: you don’t need to go through all numbers to find a peak)
6-peak.py must contain the function
6-peak.txt must contain the complexity of your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2)

7. Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.

You are not allowed to use any pipe, redirection, etc.
You are not allowed to use ; and &&

8. Write a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.

Your script must send a POST request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request

9. Write a Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.

You have to use curl
You are not allow to use echo, cat, etc. to display the final result

