# looker_upper

Look up what I want. Tell me if this product is safe or if it's gonna make my skin so super sad.

Here's what it's about:

* put my api stuff in a yml file that i don't check into git
* Take a UPC code and look up product ingredients.
* have a list of what you are allergic to.
* * Look up what you input as your allergens and find related ones and that makes the list of "baddies"
* compare the "baddies" to the ingredients in the product.
  * What about misspellings like Quanternium-15? That's in the J&J baby shampoo.
* upc scanning for the product. scan upc. get the product in the db.

## Things to think about

* Misspellings of ingredients. Maybe get similar names?
* Product ingredient updates. Maybe this database isn't reliable?
