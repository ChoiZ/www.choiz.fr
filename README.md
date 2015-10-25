choiz.github.io
===============

Personnal blog available on: http://www.choiz.fr

- Create a new post on ```content/``` folder using command:
```python
py write.py
```

- Test localy with command:
```bash
./develop_server.sh start
```

- Open [http://localhost:8000](http://localhost:8000)

- Stop local server
```bash
./develop_server.sh stop
```

- Add file to repository:
```git
git add content
git commit content
```

- Publish to master:
```bash
make github
```
