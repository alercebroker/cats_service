import uvicorn
from fastapi import FastAPI, status, Query, Depends
from fastapi.responses import HTMLResponse
from src.controllers.controller import (
    controller_conesearch,
    controller_conesearch_all,
    controller_crossmatch,
    controller_crossmatch_all,
)
from src.presentation.response_models import (
    CrossMatchModel,
    CrossMatchAllModel,
    ConeSearchModel,
    ConeSearchAllModel,
)
from starlette_prometheus import metrics, PrometheusMiddleware
import os
from pydantic.dataclasses import dataclass


app = FastAPI(
    description="Cats Service provides conesearch and cross-match on different catalogs. It is based on catsHTM.",
    title="ALeRCE CatsHTM Service",
    root_path=os.getenv("ROOT_PATH", "/"),
)

app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics/", metrics)


@app.get("/health", status_code=status.HTTP_200_OK)
def health():
    return {}


@app.get("/", response_class=HTMLResponse)
def welcome():
    return """<!DOCTYPE html>
              <html>
              <head>
              <title>ALeRCE Cats Service</title>
              </head>
              <body>
              <h3>Welcome to the Cats Service</h3>
              <p>Documentation can be found
              <a href="https://alerceapi.readthedocs.io/en/latest/catshtm.html">
              here</a>.</p>
              </body>
              </html>"""


@dataclass
class ConesearchInput:
    catalog: str = Query(
        description="name of the catalog, e.g., FIRST, AAVSO_VSX, AKARI"
    )
    ra: float = Query(description="ra coordinate of the point to search in degrees.")
    dec: float = Query(description="dec coordinate of the point to search in degrees.")
    radius: float = Query(description="radius of the point to search in arsec")


@app.get("/conesearch", response_model=list[ConeSearchModel])
def conesearch(params: ConesearchInput = Depends()):
    """
    This function returns the cone search result, it uses an auxiliary
    function to generate the result.
    """

    return controller_conesearch(params)


@dataclass
class ConesearchAllInput:
    ra: float = Query(description="ra coordinate of the point to search in degrees.")
    dec: float = Query(description="dec coordinate of the point to search in degrees.")
    radius: float = Query(description="radius of the point to search in arsec")


@app.get("/conesearch_all", response_model=ConeSearchAllModel)
def conesearch_all(params: ConesearchAllInput = Depends()):
    """
    This function returns the result of running a cone search over all
    available catalogs. It uses the 'conesearch' function to generate this
    results.
    """
    return controller_conesearch_all(params)


@dataclass
class CrossmatchInput:
    catalog: str = Query(
        description="name of the catalog, e.g., FIRST, AAVSO_VSX, AKARI"
    )
    ra: float = Query(description="ra coordinate of the point to search in degrees.")
    dec: float = Query(description="dec coordinate of the point to search in degrees.")
    radius: float | None = Query(
        None,
        description="radius of the point to search in arsec, if not provided, the default value for that catalog is used.",
    )


@app.get("/crossmatch", response_model=list[CrossMatchModel])
def crossmatch(params: CrossmatchInput = Depends()):
    """
    This function returns the result of running a crossmatch over one catalog.
    It uses an auxiliary function to compute the results.
    """
    return controller_crossmatch(params)


@dataclass
class CrossmatchAllInput:
    ra: float = Query(description="ra coordinate of the point to search in degrees.")
    dec: float = Query(description="dec coordinate of the point to search in degrees.")
    radius: float | None = Query(
        None,
        description="radius of the point to search in arsec, if not provided, the default value for that catalog is used.",
    )


@app.get("/crossmatch_all", response_model=CrossMatchAllModel)
def crossmatch_all(params: CrossmatchAllInput = Depends()):
    """
    This function returns the result of running a crossmatch over all
    available catalogs.
    """
    return controller_crossmatch_all(params)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)
