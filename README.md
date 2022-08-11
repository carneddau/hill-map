# Hill Map
Project for messing around with hill map data

## Install
Install using [Poetry](https://python-poetry.org/docs/)

## Usage
Create a [MapBox API Token](https://docs.mapbox.com/api/accounts/tokens/) and export
a shell environment variable before running the tool.

```shell
export MAPBOX_TOKEN=<TOKEN>
```
Alternatively, create a file named `.env` with contents similar to the [example](./.env.example)

Run the tool
```
hill-map ./data.csv
```

This will open your browser to a visualisation of [Nuttalls](https://en.wikipedia.org/wiki/Lists_of_mountains_and_hills_in_the_British_Isles#Nuttalls)
in the British Isles.

## Acknowledgments
The [data in this repo](./data.csv) is derived from the
[Database of British and Irish Hills v17.4](http://www.hills-database.co.uk) (DoBIH),
which is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

The file is a filtered subset of the DoBIH database, containing only Nuttalls.
