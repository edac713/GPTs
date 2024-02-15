Creating a shortcut that converts webpages to markdown can be intricate. Let's break it down into a detailed, step-by-step guide that you can follow and understand even with a basic knowledge of Shortcuts and Python.

### Step-by-Step Guide to Build a Webpage to Markdown Shortcut

#### Step 1: Prepare Your Shortcut
- **Open the Shortcuts app** on your iPhone.
- **Create a new shortcut** by tapping the "+" button.

#### Step 2: Add Safari Webpage Content Action
- Add the **"Get Details of Safari Webpage"** action.
- Choose the **"Page Contents"** detail. This will grab the HTML content of the webpage you are viewing in Safari.

#### Step 3: Run JavaScript on Safari Webpage
- Add the **"Run JavaScript on Safari Webpage"** action. This lets you execute custom JavaScript on the page.
- Use this to extract the elements you're interested in. For example:
```javascript
var content = document.body.innerHTML; // or document.querySelector if you need a specific element
completion(content);
```
- This script grabs the inner HTML of the body tag, which contains all content of the page.

#### Step 4: Process HTML to Markdown
- **Add a "Text" action** where you will place your JavaScript code to process the HTML.
- You might need to **write or find a JavaScript function** that converts HTML to Markdown. This function should take HTML as input and output Markdown.

#### Step 5: Handle Images
- In your JavaScript code, include handling for images, like so:
```javascript
html = html.replace(/<img[^>]*alt="([^"]*)"[^>]*>/gi, function (match, alt) {
    return '![' + alt + '](URL)';
});
```
- Replace "URL" with the actual image URL or a placeholder if you're not extracting the URLs.

#### Step 6: Quick Look to Preview
- Add the **"Quick Look"** action. This will let you preview the markdown before saving it.
- Pass the converted Markdown text to Quick Look.

#### Step 7: Save the Markdown File
- Add the **"Save File"** action to save your Markdown text as a file.
- Choose where to save the file, like iCloud Drive or local storage.
- Set the name of the file, making sure it ends with ".md".

#### Step 8: Test Your Shortcut
- **Run your shortcut** from the share sheet in Safari to test it.
- You may have to go back and tweak your JavaScript for better results.

#### Step 9: Troubleshooting
- If something doesn't work, **check the JavaScript console** for errors.
- Make sure your JavaScript correctly targets the elements on the page.
- You may need to adjust your HTML-to-Markdown conversion script to handle different webpage structures.

#### Step 10: Iteration
- Iterate over the process, refining your JavaScript and actions based on the results you get.
- Testing with different webpages will help you cover more cases and improve the accuracy of the conversion.

#### Open-Ended Nature
This guide is designed to give you a starting point. You'll likely need to fill in gaps with your own JavaScript code, especially for the HTML-to-Markdown conversion, which can get complex. As you build and test your shortcut, note down any specific areas where you encounter issues. This will make it easier to troubleshoot and seek help for those particular steps.

Remember, building a shortcut like this is a process of trial and error, especially when dealing with the variability of web content. Good luck, and don't hesitate to reach out with questions about specific steps!