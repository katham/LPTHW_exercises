# -*- coding: utf-8 -*-

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.", #i used the single-quote for the didnt
                        # so the quotation marks have to be the double-ones
    "So I said goodnight."
)
