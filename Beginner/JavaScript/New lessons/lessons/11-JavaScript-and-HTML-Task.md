___
### Task 1: Linking our HTML and JavaScript

In this task you may have noticed we have some starter code this time. There is a simple restaurant website made up of 3 files:
- index.html
- style.css
- script.js

To link the script.js to the index.html open the HTML file and just above the closing body tag `</body>` there is a comment that says "Where to add in Script Tag" and just as the wise mysterious comment suggests this is where we will add the script tag to link the 2 files. So take a new line underneath this comment and add:

```html
<script src="script.js"></script>
```

Once again we are using the script tag but this time, we have added this "src" attribute which stands for source, and we give it the this value "script.js" which is the name of our JavaScript file we want to link.

**Important:** Bear in mind that if your JavaScript file is in a separate folder to your HTML you will need to provide the path to that folder. If you don't know what that means, google it I believe in you!

Congratulations!! you have now just linked the 2 files!!!

___

### Global VS Local Variables

Unfortunately this is not a Royal Rumble between 2 variables, before we get onto the fun programming there is 1 thing we need to cover quickly and that is Global and Local variables.

When we create variables they have what is called scope which is where we can access them from. Global variables can be accessed from anywhere in a program. Whereas local variables only exist within a small scope.

In JavaScript if we make a variable outside of a function just in the file then it is global, typically we define them at the top of the file so they are all in the same place. But if we make a variable inside a function for example then that variable only exists inside that function. Typically we want to use local variables as it allows us to confine where they can be accessed from this promotes:

- Less confusing code
- Reduces the chance of bugs
- Makes fixing bugs easier 

Take a look at the below example:
```js
const globalVar = "this is a global variable"

function myfunction() {
const localVar = "this is a local variable"

}
```

During the next few tasks we will use both but don't worry I will give a few hints as to what needs to be what.

___
### Task 2: Table Counter

In this task we are going to add a table counter so users can check if there are any available tables. To do this we are going to:

1. Create a Variable that stores the total number of tables (*mysterious voice: this will need to be a global variable*)
2. Create a Variable that stores the current number of booked tables (*mysterious voice: this will also need to be a global variable*)
3. Create a Function that checks if there are any free tables
4. Display whether there are available tables or not

I believe you can complete up to step 2 of this on your own but in step 3 and 4 we are going to introduce a new thing, exciting I know. We are going to update the HTML from within the JavaScript. The eagle eye'd of you might have noticed there is an `<h4>` tag with the `id` "availability-counter" has no text in it. This is the element we are going to update to display the number of available tables. The other new thing we are going to learn is calling a function from the HTML file.

#### Calling Function from HTML

To call a function from the HTML file is not complicated at all. First we need to find the thing that is going to call our function. In our case this is simple its a button, specifically the `<button>` directly below the `<h4>` tag we are updating. We need to add the 'onclick' attribute to this button and then name the function we are calling like so:

```html
<button onclick="whatever-your-function-is-called()">Check Availability</button>
```

*Please do not name your function "whatever-your-function-is-called" because that is a truly terrible name for a function.*

If you want to test that your button is linked to your function you can place a console.log inside or an alert() and click the button and see if something happens.
#### Updating Element

To update this element what we need to do first is select it and we are going to do that using the magic of `document.getElementById()`. `document` is a keyword that represents all the elements in the linked HTML file. `.getElementById` is a function that the kind people that made JavaScript provided us with, similar to `console.log` its a function we get out the box. It allows us to search the `document` for a specific element by its `id` which is "availability-counter". So we can use it like the following:

```js
let counterElement = document.getElementById("availability-counter")
```

This sets the variable `counterElement` to represent our `<h4>` element. We can now access the `.innerHTML` property of the `counterElement` this property controls what text is displayed with this element. So if we did something like the following:

```js
counterElement.innerHTML = "Some Changed Text"
```

Would change the element to display "Some Changed Text" - So if we updated this to use a variable instead of hardcoded text... you might be able to complete step 4.

*Also to note there are other ways to select HTML elements other than id such as:*
- ByName
- ByTagName
- ByClassName

___

### Task 3: Book a Table

Now you are going to update the website to allow a user to book a table at the restaurant. To do this we are going to need to:

1. Create new function
2. Collect the information the user has entered
3. Organise the info the user has entered into an object
4. save that object to an array (*mysterious voice: this array will need to be a global variable*)
5. display some notification to the user that their booking has been saved. Could be an Alert or could be some HTML element you update, I shall leave that in your capable hands.

Now there are a couple new things here around objects, arrays and collecting user inputted data. But first lets start small, lets refresh ourselves on what an object and an array are:

- **Arrays**: An array is a **list** of values stored in one variable.
- **Objects**: An object is a way to store a group of related information.

#### Collecting data from an Entry Box

To collect the value entered in an entry box we are going to use our old friend `getElementById`. Below is an example for the first entry box, email the rest are up to you.

Inside your new JavaScript function for this we are going to add:
```js
let email = document.getElementById("email").value
```

Its that simple, everything is working exactly as before when changing the text but instead of using `innerHTML` we are using this `value` property to get the entered text to the entry box. This means the variable email contains whatever the user has entered.

#### Creating Objects

Objects are another data type we haven't used yet. Objects allow us to store multiple related values in one variable. This is perfect in this case as we need to store a user's booking information which is made up of a few different values.

To create an object we do the following:

```js
let booking = { firstName: fname, lastName: lname, email: email, date: date };
```

we create a new variable just as we have many times before but when we set the value we use these curly brackets {} to show it is an object. Within the brackets for each value we give that value a name which comes first. So looking at the first value we have given it the name "firstName" we then follow that with a colon (:) and then the variable with the data we want to store in this case `fname`. We then repeat that for the rest of the values we are storing.

#### Creating and Storing things in an Array

The second new data type we are going to create is an Array, arrays similar to objects allow us to store multiple values but, we cannot give these values names like in objects. To create an array we use square brackets [] like so:

```js
const myArray = []
```

It is that easy! To add values to this array it is just as easy, we use the name of the array in this case `myArray` and use `.push()` with the value we want to add to the array inside the brackets. 

So if we wanted to add the object we created before to this array it would look like:

```js
myArray.push(booking)
```


___

### Task 4: Searching for a Booking:

Now you are going to add the ability for a user to search for their booking, to do this the user is going to enter the email address they used to create the booking and we will search through the Array of bookings we have and search for one that has a matching email address. To do this we will need to:

1. Make a new function
2. Collect the email address the user has entered
3. Search through the Array of booking objects until we find one with the matching email address
4. Display the booking information back to the user

Steps 1, 2 and 4 you should be able to do now but step 3 is doing something we haven't covered yet:

To accomplish step 3 we are going to need to combine a for loop and an if statement. But first we will look at how to access the different elements of an array as we will need to do that to search it.

#### How to access the elements of an Array:

To access the different elements of an array is simple we just use some square brackets [] and put the number of place we want to access between them, like so:

```js
const myArray = ["cat", "dog", "parrot", "cow"]
console.log(myArray[1])

```

Can you guess what this would display???, this would actually display "dog". Confusing I know, an important thing to remember is the first element of an Array is in position 0. So to access the value "cat" we would need to print:

```js
console.log(myArray[0]) //displays "cat"
```

#### How to Search an Array

To search an array we need to combine 2 things we have learnt before, For Loops and If Statements. First we are going to need to use the for loop to loop through each element of the array so we can check if it contains the email we need. To do that we do the following:

```js
for (let i=0; i < myArray.length; i++ ) {
	console.log(myArray[i])
}
```

This is very similar to the other for loops we have seen however, there are a few differences. The first being whatever this `myArray.length` thing is doing? 

`.length` is something we can add to an array that returns how many elements are in the array. This means the for loop will repeat for how elements are in the array. We can then access the array using the variable `i` this means the first time we go through the for loop and `i` will equal 0 when we access the array using `i` that will return the first element. Then when the loop goes round and `i` increases by 1 to equal 1 and we access the array again we will get the second element. This will repeat and we can access every element and stop when we reach the end of the list.

We can improve this by adding an if statement to check if each element is equal to the email address we are searching for like so:

```js
let found = false;

for (let i=0; i < myArray.length; i++ ) {
	if (myArray[i].email == userEmail) {
		console.log(myArray[i])
		found = true;
	}
}

if (!found) {
	console.log("Not Found")
}
```

So lets recap - each time the for loop repeats we are checking another element of the list and using the `.email` access the email attribute of the object and we are checking if that is equal to a variable that stores the email the user entered `userEmail`. If it matches we console.log the object and set `found` to `true` so we remember we matched something. Once the loop has finished checking every element, we then check `found` - if it is still `false` that means we never matched anything, so only then do we print "Not Found". Here you could display the booking details to the user properly, rather than just a console.log.

And with that I bid you farewell, your training is complete young Padawan I have taught you all I can teach and you are ready to tackle any programming task you may come to find.
