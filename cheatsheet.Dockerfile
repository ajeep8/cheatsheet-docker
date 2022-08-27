FROM node:14-alpine AS cheatsheet

COPY cheat-sheet-maker /cheat-sheet-maker

WORKDIR /cheat-sheet-maker
CMD [ "npm", "run", "start" ]

