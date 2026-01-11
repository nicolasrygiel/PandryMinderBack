# Standard
    -   official doc : https://peps.python.org/pep-0008/
    -   4 space indent

    -   80 chars per line

    -   docstrings are wrapped at 72 characters

    -    The preferred way of wrapping long lines is by using Python’s implied 
        line continuation inside parentheses, brackets and braces. Long lines 
        can be broken over multiple lines by wrapping expressions in 
        parentheses.These should be used in preference to using a backslash for 
        line continuation.

    -    Operators : 
        income = (gross_wages
                  + taxable_interest
                  + (dividends - qualified_dividends)
                  - ira_deduction
                  - student_loan_interest)

    -   Blank lines :
        Surround top-level function and class definitions with two blank lines.

        Method definitions inside a class are surrounded by a single blank line.

        Extra blank lines may be used (sparingly) to separate groups of related 
        functions. Blank lines may be omitted between a bunch of related 
        one-liners (e.g. a set of dummy implementations).

    -   Standard library imports.
        Related third party imports.
        Local application/library specific imports.

    -   Variables, functions ... : lowercase_with_underscore
        Classes : CapitalizedWords
        Global and constants : GLOBAL_VARS

    - lookup public private for classes attributes, __all__