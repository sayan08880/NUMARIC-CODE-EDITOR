  1. Capital Letters: Represented with + before their position value.
    Example: A → +1, Bc → +2 3.

  2. Lowercase Letters: Represented with their position value as is.
    Example: a → 1, b → 2, abc → 1 2 3.

  3. Special Characters (@): Remain unchanged and are inserted in their position.
    Example: a@b → 1 @ 2, abc@ → 1 2 3 @.

  4. Numbers: Represented with - before each digit.
    Example: 2005 → -2 -0 -0 -5, 15 → -1 -5.

    Spaces: Spaces are preserved between components.

Examples:

    Ab → +1 2
    abcD → 1 2 3 +4
    ab@ → 1 2 @
    aBc@2005 → 1 +2 3 @ -2 -0 -0 -5
    Bcde@15 → +2 3 4 5 @ -1 -5
