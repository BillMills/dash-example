Simple example of a dash app that will ingest and plot data from a file.

```
docker image build -t billmills/plotter:dev .
docker container run -d -p 8050:8050 -v $(pwd)/data:/data billmills/plotter:dev
```