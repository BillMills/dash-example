Simple example of a dash app that will ingest and plot data from a file. Note the memory limit to force memory to disk if we're running on a wee little rpi or similar. 

```
docker image build -t billmills/plotter:dev .
docker container run -d -p 8050:8050 -v $(pwd)/data:/data --restart always  --memory 50m --memory-swap 200m --restart unless-stopeed billmills/plotter:dev
```

Note memory limits don't actually work on my rpi0 w2 - but might be enableable? TBD.
