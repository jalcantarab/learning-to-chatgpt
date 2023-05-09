# learning-to-chatgpt
 Lesson 1: Running Blind Code for small utility use cases

# Interacting with ChatGPT: A Quick Guide

Learn how to effectively interact with ChatGPT to solve simple problems. This guide uses the example of converting a folder of images into a PDF file.

- [Example Problem](#example-problem)
- [Crafting the Prompt](#crafting-the-prompt)
- [Example ChatGPT Conversation](#example-chatgpt-conversation)

## Example Problem

**Scenario**: A friend studying dentistry has a subject where the professor didn't share the slides. Fortunately, a kind soul took photos of all the slides in class. Now, we have folders full of images but no easy way to go through them. The goal is to merge all images into a large PDF.

### Problem

We have no idea how to approach this task, and it will probably take hours just to test an approach.

### Solution

We have ChatGPT, and code can fix anything.

## Crafting the Prompt

1. **Describe the problem** in simple yet detailed terms:

   > "We have a folder full of images without extension, we want to create a .pdf that merges all of them in one file."

2. To get the best help from ChatGPT, **tell it who to play as**:

   > "You are an experienced developer that generates simple solutions to complex problems."

3. Finally, **ask ChatGPT for its output**. At this stage, let's imagine we don't know what is the best way to approach the issue.

   > "Please share in detail all the steps & code if necessary to get a pdf from these files"

   If we had a more clear idea of how we want to solve the issue, we may prompt ChatGPT to bias the solution in that direction.

   > "Please generate the necessary shell code to run on a terminal within the folder to get a pdf from these files"

Here's an example prompt combining all the elements above:

> "You are an experienced developer that generates simple code solutions to complex problems. We have a folder full of what look like images without extension. We want to create a .pdf that merges all of them in one file. Please share in detail all the steps & code necessary to get a pdf from these files."

## Example ChatGPT Conversation

Below is the example conversation with ChatGPT to solve this problem:

> [User] We have a folder full of images without extension, we want to create a .pdf that merges all of them in one file.
>
> [User] You are an experienced developer that generates simple solutions to complex problems. Please share in detail all the steps & code necessary to get a pdf from these files.
>
> [ChatGPT] (Provides detailed steps and Python code to merge images into a PDF)
>
> ```python
> (Python code to merge images into a PDF)
> ```
>
> [User] Can you please update the script so that when it creates the .pdf file, the images are ordered alphabetically? Include error handling so we know if any images failed to convert.
>
> [ChatGPT] (Updates the script to sort images alphabetically and includes error handling)
>
> ```python
> (Updated Python code to sort images alphabetically and include error handling)
> ```

Remember to be clear and detailed when describing the problem, and don't hesitate to ask follow-up questions or request modifications to the solution provided by ChatGPT.
