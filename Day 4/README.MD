"A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

    aa bb cc dd ee is valid.
    aa bb cc dd aa is not valid - the word aa appears more than once.
    aa bb cc dd aaa is valid - aa and aaa count as different words.

The system's full passphrase list is available as your puzzle input. How many passphrases are valid?

Your puzzle answer was 451."

<b>This was a relatively easy challenge (compared to yesterday especially). I got a little confused at first and thought that it was all of the words and not each line. I kept wondering "why didn't they specify how long each phrase should be". After I realized my mistake I very quickly read the file line by line and then comapred each words in it. There are likely more elegant ways of solving the problems but my solution got it done.</b>

"For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

For example:

    abcde fghij is a valid passphrase.
    abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
    a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
    iiii oiii ooii oooi oooo is valid.
    oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.

Under this new system policy, how many passphrases are valid?

Your puzzle answer was 223."

<b>This, hands down has to be the fastest I have solved one of these puzzles. The exact code as before worked. The only difference was that I simply had to check for anagrams. Well, sorting the list would provide this information very quickly</b>
