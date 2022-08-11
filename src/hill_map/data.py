from os import PathLike

from pandas import read_csv
from plotly import colors
from plotly.express import scatter_mapbox, set_mapbox_access_token

from .settings import get_settings


def display_csv_data(file: PathLike):
    settings = get_settings()
    set_mapbox_access_token(settings.mapbox_token)

    df = read_csv(
        file, usecols=["Hillnumber", "Hillname", "Longitude", "Latitude", "Metres"]
    )

    fig = scatter_mapbox(
        df,
        lat=df["Latitude"],
        lon=df["Longitude"],
        color_continuous_scale=colors.sequential.Viridis,
        color=df["Metres"],
        hover_name="Hillname",
        mapbox_style="outdoors",
    )

    fig.show()
