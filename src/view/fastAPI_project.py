import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from src.controllers.controller import controller_conesearch, controller_conesearch_all, controller_crossmatch, controller_crossmatch_all
from typing import Union
from src.presentation.response_models import CrossMatchModel, CrossMatchAllModel, ConeSearchModel, ConeSearchAllModel

app = FastAPI()

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




@app.get("/conesearch", response_model=list[ConeSearchModel])
def conesearch(catalog: str, ra: float, dec: float, radius: float):
    """
    This function returns the cone search result, it uses an auxiliary
    function to generate the result.

    Args:
        A Request

    Returns:
        The JSON representation of the cone search result for a single catalog.
    """
    request = {
        "ra":ra,
        "dec":dec,
        "radius":radius
    }
 
    return controller_conesearch(catalog,request)


@app.get("/conesearch_all", response_model=ConeSearchAllModel)
def conesearch_all(ra: float, dec: float, radius: float):
    """
    This function returns the result of running a cone search over all
    available catalogs. It uses the 'conesearch' function to generate this
    results.

    Args:
        A request

    Returns:
        The JSON representation of the cone search results for all catalogs.
    """
    request = {
        "ra":ra,
        "dec":dec,
        "radius":radius
    }
    return controller_conesearch_all(request)


@app.get("/crossmatch",response_model=list[CrossMatchModel])
def crossmatch(catalog: str, ra: float, dec: float, radius: Union[float, None] = None):
    """
    This function returns the result of running a crossmatch over one catalog.
    It uses an auxiliary function to compute the results.

    Args:
        A request
    Returns:
        The JSON representation of the crossmatch result.
    """
    request = {
        "ra":ra,
        "dec":dec,
        "radius":radius
    }

    return controller_crossmatch(catalog,request)



@app.get("/crossmatch_all",response_model=CrossMatchAllModel)
def crossmatch_all(ra: float, dec: float, radius: Union[float, None] = None):
    """
    This function returns the crossmatch result for all catalogs.

    Args:
        A request
    Returns:
        The JSON representation of the crossmatch result for all catalogs.
    """
    request = {
        "ra":ra,
        "dec":dec,
        "radius":radius
    }
    return controller_crossmatch_all(request)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)