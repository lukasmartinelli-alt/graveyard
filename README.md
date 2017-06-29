# vectorbaker
Turn GeoJSON/Shapefiles into vector tiles on disk.

```js
npm install
```

This will

1. Invoke tippecanoe with GeoJSON and produce MBTiles file
2. Copy and convert tiles from MBTiles to disk in XZY format

```js
wget https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_admin_1_states_provinces_shp.geojson
node bin/make-vectortiles.js -i ne_110m_admin_1_states_provinces_shp.geojson -d my_tiles
```
