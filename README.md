# Eurydice

This is an IRC bot written in python. It's really just for me to get a feel for python and practice some stuff, but it could be useful as a task management tool as well.

## TODO

- Clean up Eurydice.py. Shit's a mess.
- Add functionality for 
  - project status
  - notifications when a project is at another person
  - More silly responses and moe bullshit
  - Language parsing?

## Mailbox Organization

- array of messages stored by destination user in a dictionary
    - {\'destination\': [\'source\', \'msg\']}
    - new messages for a user get appended to that user's list
    - mb[\'destination\'].append(message())
- Maybe three files instead? Dests, bodies, mappings between the two?
    - I dunno
