choiz.github.com
================

Personnal blog available on http://blog.choiz.fr

- Create a new post on content folder

- Test localy with command:
```bash
./develop_server.sh start
```

- Open http://localhost:8000

- Stop local server
```bash
./develop_server.sh stop
```

- Add file to repository:
```git
git add content/new_post
git commit content/new_post
```

- Publish to master:
```bash
make github
```
