---
title: Managing Data with Gaia
description: This series will focus on teaching you to think like a Blockstack developer working with Gaia.
image: /images/tutorials/managing-data-with-gaia.png
---

If you’ve gone through tutorials and documentation for blockstack.js and Gaia, you’ll know the `blockstack.js` interface is dead simple. First, you authenticate a user into your app. Once that’s complete, you’re free to read and write app data in the user’s storage provider with two data operations:


- `putFile`: Writes to a specified path
- `getFile`: Gets the file at a specified path

That’s it. You’re reading files and you’re writing files. All file types are supported, so you can choose to manage data with sql, markdown, json, or even your own custom format! Gaia operations are purposefully left primitive so that you have complete control over which tools you use on top. In the future, we imagine a variety of data management libraries will emerge that wrap Gaia and help you interact with your data layer via expressive APIs.

If you’re anything like most developers, you’re probably used to working with highly abstracted libraries that offer collection management, querying, pagination, documented schema models, and more. Developing apps on Blockstack is thrilling because you quickly learn that you don’t need training wheels. You can create a meaningful and complex data layer using two methods: `putFile` and `getFile`. This limited interface forces you to think about your fundamental data architecture and make some decisions about how you’re modeling data to gain back the benefits you get with large frameworks.

This series will focus on teaching you to think like a Blockstack developer working with Gaia. Let’s get started!


## Working with Data Collections

For the purposes of this tutorial, let’s pretend that we’re building a simple grocery list app called Grublist. As a user of Grublist, you should be able to create, read, update, and delete grocery lists.

Let’s think in terms of JSON since it’s easy and familiar.

### Single-File Collection Approach

Here’s a Single-File Collection approach to modeling our data:

```
// grocerylists.json
{
  "3255": {
    "items": [
      "1 Head of Lettuce",
      "Haralson apples"
    ]
  },
  // ...more lists with items
}
```

Notice that items are stored as an array nested inside of each grocery list.

This is conceptually the simplest way to manage your grocery lists. It’s very easy to wrap your brain around what’s going on with the data. When you read the `/grocerylists.json` file, you get back exactly what you need: grocery lists and their items. When you write, you’re always writing to one place.

There is one caveat to this approach that you should seriously consider: Every time you update one of your grocery lists in any way, you’re overwriting the entire file of all your grocery lists. This is because using the `putFile` method will overwrite anything at `/grocerylists.json` if it exists, so if you’re doing a write operation for a new grocery list, you must submit all previous grocery lists plus the new grocery list.

That’s actually kind of scary, especially considering this code is running on the client where anything can go wrong. Imagine your client-side code encounters a parsing error with a user-input value and you overwrite two years worth of a user’s grocery lists with:


```
"line 6: Parsing Error: Unexpected token ."
```


**To summarize the Single-File Collection approach:**

Pros:

- **Simplified reads**: Just request a single file and get back a list of all your data.
- **Simplified writes**: Some people might be more comfortable working with a Javascript array of items on the client.

Cons:

- **Pagination is impossible**: Using a simple storage strategy like this, you have no choice but to download the entire file of all grocery lists. A user could have 1000 grocery lists, and every time they enter your app they would be forced to download all 1000 grocery lists worth of data.
- **Too heavy-handed**: This is the issue I mentioned above about overwriting an entire file of all grocery lists. Generally, you should try to avoid managing entire collections of data at a time.
- **Less control over file permissions**: You’ll need to perform data acrobatics if you want to share only a single grocery list with a trusted party.


### Multi-File Collection Approach

It would be great if we could split out grocery lists into their own files to minimize the risk of destroying all the user’s grocery list data and make it easier to paginate the lists.

Here’s a diagram of a Multi-File Collection approach:


<img src="/images/tutorials/grocery-lists.png" style="max-width: 80%;" />


With this approach, we maintain an index file that stores an array of list IDs. Each list ID is predictably the name of a file under a `grocerylists` folder.


**To summarize the Multi-File Collection approach:**

Pros:

- **Performant pagination**: Just request the `grocerylists.json` file, and from there you can request as many of the collection items as you need.
- **Less risk of data corruption**: By only manipulating one grocery list at a time, you can guarantee that if something goes wrong with your write operation, it won’t affect the other grocery list data. You might say, “but I still need to overwrite the list of IDs every time I operate.” That’s true, but you can optimize your code so that you’re only updating that file when you add or remove a grocery list. Managing a list of IDs is also much more manageable than a big list of user input data.
- **More control over file permissions**: If you wanted to share only a single grocery list with a trusted party, it’s much easier to do when the list data is isolated to its own file.

Cons

- **More network requests**: If you have 10 grocery lists and want to fetch them all, you’re going to be making 11 network requests. Using HTTP/2 and requesting limited items at a time will help with performance.
- **More complex architecture**: Rather than simply requesting the file of all your data, you now have to request each item individually and stitch them all together once all requests have finished.


### Implementing these approaches

We’ve shown you conceptually how you might think about organizing your data, but you have not seem much implementation code. Check out the sandbox linked below for an implementation of services that can accommodate either the single-file or multi-file approaches for all of your collections.

Note that we’ve included an interstitial “driver” layer for a few reasons:

1. In the sandbox, we’re swapping out the Blockstack driver for a localstorage driver for demonstration purposes.
2. It’s good practice to have all data flow through an interface you control, so that you can add logging or perform other operations.
3. If the `blockstack.js` API changes in the future, you can update your code once in the driver.
4. You can DRY up your code by declaring the Gaia config once per collection.

Click the button below to spin up a sandbox environment:

[![](/images/tutorials/edit-sandbox.png)](https://codesandbox.io/s/8kzmjjr9nj)


## Summary

There are many valid ways to organize your data and you should pick what makes the most sense for your needs. I would recommend using a single-file collection approach for predictably small collections of data. For larger collections, the risk of data corruption is too high to be passing around entire collections worth of data with one `putFile` request, so opt for an architecture that looks more like the multi-file collection model.

Most importantly, feel free to experiment with data architecture. There are concepts and patterns you can introduce into this process that can help you validate schema, migrate data, and more. Check out more of our tutorials for a deeper dive into developing a sample app.
