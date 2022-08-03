from flask import Flask, Response, request, jsonify
from loguru import logger

from async_parser.tasks import download_parse_save


app = Flask(__name__)


@app.route('/')
def index() -> str:
    return 'Send your queries to /parse'


@app.route('/parse')
def parse() -> Response:
    """
    Example: http://127.0.0.1:5000/parse?url=http://replay191.valve.net/570/6216665747_89886887.dem.bz2
    """
    dem_url = request.args.get('url')
    logger.info(f'{dem_url=}')
    if dem_url is None:
        return jsonify(dict(
            success=False,
            error='Demo URL not found'
        )), 400
    dem_url = dem_url.strip()

    async_result = download_parse_save(dem_url)
    logger.info(f'{async_result}')
    return jsonify(dict(
        success=True,
        url=dem_url,
        job_id=async_result.id
    ))
