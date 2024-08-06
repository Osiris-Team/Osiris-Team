# General guidelines for contributions on open source software

Why do you not accept @author lines in your source code?

- Because the author tags in the java files are a maintenance nightmare
- A large percentage is wrong, incomplete or inaccurate.
- Most of the time, it only contains the original author. Many files are completely refactored/expanded by other authors.
- Git is accurate, that is the canonical source to find the correct author.
- Because the author tags promote code ownership, which is bad in the long run.
- If people work on a piece they perceive as being owned by someone else, they tend to:
only fix what they are assigned to fix, instead of everything that's broken, discard responsibility if that code doesn't work properly and be scared of stepping on the feet of the owner.

Credit to the authors is given with Open Hub which also has statistics and in the GitHub web interface under contributors.