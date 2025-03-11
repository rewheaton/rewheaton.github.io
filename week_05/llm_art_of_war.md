---
layout: post
author: Rob Wheaton
tags: [cscc]
---

### Art of War
I chose [The Art of War](https://www.gutenberg.org/cache/epub/17405/pg17405.txt) by Sun Tzu from Project Gutenberg to discuss with [Gemini](https://gemini.google.com/) from Google. I chose this book because it's one of my favorites and it's relatively short, so I was confident that an LLM could analyze it in memory. I first asked Gemini to pull some quotes about retreating from the book and it did pretty well:

```
Sure, here are some quotes about retreating from the text:

"If the enemy is in superior strength, evade him."    
"Hence, though an obstinate fight may be made by a small force, in the end it must be captured by the larger force."    
"If quite unequal in every way, we can flee from him."    
"You may retire and be safe from pursuit if your movements are more rapid than those of the enemy."    
"Do not pursue an enemy who simulates flight."    
"When envoys are sent with compliments in their mouths, it is a sign that the enemy wishes for a truce."    
"The general who advances without coveting fame and retreats without fearing disgrace, whose only thought is to protect his country and do good service for his sovereign, is the jewel of the kingdom."
```
A few of those quotes weren't actually about retreating yourself but rather about when your opponent does.

The second question I asked it was, "Do you think this book has applications outside of warfare?" and the answer blew me away at first:

```

Yes, I think this book has applications outside of warfare. The text is a collection of military strategies and tactics written by Sun Tzu, a Chinese general, strategist, and philosopher who lived during the second half of the Zhao dynasty in ancient China (771 to 256 BCE).  The text has had a significant impact on military thinking around the world, but its lessons can also be applied to a variety of other fields, including business, law, and personal relationships.    

For example, the principle of "knowing your enemy" is just as important in business as it is in war.  If you are trying to launch a new product, for example, you need to understand your competitors and their strengths and weaknesses.  The principle of "using deception" can also be applied to business negotiations.  If you are trying to get a better price for a product, for example, you might pretend that you are not interested in buying it.    

The principles of "The Art of War" can also be applied to personal relationships.  For example, the principle of "choosing your battles" is important in any relationship.  If you are always arguing with your partner, you are likely to damage the relationship.  The principle of "knowing your enemy" can also be helpful in personal relationships.  If you are having a conflict with someone, it is helpful to understand their perspective and their motivations.    

Overall, I think "The Art of War" is a valuable book that has applications outside of warfare.  The book's principles can be applied to a variety of fields, including business, law, and personal relationships.  If you are looking for a book that can help you to think strategically and to achieve your goals, "The Art of War" is a good place to start. 
```

I felt like this was particularly impressive until I realized that this type of analysis has been done by countless students for decades and the LLM might just be repeating text that it was trained on. To test whether the LLM was coming up with truly original content, I asked it, "How do the principles of this book apply to cooking?":

```

While "The Art of War" is primarily about military strategy, many of its principles can be surprisingly applicable to cooking. Here are a few examples:

1. Know your ingredients (Know your enemy and know yourself): Just as a general must know the strengths and weaknesses of their army and their enemy, a cook must be intimately familiar with their ingredients. Understanding the properties of different ingredients, how they react with each other, and their flavors and textures is crucial for successful cooking.    

2. Preparation is key (Laying plans): Sun Tzu emphasizes the importance of meticulous planning and preparation before battle. Similarly, good cooking relies heavily on preparation. This includes gathering quality ingredients, having the right tools, prepping ingredients beforehand (chopping vegetables, measuring spices), and understanding the recipe thoroughly.    

3. Timing is everything (Energy): A good general knows when to strike and when to wait. Likewise, a cook must master timing. Whether it's knowing when to flip a steak, how long to simmer a sauce, or when to take a dish out of the oven, timing is essential for achieving the desired outcome.    

4. Adapt to the situation (Variation in tactics): Sun Tzu advises generals to be flexible and adapt their strategies to changing circumstances. Similarly, a skilled cook must be able to adjust their approach based on the ingredients available, the cooking equipment, or unexpected challenges that arise during the cooking process.    

5. Use deception (Attack by stratagem): In war, deception can be used to confuse the enemy. In cooking, creative presentation and unexpected flavor combinations can delight and surprise the diner. Think of a deceptively simple-looking dish that's packed with complex flavors, or a dessert that looks like one thing but tastes like another.    

6. Keep your cool (Maneuvering): A general must remain calm under pressure, and so must a cook. When things get hectic in the kitchen, a level head and the ability to prioritize tasks are essential for avoiding culinary disasters.    

In essence, while the battlefield and the kitchen may seem worlds apart, the underlying principles of strategy, preparation, timing, adaptability, and even deception can be found in both. A good cook, like a good general, understands these principles and uses them to achieve victory in their respective domains.
```

This response was the most human-like to me. It shows an ability to make connections across disperate domains and to an extent, make pretty thin connections which is very human-like indeed. One interesting thing I noticed was that when the LLM referred to the author, it used "Sun Tzu" which is how I've read it in the copy I own however in the text file, it uses "Sun Tzŭ" with the modifier on the letter u. My takeaway from this is that the LLM is at least somewhat familiar with this book already and it is using previous experience with another copy to interact with me.